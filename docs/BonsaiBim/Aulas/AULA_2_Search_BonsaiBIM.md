# Aula 2: Search no BonsaiBIM (conteúdo integrado)

> Material integrado das aulas AULA2_a e AULA2_b, sem repetições.

## Objetivo

Aprender a selecionar entidades IFC no BonsaiBIM com queries para:

- filtrar elementos por classe, pavimento, tipo, propriedade, material e quantitativos;
- combinar filtros para usos de quantificação, custo e conferência de modelo;
- usar regex, negação e união de grupos em casos avançados.

## Onde usar queries no BonsaiBIM

- Manual Quantification
- Cost Schedule (coluna `Query` em CSV)
- Filtros visuais no modelo 3D

## Acesso na interface

`Properties Panel (N) -> Project Overview -> Grouping and Filtering`

- Clique no ícone de funil ao lado de `Add Search Group` para editar/ver query.
- Use `Add Search Group` para criar grupos adicionais.
- Use seta `UP` para salvar busca e seta `DOWN` para recuperar.

## Sintaxe essencial

Estrutura geral:

```text
<TipoIFC>
<TipoIFC>, <filtro>="<valor>"
<TipoIFC>, <filtro1>="<valor1>", <filtro2>="<valor2>"
```

Regras:

1. Dentro de um grupo, filtros separados por vírgula funcionam como `AND`.
2. Classes IFC separadas por vírgula funcionam como `OR`.
3. Grupos separados por `+` funcionam como união (`OR` entre grupos).
4. Use `TRUE` e `FALSE` em maiúsculas para booleanos.
5. Em nomes com espaço, use aspas duplas.

## Tipos IFC comuns

```text
IfcColumn, IfcBeam, IfcSlab, IfcWall, IfcFooting, IfcPile
IfcDoor, IfcWindow, IfcStair, IfcRailing, IfcRoof, IfcCovering
IfcLightFixture, IfcOutlet, IfcPipe, IfcDuct, IfcCableCarrier
IfcFurnishing, IfcSpace, IfcSite, IfcBuildingStorey, IfcElement
```

Referência completa: [IFC 4.3 Documentation](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/)

## Filtros principais com exemplos

### 1) Classe IFC

```text
IfcDoor
IfcWall
IfcSpace
IfcDoor, IfcWindow
IfcWall, IfcSlab, IfcColumn
IfcElement
```

### 2) Localização (pavimento/estrutura espacial)

```text
IfcDoor, location="Térreo"
IfcColumn, location="1º Pavimento"
IfcWindow, location="Subsolo"
IfcDoor, location="Ground Floor"
IfcDoor, location="Pavimento Térreo"
```

### 3) Tipo (`type`)

```text
IfcDoor, type="P1"
IfcWindow, type="J1"
IfcColumn, type="Pilar 20x50"
IfcDoor, type=Single-Flush
IfcWall, type=WAL-200
IfcColumn, type=UC-203x203x46
```

### 4) Atributos IFC (`Name`, `LongName`, `Tag`, `GlobalId`)

```text
IfcDoor, name="Porta Principal"
IfcSpace, name="Sala 101"
IfcDoor, Name=D01
IfcWall, Name=WAL-200
IfcSpace, LongName=Sala de Reunião
IfcColumn, tag="P1"
IfcBeam, tag="V10"
325Q7Fhnf67OZC$$r43uzK
325Q7Fhnf67OZC$$r43uzK, 2VlJ7nbF5AFfQQuRvSWexT
```

### 5) Property Sets (Psets)

```text
IfcDoor, Pset_DoorCommon.IsExternal=TRUE
IfcWall, Pset_WallCommon.LoadBearing=TRUE
IfcWall, Pset_WallCommon.FireRating=2HR
IfcWindow, Pset_WindowCommon.IsExternal=TRUE
IfcElement, Pset_ElementCommon.Status=DEMOLISH
IfcElement, Pset_WallCommon.FireRating != NULL
```

### 6) Quantity Sets (Qtos)

```text
IfcSlab, Qto_SlabBaseQuantities.NetVolume > 10
IfcWall, Qto_WallBaseQuantities.GrossFootprintArea > 20
IfcDoor, Qto_DoorBaseQuantities.Height > 2.1
IfcSlab, Qto_SlabBaseQuantities.GrossArea > 50
```

### 7) Material

```text
IfcWall, material="Alvenaria"
IfcSlab, material="Concreto"
IfcWall, material=concrete
IfcSlab, material=steel
IfcBeam, material=timber
IfcSlab, material=concrete, Qto_SlabBaseQuantities.GrossArea > 50
```

### 8) Classificação

```text
IfcElement, classification=Pr_40_50_12
```

### 9) Combinações e união de grupos

```text
IfcDoor, location="Térreo", type="P1"
IfcWindow, location="1º Pavimento", type="J1"
IfcColumn, location="Subsolo", type="Pilar 30x30"
IfcDoor, Pset_DoorCommon.IsExternal=TRUE + IfcWindow, Pset_WindowCommon.IsExternal=TRUE
IfcSlab, material=concrete + 325Q7Fhnf67OZC$$r43uzK
```

### 10) Negação e exclusão

```text
IfcElement, ! IfcSpace
IfcWall, ! 325Q7Fhnf67OZC$$r43uzK
```

### 11) Regex (avançado)

```text
IfcDoor, Name=/D[0-9]{2}/
IfcWall, Name=/^WAL/
IfcSpace, LongName=/[Ss]ala/
IfcElement, /Pset_.*Common/.IsExternal=TRUE
IfcWall, IfcColumn, IfcBeam, IfcFooting, /Pset_.*Common/.LoadBearing=TRUE
IfcElement, /Pset_.*Common/.FireRating != NULL
IfcElement, /Pset_.*Common/./.*Rating/=2HR
IfcWall, Pset_WallCommon.FireRating=/[12]HR/
IfcElement, /Pset_.*Common/.Status=/NEW|EXISTING/
IfcElement, material=/[Cc]oncrete/
IfcElement, material=/timber|wood|CLT/
IfcColumn, type=/^UC/
IfcWall, type=/[12]00mm/
IfcDoor, location=/Level [0-9]+/
IfcElement, classification=/Pr_.*/
```

## Como descobrir os valores corretos para query

1. Selecione um elemento no modelo 3D.
2. Abra `BIM -> Manual Quantification`.
3. Confira os valores reais de `Name`, `ObjectType/Type`, `Tag` e demais propriedades.
4. Na árvore do projeto, verifique os nomes exatos de `IfcBuildingStorey` para usar em `location`.
5. Comece simples e refine progressivamente.

Exemplo de refinamento:

1. Comece com uma classe IFC.
2. Adicione `location`.
3. Adicione `type` para chegar ao recorte final.

## Casos práticos diretos

```text
IfcColumn, location="Subsolo", type="Pilar 20x50"
IfcColumn, location="Térreo", type="Pilar 25x60"
IfcBeam, location="1º Pavimento", type="V1 15x40"
IfcBeam, location="1º Pavimento", type="V2 20x50"
```

## Erros comuns e solução

1. Query sem retorno: valide grafia exata de pavimento/tipo/propriedade no modelo.
2. Retorno excessivo: adicione filtros (`location`, `type`, Psets, Qto).
3. Problemas com acento: use exatamente a grafia que está no IFC.
4. Booleanos inválidos: use `TRUE/FALSE`, não `true/false`.

## Checklist rápido

- Defini a classe IFC correta?
- Preciso restringir por `location`?
- Preciso restringir por `type`?
- Usei valores exatamente como no modelo?
- Testei primeiro uma query mais genérica?

## Exercícios sugeridos

1. Escreva query para todas as lajes, janelas e guarda-corpos.
2. Escreva query para paredes do térreo, pilares do 1º pavimento e vigas do 2º pavimento.
3. Escreva query para portas P1, portas P2 e portas P1 do térreo.

Consulte a tabela de referência no arquivo de apoio: `AULA_2_search_references.md`.
