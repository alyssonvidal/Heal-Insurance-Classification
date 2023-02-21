# Heal Insurance Cross Sell

<center><img src="/images/banner.jpg" alt="logo" width="800" height="600"/></center>

# Descrição do Problema

Cross-Sell, ou venda cruzada, se refere a à venda de produtos ou serviços relacionados e complementares com base no interesse do cliente ou na compra de um produto. Neste estudo de caso a empresa é lider de mercado no que diz respeito a seguro de vida, neste projeto será analisado a viabilidade de ampliar o serviço para venda de seguros veiculares.

A Insurance All é uma empresa tradicional de seguros de saúde, através de uma pesquisa de mercado com os atuais clientes da empresa, ela obteve retorno de 304 mil clientes sobre o interesse em adquirir um seguro de veículo. Entretanto a empresa conta com ainda mais 76 mil clientes, que ou não responderam a pesquisa ou não foram entrevistados. 

Como são muitos clientes na base de dados e a capacidade de atendimento do call center é limitada, o CEO da empresa requisitou a sua equipe de cientista de dados para verificar se através dessa pesuisa de mercado é possivel criar um modelo de previsão de clientes possivelmente interessados em addquirir um seguro veicular, o que economizaria bastante o custo de marketing e atendimento do call center.


O dataset contém informações referentes aos clientes de uma seguradora localizada no Pasquistão. A base de dados original pode ser acessada diretamente pelo [kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction)<br><br>

# Objetivo

* Desenvolver uma solução dentre o escopo de atuação do cientista de dados para o problema de classificação de clientes (Interessados/ Não Interessados no seguro veícular).
* Identificar quais são as principais variavéis que determinam se o cliente possuí ou não interesse em adquirir o serviço de seguro veícular
* Apresentar um possivel plano de ação com base nos resultados obtidos.<br><br>

# Estágios de Desenvolvimento
[**Pré Processamento dos dados**](https://github.com/alyssonvidal/Bank-Marketing-Cluster/blob/main/notebooks/part01_preprocessing.ipynb)<br>
Carregamento, Dados Faltantes (KNN Imputer), Dados Duplicados, Engenharia de Dados...

[**Analise Exploratória dos dados**](https://github.com/alyssonvidal/Bank-Marketing-Cluster/blob/main/notebooks/part02_eda.ipynb)<br>
Analise Univariada, Analise Bivariada, Analise Multivariada.

[**Preparação dos dados**](https://github.com/alyssonvidal/Bank-Marketing-Cluster/blob/main/notebooks/part03_model.ipynb)<br>
Detecção de Outlier (Isolation Forest), Normalização, Padronização, Redução de Dimensionalidade (PCA, UMAP, t-SNE).

[**Modelo de Machine Learning**](https://github.com/alyssonvidal/Bank-Marketing-Cluster/blob/main/notebooks/part03_model.ipynb)<br>
 LGBM, XGB, RF, RNN<br><br>


<center><img src="/images/deploy_structure.png" alt="deploy_structure" width="1190" height="794"/></center>
<sub>**Note:** O kaggle possuí tanto a base de dados de treino quanto de teste, no entanto para fins ditáticos e para dificultar o projeto os dados de treino/testes foram retirados de fontes diferentes.</sub><br><br>

# Relatórios
[**Resumo Técnico**](https://github.com/alyssonvidal/Bank-Marketing-Cluster/blob/main/reports/resultados.md)<br>

# Ferramentas
Linguagens: Python<br>
IDE: Visual Studio Code, Jupyter Notebook<br>
Bibliotecas: Pandas, Matplotlib, Seaborn, Plotly, Sklearn, scipy, yellowbricks<br>
Metodologia: CRISP-DM<br><br>

***


# Resultados

## Plano de Ação

