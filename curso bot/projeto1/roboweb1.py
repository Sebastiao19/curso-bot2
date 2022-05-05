from requests import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')

# comando pra abrir o navegador 
driver = webdriver.Chrome('/home/tiao/Documentos/curso_python_bot/chromedriver')
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id('is-avail-field')
pesquisa.clear()
pesquisa.send_keys('roboscompython.com.br')
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()