// balance/static/js/balance.js

// Espera a que el DOM esté completamente cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    const contenidoDinamico = document.getElementById('contenido-dinamico');

    // **IMPORTANTE:** Accede a las URLs definidas en la plantilla (balance_home.html).
    // window.urlsBalance es el objeto que creamos en la plantilla.
    const urls = urlsBalance || {}; 

    // Función genérica para cargar contenido de una URL específica
    function cargarContenido(url) {
        if (!contenidoDinamico) {
            console.error('Error: El elemento #contenido-dinamico no se encontró en la página.');
            return;
        }
        if (!url) {
            console.warn('Advertencia: No se proporcionó una URL para cargar el contenido. Verifica la configuración.');
            contenidoDinamico.innerHTML = '<p class="text-muted">No hay URL configurada para esta opción.</p>';
            return;
        }

        // Muestra un mensaje de "Cargando..." mientras se espera la respuesta
        contenidoDinamico.innerHTML = '<p class="text-info">Cargando datos. Por favor, espera...</p>';

        fetch(url) // Realiza la petición GET a la URL proporcionada
            .then(response => {
                // Verifica si la respuesta HTTP es exitosa (código de estado 200-299)
                if (!response.ok) {
                    // Si hay un error HTTP (ej. 404, 500), lanza una excepción
                    throw new Error(`Error de red o servidor: ${response.status} - ${response.statusText}`);
                }
                return response.text(); // Devuelve el cuerpo de la respuesta como texto (HTML)
            })
            .then(html => {
                // Una vez que el HTML es recibido, lo inyecta en el contenedor dinámico
                contenidoDinamico.innerHTML = html;
            })
            .catch(error => {
                // Captura cualquier error durante la petición o procesamiento
                console.error('Error al cargar el contenido dinámico:', error);
                contenidoDinamico.innerHTML = `<p class="text-danger">Hubo un error al cargar los datos: ${error.message}. Por favor, inténtalo de nuevo.</p>`;
            });
    }

    // --- Configuración de Event Listeners para los Botones ---

    // Botón "Balance por Mes"
    const btnMostrarMes = document.getElementById('btn-mostrar-mes');
    if (btnMostrarMes) { // Asegúrate de que el botón exista antes de añadir el listener
        btnMostrarMes.addEventListener('click', function() {
            cargarContenido(urls.citasMesPartial); // Llama a la función con la URL del balance por mes
        });
    }

    // Botón "Balance por Día"
    const btnMostrarDia = document.getElementById('btn-mostrar-dia');
    if (btnMostrarDia) {
        btnMostrarDia.addEventListener('click', function() {
            cargarContenido(urls.citasDiaPartial); // Llama a la función con la URL del balance por día
        });
    }

    // Puedes replicar este patrón para los demás botones (hora, estilista, cliente, servicio)
    // Ejemplo:
    // const btnMostrarHora = document.getElementById('btn-mostrar-hora');
    // if (btnMostrarHora) {
    //     btnMostrarHora.addEventListener('click', function() {
    //         cargarContenido(urls.citasHoraPartial);
    //     });
    // }
    // ... y así sucesivamente

    // --- Carga de Contenido Predeterminado al Iniciar la Página ---
    // Esto hace que el primer gráfico (ej. citas por mes) se muestre automáticamente
    // cuando la página carga por primera vez, sin necesidad de un clic inicial.
    if (urls.citasMesPartial) { // Si la URL para citas por mes está definida
        cargarContenido(urls.citasMesPartial); // Carga el contenido por defecto
    }
});