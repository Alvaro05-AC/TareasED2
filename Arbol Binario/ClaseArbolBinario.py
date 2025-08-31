
from ClaseNodo import ClaseNodo

class ArbolBinario:
    
     def __init__(self):
        self.raiz=None
        
     def insertar(self, valor):
         self.raiz=self._insertarRecursivo(self.raiz, valor)
         
     def _insertarRecursivo(self, raizAux, valor):
         #Caso Base
            if raizAux is None:
                raizAux=ClaseNodo(valor)
                return raizAux
            #CasoGeneral
            else:
                if valor < raizAux.obtener_valor():
                    raizAux.hijoIzquierdo=self._insertarRecursivo(raizAux.hijoIzquierdo, valor)
                
                else:
                    raizAux.hijoDerecho=self._insertarRecursivo(raizAux.hijoDerecho, valor)
                return raizAux
#-----------------------------------------------------------------------------------------------------------------
    # Cuenta los Nodos del arbol iterativo y Recursivo
     def ContarNodos(self):
         return self._ContarNodosRecursivo(self.raiz)
     
     def _ContarNodosRecursivo(self, raizAux):
         if raizAux is None:
             return 0
         return 1 + self._ContarNodosRecursivo(raizAux.hijoIzquierdo) + self._ContarNodosRecursivo(raizAux.hijoDerecho)
#------------------------------------------------------------------------------------------------------------------       
    #Cuenta los Nodos Pares del arbol iterativo y Recursivo
     def Contar_Nodos_Pares(self):
            return self._Contar_Nodos_Pares_Recursivo(self.raiz)
        
     def _Contar_Nodos_Pares_Recursivo(self, raizAux):
        if raizAux is None:
            return 0
        hi= self._Contar_Nodos_Pares_Recursivo(raizAux.hijoIzquierdo) 
        hd= self._Contar_Nodos_Pares_Recursivo(raizAux.hijoDerecho) 
        if raizAux.obtener_valor() % 2 == 0:
                return hi + hd + 1
        else:
                return hi + hd 
            
#------------------------------------------------------------------------------------------------------------------        
    # Verifica si el arbol esta vacio        
     def isVacio(self):
          return self.raiz is None

#-----------------------------------------------------------------------------------------------------------------
# Muestra el arbol en General
if __name__ == "__main__":
    arbol1= ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(50)
    arbol1.insertar(150)
    arbol1.insertar(25)
    arbol1.insertar(75)
    arbol1.insertar(125)
    arbol1.insertar(175)
         
    print("Cantidad de Nodos en el Arbol:", arbol1.ContarNodos())
    print("Cantidad de Nodos Pares:", arbol1.Contar_Nodos_Pares())           
                    
                