from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Escaneie o QR Code e pressione Enter")

def enviar_mensagem(contato, mensagem):
    search_box = driver.find_element('xpath', "//div[@title='Search input textbox']")
    search_box.send_keys(contato + Keys.ENTER)
    time.sleep(2)
    msg_box = driver.find_element('xpath', "//div[@contenteditable='true']")
    msg_box.send_keys(mensagem + Keys.ENTER)

contatos = ['Contato1', 'Contato2']
mensagem = "Olá, esta é uma mensagem automatizada!"

for contato in contatos:
    enviar_mensagem(contato, mensagem)
