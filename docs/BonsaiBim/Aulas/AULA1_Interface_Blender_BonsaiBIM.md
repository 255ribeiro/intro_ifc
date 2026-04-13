# Aula 1: Interface Blender e BonsaiBIM Básico

## 📋 Índice
1. [Introdução ao Blender e BIM](#introdução-ao-blender-e-bim)
2. [Interface do Blender](#interface-do-blender)
3. [Configurações Recomendadas](#configurações-recomendadas)
4. [Instalação do BonsaiBIM](#instalação-do-bonsaibim)
5. [Abrindo Arquivos IFC](#abrindo-arquivos-ifc)
6. [Navegação no Modelo 3D](#navegação-no-modelo-3d)
7. [Salvando Arquivos (.blend vs .ifc)](#salvando-arquivos)
8. [Exercícios Práticos](#exercícios-práticos)

---

## Introdução ao Blender e BIM

### O que é Blender?

**Blender** é um software de código aberto (gratuito) para:
- Modelagem 3D
- Animação
- Renderização
- Edição de vídeo
- E muito mais...

**Por que Blender para BIM?**
- ✅ Gratuito e open source
- ✅ Multiplataforma (Windows, Mac, Linux)
- ✅ Poderoso para visualização 3D
- ✅ Com BonsaiBIM: suporte completo a IFC

### O que é BonsaiBIM?

**BonsaiBIM** (antes chamado BlenderBIM) é um **add-on** (extensão) para o Blender que adiciona funcionalidades BIM:
- Abrir e editar arquivos IFC nativamente
- Visualizar propriedades IFC
- Quantificação e orçamento
- Criar e modificar elementos BIM
- Exportar IFC compatível com outros softwares

**Versão do curso:** BonsaiBIM 0.8.5

---

## Interface do Blender

### Primeira abertura

Quando você abre o Blender pela primeira vez, verá uma tela de boas-vindas.

**Configuração inicial recomendada:**
1. Idioma: **Português** (ou English, conforme preferência)
2. Tema: **Blender Dark** (padrão)
3. Shortcuts: **Blender** (padrão)

Clique fora da janela de boas-vindas para começar.

---

### Layout da tela

```
┌─────────────────────────────────────────────────────────┐
│  Menu Superior (File, Edit, Render, Window, Help)      │
├──────────┬──────────────────────────────────┬──────────┤
│          │                                  │          │
│ Outliner │      3D Viewport                 │Properties│
│          │   (Janela de visualização 3D)    │ Panel    │
│  (Árvore │                                  │          │
│de objetos)                                  │          │
│          │                                  │          │
│          │                                  │          │
├──────────┴──────────────────────────────────┴──────────┤
│            Timeline (Linha do tempo)                    │
└─────────────────────────────────────────────────────────┘
```

### Áreas principais

**1. 3D Viewport (Centro)**
- Onde você visualiza o modelo 3D
- Área de trabalho principal

**2. Outliner (Esquerda)**
- Árvore hierárquica dos objetos
- Lista todos os elementos da cena
- **Muito importante para BIM!**

**3. Properties Panel (Direita)**
- Propriedades dos objetos selecionados
- Configurações da cena
- **Aqui aparece o painel BIM quando instalado**

**4. Timeline (Parte inferior)**
- Para animações (não usaremos muito)
- Pode ser minimizada

---

### Navegação básica no 3D Viewport

#### Com mouse de 3 botões:

**Rotacionar vista:**
- Botão do meio do mouse (scroll wheel) **pressionado e arraste**
- Ou: Mantenha `Shift` + botão direito e arraste

**Mover vista (Pan):**
- `Shift` + botão do meio + arraste

**Zoom:**
- Roda do mouse (scroll)
- Ou: `Ctrl` + botão do meio + arraste

**Focar em objeto:**
- Selecione o objeto (clique com botão esquerdo)
- Pressione `.` (ponto) no teclado numérico
- Ou: `View → Frame Selected` no menu

#### Atalhos de vista:

- `1` (numpad) → Vista frontal
- `3` (numpad) → Vista lateral direita
- `7` (numpad) → Vista superior
- `9` (numpad) → Vista oposta
- `5` (numpad) → Alternar perspectiva/ortográfica

**Importante:** Use o **teclado numérico** (à direita), não os números da linha superior!

---

### Seleção de objetos

**Selecionar um objeto:**
- Clique esquerdo no objeto

**Selecionar múltiplos:**
- `Shift` + clique esquerdo (adiciona à seleção)

**Selecionar todos:**
- `A` (All)

**Desselecionar todos:**
- `Alt + A`
- Ou clique em área vazia

**Selecionar por caixa:**
- `B` (Box select)
- Arraste para criar caixa
- Clique esquerdo para confirmar

---

## Configurações Recomendadas

### Antes de começar a trabalhar com BIM

**1. Unidades do sistema**

Arquivo importante para BIM usar as unidades corretas!

1. Vá em: **Edit → Preferences** (ou `Ctrl+,`)
2. Aba **System**
3. Em **Units**:
   - **Unit Scale**: `1.0`
   - **Length**: `Meters` (Métrico)
4. Clique em **Save Preferences**

---

**2. Interface**

1. **Edit → Preferences → Interface**
2. Recomendado:
   - ✅ **Display → Developer Extras** (para opções avançadas)
   - ✅ **Display → Python Tooltips** (ajuda com scripts)
3. **Save Preferences**

---

**3. Add-ons (vamos fazer na próxima seção)**

---

**4. Tema (opcional)**

1. **Edit → Preferences → Themes**
2. Escolha o tema que preferir
3. Recomendação: **Blender Dark** (padrão) ou **Blender Light**

---

**5. Salvar automaticamente**

1. **Edit → Preferences → Save & Load**
2. Configure:
   - ✅ **Auto Save** (salvar automaticamente)
   - **Auto Save Time**: `5` minutos (recomendado)
3. **Save Preferences**

---

## Instalação do BonsaiBIM

### Método 1: Instalação direta do Blender (MAIS FÁCIL)

**Blender 3.6 ou superior já vem com BonsaiBIM!**

1. **Edit → Preferences**
2. Vá na aba **Add-ons**
3. Na busca, digite: `bonsai`
4. ✅ Marque a caixa ao lado de **Import-Export: BonsaiBIM**
5. Aguarde alguns segundos (vai baixar e instalar)
6. Clique em **Save Preferences**

**Verificar se instalou:**
- Olhe na barra lateral direita (Properties)
- Deve aparecer um ícone de casa 🏠 (BIM)
- Se não aparecer, pressione `N` no 3D Viewport

---

### Método 2: Download manual (se método 1 não funcionar)

**Passo 1: Baixar**
1. Acesse: [https://bonsaibim.org/](https://bonsaibim.org/)
2. Clique em **Download**
3. Escolha a versão para seu sistema operacional
4. Salve o arquivo `.zip`

**Passo 2: Instalar**
1. No Blender: **Edit → Preferences**
2. Aba **Add-ons**
3. Clique em **Install...** (canto superior direito)
4. Navegue até o arquivo `.zip` baixado
5. Clique em **Install Add-on**
6. ✅ Marque a caixa ao lado de **Import-Export: BonsaiBIM**
7. **Save Preferences**

---

### Verificação

Após instalar, você deve ver:

**Na barra de propriedades (direita):**
- Novo ícone 🏠 (BIM) entre os ícones existentes

**No menu File:**
- **File → Import → Industry Foundation Classes (.ifc)**
- **File → Export → Industry Foundation Classes (.ifc)**

**Na barra lateral do 3D Viewport:**
- Pressione `N` para abrir
- Nova aba **BIM** deve aparecer

✅ Se vir isso, está instalado corretamente!

---

## Abrindo Arquivos IFC

### Método 1: Import IFC (Recomendado para iniciantes)

1. **File → Import → Industry Foundation Classes (.ifc)**
2. Navegue até seu arquivo `.ifc`
3. Selecione o arquivo
4. Clique em **Import IFC**
5. Aguarde o carregamento (pode levar alguns segundos para modelos grandes)

**O que acontece:**
- O modelo IFC é carregado no Blender
- A hierarquia aparece no Outliner (painel esquerdo)
- Elementos ficam visíveis no 3D Viewport

---

### Método 2: Open IFC Project (Para usuários avançados)

1. Vá na aba **BIM** (no painel de propriedades à direita)
2. Clique em **BIM Project**
3. Clique em **Open Project**
4. Selecione o arquivo `.ifc`

**Diferença:**
- Este método é mais "nativo" ao BonsaiBIM
- Mantém melhor as propriedades IFC
- Recomendado para edição de IFC

---

### Entendendo a hierarquia

Após abrir o IFC, olhe no **Outliner** (painel esquerdo):

```
IfcProject
└── IfcSite (Terreno)
    └── IfcBuilding (Edifício)
        ├── IfcBuildingStorey (Térreo)
        │   ├── IfcWall
        │   ├── IfcWall
        │   ├── IfcColumn
        │   └── IfcDoor
        ├── IfcBuildingStorey (1º Pavimento)
        │   ├── IfcWall
        │   └── IfcWindow
        └── IfcBuildingStorey (2º Pavimento)
```

**Importante:**
- IfcProject = raiz do projeto
- IfcSite = terreno
- IfcBuilding = edifício
- IfcBuildingStorey = pavimentos (andares)
- Dentro dos pavimentos: elementos (paredes, portas, etc.)

---

### Navegação pela hierarquia

**Expandir/Recolher:**
- Clique na **setinha** ao lado do nome

**Ocultar/Mostrar elementos:**
- Clique no **ícone de olho** 👁️

**Isolar pavimento:**
1. Selecione o pavimento no Outliner
2. Pressione `/` no teclado numérico (isola seleção)
3. Pressione `/` novamente para mostrar tudo

---

## Navegação no Modelo 3D

### Explorando o modelo

**1. Vista geral**
- Pressione `7` (numpad) para vista superior
- Use scroll do mouse para dar zoom
- Rotacione com botão do meio

**2. Ver pavimento específico**
- No Outliner, clique no pavimento
- Pressione `.` (ponto do teclado numérico) para focar

**3. Ocultar elementos**
- Útil para ver estrutura interna
- No Outliner: clique no 👁️ ao lado dos elementos
- Exemplo: ocultar lajes para ver pilares

**4. Isolar elemento**
- Selecione o elemento
- Pressione `/` (numpad) para isolar
- Apenas esse elemento fica visível

---

### Visualização dos elementos

**Modos de visualização (Shading):**

No canto superior direito do 3D Viewport, você verá 4 círculos:

1. **Wireframe** (Aramado) - linhas apenas
2. **Solid** (Sólido) - mais usado para BIM
3. **Material Preview** - com materiais aplicados
4. **Rendered** - renderização final

**Recomendação para BIM:** Use **Solid** (segundo círculo)

---

### Selecionando elementos IFC

**Por clique:**
- Clique esquerdo no elemento no 3D Viewport

**Pelo Outliner:**
- Clique no nome do elemento no Outliner

**Ver propriedades:**
- Selecione o elemento
- Olhe no painel BIM (à direita)
- Veja propriedades IFC do elemento

---

## Salvando Arquivos

### Diferença entre .blend e .ifc

**Arquivo .blend:**
- Formato nativo do Blender
- Salva TUDO: geometria, câmeras, luzes, materiais, etc.
- Mais rápido para abrir
- **Use para trabalho diário no Blender**

**Arquivo .ifc:**
- Formato padrão BIM (interoperável)
- Compatível com outros softwares (Revit, ArchiCAD, etc.)
- Apenas dados BIM (propriedades IFC)
- **Use para compartilhar com outros programas**

### Regra geral

```
Trabalho diário → Salve .blend
Compartilhar/entregar → Exporte .ifc
```

---

### Como salvar .blend

**Primeira vez (Save As):**
1. **File → Save As...** (ou `Shift + Ctrl + S`)
2. Navegue até a pasta desejada
3. Digite o nome: `meu_projeto.blend`
4. Clique em **Save As Blender File**

**Próximas vezes (Save):**
- **File → Save** (ou `Ctrl + S`)
- Salva rapidamente no mesmo arquivo

**Recomendação:**
- Crie pastas organizadas por projeto
- Use nomes descritivos: `residencial_silva_v01.blend`

---

### Como exportar .ifc

**Método 1: Export simples**

1. **File → Export → Industry Foundation Classes (.ifc)**
2. Navegue até a pasta
3. Digite o nome: `meu_projeto.ifc`
4. Clique em **Export IFC**

**Método 2: Save IFC Project (mais correto)**

1. Painel BIM → **BIM Project**
2. Clique em **Save Project**
3. Escolha local e nome
4. Salvar

**Quando exportar IFC:**
- Ao finalizar modelagem
- Para enviar para cliente
- Para abrir em outro software BIM
- Para validar IFC

---

### Versionamento (boas práticas)

**Organize seus arquivos:**

```
Projeto_Residencial/
├── modelo/
│   ├── residencial_v01.blend
│   ├── residencial_v02.blend
│   └── residencial_v03.blend
├── exportacao/
│   ├── residencial_v01.ifc
│   ├── residencial_v02.ifc
│   └── residencial_final.ifc
└── documentacao/
    └── quantitativos_v01.csv
```

**Dica:**
- Use números de versão: v01, v02, v03
- Mantenha versões antigas (pelo menos últimas 3)
- Nunca sobrescreva a única cópia!

---

## Exercícios Práticos

### Exercício 1: Instalação e configuração

**Objetivo:** Preparar o Blender para trabalho BIM

Checklist:
- [ ] Abrir Blender
- [ ] Configurar idioma (se desejar)
- [ ] Configurar unidades para Meters
- [ ] Instalar BonsaiBIM add-on
- [ ] Verificar aba BIM no painel de propriedades
- [ ] Configurar auto-save para 5 minutos
- [ ] Salvar preferências

---

### Exercício 2: Abrir e navegar em IFC

**Objetivo:** Familiarizar com interface e navegação

Passos:
1. Baixe um modelo IFC de exemplo (professor fornecerá)
2. Importe o IFC no Blender
3. Explore a hierarquia no Outliner
4. Pratique navegação:
   - Vista superior (tecla 7)
   - Vista frontal (tecla 1)
   - Vista lateral (tecla 3)
   - Rotacionar com botão do meio
   - Zoom com scroll
5. Selecione diferentes elementos
6. Oculte e mostre pavimentos

---

### Exercício 3: Visualização

**Objetivo:** Dominar modos de visualização

Tarefas:
1. Mude entre modos de shading (wireframe, solid, material)
2. Oculte todas as lajes (no Outliner)
3. Veja a estrutura interna (pilares e vigas)
4. Isole um pavimento específico (tecla /)
5. Selecione uma porta e veja suas propriedades IFC

---

### Exercício 4: Salvar arquivos

**Objetivo:** Praticar salvamento .blend e .ifc

Passos:
1. Crie uma pasta para o exercício
2. Salve o projeto como .blend
   - Nome: `exercicio_01.blend`
3. Faça uma pequena mudança (oculte um elemento)
4. Salve novamente (Ctrl+S)
5. Exporte como .ifc
   - Nome: `exercicio_01.ifc`
6. Verifique que ambos os arquivos existem na pasta

---

### Exercício 5: Hierarquia IFC

**Objetivo:** Entender estrutura de um modelo IFC

Tarefas:
1. No Outliner, expanda toda a hierarquia
2. Identifique e anote:
   - Quantos pavimentos tem?
   - Quais os nomes dos pavimentos?
   - Que tipos de elementos existem? (IfcWall, IfcDoor, etc.)
3. Selecione um elemento de cada tipo:
   - IfcColumn (pilar)
   - IfcBeam (viga)
   - IfcDoor (porta)
   - IfcWindow (janela)
4. Para cada um, veja as propriedades IFC no painel BIM

---

## Dicas e Atalhos Importantes

### Atalhos essenciais

| Ação | Atalho |
|------|--------|
| Salvar | `Ctrl + S` |
| Salvar como | `Shift + Ctrl + S` |
| Desfazer | `Ctrl + Z` |
| Refazer | `Shift + Ctrl + Z` |
| Selecionar tudo | `A` |
| Desselecionar tudo | `Alt + A` |
| Deletar | `X` |
| Focar seleção | `.` (numpad) |
| Isolar seleção | `/` (numpad) |

### Navegação 3D

| Ação | Atalho |
|------|--------|
| Rotacionar vista | Botão do meio + arraste |
| Pan (mover) | `Shift` + botão do meio |
| Zoom | Scroll do mouse |
| Vista frontal | `1` (numpad) |
| Vista lateral | `3` (numpad) |
| Vista superior | `7` (numpad) |
| Perspectiva/Ortográfica | `5` (numpad) |

---

## Resolução de Problemas

### BonsaiBIM não aparece

**Sintomas:**
- Não vejo o ícone BIM
- Menu Import não tem opção IFC

**Soluções:**
1. Verifique se o add-on está ativado:
   - Edit → Preferences → Add-ons
   - Procure "BonsaiBIM"
   - Certifique-se que está marcado ✅
2. Reinicie o Blender
3. Tente instalação manual (Método 2)

---

### IFC não abre

**Sintomas:**
- Erro ao importar IFC
- Modelo não aparece

**Soluções:**
1. Verifique se o arquivo IFC não está corrompido
   - Tente abrir em outro software BIM
2. Verifique tamanho do arquivo
   - Arquivos muito grandes (>500MB) podem travar
3. Tente importar em um novo arquivo Blender vazio
4. Verifique versão do IFC (IFC2x3 ou IFC4)

---

### Navegação lenta

**Sintomas:**
- Modelo trava ao rotacionar
- Zoom muito lento

**Soluções:**
1. Modelo muito grande:
   - Oculte pavimentos que não está usando
   - Use modo Wireframe
2. Reduza geometria de visualização
3. Feche outros programas

---

### Perdi meu trabalho

**Prevenção:**
1. ✅ Configure Auto-Save!
2. ✅ Salve manualmente com frequência (Ctrl+S)
3. ✅ Use versionamento (v01, v02, v03)

**Recuperação:**
- File → Recover → Last Session
- File → Recover → Auto Save

---

## Checklist da Aula

Ao final desta aula, você deve saber:

- [ ] Abrir o Blender
- [ ] Configurar unidades para metros
- [ ] Instalar o add-on BonsaiBIM
- [ ] Navegar pelo 3D Viewport (rotacionar, pan, zoom)
- [ ] Usar vistas (frontal, lateral, superior)
- [ ] Importar arquivos .ifc
- [ ] Explorar hierarquia no Outliner
- [ ] Selecionar elementos
- [ ] Ocultar/mostrar elementos
- [ ] Ver propriedades IFC
- [ ] Salvar arquivo .blend
- [ ] Exportar arquivo .ifc
- [ ] Diferenciar quando usar .blend vs .ifc

---

## Próxima Aula

**Aula 2: Search - Seleção de Entidades IFC**

Na próxima aula vamos aprender:
- Como usar queries para selecionar elementos
- Filtros por pavimento, tipo, nome
- Preparação para quantificação automática

---

## Recursos Adicionais

**BonsaiBIM:**
- 🌐 [Site oficial](https://bonsaibim.org/)
- 📖 [Documentação](https://docs.bonsaibim.org/)
- 🎥 [Canal YouTube](https://www.youtube.com/@BonsaiBIM)
- 💬 [Comunidade](https://community.osarch.org/)

**Blender:**
- 📖 [Manual oficial](https://docs.blender.org/)
- 🎓 [Tutoriais](https://www.blender.org/support/tutorials/)

---

*Documentação criada para BonsaiBIM 0.8.5 + Blender 3.6+*  
*Aula 1: Interface Blender e BonsaiBIM Básico*  
*Última atualização: Abril 2026*
