# Análise Arquitetural do ChatTTS
## Autores
- Filippi Reis Menezes - 202300027230
- Jackson Santana Carvalho Júnior - 202300027365
- Gabriel Bastos Pimentel - 202300061590 
- Marcos Vinícius Dantas Aguiar - 201800084345
- Caio Victor Prado Cruz - 202100011234
- Yan Victor Araujo do Nascimento - 202100046006
- Leonardo de Souza Aragão - 202200117002
- Vênisson Cardoso Dos Santos – 201700063182

Contribuição:

Responsáveis pelos modelos DistilBERT, BERT-NER, CodeBERT:
- Filippi Reis Menezes certo 
- Jackson Santana Carvalho Júnior
- Gabriel Bastos Pimentel
- Marcos Vinícius Dantas Aguiar certo 
- Caio Victor Prado Cruz
- Vênisson Cardoso Dos Santos


Responsáveis pelos modelos Flan-T5 Base e RoBERTa Sentiment:
- Yan Victor Araujo do Nascimento
- Leonardo de Souza Aragão

## Introdução
**DistilBERT/BERT-NER/CodeBERT + RoBERTa + FLAN-T5**

Este repositório contém o código, artefatos e documentação utilizados
para realizar **duas análises arquiteturais independentes** do projeto
**ChatTTS** (modelo de text-to-speech open-source)(https://github.com/2noise/ChatTTS).\
A análise foi implementada em **notebooks Python executados no Google
Colab**, utilizando diferentes modelos da Hugging Face (DistilBERT + BERT-NER + CodeBERT,RoBERTa + FLAN-T5) aplicados a arquivos do repositório original.

------------------------------------------------------------------------

## Estrutura do Repositório

    .
    ├── DistilBERT_BERT-NER_CodeBERT/
    │   └── ChatTTSTestes.ipynb     → Pipeline 1
    │
    ├── RoBERTa_FLANT5/
    │   └── script.ipynb            → Pipeline 2
    │
    ├── [nome_dos_integrantes].pdf -> tutorial escrito
    └── README.md  ← este arquivo

------------------------------------------------------------------------

## Objetivo do Projeto

O propósito deste estudo é:

1.  **Extrair informações arquiteturais** do repositório ChatTTS.\
2.  **Aplicar técnicas de NLP** em documentação e
    arquivos-fonte.\
3.  **Comparar a eficácia de diferentes modelos Hugging Face**.\
4.  **Gerar uma classificação arquitetural final**.

Duas pipelines foram desenvolvidas:

### **Pipeline 1: DistilBERT + BERT-NER + CodeBERT**

Localizada em: `./DistilBERT_BERT-NER_CodeBERT/ChatTTSTestes.ipynb`

✔ Classificação textual\
✔ Extração de entidades arquiteturais\
✔ Similaridade semântica entre arquivos/códigos

------------------------------------------------------------------------

### **Pipeline 2: RoBERTa + FLAN-T5**

Localizada em: `./RoBERTa_FLANT5/script.ipynb`

✔ Classificação zero-shot (RoBERTa)\
✔ Geração explicativa e análise contextual (FLAN-T5)\
✔ Refinamento da categorização arquitetural

------------------------------------------------------------------------

## Como Executar

Toda a execução é feita **no Google Colab** utilizando o plano Free(gratuito).

### **1. Abrir o Colab**

Faça upload do notebook desejado:

-   `DistilBERT_BERT-NER-CodeBERT/ChatTTSTestes.ipynb`
-   `RoBERTa_FLANT5/script.ipynb`

Ou abra diretamente pelo Google Drive.

------------------------------------------------------------------------

### **2. Executar o notebook**

Basta clicar no botão "Run all" do colab para que as células que fazem os
passos a seguir sejam executadas:

1.  Instalar dependências\
2.  Baixar arquivos do ChatTTS pelo GitHub API.\
3.  Processar os dados e gerar datasets intermediários.\
4.  Rodar inferência nos modelos.\
5.  Exportar outputs para `results/`.

Os resultados são reproduzíveis desde que o ambiente Colab seja mantido
com as versões indicadas.
------------------------------------------------------------------------
