from ClaseNodoAVL import ClaseNodoAVL

class ArbolAVL:
    def __init__(self):
        self.raiz = None

#Metodos de utilidad-------------------------------------------------------------------------------- 
    def obtener_altura(self, nodo): #Obtiene la altura del Nodo
        if not nodo:
            return 0
        return nodo.altura
    
    def obtenerFactor_balance(self, nodo): #obtiene el factor de balance del Nodo
        if not nodo:
            return 0
        return self.obtener_altura(nodo.hijoizq) - self.obtener_altura(nodo.hijoder)    
    
#Metodos Auxiliares--------------------------------------------------------------------------------
    def Minimo(self, nodo): #Encuentra el nodo con el valor minimo en un subArbol y esta en la izquierda
        actual = nodo
        while actual.hijoizq is not None:
            actual = actual.hijoizq
        return actual
    
    def Maximo(self, nodo): #Encuentra el nodo con el valor maximo en un subArbol y esta en la derecha
        actual = nodo
        while actual.hijoder is not None:
            actual = actual.hijoder
        return actual
    
    def EsArbolVL(self, nodo): #Verifica si un arbol es AVL
        def esAVL(nodo):
            if not nodo:
                return True, 0           
            izq_ok, izq_altura = esAVL(nodo.hijoizq)
            der_ok, der_altura = esAVL(nodo.hijoder)
            balance = izq_altura - der_altura
            actual_ok = izq_ok and der_ok and abs (balance) <= 1
            altura_actual = 1 + max(izq_altura, der_altura)
            
            return actual_ok, altura_actual
        return esAVL(nodo)[0]
    
    def ContarHojas(self, nodo): #Cuenta la cantidad de hojas en un arbol
        if nodo is None:
            return 0 
        pilaNodo = [nodo]
        ContHoja= 0
        while pilaNodo:
            nodoActual= pilaNodo.pop()
            if nodoActual.hijoizq is None and nodoActual.hijoder is None:
                ContHoja += 1
            if nodoActual.hijoder is not None:
                pilaNodo.append(nodoActual.hijoder)
            if nodoActual.hijoizq is not None:
                pilaNodo.append(nodoActual.hijoizq)
        return ContHoja
    
    def Vaciar(self): #Vacia el arbol AVL
        if self.raiz is None:
            return "El arbol ya esta vacio"
        self.raiz =None 
        return "El arbol ha sido vaciado"   
    
#Rotaciones----------------------------------------------------------------------------------------
    def rotacionDerecha(self, y): #Rotacion simple a la derecha
        x = y.hijoizq
        z = x.hijoder
        x.hijoder = y
        y.hijoizq = z
        #Actualizar Alturas
        y.altura = 1 + max(self.obtener_altura(y.hijoizq), self.obtener_altura(y.hijoder))
        x.altura = 1 + max(self.obtener_altura(x.hijoizq), self.obtener_altura(x.hijoder))
        return x #Nueva raiz
    
    def rotacionIzquierda(self, x): #Rotacion simple a la izquierda
        y = x.hijoder
        z = y.hijoizq
        y.hijoizq = x
        x.hijoder = z
        #Actualizar Alturas
        x.altura = 1 + max(self.obtener_altura(x.hijoizq), self.obtener_altura(x.hijoder))
        y.altura = 1 + max(self.obtener_altura(y.hijoizq), self.obtener_altura(y.hijoder))
        return y #Nueva raiz
    
    def rotacionDobleIzquierda_Derecha(self, x): #Rotacion doble izquierda-derecha
        x.hijoizq=self.rotacionIzquierda(x.hijoizq)
        return self.rotacionDerecha(x)
    
    def rotacionDobleDerecha_Izquierda(self, y): #Rotacion doble derecha-izquierda
        y.hijoder=self.rotacionDerecha(y.hijoder)
        return self.rotacionIzquierda(y)
    
#Metodos Principales--------------------------------------------------------------------------------
    def insertar(self, clave):
        self.raiz= self._insertar(self.raiz, clave)
        
    def _insertar(self, nodo, clave): #Inserta un nuevo nodo en el Arbol AVL
        if nodo is None:
            return ClaseNodoAVL(clave)
        if clave < nodo.valor: #si la clave es menor, se inserta a la izquierda
            nodo.hijoizq = self._insertar(nodo.hijoizq, clave)
        elif clave > nodo.valor: #si la clave es mayor, se inserta a la derecha
            nodo.hijoder = self._insertar(nodo.hijoder, clave)
        else:
            return nodo #No se permiten valores duplicados
        #Actualizar la altura del nodo ancestro
        nodo.altura = 1 + max(self.obtener_altura(nodo.hijoizq), self.obtener_altura(nodo.hijoder))
        balance= self.obtenerFactor_balance(nodo)
        #Si el nodo se desbalancea, hay 4 casos
        #Caso Izquierda Izquierda
        if balance > 1 and clave < nodo.hijoizq.valor:
            return self.rotacionDerecha(nodo)                                           
        #Caso Derecha Derecha
        if balance < -1 and clave > nodo.hijoder.valor:
            return self.rotacionIzquierda(nodo)
        #Caso Izquierda Derecha
        if balance > 1 and clave > nodo.hijoizq.valor:
            return self.rotacionDobleIzquierda_Derecha(nodo)
        #Caso Derecha Izquierda
        if balance < -1 and clave < nodo.hijoder.valor:
            return self.rotacionDobleDerecha_Izquierda(nodo)
        return nodo   
        
    def Eliminar(self, clave):
        self.raiz= self._Eliminar(self.raiz, clave)
           
    def _Eliminar(self, nodo, clave): #Elimina un nodo del Arbol AVL
        if nodo is None:
            return nodo 
        if clave < nodo.valor: #Si la clave es menor, se busca en el subarbol izquierdo
            nodo.hijoizq = self._Eliminar(nodo.hijoizq, clave)
        elif clave > nodo.valor: #Si la clave es mayor, se busca en el subarbol derecho
            nodo.hijoder = self._Eliminar(nodo.hijoder, clave)
        else: #Nodo con la clave encontrada
            #Nodo con un solo hijo o sin hijos
            if nodo.hijoizq is None: 
                return nodo.hijoder
            elif nodo.hijoder is None:
                return nodo.hijoizq
            #Nodo con dos hijos: Obtener el sucesor inorder (el mas pequeño en el subarbol derecho)
            MinD= self.Minimo(nodo.hijoder)
            nodo.valor= MinD.valor
            nodo.hijoder= self._Eliminar(nodo.hijoder, MinD.valor)
        #Actualizar la altura del nodo ancestro
        nodo.altura = 1 + max(self.obtener_altura(nodo.hijoizq), self.obtener_altura(nodo.hijoder))
        balance= self.obtenerFactor_balance(nodo)
        #Si el nodo se desbalancea, hay 4 casos
        #Caso Izquierda Izquierda
        if balance > 1 and self.obtenerFactor_balance(nodo.hijoizq) >= 0:
            return self.rotacionDerecha(nodo)           
        #Caso Derecha Derecha
        if balance < -1 and self.obtenerFactor_balance(nodo.hijoder) <= 0:
            return self.rotacionIzquierda(nodo)
        #Caso Izquierda Derecha
        if balance > 1 and self.obtenerFactor_balance(nodo.hijoizq) < 0:
            return self.rotacionDobleIzquierda_Derecha(nodo)
        #Caso Derecha Izquierda
        if balance < -1 and self.obtenerFactor_balance(nodo.hijoder) > 0:
            return self.rotacionDobleDerecha_Izquierda(nodo)
        return nodo
    
    def Buscar_Iterativo(self, clave): #Busca un nodo en el arbol de forma iterativa
        actual = self.raiz
        while actual is not None:
            if clave == actual.valor: 
                return actual
            elif clave < actual.valor:
                actual = actual.hijoizq
            else:
                actual = actual.hijoder
        return None
    
    def Buscar_Recursivo(self, nodo, clave):  
        if nodo is None or nodo.valor==clave:
            return nodo
        if clave < nodo.valor: 
            return self.Buscar_Recursivo(nodo.hijoizq, clave )
        else:
            return self.Buscar_Recursivo(nodo.hijoder, clave)
        

#Recorridos----------------------------------------------------------------------------------------------------------------------------------------------
    #IN-ORDEN
    def Inorden_recursivo(self, nodo): #En Inorden Recursivo
        if nodo:
            self.Inorden_recursivo(nodo.hijoizq)
            print(nodo.valor, end=' ')
            self.Inorden_recursivo(nodo.hijoder)
            
            
            
    def Inorden_Iterativo(self): #Iterativo
        stack=[]
        actual= self.raiz
        while stack or actual:
            if actual:
             stack.append(actual)
             actual = actual.hijoizq
            else:
                actual = stack.pop()
                print (actual.valor, end=' ')
                actual = actual.hijoder 
                
     #PRE-ORDEN 
    def preorden_recursivo(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.preorden_recursivo(nodo.hijoizq)
            self.preorden_recursivo(nodo.hijoder) 
            
    def preorden_iterativo(self):
        if not self.raiz:
            return
        stack = [self.raiz]
        while stack:
            actual = stack.pop()
            print(actual.valor, end=' ')
            if actual.hijoder:
                stack.append(actual.hijoder)
            if actual.hijoizq:
                stack.append(actual.hijoizq)
                
     #POST-ORDEN 
    def postorden_recursivo(self, nodo):
        if nodo:
            self.postorden_recursivo(nodo.hijoizq)
            self.postorden_recursivo(nodo.hijoder)
            print(nodo.valor, end=' ') 
            
    def postorden_iterativo(self):
        if not self.raiz:
            return
        stack1 = [self.raiz]
        stack2 = []
        while stack1:
            actual = stack1.pop()
            stack2.append(actual)
            if actual.hijoizq:
                stack1.append(actual.hijoizq)
            if actual.hijoder:
                stack1.append(actual.hijoder)
        while stack2:
            print(stack2.pop().valor, end=' ')  
            
    #POR-NIVEL
    def recorrer_nivel(self, nodo, nivel):
        if nodo is None:
            return
        if nivel == 1:
            print(nodo.valor, end=' ')
        elif nivel > 1:
            self.recorrer_nivel(nodo.hijoizq, nivel - 1)
            self.recorrer_nivel(nodo.hijoder, nivel - 1)

    def recorrido_por_niveles_recursivo(self):
        altura = self.obtener_altura(self.raiz)
        for i in range(1, altura + 1):
            self.recorrer_nivel(self.raiz, i) 
            
    def recorrido_por_niveles_iterativo(self):
        if self.raiz is None:
            return

        from collections import deque
        cola = deque()
        cola.append(self.raiz)

        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual.valor, end=' ')
            if nodo_actual.hijoizq:
                cola.append(nodo_actual.hijoizq)
            if nodo_actual.hijoder:
                cola.append(nodo_actual.hijoder)
                
  
#Contar Nodo
def contar_Nodos(nodo):
        if not nodo:
            return 0
        return 1 + contar_Nodos(nodo.hijoizq) + contar_Nodos(nodo.hijoder)
                  

if __name__ == "__main__":
    avl= ArbolAVL()
    
    #Insertar y mostrar confirmacion
    valores=[50,30,70,20,10,40,35,100]
    print("--------Insertando Valores--------")
    for val in valores:
        avl.insertar(val)
        print(f"Insertado:{val}")
        
    print(f"Altura:{avl.obtener_altura(avl.raiz)}")
    print(f"Cantidad de hojas en el arbol:{avl.ContarHojas(avl.raiz)}")
    print(f"Cantidad de nodos:{contar_Nodos(avl.raiz)}")
    minimo=avl.Minimo(avl.raiz)
    maximo=avl.Maximo(avl.raiz)
    print(f"Nodo Minimo en el Arbol es:{minimo.valor}")
    print(f"Nodo Maximo en el Arbol es:{maximo.valor}")
    
    
     #Recorridos
    print("\n----Los recorridos-----")
    print("InOrden:", end=" ")
    avl.Inorden_recursivo(avl.raiz)
    print()
    print("PreOrden:", end=" ")
    avl.preorden_recursivo(avl.raiz)
    print()
    print("PostOrden:", end=" ")
    avl.postorden_recursivo(avl.raiz)
    print()
        
    #Eliminar
    print("\n\n------Eliminando datos------")
    valoreseliminados=[20,15,100]
    for val in valoreseliminados:
        nodo=avl.Buscar_Iterativo(val)
        if nodo:
            avl.Eliminar(val)
            print(f"Eliminado:{val}")
        else:
            print(f"No se encontro el valor:{val}")
            
    #Mostar el estado del Arbol
    print("\n\n-------Estado del Arbol, Despues de hacer los cambios anteriores-----")
    print(f"Esta Balanceado?:{avl.EsArbolVL(avl.raiz)}")
    print(f"Altura:{avl.obtener_altura(avl.raiz)}")
    print(f"Cantidad de hojas en el arbol:{avl.ContarHojas(avl.raiz)}")
    print(f"Cantidad de Nodos:{contar_Nodos(avl.raiz)}")
    minimo=avl.Minimo(avl.raiz)
    maximo=avl.Maximo(avl.raiz)
    print(f"Nodo Minimo en el Arbol es:{minimo.valor}")
    print(f"Nodo Maximo en el Arbol es:{maximo.valor}")
    
    #Recorridos
    print("\n----Los recorridos-----")
    print("InOrden:", end=" ")
    avl.Inorden_recursivo(avl.raiz)
    print()
    print("PreOrden:", end=" ")
    avl.preorden_recursivo(avl.raiz)
    print()
    print("PostOrden:", end=" ")
    avl.postorden_recursivo(avl.raiz)
    
           
            
        
        
        
             
        
            
    
    