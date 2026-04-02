# BIM Execution Plan (BEP)

> **Documento central de governança BIM** — define quem faz o quê, quando, com qual software e em qual nível de detalhe ao longo de todo o ciclo de vida do projeto.

---

## Sumário

1. [O que é o BEP](#o-que-é-o-bep)
2. [Relação com o EIR](#relação-com-o-eir)
3. [Tipos de BEP](#tipos-de-bep)
4. [Seções obrigatórias](#seções-obrigatórias)
5. [Modelo básico de BEP](#modelo-básico-de-bep)
6. [BEP no contexto da ISO 19650](#bep-no-contexto-da-iso-19650)
7. [Fluxo de elaboração](#fluxo-de-elaboração)
8. [Checklist de verificação](#checklist-de-verificação)
9. [Referências](#referências)

---

## O que é o BEP

O **BIM Execution Plan (BEP)** é um documento formal que define como os processos BIM serão conduzidos em um projeto específico.[^1] Ele estabelece:

- o **escopo de uso do BIM** (quais BIM Uses serão aplicados);
- os **papéis e responsabilidades** de cada membro da equipe;
- os **procedimentos de colaboração** e protocolos de troca de informação;
- as **especificações de software**, versões e formatos de intercâmbio.

Em síntese, o BEP responde à pergunta: *"Como o BIM será implementado com sucesso neste projeto?"*[^2]

!!! note "Documento vivo"
    O BEP deve ser atualizado ao longo de todo o ciclo de vida do projeto à medida que novas decisões são tomadas, membros entram na equipe ou o escopo evolui. A ISO 19650-2 define momentos específicos de revisão e aprovação.[^3]

!!! tip "Terminologia"
    O BEP também aparece nas siglas **BIM PxP**, **BIM PEP**, **BIMEx** ou **BxP** em diferentes guias. A ISO 19650 adotou oficialmente o termo **BEP**, que tende a se consolidar internacionalmente.[^4]

---

## Relação com o EIR

O BEP é preparado como **resposta ao EIR** (Employer's Information Requirements). O contratante define suas expectativas de informação; a equipe de projeto responde descrevendo como entregará essas expectativas.

```mermaid
flowchart LR
    A([Contratante]) -->|publica| B[EIR\nEmployer's Information\nRequirements]
    B -->|fundamenta| C[BEP\nBIM Execution Plan]
    C -->|responde a| B
    C -->|governa| D[Execução BIM\ndo Projeto]
    D -->|gera| E[Entregáveis\nIFC · COBie · BCF]
    E -->|validados contra| F[IDS\nInformation Delivery\nSpecification]
    F -->|derivado do| B
```

### Ecossistema de documentos relacionados

| Sigla | Nome | Elaborado por |
|-------|------|--------------|
| **OIR** | Organizational Information Requirements | Contratante (nível organizacional) |
| **PIR** | Project Information Requirements | Contratante (nível de projeto) |
| **EIR** | Employer's Information Requirements | Contratante (para licitação) |
| **BEP** | BIM Execution Plan | Equipe de entrega (resposta ao EIR) |
| **MIDP** | Master Information Delivery Plan | Líder da equipe |
| **TIDP** | Task Information Delivery Plan | Cada disciplina/empresa |
| **IDS** | Information Delivery Specification | Contratante ou BIM Manager |

---

## Tipos de BEP

A ISO 19650-2 define duas iterações principais do BEP ao longo do processo de contratação.[^5]

```mermaid
timeline
    title Evolução do BEP ao longo do projeto
    section Licitação
        Publicação do EIR : Contratante define requisitos
        Pre-appointment BEP : Equipes concorrentes elaboram proposta BIM
    section Contratação
        Avaliação dos BEPs : Contratante seleciona equipe
        Delivery Team BEP  : Equipe contratada confirma e detalha o BEP
    section Execução
        BEP Fase LP/AP  : Revisão e atualização por fase
        BEP Fase EP     : Revisão e atualização por fase
        BEP Obras       : Revisão e atualização por fase
    section Entrega
        Handover BEP    : Atualização final para FM/operação
```

### Pré-appointment BEP

Elaborado pelo potencial líder da equipe de entrega durante a licitação, como parte da proposta técnica.[^6]

- Propõe como os requisitos do EIR serão atendidos, **sem garantia de contratação**
- Permite ao contratante avaliar a **capacidade técnica BIM** dos concorrentes
- Inclui visão geral de abordagem, equipe proposta e metodologia
- Referenciado na **ISO 19650-2, Cláusula 5.3.2**

### Delivery Team BEP

Confirmado após a contratação, desenvolvido colaborativamente pela equipe completa.[^6]

- É o **documento de referência operacional** durante toda a execução
- Detalha todos os procedimentos, padrões e responsabilidades com base no contrato
- Incorpora feedbacks do contratante ao pré-BEP
- Referenciado na **ISO 19650-2, Cláusula 5.4.1**

---

## Seções obrigatórias

Com base na ISO 19650, Penn State BEP Guide e NBIMS-US, as seções essenciais de um BEP completo são:[^7][^8][^9]

```mermaid
mindmap
  root((BEP))
    Identificação
      Capa e controle de revisões
      Informações do projeto
    Estratégia BIM
      Objetivos e BIM Uses
      Níveis de informação LOD/LOI
      Estratégia de entrega MIDP/TIDP
    Pessoas
      Equipe e responsabilidades
      Matriz RACI
    Processos
      Processos de colaboração
      Gestão de qualidade QA/QC
      Segurança da informação
    Tecnologia
      Infraestrutura de software
      Common Data Environment CDE
      Padrões e convenções
    Entrega
      Handover e FM
      Apêndices e templates
```

A NATSPEC estrutura as seções do BEP em três aspectos conforme a **ISO 19650.1, Seção 5**:[^10]

- **Comercial** — entrega, contrato, equipe, finalidades da informação
- **Gerencial** — QA, segurança, gestão do CDE, revisões
- **Técnico** — padrões, software, formatos, convenções

---

## Modelo básico de BEP

A seguir, o conteúdo esperado em cada seção de um BEP típico para projeto de edificação.

---

### 1.0 Capa e Controle de Revisões

Identifica o documento e registra seu histórico.

| Campo | Valor |
|-------|-------|
| Título | BIM Execution Plan — [Nome do Projeto] |
| Número | [PROJ-BEP-001] |
| Status | Rascunho / Compartilhado / Publicado |
| Versão | [1.0] |

**Histórico de revisões:**

| Rev. | Data | Descrição | Elaborado por | Aprovado por |
|------|------|-----------|---------------|--------------|
| P0 | dd/mm/aaaa | Emissão inicial | [Nome] | [Nome] |
| P1 | dd/mm/aaaa | Incorpora feedback do EIR | [Nome] | [Nome] |
| C0 | dd/mm/aaaa | Versão contratual | [Nome] | [Nome] |

---

### 2.0 Informações do Projeto

| Campo | Conteúdo |
|-------|----------|
| Nome do projeto | [Nome oficial] |
| Localização | [Endereço completo] |
| Cliente / Contratante | [Razão social + CNPJ] |
| Fases cobertas | [EP / LP / AP / Obras / Operação] |
| Disciplinas | [ARQ / EST / HID / ELT / AR-COND / ...] |
| Versão IFC adotada | [IFC 4 / IFC 4.3] |
| Norma de referência | ISO 19650-2:2018 / ABNT NBR ISO 19650 |

---

### 3.0 Objetivos e Usos do BIM

Lista os BIM Uses definidos para o projeto, com objetivos mensuráveis para cada um.[^1]

| # | BIM Use | Fase | Objetivo mensurável | Responsável |
|---|---------|------|--------------------:|-------------|
| 01 | Modelagem de projeto | LP → EP | Modelo único de referência por disciplina | BIM Author |
| 02 | Coordenação 3D / Clash detection | AP → EP | Zero clashes hard antes do início da obra | BIM Coordinator |
| 03 | Quantitativos e orçamento | EP | Extração automática com desvio ≤ 5% | Orçamentista |
| 04 | Planejamento 4D | Obras | Sequenciamento vinculado ao cronograma Ms Project | Const. BIM |
| 05 | Análise de sustentabilidade | AP | Simulação energética para LEED/AQUA | Consultor |
| 06 | Gestão de ativos (FM) | Entrega | Modelo COBie para CMMS do cliente | FM Manager |

---

### 4.0 Equipe e Responsabilidades

```mermaid
graph TD
    A[BIM Manager\nLíder da Equipe] --> B[BIM Coordinator\nArquitetura]
    A --> C[BIM Coordinator\nEstrutura]
    A --> D[BIM Coordinator\nMEP]
    A --> E[Gestor de\nInformação / CDE]
    B --> F[BIM Author ARQ\nEmpresa A]
    C --> G[BIM Author EST\nEmpresa B]
    D --> H[BIM Author HID\nEmpresa C]
    D --> I[BIM Author ELT\nEmpresa C]
```

**Matriz de responsabilidades (RACI):**

| Atividade | BIM Manager | BIM Coord. | BIM Author | Gestor Info. | Contratante |
|-----------|:-----------:|:----------:|:----------:|:------------:|:-----------:|
| Elaborar e aprovar BEP | A | C | I | C | A |
| Modelar por disciplina | I | R | R | I | I |
| Clash detection | A | R | C | I | I |
| Publicar no CDE | A | C | C | R | I |
| Verificação QA/QC | A | R | R | C | I |
| Aprovação de entregas | C | C | I | I | A |

> **Legenda:** R = Responsável · A = Aprovador · C = Consultado · I = Informado

---

### 5.0 Estratégia de Entrega de Informação

O **MIDP** (Master Information Delivery Plan) consolida todos os entregáveis de informação do projeto. Cada disciplina elabora seu **TIDP** (Task Information Delivery Plan).[^8]

| Disciplina | Marco de entrega | Data prevista | Formato nativo | Intercâmbio | LOD | Responsável |
|------------|-----------------|:-------------:|:----------:|:---:|:---:|-------------|
| ARQ | Entrega EP | dd/mm/aaaa | .rvt | IFC 4 | 350 | BIM Coord. ARQ |
| EST | Entrega EP | dd/mm/aaaa | .tekla | IFC 4 | 350 | BIM Coord. EST |
| HID | Entrega EP | dd/mm/aaaa | .rvt MEP | IFC 4 | 300 | BIM Coord. MEP |
| ELT | Entrega EP | dd/mm/aaaa | .rvt MEP | IFC 4 | 300 | BIM Coord. MEP |
| AR-COND | Entrega EP | dd/mm/aaaa | .rvt MEP | IFC 4 | 300 | BIM Coord. MEP |
| Federado | Coord. semanal | toda sexta | — | IFC 4 + BCF | — | BIM Manager |

---

### 6.0 Padrões e Convenções

#### Convenção de nomenclatura de arquivos

```
[PROJ]-[ORIG]-[VOL/SIST]-[NÍVEL]-[TIPO]-[FUNC]-[NUM]
```

**Exemplo:** `EDIF-ARQ-ZA-00-MOD-001` = Edificação · Arquitetura · Zona A · Térreo · Modelo · Arquivo 001

| Campo | Opções |
|-------|--------|
| PROJ | Código de 4 letras do projeto |
| ORIG | ARQ / EST / HID / ELT / AR / PAI |
| VOL/SIST | Zona ou sistema (ZA, ZB, EST, MEP...) |
| NÍVEL | 00 (térreo) / 01 / 02 / SS1 / COB |
| TIPO | MOD (modelo) / DWG (desenho) / DOC (documento) |
| NUM | Sequencial de 3 dígitos |

#### Sistema de coordenadas

- **Sistema:** SIRGAS 2000 / UTM Fuso 23S (adaptar conforme localização)
- **Ponto de origem compartilhado:** definido no arquivo de vínculo de coordenadas no CDE
- **Elevação Z=0,000:** corresponde ao nível ±0 = piso acabado do pavimento térreo

#### Unidades

| Grandeza | Unidade |
|----------|---------|
| Comprimento | Milímetros (mm) |
| Área | Metro quadrado (m²) |
| Volume | Metro cúbico (m³) |
| Ângulo | Graus decimais |
| Temperatura | Graus Celsius (°C) |

#### Código de status de documentos

| Código | Status | Descrição |
|--------|--------|-----------|
| S0 | Work In Progress (WIP) | Em elaboração — acesso restrito à equipe autora |
| S1 | Shared | Compartilhado para revisão interna |
| S2 | Published | Aprovado para uso por outras disciplinas |
| S3 | Archived | Versão arquivada / substituída |
| S4 | Void | Documento obsoleto / cancelado |

---

### 7.0 Common Data Environment (CDE)

```mermaid
stateDiagram-v2
    [*] --> WIP : Criação do arquivo
    WIP --> Shared : Equipe autora compartilha para revisão
    Shared --> WIP : Revisão solicita correções
    Shared --> Published : BIM Manager aprova
    Published --> Archived : Nova versão publicada
    Published --> Void : Documento cancelado
    Archived --> [*]
    Void --> [*]

    note right of WIP
        Acesso: somente a equipe autora
        Localização: pasta da disciplina
    end note
    note right of Published
        Acesso: toda a equipe
        Fonte de verdade do projeto
    end note
```

| Campo | Detalhamento |
|-------|-------------|
| Plataforma CDE | [Autodesk Construction Cloud / BIMcollab NEXUS / Trimble Connect] |
| URL de acesso | [https://...] |
| Responsável pela administração | [Gestor de Informação — e-mail / telefone] |
| Política de acesso | [Descrever permissões por papel: leitura, edição, aprovação] |
| Frequência de backup | [Diário automático / política da plataforma] |

---

### 8.0 Processos de Colaboração

| Atividade | Frequência | Ferramenta | Responsável | Participantes |
|-----------|:----------:|-----------|-------------|--------------|
| Reunião BIM de kickoff | Início do projeto | Videoconferência | BIM Manager | Toda a equipe |
| Reunião de coordenação BIM | Semanal | Navisworks / Solibri | BIM Manager | BIM Coordinators |
| Clash detection — Hard clashes | Semanal | Navisworks / BIMcollab | BIM Coord. MEP | Todos coords. |
| Clash detection — Soft clashes | Quinzenal | Navisworks | BIM Coord. ARQ | Todos coords. |
| Revisão e fechamento de issues (BCF) | Semanal | BIMcollab / ACC | Todos coords. | Equipe autora |
| Publicação de modelo federado | Mensal | CDE | BIM Manager | — |
| Revisão de fase | Por marco contratual | CDE + reunião | BIM Manager | Contratante |

---

### 9.0 Garantia de Qualidade da Informação (QA/QC)

```mermaid
flowchart TD
    A[BIM Author\nconclui modelagem] --> B{Verificação\nvisual}
    B -->|Aprovado| C{Verificação\nde consistência\nIfcOpenShell / Solibri}
    B -->|Reprovado| A
    C -->|Aprovado| D{Verificação\nde propriedades\nIDS}
    C -->|Reprovado| A
    D -->|100% PASS| E[Status: Shared\nno CDE]
    D -->|FAIL| A
    E --> F{Clash\ndetection}
    F -->|Zero hard clashes| G[Aprovação\nBIM Manager]
    F -->|Clashes encontrados| H[Issue BCF\ncriada]
    H --> A
    G --> I[Status: Published\nno CDE]
```

| Tipo de verificação | Ferramenta | Frequência | Critério de aprovação |
|--------------------|-----------|:----------:|----------------------|
| Visual (walkaround) | Navisworks / BIMvision | Antes de cada entrega | Sem objetos faltantes ou mal posicionados |
| Consistência IFC | Solibri / BIMcollab Zoom | Antes de cada entrega | Zero erros críticos de schema |
| Propriedades (IDS) | Solibri / IfcOpenShell | A cada entrega | 100% PASS nas specs obrigatórias |
| Clash detection (hard) | Navisworks / Solibri | Semanal | Zero clashes hard não resolvidos |
| Clash detection (soft) | Navisworks | Quinzenal | Registro e priorização de todos |
| Revisão de fase | — | Por marco | Aprovação formal no CDE pelo contratante |

---

### 10.0 Infraestrutura Tecnológica

| Disciplina | Software | Versão | Formato nativo | Intercâmbio |
|-----------|---------|:------:|:----------:|:----------:|
| Arquitetura | Autodesk Revit | 2025 | .rvt | IFC 4 |
| Estruturas | Tekla Structures | 2024 | .tekla | IFC 4 |
| MEP (instalações) | Autodesk Revit MEP | 2025 | .rvt | IFC 4 |
| Coordenação / Clash | Autodesk Navisworks | 2025 | .nwd / .nwf | BCF 2.1 |
| Validação IDS | Solibri / IfcOpenShell | — | — | Relatório .bcf / .json |
| CDE | Autodesk Construction Cloud | — | — | API REST |
| Issues / BCF | BIMcollab / ACC | — | — | BCF 2.1 |

!!! warning "Interoperabilidade"
    Todos os arquivos trocados entre disciplinas devem ser exportados em **IFC 4** (schema `IFC4`). Formatos nativos (.rvt, .tekla) são mantidos internamente pela equipe autora e não constituem formato oficial de intercâmbio entre empresas.

---

### 11.0 Segurança da Informação

| Requisito | Detalhamento |
|-----------|-------------|
| Segregação de dados | Informações sensíveis (dados estruturais críticos, segurança) em pasta de acesso restrito no CDE |
| Controle de acesso | Baseado em papéis (RBAC) — definido pelo Gestor de Informação |
| Conformidade LGPD | Dados pessoais de membros da equipe tratados conforme Lei 13.709/2018 |
| Requisitos do contratante | [Inserir referência ao documento de segurança do contratante, quando aplicável] |

---

### 12.0 Entrega Final e Handover

| Item | Detalhamento |
|------|-------------|
| Formatos de entrega final | IFC 4 (modelo), COBie 2.4 (FM), PDF/A (documentação), DWG R2018 (plantas de registro) |
| Dados de FM obrigatórios | Fabricante, número de série, data de instalação, garantia, manual de manutenção |
| Processo de as-built | [Responsável e prazo para incorporar alterações de obra ao modelo] |
| Sistema de destino (CMMS) | [IBM Maximo / SAP PM / ARCHIBUS / Outro] |
| Aprovação final | Checklist de entrega + aprovação formal no CDE pelo contratante |

---

### 13.0 Apêndices

| Apêndice | Documento | Localização no CDE |
|----------|-----------|-------------------|
| A | MIDP — Master Information Delivery Plan | [Link CDE] |
| B | TIDPs por disciplina (ARQ, EST, MEP...) | [Link CDE] |
| C | Arquivo IDS do projeto (.ids) | [PROJ-IDS-001.ids] |
| D | Templates de modelo por disciplina | [Link CDE] |
| E | Checklists de QA por fase | [Link CDE] |
| F | Diagrama de fluxo do CDE | [Link CDE] |
| G | Tabela LOD/LOI por elemento e fase | [Ref. BIM Forum LOD Spec] |

---

## BEP no contexto da ISO 19650

```mermaid
sequenceDiagram
    autonumber
    actor CP as Contratante<br/>(Appointing Party)
    actor LE as Líder da Equipe<br/>(Lead Appointed Party)
    actor EQ as Equipes<br/>(Appointed Parties)

    CP->>LE: Publica EIR + documentos de licitação
    LE->>CP: Entrega Pré-appointment BEP (ISO 19650-2 §5.3.2)
    CP->>LE: Avalia e seleciona equipe
    CP->>LE: Confirmação da contratação
    LE->>EQ: Solicita contribuição para Delivery Team BEP
    EQ->>LE: Entregam TIDPs e informações de processo
    LE->>CP: Entrega Delivery Team BEP (ISO 19650-2 §5.4.1)
    CP->>LE: Aprovação formal do BEP
    Note over LE,EQ: Execução do projeto — BEP é referência operacional
    LE->>CP: Revisão do BEP a cada nova fase / marco
    CP->>LE: Aprovação das revisões
```

### Hierarquia de documentos na ISO 19650

```mermaid
graph TD
    OIR["OIR\nOrganizational Information\nRequirements\n(nível organizacional)"]
    PIR["PIR\nProject Information\nRequirements\n(nível de projeto)"]
    EIR["EIR\nEmployer's Information\nRequirements\n(licitação)"]
    preBEP["Pre-appointment BEP\n(proposta — pré-contrato)"]
    dtBEP["Delivery Team BEP\n(pós-contrato — documento operacional)"]
    MIDP["MIDP\nMaster Information\nDelivery Plan"]
    TIDPs["TIDPs\nTask Information\nDelivery Plans\n(por disciplina)"]
    IDS["IDS\nInformation Delivery\nSpecification"]

    OIR --> PIR --> EIR
    EIR -->|"fundamenta"| preBEP
    preBEP -->|"evolui para"| dtBEP
    dtBEP --> MIDP
    MIDP --> TIDPs
    EIR -.->|"gera"| IDS
    IDS -.->|"referenciado em"| dtBEP
```

---

## Fluxo de elaboração

```mermaid
flowchart TD
    S1["📋 1. Revisar o EIR e objetivos\nAnalisar requisitos mandatórios e opcionais\nCompreender objetivos estratégicos do cliente"]
    S2["🎯 2. Definir os BIM Uses\nSelecionar usos BIM aplicáveis\nDefinir objetivo mensurável para cada um"]
    S3["👥 3. Mapear equipe e responsabilidades\nIdentificar todos os participantes\nCriar organograma BIM e matriz RACI"]
    S4["📐 4. Definir padrões, convenções e CDE\nAcordar nomenclatura, coordenadas, templates\nSelecionar e configurar a plataforma CDE"]
    S5["📅 5. Elaborar MIDP e TIDPs\nConsolidar entregáveis, datas, formatos e LOD\nCada disciplina elabora seu TIDP"]
    S6["✅ 6. Definir processos de QA/QC e colaboração\nDocumentar rotinas de verificação e clash\nDefinir fluxo de aprovação e BCF"]
    S7["📤 7. Revisar, aprovar e publicar\nCompartilhar rascunho com todas as partes\nPublicar no CDE com status aprovado"]
    S8["🔄 8. Manter e atualizar\nRevisar a cada nova fase ou mudança relevante\nRegistrar todas as revisões no histórico"]

    S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8
    S8 -.->|"nova fase / mudança"| S1
```

### Boas práticas de elaboração

- **Envolver todos cedo:** incluir as equipes de projeto e construção desde a elaboração do pré-BEP evita revisões custosas após a contratação.[^11]
- **BIM Uses com objetivos mensuráveis:** cada uso BIM deve ter um critério de sucesso verificável — "reduzir RFIs em 40%" é melhor que "melhorar a coordenação".[^2]
- **Flexibilidade planejada:** um BEP rígido se torna obsoleto; prever ciclos de revisão garante que o documento permaneça relevante.[^3]
- **Usar templates como ponto de partida:** templates da Penn State, NATSPEC ou CDBB são bases consolidadas — adapte ao projeto, nunca copie sem reflexão.[^9][^10]
- **Validar contra o IDS:** quando o projeto tiver um IDS definido, referenciar explicitamente no BEP como os modelos serão validados automaticamente.[^12]

---

## Checklist de verificação

Use esta lista antes de submeter o BEP ao contratante.

### Identificação e controle

- [ ] Capa com título, número do documento, versão, data e status
- [ ] Controle de revisões com histórico completo de alterações
- [ ] Aprovações formais identificadas por papel

### Estratégia BIM

- [ ] Informações completas do projeto e fases cobertas pelo BEP
- [ ] Lista de BIM Uses com objetivos mensuráveis para cada um
- [ ] Tabela de LOD/LOI por tipo de elemento e fase do projeto

### Pessoas e processos

- [ ] Organograma BIM com papéis claramente identificados
- [ ] Matriz RACI ou equivalente por disciplina / atividade
- [ ] Protocolo de reuniões de coordenação definido

### Informação e entregas

- [ ] MIDP com todos os entregáveis, datas e formatos
- [ ] TIDPs por disciplina incluídos como apêndice
- [ ] Formatos de intercâmbio IFC e versão especificados

### Padrões técnicos

- [ ] Convenções de nomenclatura de arquivos documentadas
- [ ] Sistema de coordenadas compartilhado e ponto de origem definidos
- [ ] Templates de modelo referenciados no CDE

### CDE e colaboração

- [ ] Plataforma CDE identificada com URL e administrador
- [ ] Fluxo de status de documentos (WIP → Shared → Published) documentado
- [ ] Política de controle de acesso por papel definida

### Qualidade e tecnologia

- [ ] Processo de QA/QC com critérios de aprovação por tipo de verificação
- [ ] Software por disciplina com versões especificadas
- [ ] Referência ao IDS do projeto (quando aplicável)

### Entrega final

- [ ] Formatos de entrega final ao contratante especificados
- [ ] Requisitos de dados para FM/CMMS documentados
- [ ] Procedimento de as-built definido com responsáveis

---

## Referências

[^1]: United BIM. *BIM Execution Plan (BEP) — Guide for Successful BEP Design and Execution*. Disponível em: <https://www.united-bim.com/bim-execution-plan-bep-guide-for-successful-bep-design-and-execution/>. Acesso em: abr. 2026.

[^2]: Penn State — Computer Integrated Construction Research Program. *BIM Project Execution Planning Guide — Version 3.0*. Disponível em: <https://psu.pb.unizin.org/bimprojectexecutionplanning/>. Licença CC BY-SA 4.0. Acesso em: abr. 2026.

[^3]: Vectorworks. *BIM Execution Planning: A Guide to Your First BEP*. Disponível em: <https://www.vectorworks.net/en-US/newsroom/bim-execution-plans>. Acesso em: abr. 2026.

[^4]: Penn State — CIC Research Program. *BIM Project Execution Planning Procedure Overview*. Disponível em: <https://bim.psu.edu/bim-an-introduction/bim-project-execution-planning-procedure-overview/>. Acesso em: abr. 2026.

[^5]: ISO. *ISO 19650-2:2018 — Organization and digitization of information about buildings and civil engineering works using BIM — Part 2: Delivery phase*. Disponível em: <https://www.iso.org/standard/68080.html>.

[^6]: CDBB — Centre for Digital Built Britain / University of Cambridge. *Pre-appointment and Delivery Team's BIM Execution Plan (BEP) Guidance*. Disponível em: <https://www.cdbb.cam.ac.uk/files/bep_guidance.pdf>. Acesso em: abr. 2026.

[^7]: NIBS — National Institute of Building Sciences. *NBIMS-US v4 — Project BIM Execution Planning (BEP) Standard*. Disponível em: <https://nibs.org/nbims/v4/bep/>. Acesso em: abr. 2026.

[^8]: Strand-co. *How to Write a Powerful BIM Execution Plan (BEP)*. Disponível em: <https://strand-co.com/blogs/write-a-powerful-bim-execution-plan-bep/>. Acesso em: abr. 2026.

[^9]: Global BIM Network. *Delivery Team's BIM Execution Plan (BEP) Template*. Disponível em: <https://globalbim.org/info-collection/delivery-teams-bim-execution-plan-bep-template/>. Acesso em: abr. 2026.

[^10]: NATSPEC. *NATSPEC BIM Execution Plan (BEP) Templates — AS ISO 19650*. Disponível em: <https://bim.natspec.org/documents/natspec-bim-execution-plan-bep-templates>. Acesso em: abr. 2026.

[^11]: Plannerly. *7 Things You Should Consider For Your BEP — 16-point checklist*. Disponível em: <https://plannerly.com/bep-bim-execution-plan-guide/>. Acesso em: abr. 2026.

[^12]: MDPI Applied Sciences. *Developing Standard BIM Execution Plans for Complex Construction Projects* (2024). Disponível em: <https://www.mdpi.com/2076-3417/14/15/6614>. Acesso em: abr. 2026.
