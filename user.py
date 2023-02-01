class User:
    age=0;

    def __init__(self, name):
        print("я создался")
        self.username=name


    def sayName(self):
        print("меня зовут", self.username)


    def sayAge(self):
        print(self.age)


    def sayAge(self, newAge):
        self.age=newAge


alex=User("alex")
mark=User("mark")
marta=User("marta")


alex.sayName()
alex.sayAge()
alex.setAge(33)
alex.sayAge()
