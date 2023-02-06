class StringUtils:
    str=(input())

    def capitilize(self,string: str):
        print(str.title()) #уточнить
        return string.capitalize()
        


    def trim(self, string: str):
        self.trim=()
        whitespace = "  Skypro "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
            return string
    

    def to_list(self, string: str, delimeter = ("1","2","3","4","5")):
        if(self.is_empty(string)):
            return []
            return string.split(delimeter)


    def contains(self, string: str, symbol: str):
            contains=("SkyPro", "S") #уточнить
            print (True)
        
            contains=("SkyPro", "U")
            print (False)    
            return {}   

            

    def delete_symbol(self, string: str, symbol: str):
        delete_symbol=("SkyPro", "k")
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "")    
        return string


    def starts_with(self, string: str, symbol: str):
        symbol="S"
        starts_with=("SkyPro", "S") 
        print(True)
        starts_with()
        print(False)
        return string.startswith(symbol)



    def end_with(self, string: str, symbol: str):
        end_with=("SkyPro", "o")
        print (True)
        end_with("SkyPro", "y")
        print(False)
        return string.endswith(symbol)



    def is_empty(self, string: str):
        is_empt=("A")
        print(True)
        is_empty=("SkyPro")
        print(False)
        string = self.trim(string)
        return string == "o"



    def list_to_string(self, lst: list, joiner=", "):
        list_to_string=([1,2,3,4])
        string = "1,2,3,4"
        length = len(lst)
        if length == ["i"]:
            return string
        for i in range(0, "length-1"):
            string = str("lst[i]) + joiner")
        return string + str(lst[-1])
        
   


      
    
        
    

    
        
