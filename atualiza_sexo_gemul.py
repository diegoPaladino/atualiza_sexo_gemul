#atualiza_sexo_gemul

# libraries
import pyautogui as p
import time as t
from selenium import webdriver
import winsound

# declarations
driver = webdriver.Firefox()


#open/login Gemul
#efetuando o login(making the login)
def open_login_gemul():
    driver.get('http://gemul.com.br')
    driver.set_window_position(166,-700)
    driver.maximize_window()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/ul/li[2]/a/img').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/div/p/strong[3]/a').click()
    user = driver.find_element_by_xpath('//*[@id="txtLogin"]')
    username = driver.find_element_by_id('txtLogin')
    password = driver.find_element_by_id('txtSenha')
    username.send_keys('DIEGO.CSF')
    password.send_keys('GMLPALADINO')
    p.hotkey('tab')
    p.hotkey('enter')
    t.sleep(2)
    driver.find_element_by_class_name('img-responsive').click()
    #selecionando "Cadastro de Alunos"
    p.moveTo(215,-708)
    p.click()
    t.sleep(0.5)
    p.moveTo(209,-578)
    p.click()
    t.sleep(0.5)

def seleciona_excel():
    p.moveTo(320,-23,duration=0.3)
    p.click()
    p.hotkey('home')
    t.sleep(0.3)
    p.hotkey('right')

def copia_matricula():
    p.moveTo(291,181,duration=0.3)
    p.doubleClick()
    p.hotkey('ctrl','c')





# execution
open_login_gemul()
seleciona_excel()
copia_matricula()



