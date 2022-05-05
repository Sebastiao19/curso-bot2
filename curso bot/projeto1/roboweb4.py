
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print('inciando nosso robô...\n')

Workbook = xlrd.open_workbook('/home/tiao/Documentos/curso_python_bot/excel.xls')
sheet = Workbook.sheet_by_name('Plan1')
rows = sheet.nrows
columns = sheet.ncols

options = webdriver.ChromeOptions()
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')

# comando pra abrir o navegador 
driver = webdriver.Chrome('/home/tiao/Documentos/curso_python_bot/chromedriver')
driver.get("https://registro.br/")


for curr_row in range(0, rows):
    x = sheet.cell_value(curr_row,0)
    pesquisa = driver.find_element_by_id('is-avail-field')
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    print('Dominio %s %s' % (x, driver.find_element_by_xpath('/html/body/div/main/section/div[2]/div/p/span/strong').text))

driver.close()