class ClaseNodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.hijoizq = None
        self.hijoder = None
        self.altura = 1 #Altura del nodo para balanceo
        
    def esHoja(self):
        return self.hijoizq is None and self.hijoder is None