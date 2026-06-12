# AULA 2 - Referências de Queries (Search BonsaiBIM)

Tabela de referência com todas as queries apresentadas na aula integrada `AULA_2_Search_BonsaiBIM.md` e o que cada uma faz.

| Query | Descrição |
|---|---|
| `IfcDoor` | Seleciona todas as portas. |
| `IfcWall` | Seleciona todas as paredes. |
| `IfcSpace` | Seleciona todos os espaços. |
| `IfcDoor, IfcWindow` | Seleciona portas e janelas (OR entre classes). |
| `IfcWall, IfcSlab, IfcColumn` | Seleciona paredes, lajes e pilares. |
| `IfcElement` | Seleciona todos os elementos construtivos. |
| `IfcDoor, location="Térreo"` | Seleciona portas do pavimento Térreo. |
| `IfcColumn, location="1º Pavimento"` | Seleciona pilares do 1º pavimento. |
| `IfcWindow, location="Subsolo"` | Seleciona janelas do Subsolo. |
| `IfcDoor, location="Ground Floor"` | Seleciona portas no pavimento Ground Floor. |
| `IfcDoor, location="Pavimento Térreo"` | Seleciona portas no local chamado Pavimento Térreo. |
| `IfcDoor, type="P1"` | Seleciona portas do tipo P1. |
| `IfcWindow, type="J1"` | Seleciona janelas do tipo J1. |
| `IfcColumn, type="Pilar 20x50"` | Seleciona pilares com tipo Pilar 20x50. |
| `IfcDoor, type=Single-Flush` | Seleciona portas do tipo Single-Flush. |
| `IfcWall, type=WAL-200` | Seleciona paredes do tipo WAL-200. |
| `IfcColumn, type=UC-203x203x46` | Seleciona colunas tipo UC-203x203x46. |
| `IfcDoor, name="Porta Principal"` | Seleciona portas com nome Porta Principal. |
| `IfcSpace, name="Sala 101"` | Seleciona espaços com nome Sala 101. |
| `IfcDoor, Name=D01` | Seleciona portas com atributo Name igual a D01. |
| `IfcWall, Name=WAL-200` | Seleciona paredes com atributo Name igual a WAL-200. |
| `IfcSpace, LongName=Sala de Reunião` | Seleciona espaços com LongName Sala de Reunião. |
| `IfcColumn, tag="P1"` | Seleciona elementos com tag P1 na classe IfcColumn. |
| `IfcBeam, tag="V10"` | Seleciona vigas com tag V10. |
| `325Q7Fhnf67OZC$$r43uzK` | Seleciona o elemento com esse GlobalId. |
| `325Q7Fhnf67OZC$$r43uzK, 2VlJ7nbF5AFfQQuRvSWexT` | Seleciona dois elementos pelos GlobalIds informados. |
| `IfcDoor, Pset_DoorCommon.IsExternal=TRUE` | Seleciona portas externas. |
| `IfcWall, Pset_WallCommon.LoadBearing=TRUE` | Seleciona paredes estruturais (portantes). |
| `IfcWall, Pset_WallCommon.FireRating=2HR` | Seleciona paredes com resistência ao fogo de 2 horas. |
| `IfcWindow, Pset_WindowCommon.IsExternal=TRUE` | Seleciona janelas externas. |
| `IfcElement, Pset_ElementCommon.Status=DEMOLISH` | Seleciona elementos marcados para demolição. |
| `IfcElement, Pset_WallCommon.FireRating != NULL` | Seleciona elementos com FireRating preenchido nesse Pset. |
| `IfcSlab, Qto_SlabBaseQuantities.NetVolume > 10` | Seleciona lajes com volume líquido maior que 10. |
| `IfcWall, Qto_WallBaseQuantities.GrossFootprintArea > 20` | Seleciona paredes com área de projeção maior que 20. |
| `IfcDoor, Qto_DoorBaseQuantities.Height > 2.1` | Seleciona portas com altura maior que 2,1 m. |
| `IfcSlab, Qto_SlabBaseQuantities.GrossArea > 50` | Seleciona lajes com área bruta maior que 50. |
| `IfcWall, material="Alvenaria"` | Seleciona paredes com material Alvenaria. |
| `IfcSlab, material="Concreto"` | Seleciona lajes com material Concreto. |
| `IfcWall, material=concrete` | Seleciona paredes com material concrete. |
| `IfcSlab, material=steel` | Seleciona lajes com material steel. |
| `IfcBeam, material=timber` | Seleciona vigas com material timber. |
| `IfcSlab, material=concrete, Qto_SlabBaseQuantities.GrossArea > 50` | Seleciona lajes de concreto com área bruta maior que 50. |
| `IfcElement, classification=Pr_40_50_12` | Seleciona elementos classificados com o código informado. |
| `IfcDoor, location="Térreo", type="P1"` | Seleciona portas P1 no Térreo. |
| `IfcWindow, location="1º Pavimento", type="J1"` | Seleciona janelas J1 no 1º pavimento. |
| `IfcColumn, location="Subsolo", type="Pilar 30x30"` | Seleciona pilares 30x30 no Subsolo. |
| `IfcDoor, Pset_DoorCommon.IsExternal=TRUE + IfcWindow, Pset_WindowCommon.IsExternal=TRUE` | União: portas externas mais janelas externas. |
| `IfcSlab, material=concrete + 325Q7Fhnf67OZC$$r43uzK` | União: lajes de concreto mais um elemento específico por GlobalId. |
| `IfcElement, ! IfcSpace` | Seleciona IfcElement excluindo espaços. |
| `IfcWall, ! 325Q7Fhnf67OZC$$r43uzK` | Seleciona paredes excluindo o GlobalId indicado. |
| `IfcDoor, Name=/D[0-9]{2}/` | Seleciona portas com Name no padrão D01, D02, etc. |
| `IfcWall, Name=/^WAL/` | Seleciona paredes com Name iniciando por WAL. |
| `IfcSpace, LongName=/[Ss]ala/` | Seleciona espaços com LongName contendo Sala/sala. |
| `IfcElement, /Pset_.*Common/.IsExternal=TRUE` | Seleciona elementos externos usando regex no nome do Pset. |
| `IfcWall, IfcColumn, IfcBeam, IfcFooting, /Pset_.*Common/.LoadBearing=TRUE` | Seleciona elementos estruturais portantes em múltiplas classes. |
| `IfcElement, /Pset_.*Common/.FireRating != NULL` | Seleciona elementos com FireRating preenchido em Psets Common. |
| `IfcElement, /Pset_.*Common/./.*Rating/=2HR` | Seleciona elementos com qualquer propriedade *Rating* igual a 2HR em Psets Common. |
| `IfcWall, Pset_WallCommon.FireRating=/[12]HR/` | Seleciona paredes com FireRating 1HR ou 2HR. |
| `IfcElement, /Pset_.*Common/.Status=/NEW|EXISTING/` | Seleciona elementos com Status NEW ou EXISTING. |
| `IfcElement, material=/[Cc]oncrete/` | Seleciona elementos com material concrete/Concrete. |
| `IfcElement, material=/timber|wood|CLT/` | Seleciona elementos com materiais de madeira (timber, wood, CLT). |
| `IfcColumn, type=/^UC/` | Seleciona colunas com tipo iniciado por UC. |
| `IfcWall, type=/[12]00mm/` | Seleciona paredes com tipo contendo 100mm ou 200mm. |
| `IfcDoor, location=/Level [0-9]+/` | Seleciona portas em pavimentos no padrão Level + número. |
| `IfcElement, classification=/Pr_.*/` | Seleciona elementos cuja classificação começa com Pr_. |
| `IfcColumn, location="Subsolo", type="Pilar 20x50"` | Caso prático: pilares 20x50 do Subsolo. |
| `IfcColumn, location="Térreo", type="Pilar 25x60"` | Caso prático: pilares 25x60 do Térreo. |
| `IfcBeam, location="1º Pavimento", type="V1 15x40"` | Caso prático: vigas V1 15x40 no 1º pavimento. |
| `IfcBeam, location="1º Pavimento", type="V2 20x50"` | Caso prático: vigas V2 20x50 no 1º pavimento. |
