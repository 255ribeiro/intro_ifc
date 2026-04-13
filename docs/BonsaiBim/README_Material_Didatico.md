# 📚 Material Didático - BonsaiBIM

## 🎯 Estrutura do Curso (3 Aulas)

Este material foi desenvolvido para um curso completo de BonsaiBIM, dividido em 3 aulas progressivas de 2-3 horas cada.

---

## 📖 Material Principal

### 👨‍🏫 Para o Professor

**`GUIA_PROFESSOR_BonsaiBIM_3aulas.md`** ⭐ **COMECE POR AQUI!**
- Roteiro detalhado das 3 aulas (minuto a minuto)
- Material necessário para cada aula
- Dicas pedagógicas específicas
- Troubleshooting por aula
- Critérios de avaliação
- 3 opções de cronograma
- Checklists pré-aula
- Métricas de sucesso

---

### 📚 Documentação das Aulas

#### **Aula 1: Interface Blender e BonsaiBIM Básico**
**Arquivo:** `AULA1_Interface_Blender_BonsaiBIM.md`  
**Duração:** 2-3 horas  
**Tópicos:**
- Introdução ao Blender e BIM
- Interface do Blender
- Configurações recomendadas
- Instalação do BonsaiBIM
- Abrindo arquivos IFC
- Navegação no modelo 3D
- Salvando .blend vs .ifc
- 5 exercícios práticos

**Pré-requisitos:** Nenhum  
**Material:** Blender instalado, arquivo IFC de exemplo

---

#### **Aula 2: Search - Seleção de Entidades IFC**
**Arquivo:** `AULA2_Search_BonsaiBIM.md`  
**Duração:** 2-3 horas  
**Tópicos:**
- O que são queries/search
- Sintaxe básica de queries
- Tipos IFC comuns
- Filtros: location, type, name, tag
- Combinando filtros
- 7 exemplos práticos
- 4 exercícios com respostas
- Link para documentação IfcOpenShell

**Pré-requisitos:** Aula 1 completa  
**Material:** Mesmo modelo IFC da aula 1

---

#### **Aula 3: Quantificação e Cálculo de Custos**
**Arquivo:** `AULA3_Quantificacao_BonsaiBIM.md`  
**Duração:** 2-3 horas  
**Tópicos:**
- Estrutura do CSV de quantificação
- Propriedades (Property): GrossVolume, Count, etc.
- **🔴 CRÍTICO:** Como salvar CSV corretamente (vírgula vs ponto)
- Workflow completo
- 4 casos de uso práticos
- Dicas e boas práticas
- Resolução de problemas

**Pré-requisitos:** Aulas 1 e 2 completas  
**Material:** Google Sheets, templates CSV

---

## 📋 Material de Apoio para Alunos

### **GUIA_RAPIDO_Salvar_CSV.md** 🖨️ **IMPRIMIR!**
- Cheat sheet de 1 página
- Instruções ultra-simplificadas Google Sheets
- Checklist final
- FAQ

**Uso:** Distribuir impresso para cada aluno na Aula 3

---

### **EXEMPLO_CSV_Correto_vs_Errado.md**
- Comparação visual lado a lado
- Mostra diferença entre 450,00 (errado) e 450.00 (correto)
- Dicas de validação

**Uso:** Projetar ou distribuir na Aula 3

---

## 📁 Templates CSV

Prontos para usar nas aulas e exercícios:

1. **`template_basico.csv`**  
   Estrutura básica para começar qualquer orçamento

2. **`template_portas_janelas.csv`**  
   Quantificar esquadrias por tipo

3. **`template_estrutura_concreto.csv`**  
   Quantificar concreto por pavimento

4. **`template_location_type.csv`**  
   Combinação avançada: pavimento + tipo

**Uso:** Disponibilizar no Drive compartilhado ou USB

---

## 🗂️ Material Complementar (Referência)

### **DOCUMENTACAO_BonsaiBIM_Quantificacao.md**
Documentação completa original (antes da divisão em 3 aulas).  
Útil como referência adicional ou consulta.

---

## 🚀 Guia Rápido de Uso

### Para o professor que vai dar o curso:

1. **📖 LEIA PRIMEIRO:**
   - `GUIA_PROFESSOR_BonsaiBIM_3aulas.md`

2. **🖨️ IMPRIMA:**
   - `GUIA_RAPIDO_Salvar_CSV.md` (1 cópia por aluno)

3. **💾 PREPARE:**
   - Instale Blender em todos os computadores
   - Baixe arquivo IFC de exemplo
   - Coloque templates CSV no Drive/USB

4. **✅ TESTE:**
   - Faça você mesmo todas as 3 aulas
   - Especialmente: processo de salvar CSV

5. **📚 DISTRIBUA AOS ALUNOS:**
   - AULA1_Interface_Blender_BonsaiBIM.md
   - AULA2_Search_BonsaiBIM.md
   - AULA3_Quantificacao_BonsaiBIM.md
   - Templates CSV

---

## ⏰ Cronogramas Disponíveis

### Opção 1: Intensivo (2 dias - 9h)
```
Dia 1 - Manhã:  Aula 1 (Interface)
Dia 1 - Tarde:  Aula 2 (Search)
Dia 2 - Manhã:  Aula 3 (Quantificação)
```

### Opção 2: Semanal (3 semanas)
```
Semana 1: Aula 1 + para casa
Semana 2: Aula 2 + para casa
Semana 3: Aula 3 + trabalho final
```

### Opção 3: Integrado em disciplina
```
Ao longo do semestre, intercalado com conteúdo teórico
```

---

## 🎯 Pontos Críticos de Atenção

### 🔴 Aula 1: Instalação
- Testar Blender em TODOS os computadores antes
- Ter plano B se internet cair
- Navegação 3D precisa de PRÁTICA

### 🔴 Aula 2: Nomes exatos
- Nomes de pavimentos e tipos devem ser EXATOS
- Copiar do modelo, não inventar
- Acentos podem dar problema

### 🔴 Aula 3: Vírgula decimal ⚠️ **CRÍTICO!**
- **Este é o erro #1 dos alunos!**
- Enfatizar 10x
- Verificar arquivo de CADA aluno
- Distribuir guia impresso

---

## 📊 Avaliação Sugerida

| Aula | Peso | Critérios principais |
|------|------|---------------------|
| Aula 1 | 20% | Instalação + Navegação + Salvamento |
| Aula 2 | 30% | Queries corretas + Filtros + Para casa |
| Aula 3 | 50% | CSV correto + Ponto decimal + Importação |

**Trabalho Final:** Orçamento BIM completo (substitui ou complementa Aula 3)

---

## 🛠️ Troubleshooting Rápido

### Aula 1
- BonsaiBIM não instala → Instalação manual
- IFC não abre → Arquivo menor/mais simples
- Navegação travando → Ocultar elementos

### Aula 2
- Query não retorna nada → Nome incorreto
- Retorna elementos demais → Adicionar filtros

### Aula 3
- Custos não calculam → **90% é vírgula decimal!**
- Abrir CSV no Bloco de Notas → procurar pontos

---

## 📞 Suporte e Recursos

### Comunidade:
- 💬 [OSArch Community](https://community.osarch.org/)
- 📖 [BonsaiBIM Wiki](https://docs.bonsaibim.org/)
- 🎥 [YouTube](https://www.youtube.com/@BonsaiBIM)

### Para professores:
- Fórum de educadores OSArch
- Materiais compartilhados
- Grupo de professores

---

## 📝 Histórico de Versões

**v1.0 (Abril 2026)**
- Material inicial criado
- Estrutura de 3 aulas
- Ênfase em problema da vírgula decimal
- Templates e guias de apoio

---

## 📄 Licença

Material didático de uso livre para fins educacionais.  
Desenvolvido para BonsaiBIM 0.8.5

---

## ✨ Agradecimentos

Comunidade OSArch e BonsaiBIM  
Contribuidores do projeto IfcOpenShell

---

**Dúvidas sobre o material?**  
Consulte primeiro o `GUIA_PROFESSOR_BonsaiBIM_3aulas.md`

**Boa aula! 🚀**
