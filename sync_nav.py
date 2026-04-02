from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


def normalize_docs_relative(path: str) -> str:
    """Normalize file paths to be relative to docs/ and use forward slashes."""
    p = path.strip().replace('\\', '/')

    if p.startswith('./'):
        p = p[2:]

    if p.lower().startswith('docs/'):
        p = p[5:]

    return p


def _indent_size(line: str) -> int:
    return len(line) - len(line.lstrip(' '))


def _is_item_line(line: str) -> bool:
    return line.lstrip(' ').startswith('- ')


def _split_nav_item(body: str) -> tuple[str, str]:
    if ':' not in body:
        raise ValueError(f"Invalid nav item (missing ':'): {body!r}")
    key, value = body.split(':', 1)
    return key.strip(), value.strip()


def _next_significant(lines: list[str], i: int) -> int:
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped and not stripped.startswith('#'):
            return i
        i += 1
    return i


def parse_mkdocs_nav(mkdocs_text: str) -> list[dict[str, Any]]:
    lines = mkdocs_text.splitlines()

    nav_header = -1
    nav_indent = 0
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('nav:'):
            nav_header = idx
            nav_indent = _indent_size(line)
            break

    if nav_header == -1:
        raise ValueError("Could not find `nav:` in mkdocs.yml")

    start = _next_significant(lines, nav_header + 1)
    if start >= len(lines):
        return []

    first_indent = _indent_size(lines[start])

    def parse_list(i: int, expected_indent: int) -> tuple[list[dict[str, Any]], int]:
        result: list[dict[str, Any]] = []

        while i < len(lines):
            stripped = lines[i].strip()

            if not stripped or stripped.startswith('#'):
                i += 1
                continue

            indent = _indent_size(lines[i])

            if indent <= nav_indent:
                break

            if indent < expected_indent:
                break

            if indent > expected_indent:
                i += 1
                continue

            if not _is_item_line(lines[i]):
                break

            body = lines[i].lstrip(' ')[2:]
            title, rest = _split_nav_item(body)

            if rest:
                result.append({title: rest})
                i += 1
                continue

            child_start = _next_significant(lines, i + 1)
            if child_start >= len(lines):
                result.append({title: []})
                i = child_start
                continue

            child_indent = _indent_size(lines[child_start])
            if child_indent <= indent:
                result.append({title: []})
                i = child_start
                continue

            children, i = parse_list(child_start, child_indent)
            result.append({title: children})

        return result, i

    nav, _ = parse_list(start, first_indent)
    return nav


def format_nav_item(item: dict[str, Any], indent: int = 2) -> list[str]:
    """Format one nav item as the expected inline-table TOML style."""
    if len(item) != 1:
        raise ValueError(f"Each nav item must have exactly one key. Got: {item}")

    title, value = next(iter(item.items()))
    pad = ' ' * indent

    if isinstance(value, str):
        return [f'{pad}{{"{title}" = "{normalize_docs_relative(value)}"}},']

    if isinstance(value, list):
        lines = [f'{pad}{{"{title}" = [']
        for child in value:
            if not isinstance(child, dict):
                raise ValueError(f"Nested nav item must be a dict. Got: {child!r}")
            lines.extend(format_nav_item(child, indent + 2))
        lines.append(f'{pad}]}},')
        return lines

    raise ValueError(
        f"Unsupported nav value type for '{title}': {type(value).__name__}. "
        "Expected str or list."
    )


def render_nav_block(nav: list[dict[str, Any]]) -> str:
    lines = ['nav = [']
    for item in nav:
        if not isinstance(item, dict):
            raise ValueError(f"Top-level nav item must be a dict. Got: {item!r}")
        lines.extend(format_nav_item(item, indent=2))
    lines.append(']')
    return '\n'.join(lines)


def find_nav_block_range(text: str) -> tuple[int, int]:
    """Find start/end indices of `nav = [ ... ]` in TOML text."""
    marker = 'nav = ['
    start = text.find(marker)
    if start == -1:
        raise ValueError("Could not find `nav = [` block in TOML file.")

    i = start + len(marker) - 1  # points to the opening '['
    depth = 0
    in_string = False
    escaped = False

    while i < len(text):
        ch = text[i]

        if in_string:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
        elif ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                return start, i + 1

        i += 1

    raise ValueError("Unterminated `nav` block in TOML file.")


def update_toml_nav(toml_path: Path, new_nav_block: str) -> None:
    text = toml_path.read_text(encoding='utf-8')
    start, end = find_nav_block_range(text)
    updated = text[:start] + new_nav_block + text[end:]
    toml_path.write_text(updated, encoding='utf-8')


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Sync nav from mkdocs.yml into zensical.toml format.'
    )
    parser.add_argument('--mkdocs', default='mkdocs.yml', help='Path to mkdocs.yml')
    parser.add_argument('--toml', default='zensical.toml', help='Path to target TOML file')
    args = parser.parse_args()

    mkdocs_path = Path(args.mkdocs)
    toml_path = Path(args.toml)

    nav = parse_mkdocs_nav(mkdocs_path.read_text(encoding='utf-8'))

    new_nav_block = render_nav_block(nav)
    update_toml_nav(toml_path, new_nav_block)

    print(f'Updated nav in {toml_path} from {mkdocs_path}.')


if __name__ == '__main__':
    main()
