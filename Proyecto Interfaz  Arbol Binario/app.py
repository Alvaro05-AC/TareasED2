from flask import Flask, render_template, request, jsonify, redirect, url_for
from ArbolBinario import ArbolBinario

app = Flask(__name__)

arbolizado = ArbolBinario()  #Instanciado la clase

@app.route('/')
def index():
    """Pagina Principal"""   #----------VERLO O TOCARLO FRONTEND-------
    return render_template('index.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    """Insertar un valor en el Arbol"""   #----------VERLO O TOCARLO FRONTEND-------
    print(" DEBUG: LLamada a /insertar recibida")
    try:
        valor= int(request.form['valor'])
        print(f"DEBUG: valor a insertar : {valor}")
        arbolizado.insertar(valor)
        print("DEBUG: Insercion completada en el arbol")
        return jsonify({
            'success': True,
            'mensaje':f'Valor {valor} insertado correctamente',
            'estructura': arbolizado.obtenerEstructuraD3(),
            'cantidad_nodos': arbolizado.ContarNodos()  
        }) 
    except Exception as e:
        print(f"DEBUG: Error {e}")
        return jsonify({'success': False, 'mensaje':f'Error{str(e)}'})  #----------VERLO O TOCARLO FRONTEND-------
    
@app.route('/eliminar', methods=['POST'])
def eliminar():
    """Eliminar un valor del Árbol"""
    try:
        valor = int(request.form['valor'])

        if arbolizado.Buscar_x_Recursivo(valor):
            arbolizado.eliminar_nodo(valor)
            return jsonify({
                'success': True,
                'mensaje': f'Valor {valor} eliminado correctamente',
                'estructura': arbolizado.obtenerEstructuraD3(),
                'cantidad_nodos': arbolizado.ContarNodos()
            })
        else:
            return jsonify({ 'success': False,'mensaje': f'El valor {valor} no existe en el árbol'}) #----------VERLO O TOCARLO FRONTEND-------
    except ValueError:
        return jsonify({ 'success': False,'mensaje': 'Por favor ingrese un número válido'}) #----------VERLO O TOCARLO FRONTEND-------
    except Exception as e:
        return jsonify({ 'success': False, 'mensaje': f'Error: {str(e)}'})
    
    
@app.route('/buscar',methods =['POST'])
def buscar():
    """Buscar un valor en el Arbol"""
    try:
        valor = int(request.form['valor'])
        nodo= arbolizado.Buscar_x_Recursivo(valor)
        encontrado= nodo is not None
        mensaje= f'El valor {valor} {"Si" if encontrado else "NO"} se encuentra en el Arbol'
        return jsonify({
            'success': True,
            'mensaje': mensaje,
             'encontrado': encontrado, 
             'estructura': arbolizado.obtenerEstructuraD3(),
             'cantidad_nodos': arbolizado.ContarNodos()       
        })
    except ValueError:
        return jsonify({'success': False,'mensaje': 'Por favor ingrese un número válido'}) #Verlo o revisar para el FRONTEND
    except Exception as e:
        return jsonify({'success': False,'mensaje': f'error{str(e)}'})
    
@app.route('/recorridos', methods= ['GET'])
def obtener_recorridos():
    """Obtener todos los recorridos del arbol"""
    try:
        if arbolizado.isVacio():
            return jsonify({
                'success': False,
                'mensaje':'El arbol esta vacio'
            })
        return jsonify({
            'success': True,
            'inorden': arbolizado.InOrdenRecursivo(),
            'preorden': arbolizado.PreOrdenRecursivo(),
            'postorden': arbolizado.PostOrdenRecursivo(),
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'error{str(e)}'})  #----------VERLO O TOCARLO FRONTEND-------


@app.route('/informacion', methods = ['GET'])
def obtener_informacion():
    """obtner informaciones sobre el Arbol"""
    try:
        return jsonify({
            'success': True,
            'cantidad_nodos': arbolizado.ContarNodos(),
            'altura':         arbolizado.Altura(),
            'vacio':          arbolizado.isVacio(),
            'estructura':     arbolizado.obtenerEstructuraD3(),
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'error{str(e)}'})  #----------VERLO O TOCARLO FRONTEND-------


@app.route('/limpiar', methods=['POST'])
def limpiar():
    """limpia el arbol binario"""
    try:
        arbolizado.limpiar_Arbol(),
        return jsonify({
           'success': True,
            'mensaje':         'Arbol limpiado correctamente',
            'estructura':       arbolizado.obtenerEstructuraD3(),
            'cantidad_nodos':0,
            'altura':0,
            'vacio':True
            
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})
    

@app.route('/cargar_ejemplo', methods=['POST'])
def cargar_ejemplo():
    """Carga un ejemplo predefinido"""
    try:
        arbolizado.limpiar_Arbol()
        valores_de_ejemplo=[100,200,150,45,50,500,350,250,180]
        for valor in valores_de_ejemplo:
            arbolizado.insertar(valor)
        return jsonify({
            'success': True,
            'mensaje':         'Ejemplo cargado correctamente',
            'estructura':       arbolizado.obtenerEstructuraD3(),
            'cantidad_nodos':arbolizado.ContarNodos(),
            'valores_insertados': valores_de_ejemplo,
            'altura':            arbolizado.Altura(),
            'vacio':             arbolizado.isVacio()
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})#----------VERLO O TOCARLO FRONTEND-------
    
    
@app.route('/obtener_arbol', methods=['GET'])
def obtener_arbol():
    try:
        return jsonify({
            "success": True,
            "arbol": arbolizado.a_diccionario()
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
