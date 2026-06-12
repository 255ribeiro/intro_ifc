# Atividade de Avaliação 03: Edital

-----

<div style= "align: top;">

<span style="float: left;">
<img src="../figs_gerais/Universidade_SENAI_CIMATEC.png" width="150">

</span>
<span style="float: right;"><br>
UNIVERSIDADE SENAI CIMATEC <br>
CURSO DE ARQUITETURA E URBANISMO / ENGENHARIA CIVIL

</span>

</div>

<br><br><br><br><br><br>

<div>
    <span style="float: left;">Docente: Prof: Dr. Fernando Ferraz Ribeiro</span>
    <span style="float: right;">Semestre: 2026.1</span>
</div>

<br>

---

<h4 style="background:lightblue">

Objetivo da avaliação

</h4>

1. Consolidar a coordenação BIM por meio da integração dos modelos IFC das disciplinas;
2. Aplicar validação de requisitos de informação com IDS, com base no mini BEP da etapa anterior;
3. Extrair quantitativos de paredes e revestimentos no BonsaiBIM, assegurando consistência dos dados para planejamento e controle.

<h4 style="background:lightblue">
Orientações gerais

</h4>

A atividade deve ser desenvolvida nas mesmas equipes das avaliações anteriores.

Esta avaliação é composta por 3 etapas obrigatórias, utilizando o BonsaiBIM e o complemento MergeIfcProjectsPlus (fornecido pelo professor).

As entregas devem demonstrar: organização de arquivos, coerência entre modelagem e regras IDS, e rastreabilidade dos resultados de validação e quantitativos.

<h4 style="background:lightblue">
Etapas da atividade
</h4>

#### Etapa 1 - Modelo IFC completo com integração dos arquivos

1. Utilizar o BonsaiBIM e o Addon MergeIfcProjectsPlus para compor um modelo IFC completo do projeto, a partir dos IFCs disciplinares.
2. Garantir que os modelos utilizados estejam atualizados com as definições da AV2.
3. Verificar consistência de posicionamento, níveis e correspondência geométrica entre disciplinas antes da geração do IFC integrado.

#### Etapa 2 - Tradução do Mini BEP para IDS e verificação do modelo

1. Traduzir os requisitos de informação definidos no mini BEP (AV2) para um ou mais arquivos IDS.
2. Executar validação do modelo IFC integrado no BonsaiBIM com base nesses IDS.
3. A validação deve verificar, no mínimo:
   1. se todas as paredes possuem espessura definida;
   2. se os revestimentos possuem a espessura correta;
   3. se os revestimentos foram exportados como IfcCovering com tipo Cladding;
   4. se a propriedade IsExternal está definida corretamente para os elementos aplicáveis.

#### Etapa 3 - Extração de quantitativos

1. Extrair quantitativos de paredes e revestimentos utilizando o BonsaiBIM.
2. Os quantitativos devem ser obtidos a partir do modelo IFC integrado validado.
3. A equipe deve apresentar, de forma clara, os critérios de medição utilizados (ex.: área, volume, comprimento, contagem), conforme a informação disponível no modelo.

<h4 style="background:lightblue">
Itens da entrega

</h4>

1. Pasta com os arquivos IFC disciplinares atualizados e o arquivo IFC integrado/federado gerado com MergeIfcProjectsPlus.
2. Arquivo(s) IDS produzido(s) pela equipe a partir do mini BEP da AV2.
3. Evidências da validação IDS no BonsaiBIM (capturas de tela e/ou relatório exportado), incluindo os resultados das quatro verificações obrigatórias.
4. Relatório de quantitativos de paredes e revestimentos extraído no BonsaiBIM (planilha, tabela exportada ou relatório equivalente).
5. Pequeno memorial descritivo (PDF ou .docx) explicando:
   1. fluxo adotado para integração dos IFCs;
   2. regras IDS implementadas;
   3. síntese dos resultados de validação;
   4. síntese dos quantitativos gerados.

Os trabalhos devem ser enviados em arquivo compactado (.zip, .rar, .7z, .tar.gz) pelo Canvas da disciplina em atividade adequada.

<h4 style="background:lightblue"> Critérios de avaliação</h4>

1. Correção e completude da integração IFC com o MergeIfcProjectsPlus;
2. Qualidade da tradução dos requisitos mini BEP para IDS;
3. Consistência dos resultados de validação (paredes, revestimentos, classificação e IsExternal);
4. Coerência técnica dos quantitativos extraídos no BonsaiBIM;
5. Organização e clareza da documentação entregue.

<h4 style="background:lightblue"> Data de entrega</h4>

   A definir pelo docente no AVA da disciplina
