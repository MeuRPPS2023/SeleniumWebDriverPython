import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://proxima2.sisprevweb.com.br/estado_01/pericia/Login/Login.aspx")

print("Título do projeto: ", browser.title)

print("URL do projeto: ", browser.current_url)

print("Código fonte do projeto: ", browser.page_source)

time.sleep(5)