/* Loader.js - Dynamically loads header and footer */

document.addEventListener("DOMContentLoaded", function () {
    // Load Header
    fetch('includes/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-placeholder').innerHTML = data;
            // Re-initialize mobile menu script after header load
            if (window.initMobileMenu) window.initMobileMenu();
        })
        .catch(error => console.error('Error loading header:', error));

    // Load Footer
    fetch('includes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-placeholder').innerHTML = data;
        })
        .catch(error => console.error('Error loading footer:', error));
});
