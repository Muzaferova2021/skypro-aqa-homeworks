x = int(input())
m = int(input())
y = int(input())

def bank(x, m, y):
    nal = x
    year = y
def money():
    if year >0:
        nal = x*1.1+m
        year = year -1
        return money()
    else:
        print(nal)
                
