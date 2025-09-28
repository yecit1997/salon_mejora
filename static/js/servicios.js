// ===== FUNCIONALIDADES PARA LA PÁGINA DE SERVICIOS =====

document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    const minPriceInput = document.getElementById('minPrice');
    const maxPriceInput = document.getElementById('maxPrice');
    const sortBySelect = document.getElementById('sortBy');
    const clearFiltersBtn = document.getElementById('clearFilters');
    const clearFiltersBtnAlt = document.getElementById('clearFiltersBtn');
    const gridViewBtn = document.getElementById('gridView');
    const listViewBtn = document.getElementById('listView');
    const servicesGrid = document.getElementById('servicesGrid');
    const resultsCount = document.getElementById('resultsCount');
    
    // Estado de filtros
    let currentFilters = {
        search: '',
        category: '',
        minPrice: '',
        maxPrice: '',
        sortBy: 'nombre'
    };
    
    // Aplicar filtros
    function applyFilters() {
        const serviceItems = document.querySelectorAll('.service-item');
        let visibleCount = 0;
        
        serviceItems.forEach(item => {
            const name = item.dataset.name || '';
            const category = item.dataset.category || '';
            const price = parseFloat(item.dataset.price) || 0;
            
            let isVisible = true;
            
            // Filtro de búsqueda
            if (currentFilters.search && !name.includes(currentFilters.search.toLowerCase())) {
                isVisible = false;
            }
            
            // Filtro de categoría
            if (currentFilters.category && category !== currentFilters.category) {
                isVisible = false;
            }
            
            // Filtro de precio mínimo
            if (currentFilters.minPrice && price < parseFloat(currentFilters.minPrice)) {
                isVisible = false;
            }
            
            // Filtro de precio máximo
            if (currentFilters.maxPrice && price > parseFloat(currentFilters.maxPrice)) {
                isVisible = false;
            }
            
            // Mostrar/ocultar elemento
            if (isVisible) {
                item.style.display = 'block';
                item.classList.add('fade-in-up');
                visibleCount++;
            } else {
                item.style.display = 'none';
                item.classList.remove('fade-in-up');
            }
        });
        
        // Actualizar contador
        if (resultsCount) {
            resultsCount.textContent = visibleCount;
        }
        
        // Mostrar mensaje si no hay resultados
        showNoResultsMessage(visibleCount === 0);
        
        // Aplicar ordenamiento
        sortServices();
    }
    
    // Ordenar servicios
    function sortServices() {
        const container = servicesGrid;
        const items = Array.from(container.querySelectorAll('.service-item:not([style*="display: none"])'));
        
        items.sort((a, b) => {
            const nameA = a.dataset.name || '';
            const nameB = b.dataset.name || '';
            const priceA = parseFloat(a.dataset.price) || 0;
            const priceB = parseFloat(b.dataset.price) || 0;
            
            switch (currentFilters.sortBy) {
                case 'nombre':
                    return nameA.localeCompare(nameB);
                case 'precio_asc':
                    return priceA - priceB;
                case 'precio_desc':
                    return priceB - priceA;
                default:
                    return 0;
            }
        });
        
        // Reordenar elementos en el DOM
        items.forEach(item => container.appendChild(item));
    }
    
    // Mostrar mensaje de no resultados
    function showNoResultsMessage(show) {
        let noResultsDiv = document.getElementById('noResultsMessage');
        
        if (show && !noResultsDiv) {
            noResultsDiv = document.createElement('div');
            noResultsDiv.id = 'noResultsMessage';
            noResultsDiv.className = 'col-12';
            noResultsDiv.innerHTML = `
                <div class="no-results">
                    <i class="bi bi-search"></i>
                    <h3>No se encontraron servicios</h3>
                    <p>No hay servicios que coincidan con los filtros seleccionados. Intenta ajustar los criterios de búsqueda.</p>
                    <button class="btn btn-primary" onclick="clearAllFilters()">
                        <i class="bi bi-arrow-clockwise me-2"></i>Limpiar Filtros
                    </button>
                </div>
            `;
            servicesGrid.appendChild(noResultsDiv);
        } else if (!show && noResultsDiv) {
            noResultsDiv.remove();
        }
    }
    
    // Limpiar todos los filtros
    function clearAllFilters() {
        currentFilters = {
            search: '',
            category: '',
            minPrice: '',
            maxPrice: '',
            sortBy: 'nombre'
        };
        
        // Limpiar inputs
        if (searchInput) searchInput.value = '';
        if (categoryFilter) categoryFilter.value = '';
        if (minPriceInput) minPriceInput.value = '';
        if (maxPriceInput) maxPriceInput.value = '';
        if (sortBySelect) sortBySelect.value = 'nombre';
        
        applyFilters();
    }
    
    // Cambiar vista (grid/list)
    function toggleView(view) {
        const serviceItems = document.querySelectorAll('.service-item');
        
        if (view === 'list') {
            servicesGrid.classList.add('list-view');
            gridViewBtn.classList.remove('active');
            listViewBtn.classList.add('active');
        } else {
            servicesGrid.classList.remove('list-view');
            gridViewBtn.classList.add('active');
            listViewBtn.classList.remove('active');
        }
        
        // Aplicar animación
        serviceItems.forEach((item, index) => {
            setTimeout(() => {
                item.classList.add('fade-in-up');
            }, index * 50);
        });
    }
    
    // Event Listeners
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            currentFilters.search = this.value.toLowerCase();
            applyFilters();
        });
    }
    
    if (categoryFilter) {
        categoryFilter.addEventListener('change', function() {
            currentFilters.category = this.value;
            applyFilters();
        });
    }
    
    if (minPriceInput) {
        minPriceInput.addEventListener('input', function() {
            currentFilters.minPrice = this.value;
            applyFilters();
        });
    }
    
    if (maxPriceInput) {
        maxPriceInput.addEventListener('input', function() {
            currentFilters.maxPrice = this.value;
            applyFilters();
        });
    }
    
    if (sortBySelect) {
        sortBySelect.addEventListener('change', function() {
            currentFilters.sortBy = this.value;
            applyFilters();
        });
    }
    
    if (clearFiltersBtn) {
        clearFiltersBtn.addEventListener('click', clearAllFilters);
    }
    
    if (clearFiltersBtnAlt) {
        clearFiltersBtnAlt.addEventListener('click', clearAllFilters);
    }
    
    if (gridViewBtn) {
        gridViewBtn.addEventListener('click', function() {
            toggleView('grid');
        });
    }
    
    if (listViewBtn) {
        listViewBtn.addEventListener('click', function() {
            toggleView('list');
        });
    }
    
    // Validación de precios
    if (minPriceInput && maxPriceInput) {
        function validatePriceRange() {
            const minPrice = parseFloat(minPriceInput.value);
            const maxPrice = parseFloat(maxPriceInput.value);
            
            if (minPrice && maxPrice && minPrice > maxPrice) {
                maxPriceInput.setCustomValidity('El precio máximo debe ser mayor al precio mínimo');
            } else {
                maxPriceInput.setCustomValidity('');
            }
        }
        
        minPriceInput.addEventListener('input', validatePriceRange);
        maxPriceInput.addEventListener('input', validatePriceRange);
    }
    
    // Animación de entrada para elementos
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);
    
    // Observar tarjetas de servicios
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(function(card) {
        observer.observe(card);
    });
    
    // Efecto hover mejorado para tarjetas
    serviceCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Cargar filtros desde URL (si existen)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('search')) {
        currentFilters.search = urlParams.get('search').toLowerCase();
        if (searchInput) searchInput.value = urlParams.get('search');
    }
    if (urlParams.get('category')) {
        currentFilters.category = urlParams.get('category');
        if (categoryFilter) categoryFilter.value = urlParams.get('category');
    }
    
    // Aplicar filtros iniciales
    applyFilters();
});

// Función global para limpiar filtros (llamada desde el template)
function clearAllFilters() {
    const event = new Event('click');
    const clearBtn = document.getElementById('clearFilters') || document.getElementById('clearFiltersBtn');
    if (clearBtn) {
        clearBtn.dispatchEvent(event);
    }
}
