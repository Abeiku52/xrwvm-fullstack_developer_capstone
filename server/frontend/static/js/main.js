// Main JavaScript for Cars Dealership Application

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
});

async function initializeApp() {
    // Check if user is authenticated
    checkAuthStatus();
    
    // Load dealers
    await loadDealers();
    
    // Load car makes
    await loadCarMakes();
    
    // Set up event listeners
    setupEventListeners();
}

function checkAuthStatus() {
    // Check if user is logged in (simplified check)
    const sessionId = getCookie('sessionid');
    const authLink = document.getElementById('auth-link');
    
    if (sessionId) {
        // User is logged in
        authLink.innerHTML = '<a href="/logout/" class="nav-link">Logout</a>';
        // Show review options for dealers
        document.body.classList.add('user-authenticated');
    } else {
        // User is not logged in
        authLink.innerHTML = '<a href="/login/" class="nav-link">Login</a>';
        document.body.classList.remove('user-authenticated');
    }
}

async function loadDealers() {
    try {
        const response = await fetch('/api/dealers/');
        const dealers = await response.json();
        displayDealers(dealers);
    } catch (error) {
        console.error('Error loading dealers:', error);
        displayError('dealers-grid', 'Failed to load dealers');
    }
}

async function loadCarMakes() {
    try {
        const response = await fetch('/api/cars/');
        const carMakes = await response.json();
        displayCarMakes(carMakes);
    } catch (error) {
        console.error('Error loading car makes:', error);
        displayError('cars-grid', 'Failed to load car inventory');
    }
}

function displayDealers(dealers) {
    const dealersGrid = document.getElementById('dealers-grid');
    
    if (!dealers || dealers.length === 0) {
        dealersGrid.innerHTML = '<p class="no-results">No dealers found.</p>';
        return;
    }
    
    dealersGrid.innerHTML = dealers.map(dealer => `
        <div class="dealer-card" data-state="${dealer.state}">
            <div class="dealer-header">
                <h3>${dealer.name}</h3>
                <div class="dealer-id">ID: ${dealer.id}</div>
                <span class="dealer-location">${dealer.city}, ${dealer.state}</span>
            </div>
            <div class="dealer-info">
                <p><i class="fas fa-map-marker-alt"></i> ${dealer.address}</p>
                <p><i class="fas fa-mail-bulk"></i> ZIP: ${dealer.zip_code}</p>
                <p><i class="fas fa-phone"></i> ${dealer.phone}</p>
                <p><i class="fas fa-envelope"></i> ${dealer.email}</p>
            </div>
            <div class="dealer-actions">
                <a href="/dealer/${dealer.id}/" class="btn-primary">View Details</a>
                <div class="auth-only">
                    <a href="/dealer/${dealer.id}/review/" class="btn-secondary">Review Dealer</a>
                </div>
            </div>
        </div>
    `).join('');
}

function displayCarMakes(carMakes) {
    const carsGrid = document.getElementById('cars-grid');
    
    if (!carMakes || carMakes.length === 0) {
        carsGrid.innerHTML = '<p class="no-results">No car inventory found.</p>';
        return;
    }
    
    carsGrid.innerHTML = carMakes.map(make => `
        <div class="car-make-card">
            <div class="make-header">
                <h3>${make.name}</h3>
                <span class="make-country">${make.country || 'International'}</span>
            </div>
            <div class="make-description">
                <p>${make.description || 'Quality vehicles from ' + make.name}</p>
            </div>
            <div class="models-list">
                <h4>Available Models:</h4>
                <ul>
                    ${make.models.slice(0, 3).map(model => `
                        <li>${model.name} (${model.year}) - ${model.car_type}</li>
                    `).join('')}
                    ${make.models.length > 3 ? `<li class="more-models">+${make.models.length - 3} more models</li>` : ''}
                </ul>
            </div>
        </div>
    `).join('');
}

function setupEventListeners() {
    // State filter
    const stateFilter = document.getElementById('state-filter');
    if (stateFilter) {
        stateFilter.addEventListener('change', filterDealersByState);
    }
}

async function filterDealersByState() {
    const stateFilter = document.getElementById('state-filter');
    const selectedState = stateFilter.value;
    
    try {
        let url = '/api/dealers/';
        if (selectedState) {
            url = `/api/dealers/state/${selectedState}/`;
        }
        
        const response = await fetch(url);
        const dealers = await response.json();
        displayDealers(dealers);
        
        // Update URL to reflect filter
        const newUrl = selectedState ? `/?state=${selectedState}` : '/';
        window.history.pushState({}, '', newUrl);
        
    } catch (error) {
        console.error('Error filtering dealers:', error);
        displayError('dealers-grid', 'Failed to filter dealers');
    }
}

function displayError(containerId, message) {
    const container = document.getElementById(containerId);
    container.innerHTML = `<div class="error-message">${message}</div>`;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initialize state filter from URL parameters
function initializeStateFilter() {
    const urlParams = new URLSearchParams(window.location.search);
    const state = urlParams.get('state');
    
    if (state) {
        const stateFilter = document.getElementById('state-filter');
        if (stateFilter) {
            stateFilter.value = state;
            filterDealersByState();
        }
    }
}

// Call initialization when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeStateFilter);