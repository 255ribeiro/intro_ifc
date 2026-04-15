# Resources no BonsaiBIM: `bpy.ops.bim.import_resources()`

> Notas técnicas extraídas do código-fonte Bonsai 0.8.4  
> Arquivo principal analisado: `ifc4d/csv2ifc.py`

---

## O que são Resources no IFC?

**Resources** (`IfcConstructionResource`) representam os **insumos de obra** — tudo que é consumido ou utilizado para executar uma atividade de construção. São a base para orçamento de composições e planejamento de cronograma físico-financeiro.

O IFC define seis subtipos:

| Valor CSV | Classe IFC | O que representa |
|---|---|---|
| `CREW` | `IfcCrewResource` | equipe (agrupa outros recursos) |
| `LABOR` | `IfcLaborResource` | mão de obra |
| `EQUIPMENT` | `IfcConstructionEquipmentResource` | equipamento |
| `SUBCONTRACTOR` | `IfcSubContractResource` | serviço terceirizado |
| `MATERIAL` | `IfcConstructionMaterialResource` | material |
| `PRODUCT` | `IfcConstructionProductResource` | produto industrializado |

---

## Cadeia de chamadas

**`bpy.ops.bim.import_resources()`** — `bonsai/bim/module/resource/operator.py:337`  
↓ Abre file explorer. Ao confirmar:

**`operator._execute()`** — `operator.py:350`  
↓ Conta recursos antes/depois e chama:

**`core.import_resources(tool.Resource, file_path)`** — `core/resource.py:178`  
↓ Delega para a ferramenta:

**`tool.Resource.import_resources(file_path)`** — `tool/resource.py:323`  
↓ Instancia e executa:

**`ifc4d.csv2ifc.Csv2Ifc(file_path, ifc_file).execute()`** — `ifc4d/csv2ifc.py:97`

> **Atenção:** Resources usa o pacote **`ifc4d`**, não `ifc5d` (que é para custos/quantificação).

O `Csv2Ifc` opera em duas etapas:
1. **`parse_csv()`** — lê o CSV e monta lista de dicts com hierarquia
2. **`create_ifc()`** — cria os objetos `IfcConstructionResource` com seus dados

---

## Colunas da planilha

### Colunas obrigatórias

Todas as colunas abaixo **devem estar presentes** no cabeçalho — o importador lança exceção se alguma faltar. A ordem das colunas não importa, mas `HIERARCHY` **deve ser a primeira coluna**.

| Coluna CSV | Parâmetro IFC | Notas |
|---|---|---|
| `HIERARCHY` | nível na árvore (1=raiz, 2=filho…) | não vai para o IFC diretamente |
| `TYPE` | define a subclasse IFC (ver tabela acima) | valores válidos: `CREW`, `LABOR`, `EQUIPMENT`, `SUBCONTRACTOR`, `MATERIAL`, `PRODUCT` |
| `ACTIVITY/RESOURCE NAME` | `IfcConstructionResource.Name` | |
| `DESCRIPTION` | `IfcConstructionResource.Description` | pode ficar vazio |
| `COST` | `IfcCostValue.AppliedValue` = `IfcMonetaryMeasure(valor)` | custo unitário do insumo; pode ficar vazio |
| `USAGE` | `IfcResourceTime.ScheduleUsage` | quantidade consumida programada; pode ficar vazio |
| `QUANTITY NAME` | `EPset_Productivity.BaseQuantityProducedName` | nome da grandeza produzida (ex: `GrossVolume`); usado com LABOR/EQUIPMENT |
| `LABOR OUTPUT` | `EPset_Productivity.BaseQuantityConsumed` | horas por unidade produzida — apenas para `TYPE=LABOR` |
| `EQUIPMENT OUTPUT` | `EPset_Productivity.BaseQuantityConsumed` | horas por unidade produzida — apenas para `TYPE=EQUIPMENT` |

### Colunas opcionais

Podem estar presentes ou ausentes. As três abaixo funcionam juntas:

| Coluna CSV | Parâmetro IFC |
|---|---|
| `BASE QUANTITY NAME` | `IfcPhysicalSimpleQuantity.Name` |
| `BASE QUANTITY VALUE` | `IfcPhysicalSimpleQuantity` valor |
| `BASE QUANTITY CLASS` | subclasse da quantidade (`IfcQuantityVolume`, `IfcQuantityCount`, etc.) |
| `GUID` | `IfcConstructionResource.GlobalId` (usado na exportação) |

> `UNIT` e `PRODUCTIVITY UNIT` aparecem em exemplos mas **não são usados** pelo importador (comentado no código: *"columns UNIT and PRODUCTIVITY UNIT are not actually used during import"*).

---

## Como funciona o OUTPUT (produtividade)

O campo `LABOR OUTPUT` / `EQUIPMENT OUTPUT` representa a **produtividade inversa**: quantas **horas** são necessárias para produzir **1 unidade** da grandeza definida em `QUANTITY NAME`.

```
LABOR OUTPUT = horas / unidade produzida
```

Exemplo: se um pedreiro produz 1 m² de alvenaria em 0,5 hora:
- `LABOR OUTPUT` = `0.5`
- `QUANTITY NAME` = `GrossArea`

O importador converte para `IfcDuration` e armazena em `EPset_Productivity`:
- `BaseQuantityConsumed` = duração por unidade
- `BaseQuantityProducedValue` = 1 (fixo no código)
- `BaseQuantityProducedName` = valor de `QUANTITY NAME`

---

## Planilha básica — exemplo mínimo

```
HIERARCHY | TYPE        | ACTIVITY/RESOURCE NAME | DESCRIPTION    | COST  | USAGE | QUANTITY NAME | LABOR OUTPUT | EQUIPMENT OUTPUT
1         | CREW        | Equipe Alvenaria        | Equipe padrão  |       |       |               |              |
2         | LABOR       | Pedreiro                |                | 25.00 |       | GrossArea     | 0.5          |
2         | LABOR       | Servente                |                | 15.00 |       | GrossArea     | 0.75         |
2         | MATERIAL    | Tijolo 6 furos          | cx 50 un       | 45.00 |       |               |              |
2         | MATERIAL    | Argamassa               | saco 20kg      | 18.00 |       |               |              |
          |             |                         |                |       |       |               |              |
1         | EQUIPMENT   | Betoneira 400L          |                | 80.00 |       | GrossVolume   | 2.0          |
```

**Regras importantes:**
- `HIERARCHY=1` → recurso raiz (sem pai)
- `HIERARCHY=2` → filho do último nível 1 acima
- Linhas **totalmente vazias** são ignoradas (útil para separar grupos visualmente)
- `COST` usa ponto como separador decimal (`25.00`, não `25,00`)
- `LABOR OUTPUT` e `EQUIPMENT OUTPUT` só são processados para `TYPE=LABOR` ou `TYPE=EQUIPMENT` respectivamente — nas demais linhas podem ficar vazios
- `QUANTITY NAME` só é relevante quando `LABOR OUTPUT` ou `EQUIPMENT OUTPUT` está preenchido

---

## Diferença entre Resources e Cost Schedule

| | Cost Schedule (`ifc5d`) | Resources (`ifc4d`) |
|---|---|---|
| Finalidade | orçamento de itens de obra com quantitativos | cadastro de insumos com produtividade |
| Objeto IFC | `IfcCostSchedule` / `IfcCostItem` | `IfcConstructionResource` |
| Vínculo com geometria | via `Query` + `Property` | via `BaseQuantity` + tarefas de cronograma |
| Operador Bonsai | `bim.import_cost_schedule_csv` | `bim.import_resources` |
| Pacote Python | `ifc5d.csv2ifc` | `ifc4d.csv2ifc` |

---

*Fonte: leitura do código-fonte Bonsai 0.8.4 — abril 2026*
