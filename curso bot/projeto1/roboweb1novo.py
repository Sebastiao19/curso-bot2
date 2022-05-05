from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

print('Iniciando nosso robô...\n')

options = webdriver.ChromeOptions()
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')

# comando pra abrir o navegador 
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome('/home/tiao/Documentos/curso_python_bot/chromedriver')
driver.get("https://registro.br/")

pesquisa = driver.find_element(By.ID,'is-avail-field')
pesquisa.clear()
pesquisa.send_keys('roboscompython.com.br')
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()