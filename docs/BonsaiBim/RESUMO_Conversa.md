# Resumo da Conversa - Desenvolvimento Material BonsaiBIM

## Contexto Inicial
Usuário (professor no Brasil) precisava de ajuda para usar arquivos CSV no BonsaiBIM 0.8.4 para calcular custos. Os volumes estavam calculando, mas custos apareciam zerados.

## Problema Identificado
1. **Coluna errada no CSV:** Arquivo original usava `RateSubtotal`, mas BonsaiBIM espera `Value`
2. **Valores em totalizadores:** Linhas de somatório (Total, Concreto) tinham valores preenchidos, mas devem ficar vazias
3. **Unidade vazia:** Faltava preencher a coluna `Unit` (m³, un, etc.)

## Solução Aplicada
Arquivo CSV corrigido com:
- Coluna renomeada: `RateSubtotal` → `Value`
- Totalizadores sem Value (vazios)
- Unit preenchido: `m³` para concreto
- Valores decimais com ponto: `10.0` (não vírgula)

## Evolução do Projeto

### 1. Descoberta da estrutura CSV correta
```csv
Index,Identification,Name,Quantity,Unit,Value,TotalPrice,Property,Query
1,,Total,,,,,,                          ← SEM Value
2,,Concreto,,,,,,                       ← SEM Value  
3,,Pilares,,m³,10.0,,GrossVolume,IfcColumn  ← COM Value
```

**Regra chave:** 
- **Property** = QUAL propriedade quantificar (GrossVolume, Count, NetArea)
- **Query** = QUAIS elementos selecionar (IfcColumn, IfcDoor, etc.)

### 2. Sintaxe de Query corrigida
Usuário forneceu exemplo real:
```
IfcDoor, location="<nome do IfcBuildingStorey>", type="<nome do tipo>"
```

### 3. Problema da vírgula decimal (CRÍTICO!)
Brasil usa vírgula (10,5) mas CSV precisa de ponto (10.5)
- Identificado como erro #1 dos alunos
- Criado material específico sobre como salvar CSV corretamente

### 4. Estrutura do curso definida
Inicialmente 2 aulas, depois reorganizado para **3 aulas**:
1. Interface Blender + instalação BonsaiBIM + abrir/salvar IFC
2. Search (queries para selecionar elementos IFC)
3. Quantificação (CSV, properties, custos)

## Material Criado

### Documentação das Aulas
1. **AULA1_Interface_Blender_BonsaiBIM.md** (NOVA)
   - Interface do Blender
   - Navegação 3D
   - Instalação BonsaiBIM
   - Diferença .blend vs .ifc
   - 5 exercícios práticos

2. **AULA2_Search_BonsaiBIM.md**
   - Sintaxe de queries
   - Tipos IFC comuns
   - Filtros: location, type, name
   - 7 exemplos + 4 exercícios
   - Link para IfcOpenShell docs

3. **AULA3_Quantificacao_BonsaiBIM.md**
   - Estrutura do CSV
   - Properties (GrossVolume, Count, etc.)
   - **Seção extensa:** Como salvar CSV (Google Sheets, LibreOffice, Excel)
   - 4 casos de uso práticos
   - Troubleshooting

### Material de Apoio
1. **GUIA_PROFESSOR_BonsaiBIM_3aulas.md**
   - Roteiro minuto a minuto das 3 aulas
   - Material necessário
   - Dicas pedagógicas
   - Troubleshooting por aula
   - 3 cronogramas (intensivo/semanal/integrado)
   - Sistema de avaliação

2. **GUIA_RAPIDO_Salvar_CSV.md** (PARA IMPRIMIR)
   - Cheat sheet de 1 página
   - Instruções Google Sheets simplificadas
   - Checklist final

3. **EXEMPLO_CSV_Correto_vs_Errado.md**
   - Comparação visual
   - Mostra diferença 450,00 vs 450.00

4. **README_Material_Didatico.md**
   - Índice geral
   - Guia de uso rápido

### Templates CSV
- `template_basico.csv`
- `template_portas_janelas.csv`
- `template_estrutura_concreto.csv`
- `template_location_type.csv`

## Insights Importantes

### Sobre CSV
- BonsaiBIM usa IfcOpenShell para queries
- Hierarquia: Index 1=total, 2=categoria, 3=subtotal, 4=itens
- Value APENAS em itens de trabalho (não em totalizadores)
- Property e Query sempre juntos em itens de trabalho

### Sobre Configuração Regional
- Problema #1: vírgula vs ponto decimal
- Google Sheets: mudar localidade para "Estados Unidos" antes de baixar
- LibreOffice: mudar separador decimal nas opções de exportação
- Excel: não recomendado (muito complicado no Brasil)

### Sobre Queries
Sintaxe: `IfcTipo, filtro1="valor1", filtro2="valor2"`

Exemplos:
- `IfcDoor` → todas as portas
- `IfcDoor, location="Térreo"` → portas do térreo
- `IfcDoor, type="P1"` → portas tipo P1
- `IfcDoor, location="Térreo", type="P1"` → portas P1 do térreo

## Estado Atual
✅ Material completo criado e organizado
✅ 3 aulas estruturadas
✅ Guia do professor detalhado
✅ Material de apoio (guias rápidos, exemplos, templates)
✅ Problema da vírgula decimal bem documentado
✅ Link para documentação IfcOpenShell incluído

## Arquivos no Pacote

### 📚 Documentação Principal
- README_Material_Didatico.md
- GUIA_PROFESSOR_BonsaiBIM_3aulas.md
- AULA1_Interface_Blender_BonsaiBIM.md
- AULA2_Search_BonsaiBIM.md
- AULA3_Quantificacao_BonsaiBIM.md

### 📋 Material de Apoio
- GUIA_RAPIDO_Salvar_CSV.md (IMPRIMIR)
- EXEMPLO_CSV_Correto_vs_Errado.md
- DOCUMENTACAO_BonsaiBIM_Quantificacao.md (referência completa)

### 📁 Templates CSV
- template_basico.csv
- template_portas_janelas.csv
- template_estrutura_concreto.csv
- template_location_type.csv

## Para Continuar Desenvolvimento

### Possíveis próximos passos:
1. Adicionar mais templates CSV para casos específicos
2. Criar exercícios práticos com gabaritos
3. Desenvolver slides/apresentações para as aulas
4. Criar vídeos tutoriais
5. Desenvolver casos de estudo reais
6. Traduzir documentação IfcOpenShell relevante
7. Criar script Python para validar CSV antes de importar
8. Desenvolver ferramenta para converter CSV errado (vírgula) em correto (ponto)

### Informações técnicas importantes:
- BonsaiBIM versão: 0.8.5
- Blender recomendado: 3.6+
- IfcOpenShell Selector Syntax: https://docs.ifcopenshell.org/ifcopenshell-python/selector_syntax.html
- Localização do usuário: Salvador, Bahia, BR
- Contexto: Material para alunos (ensino superior/técnico)

### Observações do usuário:
- Alunos usarão principalmente Google Sheets
- Foco em open source (Blender + BonsaiBIM)
- Importância da interoperabilidade (.ifc)
- Necessidade de material em português BR
- Ênfase em problemas práticos (vírgula decimal)

---

*Resumo criado em: Abril 2026*
*Material completo para curso BonsaiBIM 0.8.5*
