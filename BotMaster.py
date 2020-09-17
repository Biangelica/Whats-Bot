from selenium import webdriver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Definir contatos, Grupos e mensagens 
contatos = []
mensagem = []
parar = 1
while parar > 0:
    print('*** ADICIONAR CONTATOS ***')
    cont = str(input('Digite o nome do contato/grupo que irá receber a mensagem:'))
    contatos.append(cont)
    parar = int(input('Gostaria de Adicionar mais um contato? Sim-1 Não-0:'))

print('*** Mensagem ***')
msg = str(input('Digite a mensagem a ser enviada: '))
mensagem.append(msg)

#Navegar Whatsaap
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(10)

#Buscar contatos/Grupos
def buscar_contatos(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contatos(contato)
    enviar_mensagem(mensagem)
## Campo de pesquisa 'copyable-text selectable-text'
## Campo de mensagem 'copyable-text selectable-text'
