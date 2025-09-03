from ClaseNodo import ClaseNodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    #-----------------------------------------------------------------------------------------------   
    # METODO INSERTAR NODO (X)
    #Recursivo
    def insertar(self, valor):
        self.raiz = self._insertarRecursivo(self.raiz, valor)

    def _insertarRecursivo(self, raizAux, valor):
        #Caso Base
        if raizAux is None:
            raizAux = ClaseNodo(valor)
            return raizAux
        #CasoGeneral
        else:
            if valor < raizAux.obtener_valor():
                raizAux.hijoIzquierdo = self._insertarRecursivo(raizAux.hijoIzquierdo, valor)
            else:
                raizAux.hijoDerecho = self._insertarRecursivo(raizAux.hijoDerecho, valor)
            return raizAux

    #Iterativo
    def insertar_Nodo(self, valor):
        nuevo_nodo = ClaseNodo(valor)  #Crea una nueva instancia de ClaseNodo con el valor que se quiere insertar
        if self.isVacio():
            self.raiz = nuevo_nodo     #Si el arbol esta vacio, el nuevo nodo se convierte en la raiz arbol 
            return 
        nodo_actual = self.raiz  #comienza en la raiz del arbol
        nodo_Padre = None        #almacenara el nodo anterior al nodo_Padre(=0)
        while nodo_actual is not None: #Mientras el NodoActual no llegue a None(finaal del camino)
            nodo_Padre = nodo_actual    #Guardamos el nodo actual como padre
            if valor < nodo_actual.obtener_valor(): #Si el valor a insertar es menor que el valor del ndodo actual
                nodo_actual = nodo_actual.hijoIzquierdo
            else:
                nodo_actual = nodo_actual.hijoDerecho
        #Una vez que se sale del bucle, se ha encontrado la posicion correcta para insertar el nuevo nodo         
        if valor < nodo_Padre.obtener_valor(): #Compara el valor con el nodoPadre 
            nodo_Padre.setHijoIzquierdo(nuevo_nodo)
        else:
            nodo_Padre.setHijoDerecho(nuevo_nodo)
#-------------------------------------------------------------------------------------------------------------------
    #METODO BUSCAR NODO(X) 
    #Recursivo
    def Buscar_x_Recursivo(self, valor):
        return self._BuscarRecursivo(self.raiz, valor)

    def _BuscarRecursivo(self, nodoActual, valor):
        # 1er Caso Base
        if nodoActual is None:
            return None
        # 2do Caso Base
        if valor == nodoActual.obtener_valor():
            return nodoActual
        #Caso General
        if valor < nodoActual.obtener_valor():
            return self._BuscarRecursivo(nodoActual.hijoIzquierdo, valor)
        else:
            return self._BuscarRecursivo(nodoActual.hijoDerecho, valor) 

    #Iterativo 
    def BuscarIterativo(self, valor):
        nodoActual = self.raiz #Apunta al nodo raiz
        while nodoActual is not None: #Mientras el nodo actual no sea None(0)
            if valor == nodoActual.obtener_valor(): #Compara el valor con el nodo actual
                return nodoActual #Si son iguales, retorna el nodo actual
            elif valor < nodoActual.obtener_valor(): #Si el valor es menor que el nodo actual
                nodoActual = nodoActual.hijoIzquierdo #Mueve el nodo actual al hijo izquierdo
            else:
                nodoActual = nodoActual.hijoDerecho #Mueve el nodo actual al hijo derecho
        return None #Si no se encuentra el valor, retorna None

#-------------------------------------------------------------------------------------------------------------------               
    #METODO VERIFICAR SI UN NODO ES HOJA(para ver si un nodo tiene hijos o no)
    #Recursivo
    def EsHoja_Recursivo(self, valor):
        nodo = self._BuscarRecursivo(self.raiz, valor)
        return nodo.eshoja() if nodo else False

    #Iterativo
    def EsHoja_Iterativo(self, valor):
        nodo = self.BuscarIterativo(valor)
        return nodo.eshoja() if nodo else False     

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
        hi = self._Contar_Nodos_Pares_Recursivo(raizAux.hijoIzquierdo) 
        hd = self._Contar_Nodos_Pares_Recursivo(raizAux.hijoDerecho) 
        if raizAux.obtener_valor() % 2 == 0:
            return hi + hd + 1
        else:
            return hi + hd 

#-------------------------------------------------------------------------------------------------------------------
#-------------------------RECORRIDOS DEL ARBOL---------------------------------------------------
# INORDEN (Izquierda, Raiz, Derecha)
# Recursivo 
    def InOrdenRecursivo(self):
        resultado = []
        self._InOrden_Recursivo(self.raiz, resultado)
        return resultado 

    #Private
    def _InOrden_Recursivo(self, nodoActual, resultado):
        if nodoActual is not None:
            self._InOrden_Recursivo(nodoActual.hijoIzquierdo, resultado)
            resultado.append(nodoActual.obtener_valor())
            self._InOrden_Recursivo(nodoActual.hijoDerecho, resultado)

    #Iterativo
    def InOrdenIterativo(self): #Un recorrido usando una pila para almacenar nodos
        resultado = [] #lista para almacenar los valores en orden 
        pila = [] #pila para controlar el reorrido del arbol 
        nodoActual = self.raiz #Comienza en la raiz del arbol 
        while pila or nodoActual is not None: #Mientras haya nodos en la pila o el nodo actual no sea None
            while nodoActual is not None: #Explora el subArbol Izquierdo
                pila.append(nodoActual) #Se guarda el nodoActual en la pila antes de ir al hijo izquierdo
                nodoActual = nodoActual.hijoIzquierdo #Mueve el nodo actual al hijo izquierdo
            nodoActual = pila.pop() #Una vez que llega al final de la rama izquierda, se saca un nodo de la pila para procesarlo
            resultado.append(nodoActual.obtener_valor()) #Se agrega el valor del nodo actual a la lista resultado
            nodoActual = nodoActual.hijoDerecho #luego de procesar el nodo izquierdo, se mueve al subArbol derecho   
        return resultado # Retorna la lista de valores en orden

#---------------------------------------------------------------------------------------------------------------------------------------
# PREORDEN (Raiz, Izquierda, Derecha)  
#Recursivo
    def PreOrdenRecursivo(self):
        resultado =[]
        self._PreOrden_Recursivo(self.raiz, resultado)
        return resultado 
    
    #Private
    def _PreOrden_Recursivo(self, nodoActual, resultado):
        if nodoActual is not None:
            resultado.append(nodoActual.obtener_valor())
            self._PreOrden_Recursivo(nodoActual.hijoIzquierdo, resultado)
            self._PreOrden_Recursivo(nodoActual.hijoDerecho, resultado)
            
    #Iterativo
    def PreOrdenIterativo(self):
        if self.isVacio(): #Si el arbol esta vacio, no hay nada que recorrer
            return [] #Devuelve la lista vacia 
        resultado= [] #Lista donde se guardara el recorrido final
        pila= [self.raiz] #se inicia la pila con la raiz del arbol 
        while pila: #Mientras haya nodos por procesar 
            nodoActual= pila.pop() #Saca el ultimo nodo agregado a la pila 
            resultado.append(nodoActual.obtener_valor()) #Procesa el nodoActual, agrega su valor al resultado
            #Se agregan los hijos en orden: primero derecho, luego izquierdo
            #Asi el izquierdo sera procesado antes o primero(porque se almacena en una pila)
            if nodoActual.hijoDerecho is not None: #Si tiene hijo derecho
                pila.append(nodoActual.hijoDerecho) #agrega a la pila 
            if nodoActual.hijoIzquierdo is not None: #Si tiene hijo izquierdo
                pila.append(nodoActual.hijoIzquierdo) #agrega a la pila 
        return resultado #Retorna la lista con el recorrido en preorden
#---------------------------------------------------------------------------------------------------------------------------------------
# POSTORDEN (Izquierda, Derecha, Raiz)
#Recursivo
    def PostOrdenRecursivo(self):
        resultado = []
        self._PostOrden_Recursivo(self.raiz, resultado)
        return resultado 

    #Private
    def _PostOrden_Recursivo(self, nodoActual, resultado):
        if nodoActual is not None:
            self._PostOrden_Recursivo(nodoActual.hijoIzquierdo, resultado)
            self._PostOrden_Recursivo(nodoActual.hijoDerecho, resultado)
            resultado.append(nodoActual.obtener_valor())

    #Iterativo
    def PostOrdenIterativo(self):
        if self.isVacio(): #Si el arbol esta vacio, no hay nada que recorrer
            return [] #Devuelve la lista vacia 
        resultado = [] #Lista donde se guardara el recorrido final
        pila1 = [self.raiz] #Pila para controlar el recorrido del arbol 
        pila2 = [] #Pila auxiliar para almacenar los nodos en orden inverso
        while pila1: #Mientras haya nodos por procesar en la pila1
            nodoActual = pila1.pop() #Saca el ultimo nodo agregado a la pila1
            pila2.append(nodoActual) #Agrega el nodo actual a la pila2 (almacena en orden inverso)
            #En post-Orden se recorre izquierda -> derecha ->raiz
            #Pero aqui se almacena en orden : raiz -> derecha -> izquierda
            #Luego se invierte usando la pila2            
            if nodoActual.hijoIzquierdo is not None: #Si tiene hijo izquierdo
                pila1.append(nodoActual.hijoIzquierdo) #agrega a la pila1 
            if nodoActual.hijoDerecho is not None: #Si tiene hijo derecho
                pila1.append(nodoActual.hijoDerecho) #agrega a la pila1 
        while pila2: #Ahora se vacia pila2 para obtener el orden correcto de postorden
            nodo = pila2.pop() #Saca los nodos de la pila2 (en orden correcto de postorden)
            resultado.append(nodo.obtener_valor()) #Agrega el valor del nodo al resultado
        return resultado #Retorna la lista con el recorrido en postorden
    
#------------------------------------------------------------------------------------------------------------------        
    # Verifica si el arbol esta vacio        
    def isVacio(self):
        return self.raiz is None

#------------------------------------------------------------------------------------------------------------------
   #ALTURA DEL ARBOL
   # Recursivo 
    def Altura(self):
        return self._Altura_Recursivo(self.raiz)
    
    def _Altura_Recursivo(self, nodoActual):
        if nodoActual is None:
            return -1 #Si el nodo es None, retorna -1 (altura de un arbol vacio)
        izquierda= self._Altura_Recursivo(nodoActual.hijoIzquierdo)
        derecha= self._Altura_Recursivo(nodoActual.hijoDerecho)
        return 1 + max(izquierda, derecha)
    
    #Iterativo
    def Altura_Iterativo(self):
        if self.isVacio(): #Si el arbol esta vacio, no tiene altura
            return 0 #Devuelve 0
        Contaltura= -1 #Contador de niveles de altura
        cola=[self.raiz] #Cola para almacenar los nodos por nivel BFS(Busqueda en anchura)
        while cola: #Mientras haya nodos en la cola
            nivelTamano= len (cola) #Numero de nodos en el nivel actual
            for _ in range(nivelTamano): #Procesa todos los nodos en el nivel actual
                nodo= cola.pop(0) #Saca el primer nodo de la cola
                if nodo.hijoIzquierdo is not None: #Si tiene hijo izquierdo
                    cola.append(nodo.hijoIzquierdo) #Lo agrega a la cola 
                if nodo.hijoDerecho is not None: #Si tiene hijo derecho
                    cola.append(nodo.hijoDerecho) #Lo agrega a la cola
            Contaltura += 1 #Incrementa 1 en 1 la altura despues de procesar un nivel completo
        return Contaltura #Retorna la altura total del arbol
        
#--------------------------------------------------------------------------------------------------------------------------
 #Amplitud del Arbol (Numero maximo de nodos en cualquier nivel del arbol)
  #Recursivo
    def _Amplitud_Recursivo(self):
        Niveles= []
        altura= self.Altura()
        for nivelTam in range(altura + 1):
            Nodo_nivel= []
            self._Recorrido_Nivel(self.raiz,nivelTam, Nodo_nivel)
            Niveles.append(len(Nodo_nivel))
        return max(Niveles) if Niveles else 0
    
    def _Recorrido_Nivel(self, nodoActual, nivel, resultado):
        if nodoActual is None:
            return 
        if nivel==0:
            resultado.append(nodoActual.obtener_valor())
        else:
            self._Recorrido_Nivel(nodoActual.hijoIzquierdo, nivel -1, resultado)
            self._Recorrido_Nivel(nodoActual.hijoDerecho, nivel -1, resultado)    
  
  #Iterativo
    def Amplitud_Iterativo(self):
        if self.isVacio():
            return 0
        max_amplitud= 0 #Variable para guardar el maximo de nodos en cualquier nivel     
        cola = [self.raiz] #Cola para almacenar los nodos por nivel BFS(Busqueda en anchura)
        while cola: #Mientras haya nodos por nivel en la cola
            nivelTamano = len(cola) #NUmero de nodos en el nivel actual
            if nivelTamano > max_amplitud: #Si este nivel tiene mas nodos que el max_amplitud 
                max_amplitud = nivelTamano #Actualiza el max_amplitud
            for _ in range(nivelTamano): #Procesa todos los nodos en el nivel actual
               nodo= cola.pop(0) #Saca el primer nodo de la cola
               if nodo.hijoIzquierdo is not None: #Si tiene hijo izquierdo
                   cola.append(nodo.hijoIzquierdo) #Lo agrega a la cola
               if nodo.hijoDerecho is not None: #Si tiene hijo derecho
                    cola.append(nodo.hijoDerecho) #Lo agrega a la cola
        return max_amplitud #Retorna la amplitud maxima del arbol
                                           
#-----------------------------------------------------------------------------------------------------------------
# Muestra el arbol en General
if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(50)
    arbol1.insertar(150)
    arbol1.insertar(25)
    arbol1.insertar(75)
    arbol1.insertar(125)
    arbol1.insertar(175)
         
    print("Cantidad de Nodos en el Arbol:", arbol1.ContarNodos())
    print("Cantidad de Nodos Pares:", arbol1.Contar_Nodos_Pares())
    #prueba de Insetar_Nodo
    arbol1.insertar_Nodo(60)
    print("Cantidad de Nodos en el Arbol despues de insertar 60:", arbol1.ContarNodos())
    #Prueba de Esvacio
    print("El arbol esta vacio?", arbol1.isVacio())
    #Prueba de EsHoja
    print("El nodo 25 es hoja?", arbol1.EsHoja_Recursivo(25))
    print("El nodo 50 es hoja?", arbol1.EsHoja_Iterativo(50))
    #Prueba de Buscar
    print("El valor 75 existe en el arbol?", arbol1.Buscar_x_Recursivo(75) is not None)
    print("El valor 200 existe en el arbol?", arbol1.BuscarIterativo(200) is not None)
    #Prueba de los Recorridos
    print("Recorrido InOrden Recursivo:", arbol1.InOrdenRecursivo())
    print("Recorrido InOrden Iterativo:", arbol1.InOrdenIterativo())
    print("Recorrido PreOrden Recursivo:", arbol1.PreOrdenRecursivo())
    print("Recorrido PreOrden Iterativo:", arbol1.PreOrdenIterativo())
    print("Recorrido PostOrden Recursivo:", arbol1.PostOrdenRecursivo())
    print("Recorrido PostOrden Iterativo:", arbol1.PostOrdenIterativo())
    #Prueba de Altura
    print("Altura del Arbol (Recursivo):", arbol1.Altura())
    print("Altura del Arbol (Iterativo):", arbol1.Altura_Iterativo())
    #Prueba de Amplitud
    print("Amplitud del Arbol (Recursivo):", arbol1._Amplitud_Recursivo())
    print("Amplitud del Arbol (Iterativo):", arbol1.Amplitud_Iterativo())