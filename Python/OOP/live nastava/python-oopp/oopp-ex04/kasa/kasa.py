import enum
class Product:
    def __init__(self,id,name,price,stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    @staticmethod
    def parse(txt):
        prod_arr = txt.strip().split(",")
        return Product(int(prod_arr[0]),prod_arr[1],float(prod_arr[2]),int(prod_arr[3]))
    def serialize(self):
        return f"{self.id},{self.name},{self.price},{self.stock}"
    def __str__(self):
        return f"id: {self.id} name: {self.name} price: {self.price} stock: {self.stock}"
class MenuCommand(enum.Enum):
    LIST    = 1
    SEARCH  = 2
    ADD     = 3 
    CONFIRM = 4
class Menu:
    def __getnumber(self,msg):
        while True: 
            id = input(f"{msg}: ")
            if not id.isnumeric():
                print("Invalid number")
                continue
            else:
                break
        return int(id)
    def quantity(self):
        return self.__getnumber("Enter quantity")
    def productid(self):
        return self.__getnumber("Enter product id")
    def main(self):
        while True:
            print("1. List all, 2. Search, 3. Add, 4. Confirm")
            cmd = input("Enter command: ")
            if not cmd.isnumeric() or cmd not in "1234":
                print("Invalid command")
                continue
            else:
                break
        return MenuCommand(int(cmd))
    
class Kasa:
    def confirm(self):
        self.file_handler.seek(0)
        r = self.file_handler.readline()
        pos = 0
        while r:
            if r.strip(): 
                p = Product.parse(r)  
                if p.id in self.basket: 
                    p.stock -= self.basket[p.id]
                    self.file_handler.seek(pos) 
                    self.file_handler.write(p.serialize()+"\n") 
            pos = self.file_handler.tell()
            r = self.file_handler.readline()
        self.file_handler.flush()
        self.basket.clear()
    def list_products(self):
        self.file_handler.seek(0)
        r = self.file_handler.readline()
        while r:
            p = Product.parse(r)  
            print(p)
            r = self.file_handler.readline()
    def find_product(self,id):
        self.file_handler.seek(0)
        r = self.file_handler.readline()
        while r:
            p = Product.parse(r)
            if p.id == id:
                return p
            r = self.file_handler.readline()
        else:
            return None
    def __init__(self):
        self.file_handler = open("products","r+",encoding="utf-8") 
        self.basket = {}
    @staticmethod
    def run():
        k = Kasa()
        m = Menu()
        while True:
            cmd = m.main() 
            if cmd == MenuCommand.LIST:
                k.list_products()
            elif cmd == MenuCommand.SEARCH:
                id = m.productid()
                prod = k.find_product(id)
                if prod:
                    print(prod)
            elif cmd == MenuCommand.ADD:
                id  = m.productid()
                qu  = m.quantity()
                k.basket[id] = qu
            elif cmd == MenuCommand.CONFIRM:
                k.confirm() 