from selenium import webdriver
import time
import webbrowser
from urllib.parse import quote

driver = webdriver.Chrome()
numero=553799751870
mensagem = quote("Teste api")

def enviamensagem(contato,message):
    mensagem = quote(message)
    print(mensagem)
    contato = str(contato)
    mensagem= message
    #link = f"https://web.whatsapp.com/send?phone{numero}&text={quote(mensagem)}"
    link = f"https://web.whatsapp.com"
    webbrowser.open(link)
    print("Pausa dos 10 segundos")
    time.sleep(120)
  
    #Procura pelo contato desejado 
    barra_pesquisa = driver.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    time.sleep(5)
    barra_pesquisa.send_keys(contato) 

    #Seleciona o contato 

    Contato_escolhido = driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    time.sleep(3)
    Contato_escolhido.click 

    #insere a mensagem na barra de mensagens
    input_message = driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    input_message.send_keys(mensagem)

    button_env = driver.find_element('xpath',' //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    time.sleep(3)
    button_env.click()

    
   




