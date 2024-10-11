import requests
from bs4 import BeautifulSoup
import smtplib

def verificar_preco(url, preco_desejado):
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    preco = float(sopa.find('span', {'class': 'preco'}).text.strip().replace('R$', '').replace(',', '.'))
    
    if preco <= preco_desejado:
        enviar_email(preco)

def enviar_email(preco):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('seu_email@gmail.com', 'sua_senha')
    mensagem = f"O preço caiu para R${preco}"
    server.sendmail('seu_email@gmail.com', 'destino@gmail.com', mensagem)
    server.quit()

verificar_preco('https://exemplo.com/produto', 100.0)
