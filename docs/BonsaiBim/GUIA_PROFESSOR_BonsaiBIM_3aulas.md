# Guia do Professor: Curso BonsaiBIM (3 Aulas)

## 📚 Estrutura do Curso

### Aula 1: Interface Blender e BonsaiBIM Básico (2-3 horas)
**Objetivo:** Familiarização com Blender, instalação do BonsaiBIM, abrir e salvar arquivos IFC

### Aula 2: Search - Seleção de Entidades IFC (2-3 horas)
**Objetivo:** Alunos aprenderem a selecionar elementos IFC usando queries

### Aula 3: Quantificação e Cálculo de Custos (2-3 horas)
**Objetivo:** Alunos aprenderem a criar orçamentos automatizados

---

## 🎯 Aula 1: Interface Blender e BonsaiBIM

### Material necessário
- [ ] Blender 3.6+ instalado em todos os computadores
- [ ] Conexão com internet (para instalar BonsaiBIM)
- [ ] Arquivo IFC de exemplo (médio porte, ~10MB)
- [ ] Documento: `AULA1_Interface_Blender_BonsaiBIM.md`
- [ ] Projetor/tela compartilhada

### Preparação prévia

**IMPORTANTE - ANTES DA AULA:**
1. Instale Blender em todos os computadores
2. Teste que todos conseguem abrir o Blender
3. Baixe arquivo IFC de exemplo
4. Teste você mesmo o processo completo

**Link para download do Blender:**
- https://www.blender.org/download/

---

### Roteiro sugerido (2-3h)

**1. Introdução (15 min)**
- O que é Blender?
- Por que usar Blender para BIM?
- O que é BonsaiBIM?
- Diferença entre software proprietário e open source

**2. Primeira abertura do Blender (10 min)**
- Abrir o programa
- Configuração inicial (idioma, tema)
- Fechar tela de boas-vindas
- **DEMO AO VIVO:** Mostrar interface

**3. Interface do Blender (20 min)**
- Explicar layout da tela
- 3D Viewport (centro)
- Outliner (esquerda)
- Properties Panel (direita)
- **EXERCÍCIO:** Pedir alunos para identificarem cada área

**4. Navegação 3D (30 min)**
- **DEMO AO VIVO - CRÍTICO!**
- Rotacionar (botão do meio)
- Pan (Shift + botão do meio)
- Zoom (scroll)
- Vistas numpad (1, 3, 7)
- **EXERCÍCIO:** 15 min de prática livre com cena padrão
- Circule pela sala ajudando

**INTERVALO (10 min)**

**5. Configurações recomendadas (15 min)**
- Edit → Preferences
- Unidades: Meters
- Auto-save: 5 minutos
- **DEMO AO VIVO:** Mostrar cada configuração
- Alunos acompanham

**6. Instalação do BonsaiBIM (20 min)**
- **CRÍTICO:** Fazer JUNTO com os alunos
- Método 1: Instalação direta (recomendado)
- Edit → Preferences → Add-ons → buscar "bonsai"
- Aguardar download e instalação
- Verificar que ícone BIM apareceu
- **Troubleshooting:** Ajudar quem tiver problema

**7. Abrindo arquivo IFC (20 min)**
- Distribuir arquivo IFC de exemplo (USB ou rede)
- **DEMO AO VIVO:** File → Import → IFC
- Esperar carregar
- Explorar hierarquia no Outliner
- **EXERCÍCIO:** Cada aluno abre o IFC

**8. Explorando o modelo (25 min)**
- Navegar pelo modelo
- Expandir hierarquia
- Ocultar/mostrar pavimentos
- Selecionar elementos
- Ver propriedades IFC
- **EXERCÍCIO:** Tarefas do material (Exercícios 2 e 3)

**9. Salvando arquivos (15 min)**
- Explicar diferença .blend vs .ifc
- **DEMO:** Salvar .blend
- **DEMO:** Exportar .ifc
- **EXERCÍCIO:** Cada aluno salva nas duas formas

**PARA CASA:**
- Explore o modelo
- Anote quantos pavimentos tem
- Liste 5 tipos diferentes de elementos (IfcWall, IfcDoor, etc.)

---

## 🎯 Aula 2: Search

### Material necessário
- [ ] Computador com Blender + BonsaiBIM
- [ ] MESMO modelo IFC da aula anterior
- [ ] Documento: `AULA2_Search_BonsaiBIM.md`
- [ ] Projetor/tela compartilhada

### Roteiro sugerido (2-3h)

**1. Revisão aula anterior (15 min)**
- Alguém teve dificuldade em casa?
- Verificar "para casa": quantos pavimentos? quais tipos?
- Relembrar como abrir IFC

**2. Introdução ao Search (15 min)**
- O que são queries?
- Por que automatizar seleções?
- Diferença entre clicar manualmente vs usar queries
- Onde vamos usar: Manual Quantification

**3. Acessando Manual Quantification (10 min)**
- **DEMO AO VIVO:** BIM → Manual Quantification
- Mostrar interface
- Explicar campo de Query

**4. Tipos IFC (20 min)**
- Revisar tipos comuns: IfcDoor, IfcColumn, etc.
- **DEMO:** Query simples `IfcDoor`
- Ver quantos elementos retornam
- **EXERCÍCIO:** Alunos testam `IfcColumn`, `IfcWall`, `IfcWindow`

**INTERVALO (10 min)**

**5. Filtros - location (30 min)**
- Como descobrir nomes de pavimentos
- Olhar no Outliner → IfcBuildingStorey
- Anotar nomes EXATOS
- **DEMO:** `IfcDoor, location="Térreo"`
- **EXERCÍCIO:** Filtrar elementos por pavimento
- Pedir para anotar quantas portas tem em cada pavimento

**6. Filtros - type (30 min)**
- Como descobrir tipos de elementos
- Selecionar elemento → ver propriedades
- **DEMO:** `IfcDoor, type="P1"`
- **EXERCÍCIO:** Separar portas por tipo
- Anotar quantas de cada tipo

**7. Filtros combinados (25 min)**
- **DEMO:** `IfcDoor, location="Térreo", type="P1"`
- Lógica AND (e)
- **EXERCÍCIO PRÁTICO:** Criar tabela:
  ```
  Pavimento | Tipo | Quantidade
  Térreo    | P1   | ?
  Térreo    | P2   | ?
  1º Pav    | P1   | ?
  ```

**8. Exercícios da documentação (20 min)**
- Trabalho em duplas
- Exercícios 1-4 do material
- Correção coletiva

**PARA CASA:**
- Criar lista completa de queries para:
  - Todos os pilares por pavimento
  - Todas as vigas por pavimento
  - Todas as portas por tipo
- Formato: planilha ou lista escrita

---

## 🎯 Aula 3: Quantificação

### Material necessário
- [ ] Computador com Blender + BonsaiBIM
- [ ] MESMO modelo IFC das aulas anteriores
- [ ] Documento: `AULA3_Quantificacao_BonsaiBIM.md`
- [ ] **IMPRIMIR:** `GUIA_RAPIDO_Salvar_CSV.md` (1 por aluno!)
- [ ] Templates CSV no Drive/USB
- [ ] Google Sheets (criar contas se necessário)
- [ ] Bloco de Notas disponível em todos os PCs

### Preparação CRÍTICA

**TESTE VOCÊ MESMO ANTES:**
1. Processo completo Google Sheets
2. Mudança de localidade
3. Verificação no Bloco de Notas
4. Importação no BonsaiBIM

**Este é o ponto onde mais alunos terão problemas!**

---

### Roteiro sugerido (2-3h)

**1. Revisão aula anterior (15 min)**
- Corrigir "para casa" (queries)
- Relembrar filtros
- Quem teve dificuldade?

**2. Introdução à quantificação (15 min)**
- O que é quantificação?
- Fluxo: Query → Property → Quantity → Value → Cost
- Mostrar exemplo de resultado final
- **DEMO:** Importar CSV exemplo, mostrar resultado

**3. ⚠️ ALERTA VERMELHO: Vírgula decimal (20 min)**
- **EXTREMAMENTE IMPORTANTE!**
- Escrever no quadro: `450,00` ❌  vs  `450.00` ✅
- Explicar POR QUÊ: CSV usa vírgula para separar campos
- Mostrar exemplo de CSV errado vs correto
- **DISTRIBUIR IMPRESSO:** Guia rápido para cada aluno
- Enfatizar: "90% dos problemas vem daqui!"

**4. Estrutura do CSV (25 min)**
- Explicar cada coluna
- Index, Name, Quantity, Unit, Value, Property, Query
- **REGRA DE OURO:** Value APENAS em itens de trabalho
- Mostrar hierarquia (Index 1, 2, 3, 4)
- **DEMO:** Abrir template no Bloco de Notas

**INTERVALO (10 min)**

**5. Properties (25 min)**
- GrossVolume → concreto (m³)
- NetArea → paredes (m²)
- Count → portas (un)
- Length → vigas (m)
- **EXERCÍCIO:** Para cada elemento, qual Property?

**6. Google Sheets - PASSO A PASSO (45 min)**
- **CRÍTICO - FAZER JUNTO, PASSO POR PASSO**
- **DEMO AO VIVO - MUITO DEVAGAR:**
  1. Importar template CSV
  2. Editar (pode usar vírgula: 450,00)
  3. **PAUSA:** Verificar que todos editaram
  4. **PONTO CRÍTICO:** Arquivo → Configurações → Localidade → **Estados Unidos**
  5. Salvar configurações
  6. Fazer download → CSV
  7. **VERIFICAÇÃO COLETIVA:** Abrir no Bloco de Notas
  8. Procurar valores: tem PONTO? ✅
- **EXERCÍCIO:** Cada aluno faz o ciclo completo 2x
- Circule pela sala verificando TODOS os arquivos

**7. Caso prático - Portas (40 min)**
- Vamos criar orçamento de portas por tipo
- Em grupo, definir:
  - Queries (da aula anterior)
  - Property: Count
  - Unit: un
  - Value: inventar preços (150, 180, 200)
- **CRIAR CSV JUNTOS** no Google Sheets
- Salvar corretamente
- **IMPORTAR NO BONSAIBIM**
- Verificar resultado
- Se não funcionar: diagnosticar juntos

**8. Troubleshooting (15 min)**
- Problemas comuns:
  - Custos não calculam → vírgula decimal
  - Quantity vazio → query errada
  - Value não aparece → Unit vazio
- **EXERCÍCIO:** Distribuir CSVs com erros para identificar

**TRABALHO FINAL:**
- Criar orçamento completo:
  - Mínimo: 1 sistema (estrutura OU esquadrias)
  - 3 tipos diferentes de elementos
  - Separar por pavimento
  - Salvar CSV corretamente
  - Importar no BonsaiBIM
- Entregar:
  - Arquivo CSV
  - Print da tela do BonsaiBIM mostrando custos calculados
  - Breve relatório (1 página): dificuldades e aprendizados

**Prazo:** 1 semana

---

## 💡 Dicas Pedagógicas Gerais

### Para Aula 1 (Interface)

✅ **Faça:**
1. Teste TUDO antes (instalação, IFC, navegação)
2. Tenha plano B se internet cair (BonsaiBIM offline?)
3. Circule pela sala durante exercícios
4. Navegação é FÍSICA - precisa praticar
5. Seja paciente: muitos nunca usaram Blender

❌ **Evite:**
1. Ir muito rápido (eles estão vendo pela primeira vez)
2. Assumir que conhecem CAD/3D
3. Pular a prática de navegação
4. Modelo IFC muito complexo

**Alerta:** Alguns alunos terão dificuldade com navegação 3D. É normal!

---

### Para Aula 2 (Search)

✅ **Faça:**
1. Use SEMPRE o mesmo modelo para todos
2. Projete sua tela durante demonstrações
3. Escreva queries no quadro também
4. Deixe tempo para exploração
5. Incentive anotação dos tipos encontrados

❌ **Evite:**
1. Queries muito complexas logo de início
2. Pular descoberta de nomes no modelo
3. Assumir que todos sabem IFC
4. Pressa - velocidade vem com prática

**Alerta:** Nomes com acentos podem dar problema! Use o modelo para pegar nomes exatos.

---

### Para Aula 3 (Quantificação)

✅ **Faça:**
1. **ENFATIZE 10X** o problema da vírgula
2. Demonstre AO VIVO todo o processo Google Sheets
3. Verifique arquivo de CADA aluno no Bloco de Notas
4. Faça processo pelo menos 2x com a turma
5. Tenha CSV correto de backup

❌ **Evite:**
1. Assumir que sabem planilhas
2. Usar Excel (complicado demais)
3. Deixar alunos travarem sozinhos
4. Pular verificação no Bloco de Notas

**Alerta:** Se 1 aluno tiver problema com vírgula, provavelmente vários terão. Resolva coletivamente!

---

## 🔧 Troubleshooting por Aula

### Aula 1: Interface

**"Professor, o Blender não abre!"**
- Verificar requisitos mínimos
- Tentar versão anterior do Blender
- Verificar drivers de vídeo

**"Não consigo instalar BonsaiBIM!"**
- Verificar conexão internet
- Tentar instalação manual
- Usar versão standalone do BonsaiBIM

**"O IFC não abre!"**
- Verificar se arquivo não está corrompido
- Tentar IFC mais simples
- Verificar tamanho (>500MB pode travar)

---

### Aula 2: Search

**"Minha query não retorna nada!"**
- Nome do pavimento/tipo está EXATO?
- Testou sem filtro primeiro?
- Elementos existem mesmo?

**"Retorna elementos demais!"**
- Filtro muito genérico
- Adicionar mais filtros
- Verificar wildcards não intencionais

---

### Aula 3: Quantificação

**"Custos não calculam!"**
- 90% das vezes: vírgula decimal
- Abrir CSV no Bloco de Notas
- Tem PONTO nos valores? (450.00)
- Unit preenchido?
- Value preenchido?

**"Quantity fica vazio!"**
- Query errada (nome incorreto)
- Property incorreta
- Elementos não têm essa propriedade

**"Google Sheets salvou com vírgula!"**
- Esqueceu de mudar localidade
- Refazer: Configurações → EUA → Baixar

---

## 📊 Avaliação Sugerida

### Distribuição de pontos

**Aula 1 - Interface (20 pontos):**
- Instalou BonsaiBIM corretamente (5 pts)
- Consegue navegar no modelo (5 pts)
- Salvou .blend e .ifc (5 pts)
- Participação (5 pts)

**Aula 2 - Search (30 pontos):**
- Queries corretas (15 pts)
- Uso de filtros (10 pts)
- Para casa completo (5 pts)

**Aula 3 - Quantificação (50 pontos):**
- CSV estruturado corretamente (15 pts)
- CSV salvo com ponto decimal (15 pts) ← CRÍTICO
- Importação no BonsaiBIM funcionou (10 pts)
- Relatório (10 pts)

---

### Trabalho final (substitui Aula 3)

**Orçamento BIM completo:**

**Requisitos mínimos (nota 6.0):**
- 1 sistema (estrutura OU esquadrias)
- 3 tipos de elementos
- CSV correto (ponto decimal)
- Importa no BonsaiBIM

**Para nota 8.0:**
- 2 sistemas
- 5 tipos de elementos
- Separação por pavimento
- Preços realistas

**Para nota 10:**
- Orçamento completo (3+ sistemas)
- Hierarquia bem organizada
- Análise crítica das quantidades
- Comparação com levantamento manual
- Documentação caprichada

**Formato de entrega:**
- CSV usado
- Prints do BonsaiBIM (antes/depois)
- Relatório (2-3 páginas):
  - Metodologia
  - Dificuldades encontradas
  - Soluções aplicadas
  - Análise dos resultados

---

## ⏰ Cronogramas Sugeridos

### Opção 1: Intensivo (2 dias - 9h total)
- **Dia 1 - Manhã (3h):** Aula 1 - Interface
- **Dia 1 - Tarde (3h):** Aula 2 - Search
- **Dia 2 - Manhã (3h):** Aula 3 - Quantificação

### Opção 2: Semanal (3 semanas)
- **Semana 1:** Aula 1 + exercícios para casa
- **Semana 2:** Aula 2 + lista de queries
- **Semana 3:** Aula 3 + início trabalho final

### Opção 3: Integrado em disciplina maior
- **Módulo 1:** Introdução BIM + Aula 1
- **Módulo 2:** IFC + Aula 2  
- **Módulo 3:** Orçamento + Aula 3
- **Módulo 4:** Trabalho final

---

## ✅ Checklists pré-aula

### Antes da Aula 1:
- [ ] Blender instalado e testado em todos os PCs
- [ ] Conexão internet funcionando
- [ ] Arquivo IFC de exemplo baixado e testado
- [ ] Material impresso (se desejar)
- [ ] Projetor testado
- [ ] Você mesmo fez o processo completo

### Antes da Aula 2:
- [ ] Todos têm o modelo IFC da aula 1
- [ ] Verificar que BonsaiBIM está instalado
- [ ] Material de exercícios preparado
- [ ] Você testou todas as queries no modelo

### Antes da Aula 3:
- [ ] **`GUIA_RAPIDO_Salvar_CSV.md` IMPRESSO** (1 por aluno)
- [ ] Google Sheets acessível (testar internet)
- [ ] Templates CSV no Drive/USB
- [ ] Bloco de Notas disponível
- [ ] Você testou TODO o processo 2x
- [ ] CSV de exemplo funcionando
- [ ] Chocolates/café (aula mais estressante!)

---

## 📦 Material Fornecido

### Documentação
1. `AULA1_Interface_Blender_BonsaiBIM.md` - Interface e instalação
2. `AULA2_Search_BonsaiBIM.md` - Queries e seleção
3. `AULA3_Quantificacao_BonsaiBIM.md` - Quantificação e custos
4. `GUIA_RAPIDO_Salvar_CSV.md` - **IMPRIMIR!**
5. `EXEMPLO_CSV_Correto_vs_Errado.md` - Comparação visual

### Templates
1. `template_basico.csv`
2. `template_portas_janelas.csv`
3. `template_estrutura_concreto.csv`
4. `template_location_type.csv`

---

## 🎓 Adaptações por Perfil de Turma

### Turma iniciante (nunca usou 3D):
- **Aula 1:** 4 horas (mais tempo navegação)
- **Aula 2:** 2.5 horas
- **Aula 3:** 3 horas (mais suporte)
- Trabalho em duplas
- Mais exercícios guiados

### Turma intermediária (já usou CAD):
- **Aula 1:** 2 horas (navegação mais rápida)
- **Aula 2:** 2.5 horas
- **Aula 3:** 2.5 horas
- Trabalho individual
- Mais autonomia

### Turma avançada (já usou Blender/BIM):
- **Aula 1:** 1.5 horas (só BonsaiBIM específico)
- **Aula 2:** 2 horas (filtros avançados)
- **Aula 3:** 2 horas
- Desafios adicionais
- Projetos mais complexos

---

## 📞 Recursos e Suporte

### Para alunos:
- 💬 [Comunidade OSArch](https://community.osarch.org/)
- 📖 [Wiki BonsaiBIM](https://docs.bonsaibim.org/)
- 🎥 [YouTube BonsaiBIM](https://www.youtube.com/@BonsaiBIM)

### Para professores:
- 📧 Fórum de educadores OSArch
- 🎓 Materiais didáticos compartilhados
- 💬 Grupo de professores (se disponível)

---

## 🎯 Objetivos de Aprendizagem

### Ao final do curso, os alunos devem ser capazes de:

**Competências técnicas:**
- [ ] Abrir e navegar em modelos IFC no Blender
- [ ] Usar o BonsaiBIM para visualização BIM
- [ ] Criar queries para selecionar elementos específicos
- [ ] Estruturar CSV de quantificação
- [ ] Calcular automaticamente custos de projeto
- [ ] Salvar corretamente arquivos .blend e .ifc

**Competências conceituais:**
- [ ] Entender estrutura hierárquica IFC
- [ ] Compreender workflow BIM
- [ ] Diferenciar tipos de elementos IFC
- [ ] Relacionar BIM com orçamento

**Competências profissionais:**
- [ ] Automatizar levantamentos quantitativos
- [ ] Reduzir erros de orçamento
- [ ] Melhorar produtividade
- [ ] Integrar ferramentas open source

---

## 📈 Métricas de Sucesso

### Indicadores por aula:

**Aula 1:**
- 90%+ conseguem instalar BonsaiBIM
- 90%+ conseguem abrir IFC
- 95%+ conseguem navegar no modelo

**Aula 2:**
- 85%+ criam queries corretas
- 90%+ conseguem filtrar por pavimento
- 80%+ conseguem combinar filtros

**Aula 3:**
- 70%+ salvam CSV corretamente (ponto decimal)
- 85%+ conseguem importar no BonsaiBIM
- 75%+ têm custos calculando

**Trabalho final:**
- 80%+ entregam trabalho funcional
- 60%+ entregam trabalho completo
- 40%+ excedem expectativas

---

## 🌟 Dicas de Ouro

### Para o sucesso do curso:

1. **Paciência é fundamental**
   - Primeira vez em 3D é difícil
   - Repita explicações se necessário
   - Celebre pequenas vitórias

2. **Demonstre AO VIVO sempre**
   - Não confie apenas em slides
   - Mostre seu próprio Blender
   - Erre na frente deles (mostra que é normal)

3. **Problema da vírgula é REAL**
   - Não subestime
   - Enfatize múltiplas vezes
   - Verifique TODOS os arquivos

4. **Circule pela sala**
   - Não fique só na frente
   - Veja telas dos alunos
   - Ajude individualmente

5. **Use o mesmo modelo sempre**
   - Facilita comparações
   - Todos têm mesmas dúvidas
   - Você conhece bem

---

*Guia do Professor - BonsaiBIM 0.8.5*  
*Curso completo: 3 aulas (6-9 horas)*  
*Última atualização: Abril 2026*
