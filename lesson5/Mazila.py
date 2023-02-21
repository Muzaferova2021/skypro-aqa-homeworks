from time import sleep   # импортируем функцию sleep  из модуля time
from selenium import webdriver
from selenium.webdriver.common.by import By

#зайти на сайт лабиринт
driver = webdriver.Firefox()  # вызов вебдрайвера для FireFox
driver.maximize_window() # открыть окно на полный размер
driver.get("http://uitestingplayground.com/dynamicid") # передаем URL драйверу

search_input = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()   # Находим по CSS  и кликаем на синюю кнопку

sleep(5)  # слип на 5 секунд. Для того, чтобы увидеть клик. Можно убрать.

driver.quit()  # Закрыть вебдрайвер
