import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.applitools.com/")

tituloLogin = browser.find_element(By.XPATH, "//h4[@class='auth-header']")
assert tituloLogin.is_displayed(), "Diferente!"
assert tituloLogin.is_enabled(), "Diferente!"

# ✅ Opção 1 — usando == False
# assert relembrar.is_displayed() == False, "Elemento deveria estar oculto!"

# ✅ Opção 2 — usando not (mais pythônico)
# assert not relembrar.is_displayed(), "Elemento deveria estar oculto!"

# ✅ Verifica que está visível
# assert relembrar.is_displayed() == True, "Elemento não está visível!"

# Elementos
username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")
buttonLogin = browser.find_element(By.ID, "log-in")
relembrar = browser.find_element(By.XPATH, "//input[@class='form-check-input']")

# Retorno
print("Display: ", username.is_displayed())
assert username.is_displayed(), "Diferente!"
print("Enable: ", username.is_enabled())
assert username.is_enabled(), "Diferente!"

assert password.is_displayed(), "Diferente!"
assert password.is_enabled(), "Diferente!"

assert buttonLogin.is_displayed(), "Diferente!"
assert buttonLogin.is_enabled(), "Diferente!"

assert relembrar.is_displayed(), "Diferente!"
assert relembrar.is_enabled(), "Diferente!"
assert not relembrar.is_selected(), "Diferente!"
relembrar.click()
assert relembrar.is_selected(), "Diferente!"

# Tempo de espera
time.sleep(3)

# Fechar browser
browser.quit() # ← executa automaticamente ao final de cada teste