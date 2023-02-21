from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #сделать экран большим
driver.get("https://ya.ru") #зайди на яндекс
sleep(5) #подожди 5 сек
driver.fullscreen_window() #аналог f1 ,типа большое окно без сложить 
sleep(5) #подожди 5 сек
driver.save_screenshot("./ya.png") #сохрани скриншот,в скобках можно указать куда сохранить ("....png")


#for x in range(1,10):для того что бы сайт ходил туда сюда 
    #driver.back()
    #driver.forward()
    #driver.refresh()когда нужно зачем нибудь обновить страницу
#driver.set.window_size(640,460) #можно задать значение размера экрана 


sleep(15)