/* Main.js - General Logic */

// Function to initialize mobile menu (called after header load)
window.initMobileMenu = function () {
    const toggleBtn = document.querySelector('.mobile-menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    const backdrop = document.querySelector('.mobile-menu-backdrop');
    const closeBtn = document.querySelector('.mobile-menu__close');

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            mobileMenu.classList.add('is-open');
            backdrop.classList.add('is-visible');
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('is-open');
            backdrop.classList.remove('is-visible');
        });
    }

    if (backdrop) {
        backdrop.addEventListener('click', () => {
            mobileMenu.classList.remove('is-open');
            backdrop.classList.remove('is-visible');
        });
    }
};

// Sticky Header Effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (header) {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
            header.style.padding = '0.5rem 0';
        } else {
            header.style.boxShadow = 'none';
            header.style.padding = '1rem 0';
        }
    }
});
