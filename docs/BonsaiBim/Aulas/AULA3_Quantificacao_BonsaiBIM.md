# Aula 3: Quantificação e Cálculo de Custos no BonsaiBIM

## 🚨 ALERTA IMPORTANTE - Leia antes de começar!

### Problema com Configuração Regional Brasileira

No Brasil usamos **vírgula (,)** para separar decimais, mas o formato CSV usa vírgula para separar campos!

```
❌ ERRADO (formato brasileiro): 10,5
✅ CORRETO (formato CSV): 10.5
```

**Se você salvar o CSV com vírgulas nos decimais, o BonsaiBIM NÃO vai calcular os custos!**

👉 **Vá direto para a seção "[Como Salvar CSV Corretamente](#como-salvar-csv-corretamente)"** para instruções detalhadas.

---

## 📋 Índice
1. [O que é Quantificação](#o-que-é-quantificação)
2. [Estrutura do CSV](#estrutura-do-csv)
3. [Propriedades (Property)](#propriedades-property)
4. [Como Salvar CSV Corretamente](#como-salvar-csv-corretamente)
5. [Workflow Completo](#workflow-completo)
6. [Casos de Uso Práticos](#casos-de-uso-práticos)
7. [Dicas e Boas Práticas](#dicas-e-boas-práticas)
8. [Resolução de Problemas](#resolução-de-problemas)

---

## O que é Quantificação?

**Quantificação** é o processo de:
1. Selecionar elementos IFC do modelo (usando **Query** - visto na aula anterior)
2. Medir propriedades desses elementos (usando **Property** - volume, área, contagem)
3. Calcular custos multiplicando quantidade × preço unitário

### Fluxo de trabalho

```
Modelo IFC → Query seleciona elementos → Property mede → Quantity calculada
                                                                    ↓
                                           Value (preço) ← Você define
                                                                    ↓
                                                          Total Cost = Quantity × Value
```

---

## Estrutura do CSV

### Colunas do arquivo CSV

| Coluna | Descrição | Exemplo | Quem preenche |
|--------|-----------|---------|---------------|
| **Index** | Nível hierárquico | `3` | Você |
| **Identification** | Código/ID (geralmente vazio) | vazio | Você (opcional) |
| **Name** | Nome do item | `Pilares Térreo` | Você |
| **Quantity** | Quantidade calculada | `0.40` | BonsaiBIM (automático) |
| **Unit** | Unidade de medida | `m³`, `un`, `m²` | Você |
| **Value** | Preço unitário | `450.00` | Você |
| **TotalPrice** | Custo total | `180.00` | BonsaiBIM (automático) |
| **Property** | Qual propriedade medir | `GrossVolume`, `Count` | Você |
| **Query** | Quais elementos selecionar | `IfcColumn, location="Térreo"` | Você |

### Hierarquia (Index)

```csv
Index 1 = Total geral
Index 2 = Categorias principais
Index 3 = Subcategorias/Subtotais
Index 4 = Itens de trabalho
Index 5 = Sub-itens (se necessário)
```

### Regra de ouro para Value

✅ **Itens de trabalho** (linhas com Property e Query) → **TÊM Value**
```csv
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn
```

❌ **Totalizadores** (linhas sem Property/Query) → **SEM Value**
```csv
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
```

### Template básico

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Categoria,,,,,,
3,,Subtotal,,,,,Property,IfcTipo
4,,Item de Trabalho,,unidade,preço,,Property,"IfcTipo, filtro=""valor"""
```

---

## Propriedades (Property)

A coluna **Property** define **QUAL propriedade** do elemento IFC será medida/calculada.

### Propriedades volumétricas

| Property | O que mede | Unidade | Uso típico |
|----------|-----------|---------|------------|
| `GrossVolume` | Volume bruto | m³ | Concreto, alvenaria |
| `NetVolume` | Volume líquido | m³ | Cálculos precisos |

**Exemplo:**
```csv
Property: GrossVolume
Query: IfcColumn
Resultado: Soma dos volumes de todos os pilares
```

### Propriedades de área

| Property | O que mede | Unidade | Uso típico |
|----------|-----------|---------|------------|
| `NetArea` | Área líquida | m² | Paredes, pisos |
| `GrossArea` | Área bruta | m² | Revestimentos |

**Exemplo:**
```csv
Property: NetArea
Query: IfcWall, location="Térreo"
Resultado: Área total das paredes do térreo
```

### Propriedades lineares

| Property | O que mede | Unidade | Uso típico |
|----------|-----------|---------|------------|
| `Length` | Comprimento | m | Vigas, tubulações |
| `Perimeter` | Perímetro | m | Rodapés, forros |

### Contagem

| Property | O que mede | Unidade | Uso típico |
|----------|-----------|---------|------------|
| `Count` | Número de elementos | un | Portas, janelas, luminárias |

**Exemplo:**
```csv
Property: Count
Query: IfcDoor, type="P1"
Resultado: Número de portas tipo P1
```

### Propriedades customizadas

Você também pode usar propriedades específicas do seu modelo:
```csv
Property: Peso
Property: Resistencia
Property: Fabricante
```

---

## Como Salvar CSV Corretamente

## ⚠️ ATENÇÃO: Configuração Regional Brasileira

**PROBLEMA:** No Brasil usamos vírgula (,) para decimais, mas o CSV usa vírgula para separar campos!
- ❌ Formato brasileiro: `10,5` (dez vírgula cinco)
- ✅ Formato CSV correto: `10.5` (dez PONTO cinco)

**Se salvar errado, o BonsaiBIM não calcula os custos!**

---

### 📊 MÉTODO RECOMENDADO: Google Sheets

#### Passo 1: Importar

1. Acesse [Google Sheets](https://sheets.google.com)
2. **Arquivo → Importar**
3. Faça upload do CSV
4. Configure:
   - **Tipo de separador**: Vírgula
   - **Converter texto em números**: ✅ Marque
5. **Importar dados**

#### Passo 2: Editar

Digite números normalmente com vírgula: `450,00`  
O Google Sheets aceita vírgula ou ponto.

#### Passo 3: Baixar (CRÍTICO!)

🚨 **ANTES de baixar:**

1. **Arquivo → Configurações**
2. **Localidade** → mude para **Estados Unidos**
3. **Salvar configurações**

✅ Agora sim: **Arquivo → Fazer download → CSV**

🔄 (Opcional) Volte a localidade para Brasil

#### Verificação

Abra o arquivo no Bloco de Notas:
```csv
✅ CORRETO:
3,,Pilares,,m³,450.00,,GrossVolume,IfcColumn

❌ ERRADO:
3,,Pilares,,m³,450,00,,GrossVolume,IfcColumn
```

---

### 📊 LibreOffice Calc (alternativa)

#### Ao abrir:
- **Conjunto de caracteres**: UTF-8
- **Separador**: Vírgula

#### Ao salvar:
1. **Salvar Como → CSV**
2. Na janela "Exportar Texto":
   - UTF-8
   - Separador de campo: `,`
   - 🔴 **IMPORTANTE**: Mudar **Separador decimal** para `.` (PONTO)

**OU** mude a localidade para Inglês (EUA) antes de salvar.

---

### ❌ Excel: NÃO RECOMENDADO

Excel no Brasil salva com vírgula decimal por padrão.  
**Use Google Sheets** - é muito mais fácil!

---

## Workflow Completo

### 1️⃣ Preparação

**Antes de criar o CSV, descubra:**
- Quais pavimentos existem no modelo?
- Quais tipos de elementos existem (P1, P2, V1, etc.)?
- Como estão escritos no modelo? (com/sem acento, português/inglês?)

**Como descobrir:**
- BIM → Manual Quantification
- Selecione elementos e veja propriedades
- Anote os nomes EXATOS

### 2️⃣ Criar estrutura do CSV

**Opção A:** Exporte um CSV existente do BonsaiBIM  
**Opção B:** Use um template (fornecidos no material)  
**Opção C:** Crie do zero

### 3️⃣ Preencher o CSV

Para cada item de custo:

1. **Name**: Descrição clara
2. **Unit**: Unidade apropriada (m³, un, m²)
3. **Value**: Preço unitário (COM PONTO DECIMAL!)
4. **Property**: O que medir (GrossVolume, Count, etc.)
5. **Query**: Quais elementos (visto na aula anterior)

**Deixe vazio:**
- Quantity (BonsaiBIM calcula)
- TotalPrice (BonsaiBIM calcula)
- Value em linhas de totalização

### 4️⃣ Salvar corretamente

Siga as instruções da seção "Como Salvar CSV"

### 5️⃣ Importar no BonsaiBIM

1. BIM → Cost
2. **Linked CSV**
3. Selecione seu arquivo
4. Aguarde o cálculo

### 6️⃣ Verificar resultados

- Confira se Quantity foi calculado
- Confira se Value aparece
- Confira se Total Cost está correto
- Se algo estiver zerado → verifique o CSV

### 7️⃣ Ajustar e refinar

- Corrija queries que não funcionaram
- Ajuste preços
- Adicione/remova itens
- Salve novamente e reimporte

---

## Casos de Uso Práticos

### Caso 1: Concreto por pavimento

**Objetivo:** Calcular volume e custo de concreto dos pilares em cada pavimento

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Estrutura de Concreto,,,,,,
3,,Pilares - Total,,,,,GrossVolume,IfcColumn
4,,Pilares Subsolo,,m³,450.00,,GrossVolume,"IfcColumn, location=""Subsolo"""
4,,Pilares Térreo,,m³,450.00,,GrossVolume,"IfcColumn, location=""Térreo"""
4,,Pilares 1º Pav,,m³,450.00,,GrossVolume,"IfcColumn, location=""1º Pavimento"""
```

**Resultado esperado:**
- Quantity: volume calculado automaticamente para cada pavimento
- Total Cost: volume × 450.00

---

### Caso 2: Portas por tipo

**Objetivo:** Contar e orçar portas separadas por tipo

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Esquadrias,,,,,,
3,,Portas - Total,,,,,Count,IfcDoor
4,,Porta P1 (60cm),,,un,150.00,,Count,"IfcDoor, type=""P1"""
4,,Porta P2 (80cm),,,un,180.00,,Count,"IfcDoor, type=""P2"""
4,,Porta P3 (90cm),,,un,200.00,,Count,"IfcDoor, type=""P3"""
```

**Resultado esperado:**
- Quantity: número de portas de cada tipo
- Total Cost: quantidade × preço unitário

---

### Caso 3: Paredes por área

**Objetivo:** Calcular área de paredes para orçar alvenaria

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Alvenaria,,,,,,
3,,Paredes - Total,,,,,NetArea,IfcWall
4,,Alvenaria Vedação,,m²,45.00,,NetArea,"IfcWall, type=""Vedação"""
4,,Alvenaria Estrutural,,m²,65.00,,NetArea,"IfcWall, type=""Estrutural"""
```

---

### Caso 4: Combinando pavimento e tipo

**Objetivo:** Portas por tipo E por pavimento

```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,
2,,Esquadrias por Pavimento,,,,,,
3,,Térreo - Portas,,,,,Count,"IfcDoor, location=""Térreo"""
4,,P1 - Térreo,,,un,150.00,,Count,"IfcDoor, location=""Térreo"", type=""P1"""
4,,P2 - Térreo,,,un,180.00,,Count,"IfcDoor, location=""Térreo"", type=""P2"""
3,,1º Pav - Portas,,,,,Count,"IfcDoor, location=""1º Pavimento"""
4,,P1 - 1º Pav,,,un,150.00,,Count,"IfcDoor, location=""1º Pavimento"", type=""P1"""
4,,P2 - 1º Pav,,,un,180.00,,Count,"IfcDoor, location=""1º Pavimento"", type=""P2"""
```

---

## Dicas e Boas Práticas

### ✅ Faça

1. **Sempre inclua uma linha de subtotal**
   ```csv
   3,,Portas - Total,,,,,Count,IfcDoor
   4,,Porta P1,,,un,150.00,,Count,"IfcDoor, type=""P1"""
   4,,Porta P2,,,un,180.00,,Count,"IfcDoor, type=""P2"""
   ```
   Soma de P1+P2 deve bater com o total

2. **Use nomes descritivos**
   ```csv
   ✅ Name: Pilares Subsolo - 20x50cm
   ❌ Name: P1
   ```

3. **Organize hierarquicamente**
   ```csv
   1. ORÇAMENTO TOTAL
     2. Infraestrutura
       3. Fundações
         4. Sapata S1
     2. Superestrutura
       3. Pilares
         4. Pilares Térreo
   ```

4. **Documente seus preços**
   - Mantenha uma planilha separada com composições
   - Atualize periodicamente

5. **Valide os resultados**
   - Confira se as quantidades fazem sentido
   - Compare com levantamentos manuais
   - Verifique se totais batem

### ❌ Evite

1. **Não preencha Quantity ou TotalPrice manualmente**
   - São calculados automaticamente
   - Se preencher, pode dar erro

2. **Não coloque Value em totalizadores**
   ```csv
   ❌ 1,,Total,,,100.00,,,
   ✅ 1,,Total,,,,,,
   ```

3. **Não misture unidades na mesma categoria**
   ```csv
   ❌
   3,,Concreto,,m³,450.00,,GrossVolume,IfcColumn
   3,,Concreto,,un,450.00,,Count,IfcColumn
   ```

4. **Não use vírgula decimal**
   ```csv
   ❌ Value: 450,00
   ✅ Value: 450.00
   ```

---

## Resolução de Problemas

### Problema: Quantity aparece como 0 ou vazio

**Causas possíveis:**
1. Query não encontrou elementos (nome errado)
2. Property incorreta
3. Elementos não têm essa propriedade

**Solução:**
- Teste a query na aula anterior (Manual Quantification)
- Verifique se os elementos existem
- Confira se a propriedade está correta

---

### Problema: Total Cost não calcula

**Causas:**
1. ❌ Unit vazio
2. ❌ Value vazio
3. ❌ Value com vírgula (450,00)

**Solução:**
- Preencha Unit
- Preencha Value com PONTO decimal (450.00)
- Abra o CSV no Bloco de Notas para verificar

---

### Problema: Valores com vírgula no CSV

**Causa:** Salvou sem mudar a localidade

**Solução:**
- No Google Sheets: mude localidade para Estados Unidos
- Baixe novamente
- Verifique no Bloco de Notas

---

### Problema: Soma não bate

**Exemplo:**
```
Total de portas: 15
Porta P1: 5
Porta P2: 8
P1 + P2 = 13 (faltam 2!)
```

**Causas:**
1. Existem portas de outro tipo (P3?)
2. Query com filtro errado
3. Portas sem tipo definido

**Solução:**
- Adicione uma linha sem filtro para pegar todas
- Compare com o total
- Investigue a diferença

---

## Checklist Final

Antes de importar no BonsaiBIM:

- [ ] Todas as linhas de trabalho têm Property e Query
- [ ] Todas as linhas de trabalho têm Unit e Value
- [ ] Nenhuma linha de totalização tem Value
- [ ] Abri o CSV no Bloco de Notas
- [ ] Valores têm PONTO decimal (450.00)
- [ ] Arquivo salvo em UTF-8
- [ ] Queries testadas na aula anterior

---

## Resumo do Fluxo

```
1. Prepare
   ↓ Descubra nomes de pavimentos e tipos
   
2. Estruture
   ↓ Crie hierarquia no CSV
   
3. Preencha
   ↓ Name, Unit, Value, Property, Query
   
4. Salve CORRETAMENTE
   ↓ Google Sheets com localidade EUA
   
5. Importe
   ↓ BIM → Cost → Linked CSV
   
6. Verifique
   ↓ Quantity e Total Cost calculados?
   
7. Ajuste
   ↓ Corrija e reimporte
```

---

## Material Complementar

### Guias fornecidos

1. **GUIA_RAPIDO_Salvar_CSV.md** - Para imprimir
2. **EXEMPLO_CSV_Correto_vs_Errado.md** - Comparação visual
3. **Templates CSV** - Prontos para usar

### Próxima aula

Com Interface Blender (Aula 1), Search (Aula 2) e Quantificação (Aula 3), você está pronto para:
- Criar orçamentos completos
- Automatizar levantamentos
- Integrar BIM com orçamento

---

## Recursos Adicionais

**BonsaiBIM**
- 🌐 [Site oficial](https://bonsaibim.org/)
- 📖 [Wiki](https://docs.bonsaibim.org/)
- 💬 [Comunidade OSArch](https://community.osarch.org/)

**IfcOpenShell**
- 📚 [Selector Syntax](https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html)

---

*Documentação criada para BonsaiBIM 0.8.5*  
*Aula 3: Quantificação e Cálculo de Custos*  
*Última atualização: Abril 2026*
