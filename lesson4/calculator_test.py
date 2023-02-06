import pytest
from calculator import Calculator


calculator=Calculator()


def test_sum_positive_nums(): #позитив сумма
    calculator=Calculator()
    res=calculator.sum(4,5)
    assert res==9

def test_sum_vegative_nums(): # негатив сумма
    calculator=Calculator()
    res=calculator.sum(-5,-10)
    assert res==-16

def test_sum_positine_end_vegative_nums(): #позитив и негатив сумма
    calculator=Calculator()
    res=calculator.sum(-6,6)
    assert res==0

def test_sum_float_nums():  #с точкой 
    calculator=Calculator()
    res=calculator.sum(5.6,4.3)
    res=round(res,1)
    assert res==9.9

def test_sum_zero_nums(): #сумма с ноль
    calculator=Calculator()
    res=calculator.sum(10,0)
    assert res==10

def test_div.positive(): #деление позитив
    calculator=Calculator()
    res=calculator.div(10,2)
    assert res==5

def test_div_by_zero(): #деление на ноль
    calculator=Calculator()
    with pytest.raises(ArithmeticError) #для того, что бы передалось название ошибки там где есть (название ошибки)
    res=calculator.div(10,20)
    assert res==None

def test_avg_empty_list(): #нахождение среднего ,пустой лист
    calculator=Calculator()
    numbers=[]
    res=calculator.avg(numbers)
    assert res==0

def test_avg_positive(): # нахождение среднего позитив
    calculator=Calculator()
    numbers=[1,2,3,4,5,6,7,8,9,5]
    res=calculator.avg(numbers)
    assert res==5