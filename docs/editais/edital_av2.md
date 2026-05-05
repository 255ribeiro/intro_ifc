# Atividade de Avaliação 02: Edital

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

1. Consolidar a organização da informação BIM com base em tópicos essenciais do BEP;
2. Padronizar nomenclatura de arquivos e estrutura de pastas para colaboração;
3. Aplicar fluxo de comunicação técnica por meio de issues BCF;
4. Atualizar os modelos previamente desenvolvidos, incorporando requisitos de informação e classificação IFC.

<h4 style="background:lightblue">
Orientações gerais

</h4>

A atividade consiste na alteração dos arquivos BIM criados previamente na disciplina, incluindo tópicos selecionados do material de BEP apresentado em [docs/bep/bep-bim-material.md](../bep/bep-bim-material.md).

O projeto deve ser desenvolvido nas mesmas equipes da AV1 (2, 3 ou 4 discentes).

Todas as entregas devem evidenciar organização, rastreabilidade de revisões e coerência entre modelos, arquivos de coordenação e documentação textual.

<h4 style="background:lightblue">
Diretrizes da atividade (BEP aplicado)
</h4>

#### A equipe deve produzir um documento de texto (PDF ou .docx) Abaixo seguem ás seções obrigatórias do documento e os tópicos que cada seção deve conter:

   1. Capa
   2. Equipe com o nome dos membros e-mails da instituição
   3. Ambiente de trabalho contendo:
      1. Convenção de nomenclatura dos arquivos adotada pela equipe, conforme orientação do BEP;
      2. Tabela com padrão de nomenclatura utilizado (campos e siglas);
      3. Exemplo de nomes de arquivos nativos, IFC, BCF e arquivo federado.
      4. A equipe deve apresentar a organização de pastas do projeto, incluindo obrigatoriamente:
         1. pasta de arquivos nativos por disciplina;
         2. pasta de IFCs exportados;
         3. pasta de arquivos BCF;
         4. pasta do projeto de coordenação (BIMcollab/Navisworks/Bonsai BIM ou equivalente);
         5. pasta para arquivos auxiliares (configurações de exortação, arquivos de parâmetros compartilhados, ...)
   4. Tecnologia:
      1. A equipe deve listar os softwares e versões utilizados no desenvolvimento e coordenação.
      2. A equipe deve declarar explicitamente:
            - versão de exportação IFC adotada: IFC 4;
            - versão de BCF utilizada no fluxo de issues (recomendado: BCF 2.1).
   5. LOD/LOI:
      1. A forma de modelagem das paredes (cebola) descrevendo as camadas com espessura definida.
      2. nomenclatura dos materiais de paredes e revestimentos (internas, externas e áreas molhadas)
      3. Os revestimentos devem ser exortados como IfcCovering to tipo Cladding
      4. Os tipos devem ter nomenclatura definida para cada caso (internas, externas e áreas molhadas)
      5. Os revestimentos das áreas molhadas devem ser modelados até a altura do forro.
   6. Entrega: o Arquivo IFC deve ser exportado contendo os dados listados abaixo.
      1. As paredes, revestimento e portas deve ser exportados contendo:
         - Pset: Common para cada classe
         - Qto: Base para cada Classe
         - Atrubuto IfcIsExternal corretamente definido.
#### Após a definição dos elementos do BEP, algumas atividades devem ser abertas por issue BCF e executadas nos arquivos disciplinares:
   1. marcação de paredes como internas e externas;
   2. marcação de portas como internas e externas;
   3. modelagem de revestimentos de parede em lógica de "parede cebola";
   4. classificação dos revestimentos de paredes como IfcCovering tipo Cladding.
   5. Os revestimentos de paredes dos sanitários devem ir apenas até a altura do forro.
   6. Caso não tenham modelado, os IfcSpaces de cada ambiente devem ser requeridos por BCF e modelados.
   7. Elementos fundamentais (via orientação) do edital 1 que não foram resolvidos, solicitados via BCF e resolvidos.
   8. Cada issue BCF deve conter título, descrição objetiva, responsável, prazo e status de resolução.

#### Obs. Verifique a seção sobre BEP do material de estudo da disciplina

<h4 style="background:lightblue">
Itens da entrega

</h4>

1. Documento textual da equipe contendo os tópicos BEP solicitados:
   1. convenção de nomenclatura;
   2. organização de pastas;
   3. lista de softwares e versões;
   4. versão IFC e versão BCF utilizadas.
2. Modelos atualizados da AV1 em formato nativo e em IFC 4.
3. Arquivos BCF com as solicitações e resoluções das atividades pedidas.
4. Arquivo de coordenação/federado (formato nativo da ferramenta de gestão utilizada).
5. Capturas de tela (ou relatório) comprovando:
   1. classificação de paredes/portas internas e externas;
   2. presença dos revestimentos modelados;
   3. classificação dos revestimentos como IfcCladding.

Os trabalhos devem ser enviados em arquivo compactado (.zip, .rar, .7z, .tar.gz) pelo Canvas da disciplina em atividade adequada.

<h4 style="background:lightblue"> Critérios de avaliação</h4>

1. Aplicação correta das convenções de nomenclatura e organização de pastas;
2. Coerência entre documento BEP simplificado e arquivos entregues;
3. Uso adequado de BCF para solicitação e rastreabilidade das alterações;
4. Qualidade da atualização dos modelos (classificações e revestimentos);
5. Consistência da exportação e interoperabilidade (IFC 4 e BCF informado).

<h4 style="background:lightblue"> Data de entrega</h4>

   24/05/2026 pelo AVA da disciplina
