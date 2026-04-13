# Documentação: Quantificação no BonsaiBIM 0.8.5

## 🚨 ALERTA IMPORTANTE - Leia antes de começar!

### Problema com Configuração Regional Brasileira

No Brasil usamos **vírgula (,)** para separar decimais, mas o formato CSV usa vírgula para separar campos!

```
❌ ERRADO (formato brasileiro): 10,5
✅ CORRETO (formato CSV): 10.5
```

**Se você salvar o CSV com vírgulas nos decimais, o BonsaiBIM NÃO vai calcular os custos!**

👉 **Vá direto para a seção "[Como Baixar e Editar o CSV](#como-baixar-e-editar-o-csv)"** para instruções detalhadas de como salvar corretamente em cada programa.

**Recomendação:** Use **Google Sheets** (mais fácil para iniciantes) - veja as instruções completas na seção 2.2.

---

## 📋 Índice
1. [Conceitos Básicos](#conceitos-básicos)
2. [Estrutura do CSV](#estrutura-do-csv)
3. [Como Baixar e Editar o CSV](#como-baixar-e-editar-o-csv)
4. [Propriedades Comuns (Property)](#propriedades-comuns)
5. [Exemplos de Query](#exemplos-de-query)
6. [Casos de Uso Práticos](#casos-de-uso-práticos)
7. [Dicas e Boas Práticas](#dicas-e-boas-práticas)

---

## Conceitos Básicos

### Estrutura de colunas do CSV

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| **Index** | Nível hierárquico (1=total, 2=grupo, 3=subgrupo, etc.) | `3` |
| **Identification** | Código/ID do item (geralmente vazio) | vazio |
| **Name** | Nome descritivo do item | `Pilares` |
| **Quantity** | Quantidade (calculada automaticamente pelo BonsaiBIM) | vazio |
| **Unit** | Unidade de medida | `m³`, `un`, `m²` |
| **Value** | Preço unitário (APENAS para itens de trabalho, NÃO para totalizadores) | `10.0` |
| **TotalPrice** | Preço total (calculado automaticamente) | vazio |
| **Property** | QUAL propriedade IFC quantificar | `GrossVolume`, `Count`, `NetArea` |
| **Query** | QUAIS entidades IFC selecionar e filtrar | `IfcColumn`, `IfcDoor, type="P1"` |

### Regra de ouro para Value

✅ **Itens de trabalho** (linhas com Property e Query preenchidos) → **TÊM Value**
```csv
3,,Pilares,,m³,10.0,,GrossVolume,IfcColumn
```

❌ **Totalizadores e grupos** (linhas sem Property/Query) → **SEM Value**
```csv
1,,Total,,,,,,
2,,Concreto,,,,,,
```

---

## Estrutura do CSV

### Template básico
```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Categoria Principal,,,,,,
3,,Subcategoria,,,,,,
4,,Item de Trabalho,,unidade,preço,,Property,Query
```

### Exemplo completo
```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
3,,Pilares - Total,,,,,GrossVolume,IfcColumn
4,,Pilares Térreo,,m³,450.00,,GrossVolume,"IfcColumn, location=""Térreo"""
4,,Pilares 1º Pavimento,,m³,450.00,,GrossVolume,"IfcColumn, location=""1º Pavimento"""
3,,Vigas - Total,,,,,GrossVolume,IfcBeam
4,,Vigas Térreo,,m³,420.00,,GrossVolume,"IfcBeam, location=""Térreo"""
```

---

## Como Baixar e Editar o CSV

### 1️⃣ Exportar CSV do BonsaiBIM

1. Abra seu projeto no BonsaiBIM
2. Vá em: **BIM → Cost**
3. Se já tem um schedule, clique em **"Export spreadsheet"**
4. Salve o arquivo (ex: `meu_orcamento.csv`)

**OU** crie um CSV do zero usando os templates desta documentação.

### 2️⃣ Editar o CSV

## ⚠️ ATENÇÃO: Configuração Regional Brasileira

**PROBLEMA:** No Brasil usamos vírgula (,) para decimais, mas o CSV usa vírgula para separar campos!
- ❌ Formato brasileiro: `10,5` (dez vírgula cinco)
- ✅ Formato CSV correto: `10.5` (dez PONTO cinco)

**SOLUÇÃO:** Siga as instruções específicas para cada programa abaixo.

---

## 📊 Opção A: Google Sheets (RECOMENDADO para alunos)

### Passo 1: Importar o CSV no Google Sheets

1. Acesse [Google Sheets](https://sheets.google.com)
2. Clique em **Arquivo → Importar**
3. Faça upload do arquivo CSV
4. Na janela de importação, configure:
   - **Tipo de separador**: Vírgula
   - **Converter texto em números e datas**: ✅ MARQUE esta opção
5. Clique em **Importar dados**

### Passo 2: Editar normalmente

- Você pode usar vírgula normalmente ao digitar números (ex: `10,5`)
- O Google Sheets aceita tanto vírgula quanto ponto
- Exemplo: Digite `450,00` ou `450.00` - ambos funcionam

### Passo 3: Baixar como CSV CORRETAMENTE

🚨 **CRÍTICO:** O Google Sheets tem um BUG que salva decimais com vírgula!

**MÉTODO CORRETO (passo a passo):**

1. **Primeiro, ajuste a configuração regional:**
   - Clique em **Arquivo → Configurações**
   - Em **Geral → Localidade**, mude para **Estados Unidos**
   - Clique em **Salvar configurações**
   
2. **Agora faça o download:**
   - Clique em **Arquivo → Fazer download → Valores separados por vírgula (.csv)**
   - O arquivo será salvo com PONTO como separador decimal ✅

3. **Após o download, volte a configuração:**
   - **Arquivo → Configurações → Localidade → Brasil** (opcional)

### Verificação rápida

Após baixar, abra o arquivo CSV em um editor de texto (Bloco de Notas) e confira:

```csv
✅ CORRETO:
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn

❌ ERRADO (não vai funcionar):
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
```

---

## 📊 Opção B: LibreOffice Calc

### Passo 1: Abrir o CSV

1. Abra o LibreOffice Calc
2. **Arquivo → Abrir**
3. Selecione o arquivo CSV
4. Na janela **Importação de Texto**, configure:
   - **Conjunto de caracteres**: Unicode (UTF-8)
   - **Separado por**: marque apenas **Vírgula**
   - **Separador de texto**: `"` (aspas duplas)
   - ⚠️ **Importante:** Em baixo, na visualização, verifique se as colunas estão separadas corretamente
5. Clique em **OK**

### Passo 2: Editar

- Digite números normalmente com vírgula: `450,00`
- O LibreOffice converte automaticamente

### Passo 3: Salvar CORRETAMENTE

🚨 **ATENÇÃO:** Não use apenas "Salvar"! Siga estes passos:

1. **Arquivo → Salvar Como**
2. **Tipo de arquivo**: escolha **Texto CSV (.csv)**
3. ⚠️ **Uma janela vai aparecer perguntando sobre o formato** - clique em **Usar formato Texto CSV**
4. **Janela "Exportar Texto"** - AQUI É CRUCIAL:
   - **Conjunto de caracteres**: Unicode (UTF-8)
   - **Separador de campo**: `,` (vírgula)
   - **Separador de texto**: `"` (aspas duplas)
   - 🔴 **MAIS IMPORTANTE:** 
     - Encontre a opção **"Separador decimal"** ou vá em **"Outras opções"**
     - MUDE o separador decimal de `,` para `.` (PONTO)
   - Se não encontrar essa opção, use este truque:
     - Antes de salvar, vá em **Ferramentas → Opções → Configurações de Idioma → Idiomas**
     - Mude **Localidade** para **Inglês (EUA)**
     - Salve o CSV
     - Volte a localidade para Português (Brasil)
5. Clique em **OK**

### Verificação

Abra o arquivo salvo no Bloco de Notas e confira se os decimais estão com PONTO:
```csv
✅ 450.00  (correto)
❌ 450,00  (errado)
```

---

## 📊 Opção C: Microsoft Excel

### Passo 1: Abrir o CSV

**Método A (Abrir diretamente - pode dar problema):**
- Duplo clique no arquivo CSV
- ⚠️ Pode não separar as colunas corretamente

**Método B (Importar - RECOMENDADO):**
1. Abra o Excel (planilha em branco)
2. **Dados → Obter Dados Externos → De Texto/CSV** (ou **Dados → De Texto/CSV** em versões mais novas)
3. Selecione o arquivo CSV
4. Configure:
   - **Origem do arquivo**: 65001: Unicode (UTF-8)
   - **Delimitador**: Vírgula
5. Clique em **Carregar**

### Passo 2: Editar

- Digite valores com vírgula normalmente: `450,00`

### Passo 3: Salvar CORRETAMENTE

🚨 **CRÍTICO:** O Excel brasileiro salva com vírgula! Use este método:

**Opção 1: Mudar configuração regional do Windows (temporariamente)**

1. Antes de salvar no Excel, mude a configuração do Windows:
   - Windows: **Painel de Controle → Relógio e Região → Região**
   - Clique em **Configurações Adicionais**
   - Na aba **Números**, mude:
     - **Símbolo decimal**: de `,` para `.`
   - Clique em **OK**
2. No Excel: **Arquivo → Salvar Como**
3. **Tipo de arquivo**: CSV (separado por vírgulas)
4. Salve
5. Volte às configurações do Windows e restaure a vírgula como decimal

**Opção 2: Usar o Power Query (Excel 2016+)**

1. Após editar, selecione toda a planilha
2. **Dados → De Tabela/Intervalo**
3. No Power Query, clique com botão direito na coluna de valores numéricos
4. **Alterar Tipo → Número Decimal**
5. **Arquivo → Fechar e Carregar Para**
6. Salve como CSV

**Opção 3: MAIS FÁCIL - Use o Google Sheets!**
- Se o Excel estiver dando problema, copie os dados para o Google Sheets
- Siga as instruções do Google Sheets acima

---

## ✏️ Opção D: Editor de Texto (VS Code, Notepad++, Bloco de Notas)

**Para usuários avançados ou quando precisa ter certeza absoluta:**

- ✅ Sempre salva exatamente o que você digita
- ✅ Sem conversões automáticas
- ✅ Total controle sobre o formato
- ⚠️ Você precisa digitar PONTO manualmente: `450.00`

**Recomendado:**
- **VS Code** (com extensão Rainbow CSV para visualizar melhor)
- **Notepad++** (leve e confiável)

**Salvar:**
- **Codificação**: UTF-8
- Digite valores com PONTO: `10.0`, `450.00`

---

## 📋 Resumo: Qual ferramenta usar?

| Ferramenta | Dificuldade | Recomendação |
|------------|-------------|--------------|
| **Google Sheets** | ⭐⭐ Média | ✅ **MELHOR para alunos** - Só lembrar de mudar localidade antes de baixar |
| **LibreOffice Calc** | ⭐⭐⭐ Difícil | ⚠️ Funciona, mas configurações são confusas |
| **Excel** | ⭐⭐⭐⭐ Muito difícil | ❌ Evite - muito complicado configurar no Brasil |
| **Editor de texto** | ⭐ Fácil | ✅ Perfeito se você é técnico |

---

## 🎓 Instruções para Alunos (Resumo)

### Se usar Google Sheets:

1. ✅ Importe o CSV no Google Sheets
2. ✅ Edite normalmente (pode usar vírgula ao digitar: 450,00)
3. 🔴 **ANTES de baixar**: Arquivo → Configurações → Localidade → **Estados Unidos**
4. ✅ Baixe: Arquivo → Fazer download → CSV
5. ✅ (Opcional) Volte a localidade para Brasil

### Se usar LibreOffice:

1. ✅ Ao abrir: UTF-8, separador vírgula
2. ✅ Edite normalmente
3. 🔴 **Ao salvar**: Salvar Como → CSV → Na janela que abrir, procure mudar separador decimal para PONTO
4. ✅ Se não achar a opção, mude a localidade para Inglês antes de salvar

### Se usar Excel:

1. ❌ **Não recomendado** - use Google Sheets!
2. Se insistir: mude configuração regional do Windows antes de salvar

---

## ✅ Como verificar se está correto

Após salvar o CSV, abra-o no **Bloco de Notas** ou **Notepad** e procure pelas linhas de valores:

```csv
CORRETO ✅
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn
3,,Vigas,,m³,420.50,,GrossVolume,IfcBeam

ERRADO ❌ (BonsaiBIM NÃO vai calcular os custos!)
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
3,,Vigas,,m³,420,50,,GrossVolume,IfcBeam
```

Se ver `450,00` em vez de `450.00`, refaça o processo de salvar seguindo as instruções acima!

### 3️⃣ Importar CSV de volta

1. No BonsaiBIM: **BIM → Cost**
2. Clique em **"Linked CSV"**
3. Selecione seu arquivo CSV editado
4. O BonsaiBIM calculará automaticamente as quantidades

### 4️⃣ Atualizar dados

- O CSV fica **vinculado** ao projeto
- Sempre que você modificar o modelo IFC, clique no botão de **refresh** no painel Cost
- As quantidades serão recalculadas automaticamente

---

## Propriedades Comuns (Property)

A coluna **Property** define QUAL propriedade do IFC será quantificada:

| Property | Descrição | Unidade comum | Exemplo de uso |
|----------|-----------|---------------|----------------|
| `GrossVolume` | Volume bruto do elemento | m³ | Concreto, alvenaria |
| `NetVolume` | Volume líquido (descontando vazios) | m³ | Cálculos precisos |
| `NetArea` | Área líquida da superfície | m² | Paredes, pisos |
| `GrossArea` | Área bruta da superfície | m² | Revestimentos |
| `Length` | Comprimento do elemento | m | Vigas, tubulações |
| `Width` | Largura | m | Elementos específicos |
| `Height` | Altura | m | Paredes, pilares |
| `Count` | Contagem de elementos | un | Portas, janelas, luminárias |
| `Perimeter` | Perímetro | m | Rodapés, guarnições |

### Propriedades customizadas

Você também pode usar propriedades customizadas do seu modelo:
```csv
Property: Peso
Property: Resistencia
Property: Fabricante
```

---

## Exemplos de Query

A coluna **Query** define QUAIS elementos IFC selecionar e como filtrá-los.

O BonsaiBIM usa a sintaxe de seletores do **IfcOpenShell**. Para referência completa sobre a sintaxe e recursos avançados, consulte:
📚 **[Documentação oficial do IfcOpenShell - Selector Syntax](https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html)**

### Sintaxe básica
```
Query: <TipoIFC>
Query: <TipoIFC>, <filtro1>="<valor1>"
Query: <TipoIFC>, <filtro1>="<valor1>", <filtro2>="<valor2>"
```

### 1. Selecionar todos os elementos de um tipo
```csv
Query: IfcColumn          # Todas as colunas
Query: IfcBeam            # Todas as vigas
Query: IfcSlab            # Todas as lajes
Query: IfcWall            # Todas as paredes
Query: IfcDoor            # Todas as portas
Query: IfcWindow          # Todas as janelas
```

### 2. Filtrar por pavimento (location)
```csv
Query: "IfcColumn, location=""Térreo"""
Query: "IfcBeam, location=""1º Pavimento"""
Query: "IfcSlab, location=""2º Pavimento"""
Query: "IfcDoor, location=""Cobertura"""
```

### 3. Filtrar por tipo (type)
```csv
Query: "IfcDoor, type=""P1"""
Query: "IfcDoor, type=""P2"""
Query: "IfcWindow, type=""J1"""
Query: "IfcColumn, type=""Pilar 20x50"""
```

### 4. Combinar filtros (location + type)
```csv
Query: "IfcDoor, location=""Térreo"", type=""P1"""
Query: "IfcWindow, location=""1º Pavimento"", type=""J1"""
Query: "IfcColumn, location=""Subsolo"", type=""Pilar 30x30"""
```

### 5. Outros filtros possíveis

**Por nome (name):**
```csv
Query: "IfcDoor, name=""Porta Principal"""
```

**Por material:**
```csv
Query: "IfcWall, material=""Alvenaria"""
```

**Por tag:**
```csv
Query: "IfcColumn, tag=""P1"""
```

---

## Casos de Uso Práticos

### 📦 Caso 1: Quantificar concreto por pavimento

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
3,,Concreto - Subsolo,,m³,450.00,,GrossVolume,"IfcColumn, location=""Subsolo"""
3,,Concreto - Térreo,,m³,450.00,,GrossVolume,"IfcColumn, location=""Térreo"""
3,,Concreto - 1º Pavimento,,m³,450.00,,GrossVolume,"IfcColumn, location=""1º Pavimento"""
```

**Como editar:**
1. Exporte o CSV
2. Adicione uma linha para cada pavimento
3. Altere apenas o campo `location=""<nome do pavimento>"`
4. O nome do pavimento deve ser EXATAMENTE como aparece no modelo IFC (IfcBuildingStorey)
5. Importe de volta

### 🚪 Caso 2: Quantificar portas por tipo

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Esquadrias,,,,,,
3,,Portas - Subtotal,,,,,Count,IfcDoor
4,,Porta P1 (60x210cm),,,un,150.00,,Count,"IfcDoor, type=""P1"""
4,,Porta P2 (70x210cm),,,un,180.00,,Count,"IfcDoor, type=""P2"""
4,,Porta P3 (80x210cm),,,un,200.00,,Count,"IfcDoor, type=""P3"""
4,,Porta P4 (90x210cm),,,un,220.00,,Count,"IfcDoor, type=""P4"""
```

**Como editar:**
1. Selecione uma porta no modelo e veja o valor da propriedade "Type"
2. Crie uma linha para cada tipo diferente
3. Use `Property: Count` (para contar unidades)
4. Use `Unit: un` (unidade)
5. Ajuste o `Value` (preço) de cada tipo

### 🪟 Caso 3: Quantificar janelas por pavimento E tipo

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Esquadrias,,,,,,
3,,Janelas - Térreo,,,,,Count,"IfcWindow, location=""Térreo"""
4,,J1 - Térreo,,,un,180.00,,Count,"IfcWindow, location=""Térreo"", type=""J1"""
4,,J2 - Térreo,,,un,250.00,,Count,"IfcWindow, location=""Térreo"", type=""J2"""
3,,Janelas - 1º Pavimento,,,,,Count,"IfcWindow, location=""1º Pavimento"""
4,,J1 - 1º Pavimento,,,un,180.00,,Count,"IfcWindow, location=""1º Pavimento"", type=""J1"""
4,,J2 - 1º Pavimento,,,un,250.00,,Count,"IfcWindow, location=""1º Pavimento"", type=""J2"""
```

### 🧱 Caso 4: Quantificar paredes por área

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Alvenaria e Revestimentos,,,,,,
3,,Paredes - Área Total,,,,,NetArea,IfcWall
4,,Alvenaria de Vedação,,m²,45.00,,NetArea,"IfcWall, type=""Alvenaria Vedação"""
4,,Alvenaria Estrutural,,m²,65.00,,NetArea,"IfcWall, type=""Alvenaria Estrutural"""
3,,Revestimento Cerâmico,,m²,85.00,,NetArea,"IfcWall, location=""Banheiros"""
```

### 🏗️ Caso 5: Quantificar elementos estruturais completos

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
3,,Pilares,,,,,GrossVolume,IfcColumn
4,,Pilares 20x50,,m³,450.00,,GrossVolume,"IfcColumn, type=""P1 20x50"""
4,,Pilares 25x60,,m³,450.00,,GrossVolume,"IfcColumn, type=""P2 25x60"""
3,,Vigas,,,,,GrossVolume,IfcBeam
4,,Vigas V1 15x40,,m³,420.00,,GrossVolume,"IfcBeam, type=""V1 15x40"""
4,,Vigas V2 20x50,,m³,420.00,,GrossVolume,"IfcBeam, type=""V2 20x50"""
3,,Lajes,,,,,GrossVolume,IfcSlab
4,,Laje h=12cm,,m³,380.00,,GrossVolume,"IfcSlab, type=""L1 h12"""
4,,Laje h=15cm,,m³,380.00,,GrossVolume,"IfcSlab, type=""L2 h15"""
```

**Como editar:**
1. Exporte o CSV
2. Para cada tipo de elemento estrutural, crie uma linha
3. Verifique os nomes de tipos no seu modelo IFC
4. Ajuste os preços unitários conforme sua composição de custos

### 🔌 Caso 6: Quantificar instalações elétricas

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Instalações Elétricas,,,,,,
3,,Luminárias,,,,,Count,IfcLightFixture
4,,Luminária LED 20W,,,un,85.00,,Count,"IfcLightFixture, type=""LED 20W"""
4,,Luminária LED 40W,,,un,120.00,,Count,"IfcLightFixture, type=""LED 40W"""
3,,Tomadas,,,,,Count,IfcOutlet
4,,Tomada 10A,,,un,25.00,,Count,"IfcOutlet, type=""10A"""
4,,Tomada 20A,,,un,35.00,,Count,"IfcOutlet, type=""20A"""
```

---

## Dicas e Boas Práticas

### ✅ DO (Faça)

1. **Use aspas duplas nos filtros**
   ```csv
   Query: "IfcDoor, type=""P1"""
   ```

2. **Mantenha hierarquia consistente**
   ```csv
   Index 1 = Total geral
   Index 2 = Categorias principais
   Index 3 = Subcategorias
   Index 4 = Itens de trabalho
   ```

3. **Deixe campos vazios quando apropriado**
   - Quantity: sempre vazio (calculado automaticamente)
   - TotalPrice: sempre vazio (calculado automaticamente)
   - Value: vazio para totalizadores, preenchido para itens

4. **Use nomes descritivos**
   ```csv
   ✅ Name: Porta P1 (60x210cm) - Madeira
   ❌ Name: P1
   ```

5. **Teste com pequenos grupos primeiro**
   - Comece com 1-2 tipos de cada elemento
   - Verifique se as quantidades batem
   - Depois expanda para todo o orçamento

6. **Crie uma linha "Total" para cada categoria**
   ```csv
   3,,Portas - Subtotal,,,,,Count,IfcDoor
   4,,Porta P1,,,un,150.00,,Count,"IfcDoor, type=""P1"""
   ```
   Isso ajuda a validar que a soma dos filtros bate com o total.

### ❌ DON'T (Não faça)

1. **Não use vírgulas dentro dos nomes sem aspas**
   ```csv
   ❌ Name: Porta P1, 60x210cm
   ✅ Name: Porta P1 - 60x210cm
   ```

2. **Não preencha Value em linhas de totalização**
   ```csv
   ❌ 1,,Total,,,100.0,,,
   ✅ 1,,Total,,,,,,
   ```

3. **Não misture unidades na mesma categoria**
   ```csv
   ❌ 
   3,,Concreto,,m³,450.00,,GrossVolume,IfcColumn
   3,,Concreto,,un,450.00,,Count,IfcColumn
   ```

4. **Não use nomes de pavimentos/tipos inventados**
   - Os nomes devem ser EXATAMENTE como aparecem no modelo IFC
   - Use as ferramentas de inspeção do BonsaiBIM para ver os valores corretos

### 🔍 Como descobrir os valores corretos

1. **No BonsaiBIM:**
   - Vá em: BIM → Manual Quantification
   - Selecione um elemento no modelo 3D
   - Veja as propriedades disponíveis no painel lateral
   - Use esses valores EXATOS no CSV

2. **Nomes de pavimentos (location):**
   - Veja a hierarquia do projeto no painel esquerdo
   - Os nomes dos IfcBuildingStorey são seus "location"

3. **Tipos de elementos (type):**
   - Selecione o elemento
   - Veja a propriedade "ObjectType" ou "Type"
   - Use esse valor exato

### 💡 Dicas de performance

1. **Para modelos grandes:**
   - Divida o CSV em categorias (estrutura, arquitetura, instalações)
   - Use arquivos CSV separados se necessário
   - Evite queries muito genéricos no início (comece específico)

2. **Validação:**
   - Sempre confira se a soma das linhas filtradas = linha de total
   - Exemplo: Total de portas = soma de P1 + P2 + P3

3. **Versionamento:**
   - Mantenha cópias do CSV antes de grandes mudanças
   - Nomeie arquivos com versão: `orcamento_v1.csv`, `orcamento_v2.csv`

### 🐛 Resolução de problemas comuns

**Problema:** Quantidade aparece como 0 ou vazio
- **Solução:** Verifique se o nome do tipo/pavimento está correto
- Tente usar apenas `IfcDoor` (sem filtros) para ver se conta algo
- Inspecione um elemento no modelo para ver os valores exatos

**Problema:** Total Cost não calcula
- **Solução:** Verifique se preencheu a coluna `Unit`
- Verifique se `Value` não está preenchido em linhas de totalização

**Problema:** Erro ao importar CSV
- **Solução:** Certifique-se que salvou como CSV UTF-8
- Verifique se não há linhas vazias no final do arquivo
- Confira se as aspas duplas estão corretas nas queries

**Problema:** Valores de diferentes pavimentos somando juntos
- **Solução:** Verifique o `Index` - itens do mesmo nível somam
- Use Index 4 para itens específicos, Index 3 para subtotais

---

## 📚 Recursos Adicionais

### Links úteis

**IfcOpenShell - Sintaxe de Seletores (Query)**
- 📚 **[Documentação oficial - Selector Syntax](https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html)**
- Referência completa sobre filtros avançados, operadores lógicos, wildcards e muito mais
- O BonsaiBIM usa esta mesma sintaxe na coluna Query

**BonsaiBIM**
- 🌐 [Site oficial do BonsaiBIM](https://bonsaibim.org/)
- 📖 [Wiki do BonsaiBIM](https://docs.bonsaibim.org/)
- 💬 [Comunidade OSArch](https://community.osarch.org/)

### Tipos IFC comuns

```
IfcColumn        - Pilares/Colunas
IfcBeam          - Vigas
IfcSlab          - Lajes
IfcWall          - Paredes
IfcDoor          - Portas
IfcWindow        - Janelas
IfcRoof          - Telhados
IfcStair         - Escadas
IfcRailing       - Guarda-corpos
IfcCovering      - Revestimentos
IfcFurnishing    - Mobiliário
IfcLightFixture  - Luminárias
IfcOutlet        - Tomadas
IfcPipe          - Tubulações
IfcDuct          - Dutos
```

### Template completo de exemplo

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,ORÇAMENTO TOTAL,,,,,,
2,,1. INFRAESTRUTURA,,,,,,
3,,1.1 Fundações,,,,,GrossVolume,"IfcFooting"
4,,Sapata S1,,m³,380.00,,GrossVolume,"IfcFooting, type=""S1"""
2,,2. SUPERESTRUTURA,,,,,,
3,,2.1 Pilares,,,,,GrossVolume,IfcColumn
4,,Pilares Térreo,,m³,450.00,,GrossVolume,"IfcColumn, location=""Térreo"""
3,,2.2 Vigas,,,,,GrossVolume,IfcBeam
4,,Vigas Térreo,,m³,420.00,,GrossVolume,"IfcBeam, location=""Térreo"""
3,,2.3 Lajes,,,,,GrossVolume,IfcSlab
4,,Lajes Térreo,,m³,380.00,,GrossVolume,"IfcSlab, location=""Térreo"""
2,,3. ARQUITETURA,,,,,,
3,,3.1 Alvenaria,,,,,NetArea,IfcWall
4,,Alvenaria Vedação,,m²,45.00,,NetArea,"IfcWall, type=""Vedação"""
3,,3.2 Esquadrias,,,,,Count,IfcDoor
4,,Portas P1,,,un,150.00,,Count,"IfcDoor, type=""P1"""
```

---

## 📝 Resumo do fluxo de trabalho

1. ✅ Exporte um CSV do BonsaiBIM (ou crie do zero)
2. ✅ Edite no Excel/LibreOffice (salve como CSV UTF-8)
3. ✅ Preencha as colunas:
   - **Name**: descrição do item
   - **Unit**: unidade (m³, un, m²)
   - **Value**: preço unitário (APENAS para itens de trabalho)
   - **Property**: qual propriedade quantificar (GrossVolume, Count, etc.)
   - **Query**: quais elementos selecionar (IfcDoor, type="P1", etc.)
4. ✅ Importe de volta no BonsaiBIM
5. ✅ Verifique as quantidades calculadas
6. ✅ Ajuste e refine conforme necessário

---

*Documentação criada para BonsaiBIM 0.8.5*
*Última atualização: Abril 2026*
