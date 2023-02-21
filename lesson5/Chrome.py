from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # вызов вебдрайвера для Google Chrome
driver.maximize_window() # открыть окно на полный размер
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")  # передаем  URL в браузер


#Нажимаем 5 раз на кнопку
search_input = driver.find_element(By.CSS_SELECTOR, "button")  # находим кнопку
# цикл - 5 раз нажимаем на кнопку
for i in range(0, 5):
    search_input.send_keys(Keys.RETURN)


#Посчитать сколько раз нажали на кнопку и вывести на экран
clicks = driver.find_elements(By.XPATH, "//*[@id='elements']/button")  # находим количество элементов кнопка "Delete"
print("Количество кнопок Delete:", len(clicks))  # Выводим в консоль количество найденных кнопок

sleep(5) # слип на 5 секунд. Для того, чтобы увидеть кнопки. Можно убрать.

driver.quit()   # Закрыть вебдрайвер
