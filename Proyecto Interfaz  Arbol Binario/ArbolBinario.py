from Nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        
        actual = self.raiz
        padre = None
        
        while actual is not None:
            padre = actual
            if valor < actual.valor:
                actual = actual.hijoIzquierdo
            elif valor > actual.valor:
                actual = actual.hijoDerecho
            else:
                return
        
        if valor < padre.valor:
            padre.hijoIzquierdo = nuevo_nodo
        else:
            padre.hijoDerecho = nuevo_nodo

    def Buscar_x_Recursivo(self, valor):
        return self._BuscarRecursivo(self.raiz, valor)

    def _BuscarRecursivo(self, nodoActual, valor):
        if nodoActual is None:
            return None
        if valor == nodoActual.valor:  # ← CORREGIDO
            return nodoActual
        if valor < nodoActual.valor:   # ← CORREGIDO
            return self._BuscarRecursivo(nodoActual.hijoIzquierdo, valor)
        else:
            return self._BuscarRecursivo(nodoActual.hijoDerecho, valor)

    def ContarNodos(self):
        return self._ContarNodosRecursivo(self.raiz)

    def _ContarNodosRecursivo(self, raizAux):
        if raizAux is None:
            return 0
        return 1 + self._ContarNodosRecursivo(raizAux.hijoIzquierdo) + self._ContarNodosRecursivo(raizAux.hijoDerecho)

    def InOrdenRecursivo(self):
        resultado = []
        self._InOrden_Recursivo(self.raiz, resultado)
        return resultado 

    def _InOrden_Recursivo(self, nodoActual, resultado):
        if nodoActual is not None:
            self._InOrden_Recursivo(nodoActual.hijoIzquierdo, resultado)
            resultado.append(nodoActual.valor)  # ← CORREGIDO
            self._InOrden_Recursivo(nodoActual.hijoDerecho, resultado)

    def PreOrdenRecursivo(self):
        resultado =[]
        self._PreOrden_Recursivo(self.raiz, resultado)
        return resultado 
    
    def _PreOrden_Recursivo(self, nodoActual, resultado):
        if nodoActual is not None:
            resultado.append(nodoActual.valor)  # ← CORREGIDO
            self._PreOrden_Recursivo(nodoActual.hijoIzquierdo, resultado)
            self._PreOrden_Recursivo(nodoActual.hijoDerecho, resultado)

    def PostOrdenRecursivo(self):
        resultado = []
        self._PostOrden_Recursivo(self.raiz, resultado)
        return resultado 

    def _PostOrden_Recursivo(self, nodoActual, resultado):
        if nodoActual is not None:
            self._PostOrden_Recursivo(nodoActual.hijoIzquierdo, resultado)
            self._PostOrden_Recursivo(nodoActual.hijoDerecho, resultado)
            resultado.append(nodoActual.valor)  # ← CORREGIDO
    
    def isVacio(self):
        return self.raiz is None

    def Altura(self):
        return self._Altura_Recursivo(self.raiz)
    
    def _Altura_Recursivo(self, nodoActual):
        if nodoActual is None:
            return 0
        izquierda = self._Altura_Recursivo(nodoActual.hijoIzquierdo)
        derecha = self._Altura_Recursivo(nodoActual.hijoDerecho)
        return 1 + max(izquierda, derecha)

    def obtenerEstructuraD3(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        return {
            "name": str(nodo.valor),
            "children": list(filter(None, [
                self.obtenerEstructuraD3(nodo.hijoIzquierdo) if nodo.hijoIzquierdo else None,
                self.obtenerEstructuraD3(nodo.hijoDerecho) if nodo.hijoDerecho else None
            ]))
        }

    def eliminar_nodo(self, x):
        self.raiz = self.__eliminarRecursivo(self.raiz, x)

    def __eliminarRecursivo(self, nodoRaiz, x):
        if nodoRaiz is None:
            return None
        if x == nodoRaiz.valor:
            return self.eliminarNodo(nodoRaiz)
        if x < nodoRaiz.valor:
            nodoRaiz.hijoIzquierdo = self.__eliminarRecursivo(nodoRaiz.hijoIzquierdo, x)
        else:
            nodoRaiz.hijoDerecho = self.__eliminarRecursivo(nodoRaiz.hijoDerecho, x)
        return nodoRaiz

    def eliminarNodo(self, nodo):
        if nodo.hijoIzquierdo is None and nodo.hijoDerecho is None:
            return None
        if nodo.hijoIzquierdo is None:
            return nodo.hijoDerecho
        elif nodo.hijoDerecho is None:
            return nodo.hijoIzquierdo

        sucesor = self._minimo(nodo.hijoDerecho)
        nodo.valor = sucesor.valor
        nodo.hijoDerecho = self.__eliminarRecursivo(nodo.hijoDerecho, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        actual = nodo
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo
        return actual

    def limpiar_Arbol(self):
        self.raiz = None

if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(50)
    arbol1.insertar(150)
    
    print("Cantidad de Nodos:", arbol1.ContarNodos())
    print("InOrden:", arbol1.InOrdenRecursivo())