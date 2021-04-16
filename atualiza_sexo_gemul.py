#atualiza_sexo_gemul
#SUCESSFUL

# libraries
import pyautogui as p
import time as t
from selenium import webdriver
import winsound
from twilio.rest import Client

# declarations
driver = webdriver.Firefox()
cont = 3
ultimo = 0

# Your Account SID from twilio.com/console
account_sid = "AC42c3b0dac480c2bf504f403704742f89"
# Your Auth Token from twilio.com/console
auth_token  = "42f2a0846d5e66bb0edc7880a99d93ca"

client = Client(account_sid, auth_token)

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
    t.sleep(1)
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
    p.press('right',presses=13)
    t.sleep(0.3)
    p.hotkey('ctrl','v')
    t.sleep(7)
    

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
    p.hotkey('home')
    t.sleep(0.8)


# execution
open_login_gemul()
seleciona_excel()

while cont > ultimo:
    try:
        copia_matricula()
        pesquisa_aluno()
        copia_sexo()
        volta_pagina()
        cola_sexo_excel()
        proximo()

    except:
        message = client.messages.create(
        to="+5562992591138", 
        from_="+14152363566",
        body="deu erro")

print(message.sid)

cont +=1
