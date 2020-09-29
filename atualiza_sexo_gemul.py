#atualiza_sexo_gemul
#SUCESSFUL

# libraries
import pyautogui as p
import time as t
from selenium import webdriver
import winsound

# declarations
driver = webdriver.Firefox()
cont = 3
ultimo = 0


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
    #selecionando "Historico Escolar Ensino Fundamental (de onde há o sexo do aluno)"
    p.moveTo(425,-707,duration=0.3)
    p.click()
    t.sleep(0.5)
    p.moveTo(451,-327,duration=0.3)
    p.click()
    t.sleep(0.5)

def seleciona_excel():
    p.moveTo(320,-23,duration=0.3)
    p.click()
    p.hotkey('esc')
    t.sleep(0.3)
    p.hotkey('home')
    t.sleep(0.3)
    p.press('right')

def copia_matricula():
    p.moveTo(291,181,duration=0.3)
    p.doubleClick()
    p.hotkey('ctrl','c')
    t.sleep(0.5)

def pesquisa_aluno():
    p.moveTo(283,-634,duration=0.3)
    p.doubleClick()
    t.sleep(0.3)
    p.hotkey('ctrl','v')
    t.sleep(0.5)
    p.hotkey('tab')
    t.sleep(1)
    p.moveTo(56,-542,duration=0.3)
    p.click()
    t.sleep(3)

def copia_sexo():
    p.moveTo(1302,-565,duration=0.3)
    p.doubleClick()
    t.sleep(0.3)
    p.hotkey('ctrl','c')
    t.sleep(0.3)

def cola_sexo_excel():
    p.moveTo(320,-23,duration=0.3)
    p.click()
    t.sleep(0.3)
    p.hotkey('esc')
    t.sleep(0.3)
    p.press('right')
    t.sleep(0.3)
    p.hotkey('ctrl','v')
    t.sleep(5)

def volta_pagina():
    p.moveTo(25,-848,duration=0.3)
    p.click()
    t.sleep(0.3)
    p.moveTo(425,-707,duration=0.3)
    p.click()
    t.sleep(0.5)
    p.moveTo(451,-327,duration=0.3)
    p.click()
    t.sleep(0.5)

def proximo():
    p.press('down')
    t.sleep(0.3)
    p.press('left')
    t.sleep(0.3)


# execution
open_login_gemul()
seleciona_excel()

while cont > ultimo:
    copia_matricula()
    pesquisa_aluno()
    copia_sexo()
    volta_pagina()
    cola_sexo_excel()
    proximo()
cont +=1
