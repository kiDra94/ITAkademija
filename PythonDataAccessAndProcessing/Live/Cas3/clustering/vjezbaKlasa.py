class Lista:
    def __init__(self, n) -> None:
        self.n = n
        self.lista = []

    def napuni_listu(self)-> None:
        znak = 1
        for i in range(1, self.n + 1):
            self.lista.append(i * znak)
            znak = -znak
    
    def __str__(self) -> str:
        return str(self.lista)
    
obj = Lista(30)
obj.napuni_listu()
print(obj)