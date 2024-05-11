class HashTable:
    def __init__(self):
        self.__data = [0] * 100
        self.__len = len(self.__data) 

    def add(self, key, value):
        index = id(key)%self.__len
        self.__data[index] = value

    def get(self,key):
        index = id(key)%self.__len
        return self.__data[index] 
        
ht = HashTable()

ht.add("my_key","Hello!")
ht.add("my_key_1","World")

print(ht.get("my_key_1"))