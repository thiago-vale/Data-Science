# [Calculadora de Alugueis]( https://calculadora-de-alugueis.herokuapp.com/)

<div align="center">
<img src="https://user-images.githubusercontent.com/77752211/132268695-4a4991c0-e540-441b-9178-773051338288.jpg" height="300" width="1000px" />
</div>

## Problema de negocio.

Conheço algumas pessoas que trabalham na zona sul do rio de janeiro e moram um pouco longe de seus trabalhos em sua maioria, vejo que eles estão sempre reclamando de morar longe e a cada dia vejo mais e mais apartamentos sendo alugados proximo do meu trabalho, toda vez que eu paro para pesquisar vejo que a maioria está o mesmo preço do que em outras áreas do Rio de Janeiro, por isso resolvi fazer este projeto não só para ajudar qualquer corretora que ainda não tenha a aplicação como tambem pessoas que se interessem em saber se estão pagando caro ou barato por um apartamento na zona sul do Rio de Janeiro, e assim podendo aumentar o numero de apartamento alugados por ali.

## [Extração dos dados.](https://github.com/thiago-vale/Data-Science/blob/main/calculadora-de-alugueis/Coletando-dados.py)

Todos os daodos foram raspados da internet de anuncios publicos no site: https://www.vivareal.com.br/ onde você pode encontrar apartamentos, casas e imoveis comerciais em todos o Brasil.

## [Tratamento dos dados.](https://github.com/thiago-vale/Data-Science/blob/main/calculadora-de-alugueis/Tratando-os-dados.py)

Os dados foram tratados de forma que ficassem organizados nas colunas apresentadas abaixo, depois foi feita uma Analise Exploratoria para saber se existiam outliers e como trata-los,


## [Analise Exploratoria dos Dados.](https://github.com/thiago-vale/Data-Science/blob/main/calculadora-de-alugueis/AED.ipynb)

Após isso foi feita duas analises exploratorias, uma antes da limpeza dos outliers outra após para indetificar qual seria um impacto na medição no caso de esses não serem removidos,

## [Removendo outliers](https://github.com/thiago-vale/Data-Science/blob/main/calculadora-de-alugueis/Limpando-outliers.py)

Podemos ver no final da Analise Exploratoria dos Dados (atravez da matriz de correlação) que a mudança foi real e os outliers impactavam e muito para o treinamento.

## [Treinamento dos modelos.](https://github.com/thiago-vale/Data-Science/blob/main/calculadora-de-alugueis/Escolhendo%20os%20Modelo.ipynb)

Foram treiandos os segintes modeelos:

[LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

[KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)

[DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)

[CatBoostRegressor](https://catboost.ai/docs/concepts/python-reference_catboostregressor.html)

## [Apresentação dos resultados.](https://github.com/thiago-vale/Data-Science/blob/main/calculadora-de-alugueis/Escolhendo%20os%20Modelo.ipynb)

Como podemos ver o melhor modelo em questão de performance no R2 score foi o CatboostRegressor, logo foi quem apresentou menos residuais.

## Melhorias Futuras

O objtivo para o futuro e extrair mais bairros do Rio de Janeiro e ir adicionando ao treinamento dos modelos de forma automatica, para que se tenha uma ferramenta que possa atender a todos os publicos.

