from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/search?keywords=ciencia%20de%20dados&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get(URL_LINKEDIN_DS)
    descricao = driver.find_element_by_class_name('description')
    
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricoes = []
    
    while True:
        for r in resultados[len(lista_descricoes):]:
            r.click()
            sleep(1)
            try:
                descricao = driver.find_element_by_class_name('description')
                lista_descricoes.append(descricao.text)
            except:
                print('Erro')
                pass
            
        resultados = driver.find_elements_by_class_name('result-card')
        
        if len(lista_descricoes) == len(resultados):
            break
        
    descricao_salvar = '\n'.join(lista_descricoes)
    with open('descricoes_vagas.txt' , 'w', encoding='utf-8') as f:
              f.write(descricao_salvar)
                
    driver.quit

