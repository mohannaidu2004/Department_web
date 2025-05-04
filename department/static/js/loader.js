document.addEventListener('DOMContentLoaded', function() {
    // Show loader when page starts loading
    const loader = document.querySelector('.loader');
    
    // Hide loader when page is fully loaded
    window.addEventListener('load', function() {
        setTimeout(function() {
            loader.classList.add('loader-hidden');
            
            // Optional: Remove loader from DOM after animation completes
            loader.addEventListener('transitionend', function() {
                if (loader.classList.contains('loader-hidden')) {
                    document.body.removeChild(loader);
                }
            });
        }, 1000); // Adjust time as needed
    });
    
    // If page takes too long to load, still hide loader after max time
    setTimeout(function() {
        loader.classList.add('loader-hidden');
    }, 5000); // 5 seconds max
});