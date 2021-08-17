# Modelo para previsão de evasores de uma empresa de telecom
![GitHub top language](https://img.shields.io/github/languages/top/thiago-vale/Data-Science)

![Telefonia](https://user-images.githubusercontent.com/77752211/129768384-482d6e30-c0a5-4d45-b4a1-584e8243d3eb.jpg)

## Problema de Negocio

No ultmo mês essa empresa de telecomunicações perdeu clientes no seu ultimo mês
No metodo atual o mesmos não estão conseguindo reter os clientes

## Bibliotecas Utilizadas no Modelo

![Bibliotecas utilizadas](https://user-images.githubusercontent.com/77752211/129759007-b944190a-2331-432b-b991-79a0bef71b62.png)

# Extração dos dados

Os dados do Projeto podem ser encontrados no seguinte repositorio: https://www.kaggle.com/blastchar/telco-customer-churn

O mesmos estão presente neste repositorio e podem ser importados pelo Link https://raw.githubusercontent.com/thiago-vale/Data-Science/main/previs%C3%A3o-de-churn/data/Churn.csv

## Tratamento e Limpeza dos dados

![DF-info](https://user-images.githubusercontent.com/77752211/129761563-7b5ea677-5224-41de-b7f8-96b8a39d753f.png)

Primeiro verifiquei se todos os dados estão em seus tipos corretos e como estão distribuidos, percebi que os dados de Pagamentos totais estavam como objeto e não como numerico.

![Conversão-TotalCharges](https://user-images.githubusercontent.com/77752211/129762109-a72ec191-55ee-4abb-a39b-895554e4bf56.png)

Tranformei os dados em numericos e Procurei se haviam dados nulos no Dataset
encontrei 11 dados nulos no propria coluna em nada nas outras

![Tratando-nulos](https://user-images.githubusercontent.com/77752211/129762843-54335fac-caea-44ac-9213-a9ea1a58abc4.png)

![Tratando-nulos-alnternativa](https://user-images.githubusercontent.com/77752211/129763599-be13100b-1eb3-43c5-8a2c-bd1048c29d35.png)

Busquei tratar os dados de forma que não interferiessem nas demais colunas, testei duas formas

![Antes de tratado](https://user-images.githubusercontent.com/77752211/129763459-1e24a5cc-a83a-4f0c-82ec-bcc0094c90da.png)
![Depois de tratado](https://user-images.githubusercontent.com/77752211/129763488-99f75f99-88df-441c-9cbd-4749067a919d.png)
![Depois de tratado alternativa](https://user-images.githubusercontent.com/77752211/129764194-48685ff5-d16b-4a17-8e63-7df5f9e15bae.png)

No caso desse data set nenhuma das duas formas de tratar esses dados apresentaram diferença significativa, porém sabemos que na realidade um cliente pode optar por mudar de plano no meio do caminho ou até mesmo por adicionar algum serviço, a empresa pode oferecer alguma promoção e por isso nesse caso em que os clientes que apresentaram dados nulos em Total Charges não tinham nem um mês completo ainda o primeiro metodo é o mais confiavel.

## Analise Exploratoria dos dados

## Preparação dos dados


## Modelagem dos dados


## Validação Cruzada

## Otimização do modelo

## Medição

## Pontos de Melhoria

## Conclusão
