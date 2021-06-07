# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:09:24 2021

@author: Thiago
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd
from tqdm import tqdm
from datetime import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())

urls = {'Cachambi' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-norte/cachambi/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwpKCDBhBPEiwAFgBzjw9Trgz0nu_wvfeakkc63bfE4D5dv-TA7LZBzujXffgYODKSeO7PLxoCGL8QAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Rio Comprido' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-central/rio-comprido/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwpKCDBhBPEiwAFgBzjzK6xU3JDciXh0noddkjMb9M6YT_barUlRHa61LuogPZzcKTcbLxHxoCc_4QAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Meier' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-norte/meier/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwpKCDBhBPEiwAFgBzjzK6xU3JDciXh0noddkjMb9M6YT_barUlRHa61LuogPZzcKTcbLxHxoCc_4QAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Tijuca' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-norte/tijuca/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=Cj0KCQjwutaCBhDfARIsAJHWnHuK-ziAczwFpEYNle6FQCvmPXCb8YUrP17V1AeA7bQclYdsKVuveTsaApGYEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Copacabana' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/copacabana/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwx6WDBhBQEiwA_dP8rfJPBiaI5zVAeBxLfzKXSYc2SGbIV-50WCRKgXNe8j6mSBcST9VGrBoCsmEQAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Ipanema' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/ipanema/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwpKCDBhBPEiwAFgBzjw9Trgz0nu_wvfeakkc63bfE4D5dv-TA7LZBzujXffgYODKSeO7PLxoCGL8QAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Botafogo': 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/botafogo/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=Cj0KCQjwutaCBhDfARIsAJHWnHuK-ziAczwFpEYNle6FQCvmPXCb8YUrP17V1AeA7bQclYdsKVuveTsaApGYEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Leblon' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/leblon/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=Cj0KCQjwutaCBhDfARIsAJHWnHuK-ziAczwFpEYNle6FQCvmPXCb8YUrP17V1AeA7bQclYdsKVuveTsaApGYEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Recreio' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-oeste/recreio-dos-bandeirantes/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwpKCDBhBPEiwAFgBzjzK6xU3JDciXh0noddkjMb9M6YT_barUlRHa61LuogPZzcKTcbLxHxoCc_4QAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Jacarepaguá' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-oeste/jacarepagua/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwx6WDBhBQEiwA_dP8rfJPBiaI5zVAeBxLfzKXSYc2SGbIV-50WCRKgXNe8j6mSBcST9VGrBoCsmEQAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Taquara' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-oeste/taquara/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=CjwKCAjwpKCDBhBPEiwAFgBzjw9Trgz0nu_wvfeakkc63bfE4D5dv-TA7LZBzujXffgYODKSeO7PLxoCGL8QAvD_BwE&utm_referrer=https%3A%2F%2Fwww.google.com%2F',
        'Barra' : 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-oeste/barra-da-tijuca/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=Cj0KCQjwutaCBhDfARIsAJHWnHuK-ziAczwFpEYNle6FQCvmPXCb8YUrP17V1AeA7bQclYdsKVuveTsaApGYEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F'}

erro = []
resultado = []

for bairro, url in urls.items():
    current_url = url
    driver.get(url)
    sleep(2)
    actions = ActionChains(driver)

    try:
        driver.find_element_by_class_name("cookie-notifier__cta").click()
    except:
            print("sem cookies!")
    
    for i in tqdm(range(30), desc=bairro):
        
        sleep(5)
        main_div = driver.find_element_by_class_name("results-main__panel")
        properties = main_div.find_elements_by_class_name("js-property-card")
        paginator = driver.find_element_by_class_name("js-results-pagination")
        next_page = paginator.find_element_by_xpath("//a[@title='Próxima página']")
        
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
            print("Next page not clickable")
            break
pd.DataFrame(resultado).to_csv("C:/Users/Thiago/Desktop/Potifolio/Projeto calculadora de imoveis/Data Sets/todos_os_resultados.csv", index=False)
driver.close()