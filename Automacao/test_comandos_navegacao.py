import time
from selenium import webdriver

# browser pode ser subistituído por qualquer outro nome
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://proxima2.sisprevweb.com.br/estado_01/pericia/Login/Login.aspx")
time.sleep(3)
browser.refresh()

browser.get("https://www.perplexity.ai/search/meu-projeto-python-nao-esta-im-cWD8JeyzSLKahcM.17KuOw")

time.sleep(3)

browser.back()

time.sleep(3)

browser.forward()

time.sleep(3)

browser.switch_to.new_window("tab")

browser.close()

time.sleep(3)

browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")

time.sleep(3)

browser.quit()