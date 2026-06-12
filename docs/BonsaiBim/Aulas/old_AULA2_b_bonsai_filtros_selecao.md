# Bonsai BIM — Guia de Seleção de Elementos pelo Funil

> **Interface em inglês (Blender/Bonsai).** Este guia usa os nomes dos painéis e botões como aparecem na UI.
>
> **Como acessar:** `Properties Panel (N) → Project Overview → Grouping and Filtering`
> Clique no ícone de **funil (🔽)** ao lado do botão **"Add Search Group"** para digitar ou ver a query atual.

---

## Lógica fundamental

A sintaxe é inspirada em CSS/IDS. Os filtros dentro de um grupo são separados por **vírgula** (`,`) e se comportam como **AND** (exceto classes IFC, que são **OR** entre si). Grupos distintos são separados por **`+`** e se comportam como **OR** (união).

```
ClasseA, ClasseB, filtro1, filtro2 + ClasseC, filtro3
   └─── OR entre classes ───┘  └── AND ──┘     └── outro grupo (OR com o anterior)
```

> **Nota sobre booleanos:** use sempre `TRUE` e `FALSE` em maiúsculas. Em Bonsai 0.8.5, `True` ou `true` não funcionam — isso segue a convenção EXPRESS, a linguagem formal do IFC.

---

## Parte 1 — Modos Básicos

### 1.1 Por Classe IFC

Seleciona todos os elementos de uma classe. Subtypes são incluídos automaticamente.

```
IfcDoor
```
```
IfcWall
```
```
IfcSpace
```

Várias classes ao mesmo tempo (OR entre elas):

```
IfcDoor, IfcWindow
```
```
IfcWall, IfcSlab, IfcColumn
```

Todos os elementos construtivos (superclasse):

```
IfcElement
```

---

### 1.2 Por Atributo IFC

Atributos são campos nativos da entidade IFC (como `Name`, `Description`, `ObjectType`, `Tag`, `GlobalId`). O nome do atributo deve seguir exatamente a nomenclatura IFC.

```
IfcDoor, Name=D01
```
```
IfcWall, Name=WAL-200
```
```
IfcSpace, LongName=Sala de Reunião
```

Busca por GlobalId (identifica um elemento único):

```
325Q7Fhnf67OZC$$r43uzK
```

Vários elementos por GlobalId:

```
325Q7Fhnf67OZC$$r43uzK, 2VlJ7nbF5AFfQQuRvSWexT
```

---

### 1.3 Por Tipo (Type)

O `type` refere-se ao `IfcTypeObject` vinculado ao elemento — o equivalente a "família/tipo" no Revit.

```
IfcDoor, type=Single-Flush
```
```
IfcWall, type=WAL-200
```
```
IfcColumn, type=UC-203x203x46
```

---

### 1.4 Por Propriedade (Property Set)

Propriedades ficam dentro de Property Sets (Psets). A sintaxe é `NomeDoPset.NomeDaPropriedade=Valor`.

Portas externas:

```
IfcDoor, Pset_DoorCommon.IsExternal=TRUE
```

Paredes estruturais:

```
IfcWall, Pset_WallCommon.LoadBearing=TRUE
```

Paredes com resistência ao fogo de 2 horas:

```
IfcWall, Pset_WallCommon.FireRating=2HR
```

Janelas externas:

```
IfcWindow, Pset_WindowCommon.IsExternal=TRUE
```

Elementos com status "demolir":

```
IfcElement, Pset_ElementCommon.Status=DEMOLISH
```

Verificar se propriedade existe (não é NULL):

```
IfcElement, Pset_WallCommon.FireRating != NULL
```

---

### 1.5 Por Quantitativo (Quantity Set)

Quantitativos ficam em Quantity Sets (Qtos). A sintaxe é `NomeDoQto.NomeDoQuantitativo` com operadores de comparação.

Lajes com volume líquido maior que 10 m³:

```
IfcSlab, Qto_SlabBaseQuantities.NetVolume > 10
```

Paredes com área de face maior que 20 m²:

```
IfcWall, Qto_WallBaseQuantities.GrossFootprintArea > 20
```

Portas com altura maior que 2,10 m:

```
IfcDoor, Qto_DoorBaseQuantities.Height > 2.1
```

Operadores disponíveis: `=`, `!=`, `>`, `<`, `>=`, `<=`

---

### 1.6 Por Material

Seleciona elementos que contêm um material cujo nome ou categoria corresponde ao valor.

```
IfcWall, material=concrete
```
```
IfcSlab, material=steel
```
```
IfcBeam, material=timber
```

Lajes de concreto com área maior que 50 m²:

```
IfcSlab, material=concrete, Qto_SlabBaseQuantities.GrossArea > 50
```

---

### 1.7 Por Localização Espacial

O filtro `location=` busca por contenção espacial (pavimento, zona, edifício). A hierarquia é considerada — um elemento em um espaço dentro de um pavimento também é encontrado.

```
IfcDoor, location="Level 1"
```
```
IfcWall, location="Ground Floor"
```

Portas externas no Pavimento Térreo:

```
IfcDoor, Pset_DoorCommon.IsExternal=TRUE, location="Pavimento Térreo"
```

> Use aspas quando o nome do local contiver espaços.

---

### 1.8 Por Classificação

```
IfcElement, classification=Pr_40_50_12
```

---

### 1.9 Negação e Exclusão

Excluir uma classe de um conjunto maior:

```
IfcElement, ! IfcSpace
```

Excluir um elemento específico pelo GlobalId:

```
IfcWall, ! 325Q7Fhnf67OZC$$r43uzK
```

---

### 1.10 União de Grupos (`+`)

O `+` une resultados de grupos independentes.

Todas as portas externas **mais** todas as janelas externas:

```
IfcDoor, Pset_DoorCommon.IsExternal=TRUE + IfcWindow, Pset_WindowCommon.IsExternal=TRUE
```

Lajes de concreto **mais** um elemento específico:

```
IfcSlab, material=concrete + 325Q7Fhnf67OZC$$r43uzK
```

---

## Parte 2 — Uso de Regex

Regex (expressões regulares) são envoltas em barras `/padrão/` e podem ser aplicadas em qualquer valor de filtro: atributos, nomes de Pset, propriedades, materiais, localizações e classificações.

---

### 2.1 Regex em Atributos

Portas com nome seguindo o padrão D + dois dígitos (ex: D01, D12):

```
IfcDoor, Name=/D[0-9]{2}/
```

Paredes cujo nome começa com "WAL":

```
IfcWall, Name=/^WAL/
```

Espaços cujo nome contém "sala" (case-insensitive não é garantido — prefira o padrão exato):

```
IfcSpace, LongName=/[Ss]ala/
```

---

### 2.2 Regex em Nomes de Property Set

Qualquer elemento externo — aplica regex ao **nome do Pset** para cobrir todas as classes de uma vez:

```
IfcElement, /Pset_.*Common/.IsExternal=TRUE
```

`/Pset_.*Common/` casa com `Pset_WallCommon`, `Pset_DoorCommon`, `Pset_WindowCommon`, etc.

Qualquer elemento estrutural (portante):

```
IfcWall, IfcColumn, IfcBeam, IfcFooting, /Pset_.*Common/.LoadBearing=TRUE
```

Qualquer elemento com resistência ao fogo definida (não NULL):

```
IfcElement, /Pset_.*Common/.FireRating != NULL
```

---

### 2.3 Regex em Nomes de Propriedade

Selecionar por qualquer propriedade cujo nome contenha "Rating":

```
IfcElement, /Pset_.*Common/./.*Rating/=2HR
```

---

### 2.4 Regex em Valores de Propriedade

Paredes com resistência ao fogo de 1 ou 2 horas:

```
IfcWall, Pset_WallCommon.FireRating=/[12]HR/
```

Elementos com status "NEW" ou "EXISTING":

```
IfcElement, /Pset_.*Common/.Status=/NEW|EXISTING/
```

---

### 2.5 Regex em Material

Elementos com material que contém "concrete" ou "Concrete":

```
IfcElement, material=/[Cc]oncrete/
```

Elementos com qualquer material de madeira (timber, wood, CLT):

```
IfcElement, material=/timber|wood|CLT/
```

---

### 2.6 Regex em Tipo (Type)

Colunas com tipo que começa com "UC" (Universal Column):

```
IfcColumn, type=/^UC/
```

Paredes com tipo contendo "100mm" ou "200mm":

```
IfcWall, type=/[12]00mm/
```

---

### 2.7 Regex em Localização

Qualquer elemento em pavimentos nomeados "Level" seguido de número:

```
IfcDoor, location=/Level [0-9]+/
```

---

### 2.8 Regex em Classificação

Elementos com código Uniclass que começa com "Pr_" (produtos):

```
IfcElement, classification=/Pr_.*/
```

---

## Referência Rápida

| Necessidade | Query |
|---|---|
| Todas as portas | `IfcDoor` |
| Todas as portas externas | `IfcDoor, Pset_DoorCommon.IsExternal=TRUE` |
| Todos os elementos externos | `IfcElement, /Pset_.*Common/.IsExternal=TRUE` |
| Paredes estruturais | `IfcWall, Pset_WallCommon.LoadBearing=TRUE` |
| Lajes com volume > 10 | `IfcSlab, Qto_SlabBaseQuantities.NetVolume > 10` |
| Portas no Térreo | `IfcDoor, location="Ground Floor"` |
| Portas externas no Térreo | `IfcDoor, Pset_DoorCommon.IsExternal=TRUE, location="Ground Floor"` |
| Paredes de concreto | `IfcWall, material=concrete` |
| Portas padrão D01–D99 | `IfcDoor, Name=/D[0-9]{2}/` |
| Qualquer elemento com FireRating | `IfcElement, /Pset_.*Common/.FireRating != NULL` |
| Portas + janelas externas (union) | `IfcDoor, Pset_DoorCommon.IsExternal=TRUE + IfcWindow, Pset_WindowCommon.IsExternal=TRUE` |

---

## Dicas de Uso na UI

- **Salvar uma busca:** após configurar a query, clique na seta **UP (↑)** e dê um nome. A busca fica salva no próprio arquivo `.ifc`.
- **Recuperar uma busca salva:** clique na seta **DOWN (↓)** para carregar.
- **Ver a query em texto:** clique no ícone do **funil** ao lado de "Add Search Group".
- **Múltiplos grupos:** use **"Add Search Group"** para criar grupos adicionais — cada grupo é processado independentemente e os resultados são unidos.
- **Antes de nova busca:** desselecione tudo no viewport antes de rodar um filtro, para evitar que a seleção anterior interfira no resultado.
