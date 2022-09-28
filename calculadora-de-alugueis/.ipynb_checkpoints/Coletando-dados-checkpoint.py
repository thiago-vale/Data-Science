# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:02:18 2021

@author: Thiago
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd
from tqdm import tqdm
from datetime import datetime

#Sempre que o chrome drvier for aberto o mesmo irá atualizar atomaticamente.
driver = webdriver.Chrome(ChromeDriverManager().install())

#Criação de um dicionario com as Urls de cada bairro
urls = {'Botafogo': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/botafogo/apartamento_residencial/',
        'Catete': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/catete/apartamento_residencial/',
        'Copacabana': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/copacabana/apartamento_residencial/',
        'Cosme Velho': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/cosme-velho/apartamento_residencial/',
        'Flamengo': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/flamengo/apartamento_residencial/',
        'Gávea': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/gavea/apartamento_residencial/',
        'Glória': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/gloria/apartamento_residencial/',
        'Humaitá': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/humaita/apartamento_residencial/',
        'Ipanema': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/ipanema/apartamento_residencial/',
        'Jardim Botanico': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/jardim-botanico/apartamento_residencial/',
        'Lagoa': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/lagoa/apartamento_residencial/',
        'Laranjeiras': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/laranjeiras/apartamento_residencial/',
        'Leblon': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/leblon/apartamento_residencial/',
        'Leme': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/leme/apartamento_residencial/',
        'São Conrado': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/sao-conrado/apartamento_residencial/',
        'Urca': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/urca/apartamento_residencial/'
        }

erro = []
resultado = []

#vai executar um loop onde o mesmo irá procurar para cada bauirro sua URL
for bairro, url in urls.items():
    current_url = url
    driver.get(url)
    sleep(2)
    actions = ActionChains(driver)

    try:
        driver.find_element_by_class_name("cookie-notifier__cta").click()
    except:
            print("sem cookies!")
            
    #Vai executar um lopp na range de paginas definidas 
    for i in tqdm(range(30), desc=bairro):        
        sleep(5)
        main_div = driver.find_element_by_class_name("results-main__panel")
        properties = main_div.find_elements_by_class_name("js-property-card")
        paginator = driver.find_element_by_class_name("js-results-pagination")
        next_page = paginator.find_element_by_xpath("//a[@title='Próxima página']")
        
        #Irá coletar as informações pedidas de acordo com cada quadro
        for i,apartment in enumerate(properties):
            url = apartment.find_element_by_class_name("js-card-title").get_attribute("href")
            apto_id = url.split("id-")[-1][:-1]
            header = apartment.find_element_by_class_name("property-card__title").text
            address = apartment.find_element_by_class_name("property-card__address").text
            area = apartment.find_element_by_class_name("js-property-card-detail-area").text
            rooms = apartment.find_element_by_class_name("js-property-detail-rooms").text
            bathrooms = apartment.find_element_by_class_name("js-property-detail-bathroom").text
            garages = apartment.find_element_by_class_name("js-property-detail-garages").text
            try:
                amenities = apartment.find_element_by_class_name("property-card__amenities").text
            except:
                amenities = None
                erro.append(url)
            price = apartment.find_element_by_class_name("js-property-card-prices").text
            try:
                condo = apartment.find_element_by_class_name("js-condo-price").text
            except:
                condo = None
                
                erro.append(url)
            crawler = bairro
            crawled_at = datetime.now().strftime("%Y-%m-%d %H:%M")
            resultado.append({"id": apto_id,
                            "url": url,
                            "header": header,
                            "address": address,
                            "area": area,
                            "rooms": rooms,
                            "bathrooms": bathrooms,
                            "garages": garages,
                            "amenities": amenities,
                            "price": price,
                            "condo": condo,
                            "crawler": crawler,
                            "crawled_at": crawled_at})
        try:
            next_page.click()
        except:
            print("Next page not clickable") #Quando atingir o Next page not clickable vai para proximo bairro
            break
pd.DataFrame(resultado).to_csv("C:/Users/Thiago/Desktop/DS Python/Potifolio/Calculadora de imoveis/Datasets/todos_os_resultados.csv", index=False)
driver.close()

