# Aula 2: Search - Seleção de Entidades IFC no BonsaiBIM

## 📋 Índice
1. [O que é Search/Query](#o-que-é-searchquery)
2. [Sintaxe Básica](#sintaxe-básica)
3. [Tipos IFC Comuns](#tipos-ifc-comuns)
4. [Filtros Disponíveis](#filtros-disponíveis)
5. [Exemplos Práticos](#exemplos-práticos)
6. [Exercícios](#exercícios)
7. [Recursos Adicionais](#recursos-adicionais)

---

## O que é Search/Query?

**Query** (consulta) é como você diz ao BonsaiBIM **QUAIS elementos IFC** selecionar do seu modelo.

É como uma busca no Google, mas para elementos BIM:
- "Me mostre todas as portas"
- "Me mostre apenas as portas do térreo"
- "Me mostre apenas as portas tipo P1"

### Onde usar Queries?

No BonsaiBIM, você usa queries em vários lugares:
- **Manual Quantification** - para selecionar e contar elementos
- **Cost Schedule** (na coluna Query do CSV) - para calcular custos
- **Filtros visuais** - para destacar elementos no modelo 3D

---

## Sintaxe Básica

### Estrutura geral
```
<TipoIFC>
<TipoIFC>, <filtro>="<valor>"
<TipoIFC>, <filtro1>="<valor1>", <filtro2>="<valor2>"
```

### Regras importantes

1. **Maiúsculas e minúsculas importam** em alguns casos
2. **Use aspas duplas** `"` para valores
3. **Separe filtros com vírgula** `,`
4. **Espaços são opcionais** mas ajudam na legibilidade

---

## Tipos IFC Comuns

### Estrutura
```
IfcColumn        Pilares/Colunas
IfcBeam          Vigas
IfcSlab          Lajes
IfcWall          Paredes
IfcFooting       Sapatas/Fundações
IfcPile          Estacas
```

### Arquitetura
```
IfcDoor          Portas
IfcWindow        Janelas
IfcStair         Escadas
IfcRailing       Guarda-corpos
IfcRoof          Telhados
IfcCovering      Revestimentos
IfcCurtainWall   Fachada cortina
```

### Instalações
```
IfcLightFixture  Luminárias
IfcOutlet        Tomadas/Pontos de força
IfcPipe          Tubulações
IfcDuct          Dutos
IfcCableCarrier  Eletrocalhas
```

### Outros
```
IfcFurnishing    Mobiliário
IfcSpace         Ambientes/Espaços
IfcSite          Terreno
IfcBuildingStorey Pavimento
```

**Lista completa:** [IFC 4.3 Documentation](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/)

---

## Filtros Disponíveis

O BonsaiBIM usa a sintaxe do **IfcOpenShell**. Principais filtros:

### 1. Por localização (pavimento)
```
location="<nome do pavimento>"
```

**Exemplos:**
```
IfcDoor, location="Térreo"
IfcColumn, location="1º Pavimento"
IfcWindow, location="Subsolo"
```

### 2. Por tipo
```
type="<nome do tipo>"
```

**Exemplos:**
```
IfcDoor, type="P1"
IfcWindow, type="J1"
IfcColumn, type="Pilar 20x50"
```

### 3. Por nome
```
name="<nome>"
```

**Exemplos:**
```
IfcDoor, name="Porta Principal"
IfcSpace, name="Sala 101"
```

### 4. Por tag/etiqueta
```
tag="<tag>"
```

**Exemplos:**
```
IfcColumn, tag="P1"
IfcBeam, tag="V10"
```

### 5. Por material
```
material="<material>"
```

**Exemplos:**
```
IfcWall, material="Alvenaria"
IfcSlab, material="Concreto"
```

### 6. Combinando filtros

Você pode usar **vários filtros** ao mesmo tempo:

```
IfcDoor, location="Térreo", type="P1"
IfcWindow, location="1º Pavimento", type="J1"
IfcColumn, location="Subsolo", type="Pilar 30x30"
```

---

## Exemplos Práticos

### Exemplo 1: Selecionar todos os elementos de um tipo

**Objetivo:** Ver todas as portas do modelo

```
Query: IfcDoor
```

**Resultado:** Seleciona TODAS as portas, independente de tipo ou localização

---

### Exemplo 2: Filtrar por pavimento

**Objetivo:** Ver apenas as portas do térreo

```
Query: IfcDoor, location="Térreo"
```

**Importante:** O nome do pavimento deve ser EXATAMENTE como aparece no modelo IFC.

**Como descobrir o nome correto:**
1. No BonsaiBIM, olhe a hierarquia do projeto no painel esquerdo
2. Os nomes dos `IfcBuildingStorey` são seus pavimentos
3. Exemplos comuns: "Térreo", "1º Pavimento", "Subsolo", "Cobertura"

---

### Exemplo 3: Filtrar por tipo

**Objetivo:** Ver apenas portas do tipo P1

```
Query: IfcDoor, type="P1"
```

**Como descobrir os tipos:**
1. Selecione uma porta no modelo
2. Vá em BIM → Manual Quantification
3. Veja a propriedade "ObjectType" ou "Type"
4. Use esse valor exato na query

---

### Exemplo 4: Combinar pavimento + tipo

**Objetivo:** Ver apenas portas P1 do térreo

```
Query: IfcDoor, location="Térreo", type="P1"
```

**Lógica:** Location E type (ambos devem ser verdadeiros)

---

### Exemplo 5: Estrutura de concreto por pavimento

**Objetivo:** Selecionar todos os pilares do subsolo

```
Query: IfcColumn, location="Subsolo"
```

**Objetivo:** Selecionar todas as vigas do 1º pavimento

```
Query: IfcBeam, location="1º Pavimento"
```

---

### Exemplo 6: Elementos por nome

**Objetivo:** Encontrar a porta principal

```
Query: IfcDoor, name="Porta Principal"
```

**Nota:** O filtro `name` geralmente procura correspondência parcial, então:
- `name="Porta"` pode retornar "Porta 1", "Porta Principal", "Porta de Serviço"

---

### Exemplo 7: Múltiplos elementos do mesmo tipo

**Objetivo:** Listar diferentes tipos de janelas

```
Query 1: IfcWindow, type="J1"
Query 2: IfcWindow, type="J2"
Query 3: IfcWindow, type="J3"
```

Cada query é uma linha diferente no seu levantamento.

---

## Exercícios

### Exercício 1: Básico
Escreva queries para:
1. Selecionar todas as lajes
2. Selecionar todas as janelas
3. Selecionar todos os guarda-corpos

<details>
<summary>Ver respostas</summary>

```
1. IfcSlab
2. IfcWindow
3. IfcRailing
```
</details>

---

### Exercício 2: Com filtro de localização
Seu modelo tem pavimentos: Térreo, 1º Pavimento, 2º Pavimento

Escreva queries para:
1. Todas as paredes do térreo
2. Todos os pilares do 1º pavimento
3. Todas as vigas do 2º pavimento

<details>
<summary>Ver respostas</summary>

```
1. IfcWall, location="Térreo"
2. IfcColumn, location="1º Pavimento"
3. IfcBeam, location="2º Pavimento"
```
</details>

---

### Exercício 3: Com filtro de tipo
Seu modelo tem portas: P1, P2, P3

Escreva queries para:
1. Apenas portas P1
2. Apenas portas P2
3. Portas P1 do térreo

<details>
<summary>Ver respostas</summary>

```
1. IfcDoor, type="P1"
2. IfcDoor, type="P2"
3. IfcDoor, location="Térreo", type="P1"
```
</details>

---

### Exercício 4: Caso real
Você precisa fazer um levantamento de:
- Pilares 20x50 do subsolo
- Pilares 25x60 do térreo
- Vigas V1 15x40 do 1º pavimento
- Vigas V2 20x50 do 1º pavimento

Escreva as queries.

<details>
<summary>Ver respostas</summary>

```
IfcColumn, location="Subsolo", type="Pilar 20x50"
IfcColumn, location="Térreo", type="Pilar 25x60"
IfcBeam, location="1º Pavimento", type="V1 15x40"
IfcBeam, location="1º Pavimento", type="V2 20x50"
```

**Nota:** Os nomes dos tipos devem ser EXATAMENTE como aparecem no seu modelo!
</details>

---

## Descobrindo Valores no Modelo

### Método 1: Usando a interface do BonsaiBIM

1. **Selecione um elemento** no modelo 3D
2. Vá em: **BIM → Manual Quantification**
3. No painel lateral, veja as propriedades:
   - **Name**: nome do elemento
   - **ObjectType** ou **Type**: tipo do elemento
   - **Tag**: etiqueta
4. Use esses valores EXATOS nas suas queries

### Método 2: Explorando a hierarquia

1. No painel esquerdo, expanda a árvore do projeto
2. Veja a estrutura:
   ```
   IfcProject
   └── IfcSite
       └── IfcBuilding
           ├── IfcBuildingStorey (Subsolo)    ← Nome do pavimento
           ├── IfcBuildingStorey (Térreo)     ← Nome do pavimento
           └── IfcBuildingStorey (1º Pavimento) ← Nome do pavimento
   ```

### Método 3: Teste e erro

1. Comece com uma query simples: `IfcDoor`
2. Veja quantos elementos retornam
3. Adicione filtros progressivamente:
   - `IfcDoor, location="Térreo"`
   - `IfcDoor, location="Térreo", type="P1"`

---

## Filtros Avançados (Opcional)

O IfcOpenShell suporta filtros mais complexos:

### Wildcards (curingas)
```
IfcDoor, type="P*"     # Pega P1, P2, P10, etc.
IfcWall, name="*Gesso" # Pega qualquer parede com "Gesso" no nome
```

### Operadores lógicos
```
IfcDoor OR IfcWindow          # Portas OU janelas
IfcColumn AND type="P1"       # Pilares E tipo P1
```

### Negação
```
IfcDoor NOT type="P1"         # Todas as portas EXCETO P1
```

**Para mais detalhes:** 📚 [IfcOpenShell Selector Syntax](https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html)

---

## Dicas e Boas Práticas

### ✅ Faça

1. **Sempre teste suas queries primeiro**
   - Use BIM → Manual Quantification para testar
   - Veja se retorna os elementos esperados

2. **Use nomes descritivos**
   ```
   ✅ Bom: IfcDoor, location="Térreo", type="Porta Madeira 80cm"
   ❌ Ruim: IfcDoor, type="P1"  (sem contexto)
   ```

3. **Documente os tipos do seu projeto**
   - Crie uma lista dos tipos usados (P1=porta 60cm, P2=porta 80cm, etc.)
   - Compartilhe com a equipe

4. **Comece genérico, depois especifique**
   ```
   Passo 1: IfcDoor (veja quantas portas existem)
   Passo 2: IfcDoor, location="Térreo" (veja quantas no térreo)
   Passo 3: IfcDoor, location="Térreo", type="P1" (específico)
   ```

### ❌ Evite

1. **Não invente nomes**
   - Use exatamente o que está no modelo
   - Não tente "adivinhar" tipos

2. **Não use acentos se o modelo não tiver**
   ```
   Se o modelo tem: "Terreo" (sem acento)
   Use: location="Terreo"
   Não use: location="Térreo"
   ```

3. **Não misture inglês e português sem verificar**
   - Alguns modelos usam "Ground Floor", outros "Térreo"
   - Sempre confira no modelo

---

## Resolução de Problemas

### Problema: Query não retorna nada

**Possíveis causas:**
1. Nome do tipo/pavimento está errado
2. Elementos não existem no modelo
3. Erro de digitação (maiúsculas/minúsculas)

**Solução:**
- Teste com query mais simples: apenas `IfcDoor`
- Selecione um elemento manualmente e veja suas propriedades
- Copie e cole o nome exato do modelo

---

### Problema: Query retorna elementos demais

**Causa:** Filtro muito genérico

**Solução:**
- Adicione mais filtros
- Use combinação location + type
- Verifique se há wildcards não intencionais

---

### Problema: Acentos não funcionam

**Causa:** Encoding do arquivo ou do modelo

**Solução:**
- Verifique como está escrito no modelo (pode estar sem acento)
- Use exatamente a mesma grafia
- Se necessário, renomeie no software de modelagem

---

## Resumo - Checklist de Query

Ao escrever uma query, pergunte-se:

- [ ] Qual tipo IFC quero selecionar? (IfcDoor, IfcColumn, etc.)
- [ ] Preciso filtrar por pavimento? → use `location="..."`
- [ ] Preciso filtrar por tipo? → use `type="..."`
- [ ] Os nomes estão EXATAMENTE como no modelo?
- [ ] Testei a query antes de usar no CSV?

---

## Recursos Adicionais

### Links úteis

**IfcOpenShell - Sintaxe de Seletores**
- 📚 **[Documentação oficial](https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html)**
- Referência completa sobre filtros avançados

**BonsaiBIM**
- 🌐 [Site oficial](https://bonsaibim.org/)
- 📖 [Wiki do BonsaiBIM](https://docs.bonsaibim.org/)
- 💬 [Comunidade OSArch](https://community.osarch.org/)

**IFC Schema**
- 📘 [IFC 4.3 Documentation](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/)
- Lista completa de tipos IFC

---

## Próximos Passos

Depois de dominar as queries, você estará pronto para:
- **Próxima aula (Aula 3):** Quantificação e cálculo de custos
- Usar queries na coluna Query do CSV de quantificação
- Criar levantamentos automáticos de materiais
- Gerar orçamentos paramétricos

---

*Documentação criada para BonsaiBIM 0.8.5*  
*Aula 2: Search e Seleção de Entidades IFC*  
*Última atualização: Abril 2026*
