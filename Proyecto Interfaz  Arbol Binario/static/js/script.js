// script.js - Árbol Binario Interactivo - VERSIÓN CORREGIDA
console.log("✅ script.js cargado correctamente");

// Configuración global
const CONFIG = {
    colors: {
        node: "#4CAF50",
        highlight: "#FFD700",
        link: "#ccc",
        text: "white"
    },
    animations: {
        duration: 500
    },
    messages: {
        duration: 3000
    }
};

// Esperar a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    console.log("🎯 DOM completamente cargado y listo");
    
    // Verificar que los elementos existen
    const elementsToCheck = [
        'insertForm', 'insertValue', 'deleteForm', 'deleteValue',
        'searchForm', 'searchValue', 'clearTree', 'loadExample',
        'showTraversals', 'showInfo'
    ];
    
    elementsToCheck.forEach(id => {
        console.log(`🔍 ${id}:`, document.getElementById(id));
    });
    
    initializeEventListeners();
    // Cargar información inicial del árbol
    updateTreeInfo();
});

function initializeEventListeners() {
    console.log("🔧 Inicializando event listeners...");
    
    // Mapeo de formularios y sus configuraciones
    const formConfigs = [
        {
            formId: 'insertForm',
            valueId: 'insertValue',
            endpoint: '/insertar',
            action: 'insertar'
        },
        {
            formId: 'deleteForm',
            valueId: 'deleteValue',
            endpoint: '/eliminar',
            action: 'eliminar'
        },
        {
            formId: 'searchForm',
            valueId: 'searchValue',
            endpoint: '/buscar',
            action: 'buscar'
        }
    ];

    // Configurar formularios de manera dinámica
    formConfigs.forEach(config => {
        const form = document.getElementById(config.formId);
        if (!form) {
            console.error(`❌ Formulario ${config.formId} no encontrado`);
            return;
        }

        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            
            const valueInput = document.getElementById(config.valueId);
            const valor = valueInput.value.trim();
            
            if (!validateInput(valor)) {
                showMessage("⚠ Ingresa un número válido", "error");
                return;
            }

            await handleFormSubmit(config.endpoint, config.action, valor, form);
            form.reset();
        });
    });

    // Limpiar árbol
    document.getElementById("clearTree").addEventListener("click", async () => {
        if (confirm("¿Estás seguro de que quieres limpiar el árbol?")) {
            try {
                const res = await fetch("/limpiar", { method: "POST" });
                const data = await res.json();

                if (data.success) {
                    showMessage("🧹 Árbol limpiado correctamente", "success");
                    updateTreeData(data);
                } else {
                    showMessage(`⚠ ${data.mensaje}`, "error");
                }
            } catch (error) {
                showMessage("❌ Error de conexión", "error");
            }
        }
    });

    // Cargar ejemplo
    document.getElementById("loadExample").addEventListener("click", async () => {
        if (confirm("¿Cargar ejemplo? Se perderán los datos actuales.")) {
            try {
                const res = await fetch("/cargar_ejemplo", { method: "POST" });
                const data = await res.json();

                if (data.success) {
                    showMessage("📥 Ejemplo cargado correctamente", "success");
                    updateTreeData(data);
                } else {
                    showMessage(`⚠ ${data.mensaje}`, "error");
                }
            } catch (error) {
                showMessage("❌ Error de conexión", "error");
            }
        }
    });

    // Mostrar/ocultar recorridos
    document.getElementById("showTraversals").addEventListener("click", async () => {
        const section = document.getElementById("traversalsSection");
        
        if (section.style.display === "none" || !section.style.display) {
            try {
                const response = await fetch('/recorridos');
                const data = await response.json();
                
                if (data.success) {
                    document.getElementById("preorder").textContent = data.preorden ? data.preorden.join(" → ") : "Vacío";
                    document.getElementById("inorder").textContent = data.inorden ? data.inorden.join(" → ") : "Vacío";
                    document.getElementById("postorder").textContent = data.postorden ? data.postorden.join(" → ") : "Vacío";
                    
                    section.style.display = "block";
                    showMessage("📊 Recorridos actualizados", "info");
                } else {
                    showMessage("⚠ No se pudieron cargar los recorridos", "error");
                }
            } catch (error) {
                console.error('❌ Error al obtener recorridos:', error);
                showMessage("❌ Error al cargar recorridos", "error");
            }
        } else {
            section.style.display = "none";
        }
    });

    // Información
    document.getElementById("showInfo").addEventListener("click", () => {
        alert("ℹ Proyecto Árbol Binario\n\nOperaciones disponibles:\n• Insertar nodos\n• Eliminar nodos\n• Buscar nodos\n• Ver recorridos (Preorden, Inorden, Postorden)\n• Limpiar árbol\n• Cargar ejemplo\n\nUsa los botones para interactuar con el árbol.");
    });
}

// Función para validar entrada
function validateInput(value) {
    return value && !isNaN(value) && value.trim() !== '';
}

// Función para manejar envío de formularios
async function handleFormSubmit(endpoint, action, value, form) {
    try {
        const formData = new FormData(form);
        
        const res = await fetch(endpoint, {
            method: "POST",
            body: formData
        });
        
        const data = await res.json();

        if (data.success) {
            if (action === 'buscar') {
                if (data.encontrado) {
                    showMessage(`✅ Nodo ${value} encontrado correctamente`, "success");
                    highlightNode(value);
                } else {
                    showMessage(`⚠ Nodo ${value} NO encontrado en el árbol`, "error");
                }
            } else {
                const actionMessages = {
                    'insertar': 'insertado',
                    'eliminar': 'eliminado'
                };
                showMessage(`✅ Nodo ${value} ${actionMessages[action]} correctamente`, "success");
            }

            if (data.estructura) {
                updateTreeVisualization(data.estructura);
            }

            await updateTreeInfo();
        } else {
            showMessage(`⚠ ${data.mensaje}`, "error");
        }
    } catch (error) {
        console.error(`❌ Error en ${action}:`, error);
        showMessage("❌ Error de conexión", "error");
    }
}

// Función para mostrar mensajes
function showMessage(msg, type = "info") {
    const messageArea = document.getElementById("messageArea");
    messageArea.textContent = msg;
    messageArea.className = `message-area ${type}`;
    
    setTimeout(() => {
        messageArea.textContent = "";
        messageArea.className = "message-area";
    }, CONFIG.messages.duration);
}

// Función para actualizar datos del árbol
function updateTreeData(data) {
    // Actualizar información básica
    document.getElementById("nodosCount").textContent = data.cantidad_nodos || 0;
    document.getElementById("alturaTree").textContent = data.altura || 0;
    document.getElementById("estadoTree").textContent = data.vacio ? "Vacío" : "Con elementos";
    
    //Actualizar texto de la seccion "Estructura del Arbol"
    const estructuraTexto= document.getElementById("estructuraTexto");
    if(estructuraTexto){
        if(data.vacio){
           estructuraTexto.textContent= "Arbol Vacio";
        }else{
            estructuraTexto.textContent= "Arbol con elementos";
        }
    } 
    
    // Actualizar visualización D3 si existe estructura
    if (data.estructura) {
        updateTreeVisualization(data.estructura);
    }else{
        d3.select("#tree").selectAll("*").remove();
    }
}

// Función para visualizar el árbol con D3 
function updateTreeVisualization(treeData) {
    console.log("🌳 Actualizando visualización del árbol:", treeData);
    
    // Limpia el SVG anterior
    d3.select("#tree").selectAll("*").remove();

    // Obtener dimensiones del contenedor
    const treeContainer = document.getElementById("tree");
    const containerWidth = treeContainer.clientWidth;
    const containerHeight = treeContainer.clientHeight;

    // Crear SVG principal
    const svg = d3.select("#tree")
        .append("svg")
        .attr("width", containerWidth)
        .attr("height", containerHeight)
        .append("g")
        .attr("transform", "translate(50,50)");

    // Crear jerarquía
    const root = d3.hierarchy(treeData);

    // Configurar layout del árbol (vertical: ancho en X, altura en Y)
    const treeLayout = d3.tree()
        .size([containerWidth - 100, containerHeight - 100]);

    treeLayout(root);

    // Dibujar las líneas (verticales)
    svg.selectAll(".link")
        .data(root.links())
        .enter()
        .append("path")
        .attr("class", "link")
        .attr("d", d3.linkVertical()
            .x(d => d.x)  // X → horizontal
            .y(d => d.y)  // Y → vertical (profundidad)
        )
        .attr("fill", "none")
        .attr("stroke", CONFIG.colors.link)
        .attr("stroke-width", 2);

    // Dibujar los nodos
    const node = svg.selectAll(".node")
        .data(root.descendants())
        .enter()
        .append("g")
        .attr("class", "node")
        .attr("transform", d => `translate(${d.x},${d.y})`);

    // Círculos
    node.append("circle")
        .attr("r", 15)
        .attr("fill", CONFIG.colors.node)
        .attr("stroke", "#fff")
        .attr("stroke-width", 2);

    // Texto dentro del nodo
    node.append("text")
        .attr("dy", "0.35em")
        .attr("text-anchor", "middle")
        .attr("fill", CONFIG.colors.text)
        .style("font-size", "12px")
        .style("font-weight", "bold")
        .style("font-family", "Courier New, monospace")
        .text(d => d.data.name);

    console.log("✅ Visualización vertical lista");
}

// Función para resaltar nodos durante búsqueda
function highlightNode(value) {
    // Remover highlight anterior
    d3.selectAll(".node").classed("highlighted", false);
    d3.selectAll("circle").attr("fill", CONFIG.colors.node);

    // Aplicar highlight al nodo encontrado
    d3.selectAll(".node")
        .filter(d => d.data.name == value)
        .classed("highlighted", true)
        .select("circle")
        .attr("fill", CONFIG.colors.highlight);
}

// Función para actualizar toda la información del árbol
async function updateTreeInfo() {
    try {
        const response = await fetch('/informacion');
        const data = await response.json();
        
        if (data.success) {
            updateTreeData(data);
        }
    } catch (error) {
        console.error('Error al actualizar información:', error);
    }
}

// Manejar redimensionamiento de ventana
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(async () => {
        await updateTreeInfo();
    }, 250);
});
