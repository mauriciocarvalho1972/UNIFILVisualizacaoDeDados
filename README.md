# Dashboard Interativo - Wine Quality (UCI)

## Identificação do Autor

- **Curso:** Bacharelado em Ciência de Dados e Inteligência Artificial  
- **Disciplina:** Visualização de Dados  
- **Professor:** Mario H. A. C. Adaniya  
- **Aluno:** Maurício de Carvalho  
- **Data:** 30/03/2026  


## 1. Introdução e Contextualização do Problema

A crescente disponibilidade de dados em diferentes áreas torna essencial o uso de técnicas de visualização para transformar informações brutas em conhecimento útil. No contexto da ciência de dados, a análise exploratória (EDA - Exploratory Data Analysis) é uma etapa fundamental para compreender padrões, identificar relações entre variáveis e apoiar a tomada de decisão baseada em dados.

Este projeto tem como objetivo desenvolver um dashboard interativo que permita explorar visualmente um conjunto de dados real, facilitando a identificação de padrões e insights relevantes.

O dataset escolhido foi o **Wine Quality**, disponível no UCI Machine Learning Repository, que contém dados físico-químicos de vinhos verdes portugueses, juntamente com uma variável de qualidade atribuída sensorialmente.


## 2. Justificativa da Escolha do Dataset

O dataset Wine Quality foi selecionado por apresentar características ideais para análise exploratória e visualização de dados:

- Possui **múltiplas variáveis numéricas contínuas**, adequadas para diferentes tipos de gráficos;
- Permite investigar a relação entre **atributos físico-químicos e qualidade do vinho**;
- Contém dados de dois grupos distintos (**vinhos tintos e brancos**), possibilitando análises comparativas;
- É amplamente utilizado em estudos acadêmicos, garantindo confiabilidade e relevância.

Essas características tornam o dataset apropriado para explorar técnicas de visualização e interatividade.


## 3. Análise Exploratória e Preparação dos Dados

A análise exploratória foi conduzida com o objetivo de compreender a estrutura do dataset e preparar os dados para visualização eficiente.

### 3.1 Preparação dos dados

As seguintes etapas foram realizadas:

- Importação dos datasets de vinhos tintos e brancos;
- Inclusão de uma nova variável categórica (`type`) para identificação do tipo de vinho;
- União dos datasets em um único DataFrame;
- Verificação de consistência dos dados (tipos, valores ausentes e distribuição);
- Seleção de variáveis numéricas para análise estatística e visual.

### 3.2 Análise inicial

Durante a análise exploratória, foram observados:

- Distribuição da variável **qualidade**, concentrada em valores intermediários;
- Diferenças entre vinhos tintos e brancos em relação a variáveis como álcool e acidez;
- Presença de relações lineares e não lineares entre variáveis;
- Possíveis correlações relevantes entre atributos químicos e qualidade.


## 4. Metodologia e Ferramentas Utilizadas

O projeto foi desenvolvido utilizando a linguagem Python e as seguintes ferramentas:

- **Pandas:** manipulação e tratamento de dados;
- **Plotly:** criação de gráficos interativos e visualmente ricos;
- **Streamlit:** desenvolvimento do dashboard interativo em ambiente web.

### 4.1 Fluxo do projeto

1. Coleta do dataset no UCI Repository;
2. Tratamento e preparação dos dados;
3. Construção das visualizações;
4. Implementação de interatividade;
5. Análise dos resultados obtidos.


## 5. Adequação das Visualizações

Foram utilizados diferentes tipos de gráficos, escolhidos de acordo com o tipo de dado e objetivo da análise:

### 5.1 Histograma
Utilizado para analisar a distribuição da variável **qualidade**, permitindo identificar concentração de valores e frequência.

### 5.2 Boxplot
Aplicado para comparar a distribuição do **teor alcoólico** entre vinhos tintos e brancos, destacando mediana, variabilidade e outliers.

### 5.3 Gráfico de Dispersão
Utilizado para investigar relações entre duas variáveis numéricas, permitindo identificar tendências, padrões e possíveis correlações.

### 5.4 Mapa de Calor (Heatmap)
Aplicado para visualizar a matriz de correlação entre variáveis, facilitando a identificação de relações positivas e negativas.

A escolha dessas visualizações segue boas práticas de visualização de dados, garantindo clareza e interpretabilidade.


## 6. Interatividade e Usabilidade do Dashboard

O dashboard foi desenvolvido com foco na experiência do usuário, permitindo exploração dinâmica dos dados.

### Funcionalidades interativas:

- Filtro por **tipo de vinho** (tinto ou branco);
- Filtro por **faixa de qualidade**;
- Filtro por **faixa de teor alcoólico**;
- Seleção dinâmica das variáveis nos eixos X e Y;
- Alteração da variável de coloração nos gráficos;
- Navegação por abas temáticas (distribuição, relações e correlação).

Esses recursos permitem que o usuário personalize a análise e explore diferentes perspectivas do dataset.


## 7. Insights Obtidos

A análise exploratória permitiu identificar diversos padrões relevantes:

- A qualidade dos vinhos concentra-se em níveis intermediários;
- O teor alcoólico apresenta relação positiva com a qualidade;
- Algumas variáveis, como acidez volátil, apresentam relação negativa com a qualidade;
- Existem diferenças claras entre vinhos tintos e brancos em relação a seus atributos químicos;
- O uso de filtros altera significativamente a percepção dos padrões, reforçando a importância da interatividade.


## 8. Conclusão

O projeto demonstrou a importância da visualização de dados como ferramenta fundamental na análise exploratória. A utilização de um dashboard interativo permitiu uma compreensão mais aprofundada do dataset, facilitando a identificação de padrões e relações entre variáveis.

Além disso, a integração entre ferramentas como Pandas, Plotly e Streamlit mostrou-se eficiente para o desenvolvimento de aplicações analíticas modernas.

O trabalho atende aos objetivos propostos, destacando o papel da visualização na tomada de decisão baseada em dados.


## 9. Estrutura do Projeto

VisualizacaoDados/
|
|- dshvinhos.py
|
|- README.md


## 10. Como Executar

Instale as dependências:

```bash
pip install streamlit pandas plotly

Execute o projeto:

```bash
pip install streamlit pandas plotly
