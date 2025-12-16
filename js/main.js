
// HEADER HTML CONTENT
const headerContent = `
<nav>
    <div class="container nav-wrapper">
        <a href="index.html" class="brand">Metocean</a>
        <ul class="nav-links">
            <li><a href="index.html" class="nav-item">Home</a></li>
            <li><a href="services.html" class="nav-item">Services</a></li>
            <li><a href="courses.html" class="nav-item">Courses</a></li>
            <li><a href="about.html" class="nav-item">About</a></li>
            <li><a href="contact.html" class="nav-item">Contact</a></li>
        </ul>
        <div class="nav-actions">
            <!-- Search Icon (Visual) -->
            <span class="material-symbols-outlined icon-hover" style="cursor: pointer;">search</span>
            
            <a href="contact.html" class="btn btn-primary btn-sm">Client Portal</a>
        </div>
        
        <!-- Mobile Menu Toggle -->
        <span class="material-symbols-outlined mobile-menu-btn" id="mobile-menu-btn">menu</span>
    </div>
</nav>

<!-- Mobile Menu Drawer -->
<div class="mobile-menu-overlay" id="mobile-menu-overlay"></div>
<div class="mobile-menu-drawer" id="mobile-menu-drawer">
    <div class="mobile-menu-header">
        <span class="brand">Metocean</span>
        <span class="material-symbols-outlined close-btn" id="mobile-menu-close">close</span>
    </div>
    <ul class="mobile-nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="courses.html">Courses</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
    <div class="mobile-menu-footer">
        <a href="contact.html" class="btn btn-primary w-full">Client Portal</a>
    </div>
</div>
`;

// FOOTER HTML CONTENT
const footerContent = `
<footer>
    <div class="container">
        <div class="footer-grid">
            <div class="footer-col animate-slide-up" style="padding-right: 2rem;">
                <a href="index.html" class="brand" style="display: block; margin-bottom: 1.5rem;">Metocean</a>
                <p style="font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.8; color: var(--text-muted);">
                    Global leaders in oceanographic consulting. Over 25 years of enabling safe offshore operations through precision engineering and data.
                </p>
                <!-- Social Icons -->
                <div class="social-icons">
                    <a href="#" class="social-icon" title="LinkedIn"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"></a>
                    <a href="#" class="social-icon" title="Twitter"><img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter"></a>
                    <a href="#" class="social-icon" title="Instagram"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram"></a>
                </div>
            </div>
            
            <div class="footer-col animate-slide-up delay-100">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="index.html" class="nav-item">Home</a></li>
                    <li><a href="about.html" class="nav-item">About Us</a></li>
                    <li><a href="services.html" class="nav-item">Services</a></li>
                    <li><a href="courses.html" class="nav-item">Courses</a></li>
                    <li><a href="contact.html" class="nav-item">Contact</a></li>
                </ul>
            </div>
            
            <div class="footer-col animate-slide-up delay-200">
                <h4>Contact Info</h4>
                <ul style="color: var(--text-muted); font-size: 0.95rem;">
                    <li style="margin-bottom: 1rem;">100 Ocean Way, Suite 500<br>Maritime City, MC 12345</li>
                    <li style="margin-bottom: 1rem;"><a href="mailto:info@metocean.com">info@metocean.com</a></li>
                    <li><a href="tel:+15551234567">+1 (555) 123-4567</a></li>
                </ul>
            </div>
        </div>
        
        <div style="border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem; display: flex; justify-content: space-between; font-size: 0.9rem; color: var(--text-muted);">
            <p>&copy; 2024 Metocean Consulting Group. All rights reserved.</p>
            <div style="display: flex; gap: 2rem;">
                <span>ISO 9001 Certified</span>
                <span>Privacy Policy</span>
            </div>
        </div>
    </div>
</footer>
`;

document.addEventListener("DOMContentLoaded", function () {
    loadIncludes();
    initCounters(); // Ensure counters start
});

function loadIncludes() {
    // Inject Header
    const headerPlaceholder = document.getElementById("header-placeholder");
    if (headerPlaceholder) {
        headerPlaceholder.innerHTML = headerContent;
        highlightActiveLink();
        initMobileMenu();
    } else {
        console.error("Header placeholder not found");
    }

    // Inject Footer
    const footerPlaceholder = document.getElementById("footer-placeholder");
    if (footerPlaceholder) {
        footerPlaceholder.innerHTML = footerContent;
        // Trigger animations for footer if it's injected late (though CSS animation triggers on load/scroll usually if viewport aware, here it's keyframes on load. For dynamic content, simple CSS animation might run on insertion)
    } else {
        console.error("Footer placeholder not found");
    }
}

function highlightActiveLink() {
    const currentPath = window.location.pathname.split("/").pop() || "index.html";
    const links = document.querySelectorAll(".nav-links a, .mobile-nav-links a");

    links.forEach(link => {
        const linkPath = link.getAttribute("href");
        if (linkPath === currentPath) {
            link.classList.add("active");
            link.style.color = "var(--primary)";
        }
    });
}

function initMobileMenu() {
    const btn = document.getElementById("mobile-menu-btn");
    const closeBtn = document.getElementById("mobile-menu-close");
    const drawer = document.getElementById("mobile-menu-drawer");
    const overlay = document.getElementById("mobile-menu-overlay");

    if (btn && drawer && overlay) {
        btn.addEventListener("click", () => {
            drawer.classList.add("open");
            overlay.classList.add("open");
        });

        const closeMenu = () => {
            drawer.classList.remove("open");
            overlay.classList.remove("open");
        };

        if (closeBtn) closeBtn.addEventListener("click", closeMenu);
        overlay.addEventListener("click", closeMenu);
    }
}

// NUMBER COUNTING ANIMATION
function initCounters() {
    // We need to wait a tick for the DOM to be fully ready if injected
    setTimeout(() => {
        const counters = document.querySelectorAll('.counter');
        if (counters.length === 0) return;

        const observerOption = {
            root: null,
            threshold: 0.5
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = +counter.getAttribute('data-target');
                    const duration = 5000; // 5 Seconds
                    const start = 0;
                    const startTime = performance.now();

                    const updateCount = (currentTime) => {
                        const elapsedTime = currentTime - startTime;
                        const progress = Math.min(elapsedTime / duration, 1);

                        // Easing (easeOutExpo)
                        const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);

                        const count = Math.floor(ease * (target - start) + start);

                        counter.innerText = count + (target > 100 ? '+' : '');

                        if (progress < 1) {
                            requestAnimationFrame(updateCount);
                        } else {
                            counter.innerText = target + '+';
                        }
                    };

                    requestAnimationFrame(updateCount);
                    observer.unobserve(counter);
                }
            });
        }, observerOption);

        counters.forEach(counter => {
            observer.observe(counter);
        });
    }, 100);
}
