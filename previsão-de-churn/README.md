# Modelo para previsão de evasores de uma empresa de telecom

<div align="center">
<img src="https://user-images.githubusercontent.com/77752211/129768384-482d6e30-c0a5-4d45-b4a1-584e8243d3eb.jpg" height="300" width="1000px" />
</div>

##
## Problema de Negocio

No ultmo mês essa empresa de telecomunicações perdeu clientes no seu ultimo mês
No metodo atual o mesmos não estão conseguindo reter os clientes

##
## Bibliotecas Utilizadas no Modelo

![Bibliotecas utilizadas](https://user-images.githubusercontent.com/77752211/129759007-b944190a-2331-432b-b991-79a0bef71b62.png)

##
# Extração dos dados

Os dados do Projeto podem ser encontrados no seguinte repositorio: https://www.kaggle.com/blastchar/telco-customer-churn

O mesmos estão presente neste repositorio e podem ser importados pelo Link https://raw.githubusercontent.com/thiago-vale/Data-Science/main/previs%C3%A3o-de-churn/data/Churn.csv

##
## Tratamento e Limpeza dos dados


![DF-info](https://user-images.githubusercontent.com/77752211/129761563-7b5ea677-5224-41de-b7f8-96b8a39d753f.png)

Primeiro verifiquei se todos os dados estão em seus tipos corretos e como estão distribuidos, percebi que os dados de Pagamentos totais estavam como objeto e não como numerico.

![Conversão-TotalCharges](https://user-images.githubusercontent.com/77752211/129762109-a72ec191-55ee-4abb-a39b-895554e4bf56.png)

Tranformei os dados em numericos e Procurei se haviam dados nulos no Dataset
encontrei 11 dados nulos no propria coluna em nada nas outras

![Tratando-nulos](https://user-images.githubusercontent.com/77752211/129762843-54335fac-caea-44ac-9213-a9ea1a58abc4.png)

Busquei tratar os dados de forma que não interferiessem nas demais colunas.

![Antes de tratado](https://user-images.githubusercontent.com/77752211/129763459-1e24a5cc-a83a-4f0c-82ec-bcc0094c90da.png)
![Depois de tratado](https://user-images.githubusercontent.com/77752211/129763488-99f75f99-88df-441c-9cbd-4749067a919d.png)

No caso desse data set nenhuma das duas formas de tratar esses dados apresentaram diferença significativa, porém sabemos que na realidade um cliente pode optar por mudar de plano no meio do caminho ou até mesmo por adicionar algum serviço, a empresa pode oferecer alguma promoção e por isso nesse caso em que os clientes que apresentaram dados nulos em Total Charges não tinham nem um mês completo ainda o primeiro metodo é o mais confiavel.

##
## Analise Exploratoria dos dados
Após Limpar os dados Fui analisa-los.

![%](https://user-images.githubusercontent.com/77752211/129940425-ffbd17cf-8fae-470d-a382-81e6585d687b.jpg)

notei que a empresa 26% de Evasores apenas esse mês, o que e um numero bem expressivo para qualquer negocio.

![Describe](https://user-images.githubusercontent.com/77752211/129940654-d0cd6168-3c8a-4327-add0-cea4a7c87fff.png)

Busquei entender um pouco mais os dados numericos pude perceber que esse mês o Ticket medio dos clientes foi de 64.76.
E que a media que os cliente permanecem como utilizando os serviços da empresa é de 32 meses.

![Churn-tenure](https://user-images.githubusercontent.com/77752211/129959003-ac775372-e179-4c2e-814f-9fe552df4b68.png)
![TenureBox](https://user-images.githubusercontent.com/77752211/129959528-4d4a9e64-3353-4137-8afb-0778cf272848.jpg)

CLientes com pouco tempo de uso dos serviços tem maior propenção a serem evasores.


![Churn-M](https://user-images.githubusercontent.com/77752211/129959031-a43ffc0c-281c-4d93-8a0e-ad1c0110ee38.png)
![M-BOX](https://user-images.githubusercontent.com/77752211/129959598-784c87ef-710c-4e5c-aa79-1db76dacec37.png)

Clientes evasores tem um gasto maior mensalmente.

![Churn-T](https://user-images.githubusercontent.com/77752211/129959054-f6bd486d-111c-4c44-8a17-473e7764229b.png)
![Total-Box](https://user-images.githubusercontent.com/77752211/129959651-1d5917ac-8087-409b-a255-77227670848f.png)

Alguns clientes que foram evasores tiveram um gasto acima da media, porém o gasto do total dos clientes que permaneceram e maior.


![Internet](https://user-images.githubusercontent.com/77752211/129959147-cb8e7a51-d171-41ca-a979-59aeb5e7ec7f.jpg)

Clientes que usam internet e fibraotica tem maior tendencia a cancelar, enquanto os que não utilizam nenhuma internet tem menor propensão a evadirem.


![Contract](https://user-images.githubusercontent.com/77752211/129959171-826ac1e1-318a-469e-a578-0398e2e15e58.jpg)

Clientes com contrato mensal tem maiors chances de serem evasores, talvez por não terem alguma multa ou coisa do tipo.

![PaymentMethod](https://user-images.githubusercontent.com/77752211/129959205-8a373f33-304b-4d35-96b5-69ff62ccff7f.jpg)

Clientes que pagam com Eletronic Check tem maiores propensão ao cancelamento se comparados aos outros.


![Senior](https://user-images.githubusercontent.com/77752211/129959374-178547fa-88dd-4a6e-8de1-4ab4d1983b8f.png)

Apesar de serem minoria clientes idosos tem maior probabilidade de cancelar se comparados com a maioria.


![Genero](https://user-images.githubusercontent.com/77752211/129959350-c1a4eb5a-c827-4167-8300-ceb701246f3e.png)

O genero dos clientes não influencia para o cancelamento.

Aqui já podemos levantar algumas hipoteses sobre o motivo dos cancelamentos

Clientes que não tem fidelidade e consomem mais produtos como internet de fibraotica ou outro serviço extra pagam um valor maior do que os demais para não ter a multa o que torna mais porém por algum motivo os leva a evadir e não fazerem um contrato com fidelidade.

Algumas Hipoteses

* Valor dos planos mensais muito alto.

* Valor dos pacotes adicionais.

* Quaidade dos serviços prestados.

* Problemas tecnicos recorrentes.

* Algum tipo de serviço com problema.

* Algum problema com a forma de pagamento.


##
## Preparação dos dados

O primeiro ponto fazer os dados que diziam não tenho determinado tipo de serviço virarem apenas não, Logo Após foi utilizada a biblioteca OrdinalEnconder para tranformar essas bibliotecas em dados binarios, onde 1 é sim e 0 é não.

Depois usei a função get.dummies para tranformar os dados cateoricos que restaram em colunas contando apenas 1 para sim e 0 para não.

Após isso removi a coluna de ID do cliente para testar o modelo sem os dados do cliente, para ser treinado as cegas, depois separei os dados em X e Y
e separei os dados na proporção 80/20 sendo 80% para treino e 20% para teste.

##
## Modelagem dos dados

No treinamento dos modelos utilizei as seguintes bibliotecas, todos tem um link para a documentação de suas bibliotecas.

[LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

[ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html)

[RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

[XGBClassifier](https://xgboost.readthedocs.io/en/latest/index.html#)

[CatBoostClassifier](https://catboost.ai/docs/concepts/python-reference_catboostclassifier.html)


##
## Validação Cruzada


##
## Otimização do modelo


##
## Medição


##
## Pontos de Melhoria


##
## Conclusão

