lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
sum=0
for item in lst:
    if item<30 and item%3==0:
        print(item)
else:
    sum=sum+item
    print('sum =', sum)  