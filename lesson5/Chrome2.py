from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

search_input = driver.find_element(By.CSS_SELECTOR, '[class*="btn-primary"]') # Находим по CSS синюю кнопку

'''
Ниже цикл. В котором  трижды кликаем на синюю кнопку найденную выше.
'''
for i in range(0, 3):
    search_input.send_keys(Keys.RETURN)
    Alert(driver).accept()
    i = i + 1

print("Нажали на кнопку", i, "раз!")

sleep(5) # слип на 5 секунд. Для того, чтобы увидеть клик. Можно убрать.

driver.quit() # Закрыть вебдрайвер
