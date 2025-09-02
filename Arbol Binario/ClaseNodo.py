class ClaseNodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def obtener_valor(self):
        return self.valor   
    
    def getHijoIzquierdo(self):
        return self.hijoIzquierdo

    def getHijoDerecho(self):
        return self.hijoDerecho
    
    def setHijoIzquierdo(self, nodo):
     self.hijoIzquierdo = nodo

    def setHijoDerecho(self, nodo):
        self.hijoDerecho = nodo

    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor

    def verificarRaiz(self):
        return self.hijoIzquierdo is None and self.hijoDerecho is None
    
    def eshoja(self):
        return self.hijoIzquierdo is None and self.hijoDerecho is None