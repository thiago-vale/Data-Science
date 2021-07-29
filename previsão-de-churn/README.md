# Model Churn Predict

Hoje eu trabalho como líder de equipe em uma grande rede de academias, um dos maiores problemas que encontro é ter que diminuir a minha taxa de Churn, muitas vezes temos que tentar fazer com que os cliente não cancelem, porém na maioria desses casos os clientes já tomarama a decisão, com base nisso pensei em um modeli de machine learning que pudesse fazer essa previsão.

Por ter se tratado de um projeto Open não pude usar os dados da empresa onde eu trabalho, então peguei os dados no Kaggle que tinha varaveis muito parecdas com as que eu enfrento hoje.

O data set apresenta as seguintes variaveis.
Variaveis
Churn: Yes or Not
Contract: Month-to-month , One year, Two year
Dependents: Yes or Not
DeviceProtection: Yes or Not
InternetService: Fiber Optic, DSL, No
MonthlyCharges= How much the customer spent per month
MultipleLines: Yes or Not
OnlineBackup: Yes or Not
OnlineSecurity: Yes or Not
PaperlessBilling: Yes or Not
Partner: Yes or Not
PaymentMethod: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)
PhoneService: Yes or Not
SeniorCitizen: 0 or 1
StreamingMovies: Yes or Not
StreamingTV: Yes or Not
TechSupport: Yes or Not
TotalCharges= how much the customer spent in total
customerID: ID
gender: The customer is a male or a female
tenure = Months The customer has stayed with the company

Após isso fui entender os dados, notei que existiam 11 dados faltantes na coluna TotalCharges, entendi que o TotalCharges era igual a multiplicação de duas variaveis, era exatamente o valor do MonthlyCharges vezes o tenure, após tratar os dados nulos.

Explorei os dados para entender quais eram as variaveis que influienciavam se o cliente seria ou não Churn
Junto disso tratei os dados para que eu pudesse treinar os modelos de classificação.

Treinei os modelos
LogisticRegression
ExtraTreesClassifier
RandomForestClassifier
XGBClassifier
CatBoostClassifier

Calibrei os modelos

Avaliei todos os modelos pelo classification report e depois pelo ROC AUC

Depois rodei o metodo de hiperparametros e treinei os modelos com os melhores parametros.

Avalei novamente e percebi que o metodo CatBoostClassifier foi o modelo que se saiu melhor por ter uma precisão de 81%

Com esse modelo eu consegiria uma lista com os clientes que deixariam de usar os serviços da empresa com 80% de precisão assim podendo entender qual e o problema desses clientes e como podemos fazer para que ele continue com os serviços oferecidos.
