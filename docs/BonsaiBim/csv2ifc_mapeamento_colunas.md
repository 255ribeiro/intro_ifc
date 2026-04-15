# CSV → IFC: Mapeamento de Colunas no BonsaiBIM

> Notas técnicas extraídas da leitura do código-fonte do Bonsai 0.8.4  
> Arquivo analisado: `ifc5d/csv2ifc.py` + `bonsai/bim/module/cost/`

---

## Cadeia de chamadas: `bpy.ops.bim.import_cost_schedule_csv()`

**`bpy.ops.bim.import_cost_schedule_csv()`** — `bonsai/bim/module/cost/operator.py:561`  
↓ Abre o file explorer via `ImportHelper`. Ao confirmar:

**`operator._execute()`** — `operator.py:583`  
↓ Resolve o caminho do arquivo e chama:

**`core.import_cost_schedule_csv(tool.Cost, path, is_schedule_of_rates)`** — `core/cost.py:341`  
↓ Passa para a ferramenta:

**`tool.Cost.import_cost_schedule_csv(path)`** — `tool/cost.py:579`  
↓ Importa e executa:

**`Csv2Ifc(path, ifc_file).execute()`** — `ifc5d/csv2ifc.py:136`

O `Csv2Ifc` faz o trabalho pesado em duas etapas:

1. **`parse_csv()`** (linha 145) — lê o CSV linha a linha, monta uma árvore de `CostItem` Python com `Index` definindo a hierarquia (1=raiz, 2=filho, etc.)
2. **`create_ifc()`** (linha 248) — para cada item da árvore chama `create_cost_item()` que cria os objetos IFC correspondentes.

---

## Mapeamento de colunas CSV → parâmetros IFC

### Colunas obrigatórias

| Coluna CSV | Parâmetro IFC | Linha no código |
|---|---|---|
| `Name` | `IfcCostItem.Name` | 273 |
| `Unit` | classe da quantidade (`IfcQuantityVolume`, `IfcQuantityCount`, etc.) | 361 |

### Colunas opcionais — metadados do item

| Coluna CSV | Parâmetro IFC |
|---|---|
| `Index` | nível na hierarquia (1=raiz, 2=filho…) — não armazenado no IFC |
| `Identification` | `IfcCostItem.Identification` |
| `Description` | `IfcCostItem.Description` |

### Colunas de custo

| Coluna CSV | Parâmetro IFC | Condição |
|---|---|---|
| `Value` | `IfcCostValue.AppliedValue` = `IfcMonetaryMeasure(valor)` | quando existe coluna `Value` |
| *qualquer outro nome* | `IfcCostValue.Category` = nome da coluna; `AppliedValue` = valor | quando **não** existe coluna `Value` — cada coluna extra vira uma categoria de custo |

### Colunas de quantificação (vinculam elementos IFC)

| Coluna CSV | O que faz |
|---|---|
| `Quantity` | valor direto → `IfcPhysicalSimpleQuantity[3]` |
| `Property` | nome da propriedade medida → `IfcPhysicalSimpleQuantity.Name` (ex: `GrossVolume`) |
| `Query` | selector IfcOpenShell → `filter_elements()` → `assign_cost_item_quantity()` — **vínculo com a geometria** |

### Colunas de tabela de preços (Schedule of Rates)

| Coluna CSV | O que faz |
|---|---|
| `RateSchedule` | nome do `IfcCostSchedule` de onde vem o preço |
| `RateID` | `IfcCostItem.Identification` do item de preço naquele schedule |

### Colunas ignoradas na importação

`TotalPrice`, `RateSubtotal`, `Subtotal` — existem apenas para exportação, o importador descarta.

---

## Regra do totalizador (Category `"*"`)

Quando um item pai tem filhos mas `Value` está vazio, o código (linha 278–283) cria automaticamente um `IfcCostValue` com `Category = "*"`. Isso instrui o IFC a **somar os valores dos filhos** automaticamente.

> Este mecanismo existe **apenas para valores monetários**, não para quantidades físicas.

---

## É possível somar volumes no item pai?

Não automaticamente — o IFC não tem equivalente a `Category="*"` para quantidades físicas.

### Solução 1: fórmula na planilha (recomendada para alunos)

Calcular o total na célula `Quantity` do pai usando fórmula no Google Sheets:

```
Index | Name     | Unit | Value | Quantity     | Property    | Query
1     | Concreto | m³   |       | =SOMA(B3:B5) |             |
2     | Pilares  | m³   | 500   |              | GrossVolume | IfcColumn
2     | Vigas    | m³   | 300   |              | GrossVolume | IfcBeam
2     | Lajes    | m³   | 800   |              | GrossVolume | IfcSlab
```

O importador cria `IfcPhysicalSimpleQuantity` no item pai com o valor somado (linha 366 do `csv2ifc.py`: a quantidade é criada sempre que `Quantity` não é `None`, mesmo em pais com filhos).

### Solução 2: pós-processamento em Python

```python
import ifcopenshell.util.cost

for cost_item in ifcopenshell.util.cost.get_schedule_cost_items(schedule):
    children = [...]  # filhos do item
    if children:
        total_vol = sum(q[3] for c in children for q in (c.CostQuantities or []))
        # criar IfcQuantityVolume no pai com total_vol
```

---

*Fonte: leitura do código-fonte Bonsai 0.8.4 — abril 2026*
