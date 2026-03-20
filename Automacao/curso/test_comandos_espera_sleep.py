import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.saucedemo.com/")

# Verificar título do site
browser.title
assert browser.title == "Swag Labs", "Errado!"

# Elementos
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btnLogin = browser.find_element(By.ID, "login-button")
tituloLogin = browser.find_element(By.CLASS_NAME, "login_logo")

# TC001
assert tituloLogin.text == "Swag Labs", "Errado!"
time.sleep(3) #Comando de espera independente do que acontecer durante os testes!
username.send_keys("standard_user")
time.sleep(3) #Comando de espera independente do que acontecer durante os testes!
password.send_keys("secret_sauce")
time.sleep(3) #Comando de espera independente do que acontecer durante os testes!
btnLogin.click()
time.sleep(3) #Comando de espera independente do que acontecer durante os testes!

# Validar login na tela Inicial
tituloTelaInicial = browser.find_element(By.CLASS_NAME, "title")
assert tituloTelaInicial.text == "Products", "Errado!"

time.sleep(3) #Comando de espera independente do que acontecer durante os testes!
browser.quit()