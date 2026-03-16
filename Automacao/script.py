from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://proxima2.sisprevweb.com.br/estado_01/pericia/Login/Login.aspx")
browser.find_element(By.ID, "txtLogin").sendKeys("1340")
browser.find_element(By.ID, "txtSenha").csendKeys("fgh38a")
browser.find_element(By.ID, "btnLogin").click()