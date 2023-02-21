




from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #создалась благодаря search_imput=driver.find_element(By.CSS_SELECTOR, search_locator)
from selenium.webdriver.common.keys import Keys#создалась благодаря search_imput.send_keys(Keys.RETURN)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #сделать экран большим
#Открыть лабиринт
driver.get("https://www.labirint.ru/") #зайди в лабирин



#В строке поиска книг написать python
#Нажать enter
search_locator="#search-field"               #эта пиздула в скобках вообще то из кода "строка " если что
search_imput=driver.find_element(By.CSS_SELECTOR, search_locator)
search_imput.send_keys("Python")                #напиши в поисковике слово питон
search_imput.send_keys(Keys.RETURN)                   #нажми на поиск



#Посчитать кол-во книг на странице, или как говорит Еремин посчитать все карточки товара
#Посчитать кол-во книг на странице
books=driver.find_elements(By.CSS_SELECTOR,"div.product")       #див продакт это элемент который обьединяет все найденные книги
print(len(books))                            #выведи весь найденный список книг




#Вывести инфо по каждой странице  вконсоль в формате Название/Автор/Цена
for book in books:               #для каждой книжки в списке книг
    title=book.find_element(By.CSS_SELECTOR,"span.product-title").text #название книги
    price=book.find_element(By.CSS_SELECTOR,"span.price-val").text     #цена книги


    author=" "
    try:                           #попробуй сделать такое то действие
        author=book.find_element(By.CSS_SELECTOR,"div.product-author").text
    except:                         #в исключительной ситуации
        author="Автор не указан"       #автор  не указан

    print(author+ "\t"+ title +"\t"+ price)




sleep(5)
