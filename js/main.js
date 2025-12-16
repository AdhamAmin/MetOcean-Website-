
// TRANSLATIONS
const translations = {
    en: {
        // Nav & Footer
        brand: "Metocean",
        home: "Home",
        services: "Services",
        courses: "Courses",
        about: "About",
        contact: "Contact",
        portal: "Get Started", // CHANGED
        footerDesc: "Global leaders in oceanographic consulting. Over 25 years of enabling safe offshore operations through precision engineering and data.",
        quickLinks: "Quick Links",
        contactInfo: "Contact Info",
        rights: "© 2025 Metocean Consulting Group. All rights reserved.",
        createdBy: "Created by <a href='https://adhamamin.github.io/My-Portflio/' target='_blank' style='color: var(--primary); text-decoration: none;'>Adham Amin the best web div</a>",
        privacy: "Privacy Policy",
        address: "100 Ocean Way, Suite 500<br>Maritime City, MC 12345",

        // Index Page - Hero
        heroTitle: "Mastering the Marine Environment",
        heroText: "Delivering critical oceanographic data and engineering criteria for the world's most challenging offshore projects. We bridge the gap between complex marine science and operational success.",
        ourServices: "Our Services",
        contactUs: "Contact Us",

        // Index - Hero Cards
        offshoreEnergy: "Offshore Energy",

        // Index - Key Sectors
        keySectors: "Key Sectors",
        viewCapabilities: "View all capabilities",
        secEnergy: "Energy",
        secInfra: "Infrastructure",
        secDefense: "Defense",

        // Index - Sectors Cards
        offshoreWind: "Offshore Wind",
        foundCriteria: "Foundation Criteria",
        oilGas: "Oil & Gas",
        exploration: "Exploration",
        ports: "Ports",
        dredging: "Dredging",
        coastal: "Coastal",
        resilience: "Resilience",

        // Index - Tech Insights
        techInsights: "Technical Insights",
        caseStudy: "Case Study",
        caseTitle: "Optimizing installation installation windows for North Sea assets",
        analysis: "Analysis",
        waveAnalysis: "Extreme Wave Height Analysis",
        innovation: "Innovation",
        floatWind: "Floating Wind Challenges",

        // Index - Stats
        impactTitle: "Our Impact by the Numbers",
        impactDesc: "Decades of experience delivering precision data.",
        projCompleted: "Projects Completed",
        yearsEx: "Years of Excellence",
        countries: "Countries Served",

        // Newsletter
        subTitle: "Subscribe to Industry Intelligence",
        subDesc: "Get the latest regulatory updates and technical best practices.",
        emailPlaceholder: "Corporate email address",
        subscribe: "Subscribe"
    },
    ar: {
        // Nav & Footer
        brand: "ميتوشيان",
        home: "الرئيسية",
        services: "خدماتنا",
        courses: "الدورات",
        about: "عن الشركة",
        contact: "اتصل بنا",
        portal: "ابدأ الآن", // CHANGED
        footerDesc: "رواد عالميون في الاستشارات الأوقيانوغرافية. أكثر من 25 عامًا من تمكين العمليات البحرية الآمنة من خلال الهندسة الدقيقة والبيانات.",
        quickLinks: "روابط سريعة",
        contactInfo: "معلومات الاتصال",
        rights: "© 2025 مجموعة ميتوشيان للاستشارات. جميع الحقوق محفوظة.",
        createdBy: "تصميم <a href='https://adhamamin.github.io/My-Portflio/' target='_blank' style='color: var(--primary); text-decoration: none;'>أدهم أمين أفضل مطور ويب</a>",
        privacy: "سياسة الخصوصية",
        address: "١٠٠ طريق المحيط، جناح ٥٠٠<br>مدينة الملاحة، ١٢٣٤٥",

        // Index Page - Hero
        heroTitle: "إتقان البيئة البحرية",
        heroText: "تقديم بيانات أوقيانوغرافية ومعايير هندسية دقيقة لأكثر المشاريع البحرية تحديًا في العالم. نحن نسد الفجوة بين العلوم البحرية المعقدة والنجاح التشغيلي.",
        ourServices: "خدماتنا",
        contactUs: "تواصل معنا",

        // Index - Hero Cards
        offshoreEnergy: "الطاقة البحرية",

        // Index - Key Sectors
        keySectors: "القطاعات الرئيسية",
        viewCapabilities: "عرض جميع القدرات",
        secEnergy: "الطاقة",
        secInfra: "البنية التحتية",
        secDefense: "الدفاع",

        // Index - Sectors Cards
        offshoreWind: "الرياح البحرية",
        foundCriteria: "معايير التأسيس",
        oilGas: "النفط والغاز",
        exploration: "التنقيب",
        ports: "الموانئ",
        dredging: "التجريف",
        coastal: "الساحلية",
        resilience: "المرونة",

        // Index - Tech Insights
        techInsights: "رؤى تقنية",
        caseStudy: "دراسة حالة",
        caseTitle: "تحسين نوافذ التثبيت لأصول بحر الشمال",
        analysis: "تحليل",
        waveAnalysis: "تحليل ارتفاع الأمواج",
        innovation: "ابتكار",
        floatWind: "تحديات الرياح العائمة",

        // Index - Stats
        impactTitle: "تأثيرنا بالأرقام",
        impactDesc: "عقود من الخبرة في تقديم بيانات دقيقة.",
        projCompleted: "مشروع مكتمل",
        yearsEx: "سنوات من التميز",
        countries: "دولة تم خدمتها",

        // Newsletter
        subTitle: "اشترك في معلومات الصناعة",
        subDesc: "احصل على أحدث التحديثات التنظيمية وأفضل الممارسات التقنية.",
        emailPlaceholder: "البريد الإلكتروني للشركة",
        subscribe: "اشترك"
    }
};

let currentLang = localStorage.getItem('lang') || 'en';
let currentTheme = localStorage.getItem('theme') || 'light';

// Apply saved settings on load
document.documentElement.setAttribute('lang', currentLang);
document.documentElement.setAttribute('dir', currentLang === 'ar' ? 'rtl' : 'ltr');
document.documentElement.setAttribute('data-theme', currentTheme);


// GENERATE CONTENT BASED ON LANGUAGE (Header/Footer)
function getHeaderContent() {
    const t = translations[currentLang];
    return `
<nav>
    <div class="container nav-wrapper">
        <a href="index.html" class="brand">${t.brand}</a>
        <ul class="nav-links">
            <li><a href="index.html" class="nav-item">${t.home}</a></li>
            <li><a href="services.html" class="nav-item">${t.services}</a></li>
            <li><a href="courses.html" class="nav-item">${t.courses}</a></li>
            <li><a href="about.html" class="nav-item">${t.about}</a></li>
            <li><a href="contact.html" class="nav-item">${t.contact}</a></li>
        </ul>
        <div class="nav-actions">
            <!-- Search Icon -->
            <span class="material-symbols-outlined icon-hover" style="cursor: pointer;">search</span>
            
            <!-- Animated Button for CTA -->
            <a href="contact.html" class="btn btn-primary btn-sm btn-animate" data-text="${t.portal}">
                <span>${t.portal}</span>
            </a>
            
            <!-- Mobile Menu Toggle (Moved inside nav-actions for alignment or kept separate) -->
            <span class="material-symbols-outlined mobile-menu-btn" id="mobile-menu-btn">menu</span>
        </div>
    </div>
</nav>

<!-- Mobile Menu Drawer -->
<div class="mobile-menu-overlay" id="mobile-menu-overlay"></div>
<div class="mobile-menu-drawer" id="mobile-menu-drawer">
    <div class="mobile-menu-header">
        <span class="brand">${t.brand}</span>
        <span class="material-symbols-outlined close-btn" id="mobile-menu-close">close</span>
    </div>
    <ul class="mobile-nav-links">
        <li><a href="index.html">${t.home}</a></li>
        <li><a href="services.html">${t.services}</a></li>
        <li><a href="courses.html">${t.courses}</a></li>
        <li><a href="about.html">${t.about}</a></li>
        <li><a href="contact.html">${t.contact}</a></li>
    </ul>
    <div class="mobile-menu-footer">
        <a href="contact.html" class="btn btn-primary w-full">${t.portal}</a>
    </div>
</div>
`;
}

function getFooterContent() {
    const t = translations[currentLang];
    // Dark/Light Icon
    const themeIcon = currentTheme === 'dark' ? 'light_mode' : 'dark_mode';

    return `
<footer>
    <div class="container">
        <div class="footer-grid">
            <div class="footer-col animate-slide-up" style="padding-right: 2rem;">
                <a href="index.html" class="brand" style="display: block; margin-bottom: 1.5rem;">${t.brand}</a>
                <p style="font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.8; color: var(--text-muted);">
                    ${t.footerDesc}
                </p>
                <!-- Social Icons -->
                <div class="social-icons">
                    <a href="#" class="social-icon" title="LinkedIn"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"></a>
                    <a href="#" class="social-icon" title="Twitter"><img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter"></a>
                    <a href="#" class="social-icon" title="Instagram"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram"></a>
                </div>
            </div>
            
            <div class="footer-col animate-slide-up delay-100">
                <h4>${t.quickLinks}</h4>
                <ul>
                    <li><a href="index.html" class="nav-item">${t.home}</a></li>
                    <li><a href="about.html" class="nav-item">${t.about}</a></li>
                    <li><a href="services.html" class="nav-item">${t.services}</a></li>
                    <li><a href="courses.html" class="nav-item">${t.courses}</a></li>
                    <li><a href="contact.html" class="nav-item">${t.contact}</a></li>
                </ul>
            </div>
            
            <div class="footer-col animate-slide-up delay-200">
                <h4>${t.contactInfo}</h4>
                <ul style="color: var(--text-muted); font-size: 0.95rem;">
                    <li style="margin-bottom: 1rem;">100 Ocean Way, Suite 500<br>Maritime City, MC 12345</li>
                    <li style="margin-bottom: 1rem;"><a href="mailto:info@metocean.com">info@metocean.com</a></li>
                    <li><a href="tel:+15551234567">+1 (555) 123-4567</a></li>
                </ul>

                <!-- Toggles MOVED HERE (Theme & Lang) -->
                <div class="footer-toggles">
                    <button class="circle-btn" onclick="toggleTheme()" title="Toggle Theme">
                        <span class="material-symbols-outlined">${themeIcon}</span>
                    </button>
                    <button class="circle-btn" onclick="toggleLanguage()" title="Switch Language">
                        <span class="material-symbols-outlined">language</span>
                    </button>
                </div>
            </div>
        </div>
        
        <div style="border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem; display: flex; justify-content: space-between; font-size: 0.9rem; color: var(--text-muted);">
            <p>${t.rights}</p>
            <div style="display: flex; gap: 2rem;">
                <span>${t.createdBy}</span>
                <span>${t.privacy}</span>
            </div>
        </div>
    </div>
</footer>
`;
}

document.addEventListener("DOMContentLoaded", function () {
    loadIncludes();
    initCounters();
    translatePage(); // Run translation for static content
});

function loadIncludes() {
    // Inject Header
    const headerPlaceholder = document.getElementById("header-placeholder");
    if (headerPlaceholder) {
        headerPlaceholder.innerHTML = getHeaderContent();
        highlightActiveLink();
        initMobileMenu();
    }

    // Inject Footer
    const footerPlaceholder = document.getElementById("footer-placeholder");
    if (footerPlaceholder) {
        footerPlaceholder.innerHTML = getFooterContent();
    }

    // Re-run translation just in case
    translatePage();
}

function toggleTheme() {
    currentTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    localStorage.setItem('theme', currentTheme);
    loadIncludes();
}

function toggleLanguage() {
    currentLang = currentLang === 'en' ? 'ar' : 'en';
    document.documentElement.setAttribute('lang', currentLang);
    document.documentElement.setAttribute('dir', currentLang === 'ar' ? 'rtl' : 'ltr');
    localStorage.setItem('lang', currentLang);
    loadIncludes();
}

// Function to translate static elements with [data-i18n]
function translatePage() {
    const t = translations[currentLang];
    const elements = document.querySelectorAll('[data-i18n]');

    elements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (t[key]) {
            // Check if it's an input placeholder
            if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                el.placeholder = t[key];
            } else {
                el.innerHTML = t[key];
            }
        }
    });

    // Update Special Button Data Attributes for CSS Animation
    const animatedBtns = document.querySelectorAll('.btn-animate');
    animatedBtns.forEach(btn => {
        const textSpan = btn.querySelector('span');
        if (textSpan) btn.setAttribute('data-text', textSpan.innerText);
    });
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
