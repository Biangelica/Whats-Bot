# Whats-Bot

REQUIRED 
webdriver_manager >=  3.2.2
selenium  >=  3.141.0

Browser
Google Chrome


Caso o webdriver_manager não consiga baixar o chrome driver, baixe manualmente do site https://chromedriver.chromium.org/downloads
 e na Llinha 22 do código substituia pelo caminho de destino
 EX:
 
#Navegar Whatsaap
driver = webdriver.Chrome(f"C:\Users\user\Downloads\chromedriver_win32")
