import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://proxima2.sisprevweb.com.br/estado_01/pericia/Login/Login.aspx")

# find_element()
username = browser.find_element(By.ID, "txtLogin")
password = browser.find_element(By.ID, "txtSenha")

buttonLogin = browser.find_element(By.ID, "btnLogin")

# send_keys
username.send_keys("1340")
password.send_keys("fgh38a")
buttonLogin.click()

time.sleep(5)

# find_elements
credenciais = browser.find_elements(By.XPATH, "//*[@class='form-control text-input']")
print(credenciais) # Mostrar os elementos encontrados
print(len(credenciais)) # Identificar a quantidade de elementos encontrados
assert len(credenciais) == 1, "Qtd de elemento(s) diferente do esperado" # Verificação da quantidade de elementos

browser.quit()