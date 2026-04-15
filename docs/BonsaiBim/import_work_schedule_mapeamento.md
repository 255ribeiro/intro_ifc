# Work Schedule no BonsaiBIM: `bpy.ops.bim.import_work_schedule_csv()`

> Notas técnicas extraídas do código-fonte Bonsai 0.8.4  
> Arquivo principal analisado: `ifc4d/csv4d2ifc.py`

---

## O que é um Work Schedule no IFC?

Um **Work Schedule** (`IfcWorkSchedule`) é o cronograma de obra — a estrutura hierárquica de tarefas com datas, durações e dependências. Equivale ao cronograma físico de um projeto de construção (similar a um MS Project ou Primavera P6, mas em IFC).

A hierarquia IFC criada pelo importador é:

```
IfcWorkPlan
  └── IfcWorkSchedule ("import")
        └── IfcTask (nível 1)
              ├── IfcTaskTime  (datas e durações)
              └── IfcTask (nível 2)
                    └── IfcTaskTime
                    └── ...
```

As dependências entre tarefas são representadas por `IfcRelSequence`.

---

## Cadeia de chamadas

**`bpy.ops.bim.import_work_schedule_csv()`** — `bonsai/bim/module/sequence/operator.py:821`  
↓ Abre file explorer. Ao confirmar:

**`operator._execute()`** — `operator.py:837`  
↓ Instancia e executa diretamente (sem passar por `core`):

**`ifc4d.csv4d2ifc.Csv2Ifc().execute()`** — `ifc4d/csv4d2ifc.py:40`

> **Nota:** diferente dos outros importadores, este não passa por uma camada `core` — o operador chama `Csv2Ifc` diretamente.

O `Csv2Ifc` opera em duas etapas:
1. **`parse_csv()`** — lê o CSV e monta lista de dicts de tarefas com hierarquia e relacionamentos
2. **`create_ifc()`** — cria `IfcWorkPlan` → `IfcWorkSchedule` → tarefas → sequências

---

## Colunas da planilha

A linha de cabeçalho é detectada quando `row[0] == "Hierarchy"` (com H maiúsculo).  
Linhas com primeira célula vazia são ignoradas.

> **Atenção:** o arquivo deve ser salvo com encoding **ISO-8859-1** (não UTF-8).  
> O código abre explicitamente com `encoding="ISO-8859-1"`.

### Todas as colunas

| Coluna CSV | Parâmetro IFC | Notas |
|---|---|---|
| `Hierarchy` | nível na árvore (1=raiz, 2=filho…) | **deve ser a primeira coluna** e o texto exato do cabeçalho |
| `Identification` | `IfcTask.Identification` | código da tarefa, usado para montar relacionamentos |
| `Name` | `IfcTask.Name` | nome da tarefa |
| `Relationships` | `IfcRelSequence` | dependências entre tarefas (ver formato abaixo) |
| `ScheduleStart` | `IfcTaskTime.ScheduleStart` | data de início prevista |
| `ScheduleFinish` | `IfcTaskTime.ScheduleFinish` | data de fim prevista |
| `ScheduleDuration` | `IfcTaskTime.ScheduleDuration` | duração prevista (formato ISO 8601) |
| `ActualStart` | `IfcTaskTime.ActualStart` | data de início real |
| `ActualFinish` | `IfcTaskTime.ActualFinish` | data de fim real |
| `ActualDuration` | `IfcTaskTime.ActualDuration` | duração real (formato ISO 8601) |

Todas as colunas acima devem estar presentes no cabeçalho. Células individuais podem ficar vazias.

---

## Formatos de data e duração

### Datas — ISO 8601
```
YYYY-MM-DD
2025-03-01
```

### Durações — ISO 8601
```
P{n}D    → dias       ex: P5D  = 5 dias
PT{n}H   → horas      ex: PT8H = 8 horas
P{n}W    → semanas    ex: P2W  = 2 semanas
P{n}DT{m}H → dias e horas ex: P3DT4H
```

> Duração e datas são alternativos — preencher `ScheduleDuration` **ou** `ScheduleStart`+`ScheduleFinish`. O código usa `DurationType = "WORKTIME"` somente quando há duração.

---

## Formato dos relacionamentos (coluna `Relationships`)

A coluna `Relationships` especifica dependências entre tarefas usando o formato:

```
{id_tarefa_1}{tipo}{id_tarefa_2}
```

Múltiplos relacionamentos separados por `;`:

```
1FS2;3SS4
```

### Tipos de sequência

| Código | Nome IFC | Significado |
|---|---|---|
| `FS` | `FINISH_START` | tarefa 1 termina → tarefa 2 começa (mais comum) |
| `FF` | `FINISH_FINISH` | as duas terminam juntas |
| `SS` | `START_START` | as duas começam juntas |
| `SF` | `START_FINISH` | tarefa 1 começa → tarefa 2 termina |

O `Identification` das tarefas é o valor da coluna `Identification`, não o `Hierarchy`.  
A busca por identificação ignora espaços e pontos (`.`).

---

## Planilha básica — exemplo mínimo

```
Hierarchy | Identification | Name                    | Relationships | ScheduleStart | ScheduleFinish | ScheduleDuration | ActualStart | ActualFinish | ActualDuration
1         | 1              | Fundações               |               | 2025-03-01    | 2025-03-15     |                  |             |              |
2         | 1.1            | Escavação               |               | 2025-03-01    | 2025-03-05     |                  |             |              |
2         | 1.2            | Formas e armação        | 1.1FS1.2      | 2025-03-06    | 2025-03-10     |                  |             |              |
2         | 1.3            | Concretagem             | 1.2FS1.3      | 2025-03-11    | 2025-03-15     |                  |             |              |
          |                |                         |               |               |                |                  |             |              |
1         | 2              | Estrutura               | 1FS2          | 2025-03-16    |                | P20D             |             |              |
2         | 2.1            | Pilares térreo          |               | 2025-03-16    | 2025-03-22     |                  |             |              |
2         | 2.2            | Lajes térreo            | 2.1FS2.2      | 2025-03-23    | 2025-03-31     |                  |             |              |
```

**Regras importantes:**
- O nome do `IfcWorkSchedule` criado é sempre `"import"` (hardcoded no código, linha 166)
- Linhas com primeira célula vazia são ignoradas — útil para separar grupos
- `ScheduleDuration` e `ScheduleStart`/`ScheduleFinish` são alternativos para a mesma tarefa
- Datas reais (`ActualStart`, `ActualFinish`, `ActualDuration`) podem ficar todas vazias para cronograma planejado

---

## Comparativo dos três importadores CSV

| | Work Schedule (`csv4d2ifc`) | Resources (`csv2ifc` ifc4d) | Cost Schedule (`csv2ifc` ifc5d) |
|---|---|---|---|
| Objeto IFC principal | `IfcTask` | `IfcConstructionResource` | `IfcCostItem` |
| Agrupador | `IfcWorkSchedule` | — | `IfcCostSchedule` |
| Coluna de nível | `Hierarchy` | `HIERARCHY` | `Index` |
| Encoding do arquivo | **ISO-8859-1** | UTF-8 (padrão) | UTF-8 |
| Vínculo com geometria | via tarefas/sequências | via `BaseQuantity` | via `Query` + `Property` |
| Pacote Python | `ifc4d.csv4d2ifc` | `ifc4d.csv2ifc` | `ifc5d.csv2ifc` |
| Operador Bonsai | `bim.import_work_schedule_csv` | `bim.import_resources` | `bim.import_cost_schedule_csv` |

---

*Fonte: leitura do código-fonte Bonsai 0.8.4 — abril 2026*
