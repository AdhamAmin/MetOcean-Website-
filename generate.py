import os

def create_page(filename, lang, title_en, title_ar, content_en, content_ar):
    is_ar = lang == 'ar'
    path = f'ar/{filename}' if is_ar else filename
    title = title_ar if is_ar else title_en
    content = content_ar if is_ar else content_en
    css_path = '../style.css' if is_ar else 'style.css'
    en_link = f'../{filename}' if is_ar else filename
    ar_link = filename if is_ar else f'ar/{filename}'
    
    html = f'''<!DOCTYPE html>
<html lang="{'ar' if is_ar else 'en'}" {'dir="rtl"' if is_ar else ''}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetOcean | {title}</title>
    <link rel="stylesheet" href="{css_path}">
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800;900&family=Barlow:wght@300;400;500;600;700&family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        {":root { --fb: 'Cairo', sans-serif; --fd: 'Cairo', sans-serif; }" if is_ar else ""}
        .dl-modal {{ position: fixed; inset: 0; z-index: 2000; background: rgba(0,0,0,0.8); display: none; align-items: center; justify-content: center; backdrop-filter: blur(4px); }}
        .dl-modal.open {{ display: flex; animation: fadeIn 0.3s ease; }}
        .dl-modal-box {{ background: #fff; padding: 40px; border-radius: 6px; text-align: center; max-width: 420px; width: 90%; position: relative; animation: popIn 0.3s ease; }}
        .dl-close {{ position: absolute; top: 15px; {'left' if is_ar else 'right'}: 20px; background: none; border: none; font-size: 28px; cursor: pointer; color: var(--ink2); }}
        .dl-close:hover {{ color: var(--brand); }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        @keyframes popIn {{ from {{ transform: scale(0.9); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}
        .page-header {{ padding: 160px 40px 80px; text-align: center; background: var(--warm); border-bottom: 1px solid var(--lg); }}
    </style>
</head>
<body>
    <!-- NAV -->
    <nav id="navbar" class="scrolled">
        <a href="index.html" class="nav-logo">
            <span style="font-family:var(--fd);font-weight:900;font-size:32px;letter-spacing:1px;color:var(--brand)">{'ميتوشيان' if is_ar else 'MetOcean'}</span>
        </a>
        <ul class="nav-menu">
            <li><a href="index.html">{'الرئيسية' if is_ar else 'Home'}</a></li>
            <li><a href="about.html" {'class="on"' if filename=='about.html' else ''}>{'من نحن' if is_ar else 'About Us'}</a></li>
            <li><a href="services.html" {'class="on"' if filename=='services.html' else ''}>{'خدماتنا' if is_ar else 'Services'}</a></li>
            <li><a href="contact.html" {'class="on"' if filename=='contact.html' else ''}>{'اتصل بنا' if is_ar else 'Contact'}</a></li>
        </ul>
        <div class="nav-right">
            <div class="lang">
                <a href="{en_link}" class="lb {'on' if not is_ar else ''}">EN</a>
                <a href="{ar_link}" class="lb {'on' if is_ar else ''}">AR</a>
            </div>
            <button class="ncta" onclick="document.getElementById('dlModal').classList.add('open')">{'ملف الشركة' if is_ar else 'Download Profile'}</button>
            <button class="nav-hamburger" id="hamburger" onclick="toggleMobNav()"><span></span><span></span><span></span></button>
        </div>
    </nav>

    <!-- MOBILE NAV -->
    <div class="mob-nav" id="mobNav">
        <a href="index.html" onclick="closeMobNav()">{'الرئيسية' if is_ar else 'Home'}</a>
        <a href="about.html" onclick="closeMobNav()">{'من نحن' if is_ar else 'About Us'}</a>
        <a href="services.html" onclick="closeMobNav()">{'خدماتنا' if is_ar else 'Services'}</a>
        <a href="contact.html" onclick="closeMobNav()">{'اتصل بنا' if is_ar else 'Contact'}</a>
        <a href="#" class="mob-nav-cta" onclick="closeMobNav(); document.getElementById('dlModal').classList.add('open')">{'ملف الشركة' if is_ar else 'Download Profile'}</a>
    </div>

    <!-- HEADER -->
    <header class="page-header">
        <div class="sl c">{'ميتوشيان' if is_ar else 'MetOcean'}</div>
        <h1 class="st c">{title}</h1>
    </header>

    <!-- CONTENT -->
    <main>
        {content}
    </main>

    <!-- FOOTER -->
    <footer>
        <div class="footer-top">
            <div class="f-col">
                <div class="f-brand-name">{'ميتوشيان' if is_ar else 'MetOcean'}</div>
                <p class="f-brand-tag">{'بيت خبرة بيئي معتمد. استشارات بيئية، دراسات بحرية، استدامة واستشارات البصمة الكربونية.' if is_ar else 'Accredited Environmental Expertise House. Environmental Consultancy, Marine Studies, Sustainability & Carbon Advisory.'}</p>
            </div>
            <div class="f-col">
                <h4>{'الشركة' if is_ar else 'Company'}</h4>
                <ul>
                    <li><a href="about.html">{'من نحن' if is_ar else 'About Us'}</a></li>
                    <li><a href="services.html">{'الخدمات' if is_ar else 'Services'}</a></li>
                    <li><a href="contact.html">{'اتصل بنا' if is_ar else 'Contact'}</a></li>
                </ul>
            </div>
            <div class="f-col">
                <h4>{'الخدمات الأساسية' if is_ar else 'Core Services'}</h4>
                <ul>
                    <li><a href="services.html">{'الدراسات البيئية' if is_ar else 'Environmental Studies'}</a></li>
                    <li><a href="services.html">{'القياسات الميدانية' if is_ar else 'Field Measurements'}</a></li>
                    <li><a href="services.html">{'النمذجة البيئية' if is_ar else 'Environmental Modeling'}</a></li>
                </ul>
            </div>
            <div class="f-col">
                <h4>{'للتواصل' if is_ar else 'Contact'}</h4>
                <div class="f-contact-item">
                    <span>HuElnaggar@metoceanms.com</span>
                </div>
                <div class="f-contact-item">
                    <span dir="ltr">+20 100 308 4597</span>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <span>&copy; 2026 {'ميتوشيان للخدمات والحلول البيئية. جميع الحقوق محفوظة.' if is_ar else 'MetOcean Environmental Services & Solutions. All rights reserved.'}</span>
        </div>
    </footer>

    <!-- DOWNLOAD MODAL -->
    <div class="dl-modal" id="dlModal">
        <div class="dl-modal-box">
            <button class="dl-close" onclick="document.getElementById('dlModal').classList.remove('open')">&times;</button>
            <h3 style="font-family: var(--fd); font-weight: 800; font-size: 26px; text-transform: uppercase; color: var(--ink); margin-bottom: 10px;">{'تحميل الملف' if is_ar else 'Download Profile'}</h3>
            <p style="font-size: 15px; color: var(--ink2); margin-bottom: 25px;">{'اختر لغتك المفضلة لتحميل ملف الشركة الخاص بميتوشيان.' if is_ar else 'Select your preferred language to download the MetOcean Corporate Profile.'}</p>
            <div style="display: flex; gap: 15px; flex-direction: column;">
                <a href="{'../' if is_ar else ''}MetOcean Profile.pdf" download class="btn-primary" style="justify-content: center; width: 100%;" onclick="document.getElementById('dlModal').classList.remove('open');">{'الإنجليزية (EN)' if is_ar else 'English (EN)'}</a>
                <a href="{'../' if is_ar else ''}MetOcean Profile.pdf" download class="btn-primary" style="justify-content: center; width: 100%; background: var(--ink);" onclick="document.getElementById('dlModal').classList.remove('open');">{'العربية (AR)' if is_ar else 'العربية (AR)'}</a>
            </div>
        </div>
    </div>
    
    <script>
        function toggleMobNav() {{
            document.getElementById('mobNav').classList.toggle('open');
            document.getElementById('hamburger').classList.toggle('active');
        }}
        function closeMobNav() {{
            document.getElementById('mobNav').classList.remove('open');
            document.getElementById('hamburger').classList.remove('active');
        }}
        document.getElementById('dlModal').addEventListener('click', function(e) {{
            if(e.target === this) this.classList.remove('open');
        }});
        
        let lastY = 0;
        window.addEventListener('scroll', () => {{
            const y = window.scrollY;
            const navEl = document.getElementById('navbar');
            if (y > 50) navEl.classList.add('scrolled');
            else navEl.classList.remove('scrolled');
            lastY = y;
            
            const reveals = document.querySelectorAll('.reveal');
            reveals.forEach(r => {{
                if (r.getBoundingClientRect().top < window.innerHeight - 100) {{
                    r.classList.add('in');
                }}
            }});
        }});
        window.dispatchEvent(new Event('scroll'));
    </script>
</body>
</html>'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

about_en = '''
<section class="wrap" style="padding: 80px 40px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; margin-bottom: 80px;">
        <div class="reveal in">
            <div class="sl">CEO Message</div>
            <h2 class="st" style="margin-bottom: 24px;">Prof. Dr. Hussein Abdel Meguid El-Naggar</h2>
            <p style="color: var(--ink2); font-size: 18px; line-height: 1.8;">MetOcean exists to meet our clients' needs with the best integrated environmental solutions available. We invest continuously in developing our team and equipping them with the latest technology, so that sustainable development is not just a goal, but a practice — built on the Best Available Techniques and the Best Environmental Practices in every engagement we undertake.</p>
        </div>
        <div class="reveal in" style="background: var(--off); padding: 40px; border-radius: 8px; border-left: 4px solid var(--brand);">
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">Vision</h3>
            <p style="color: var(--ink2); margin-bottom: 24px;">To be a leading force in Egypt's environmental sector — helping shape a sustainable community and economy, and working steadily toward a cleaner, greener environment.</p>
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">Mission</h3>
            <p style="color: var(--ink2);">To meet every client's needs through the best integrated environmental solutions, continuously developing our team and adopting the Best Available Techniques (BAT) and Best Environmental Practices (BEP).</p>
        </div>
    </div>
    
    <!-- Timeline Section -->
    <div style="margin-top: 100px; text-align: center;" class="reveal in">
        <div class="sl c">Our Journey</div>
        <h2 class="st c" style="margin-bottom: 60px;">Experience Timeline</h2>
        <div class="timeline">
            <div class="timeline-item reveal in">
                <div class="timeline-date">2011</div>
                <div class="timeline-content">First international engagements, including a power-station EIA in Kuwait.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2014-16</div>
                <div class="timeline-content">Coastal-tourism and marine-biodiversity studies expand across the Red Sea, Jordan, Oman and Lebanon.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2019</div>
                <div class="timeline-content">Baseline marine surveys support Saudi Arabia's Red Sea electrical-interconnection and giga-project developments.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2021-22</div>
                <div class="timeline-content">National industrial EIA portfolio scales sharply, covering waste, manufacturing and petrochemical facilities.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2023-24</div>
                <div class="timeline-content">Regional marine-monitoring programs for JIGPC and WES Kuwait; national wastewater compliance audits in Saudi Arabia.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2025</div>
                <div class="timeline-content">600+ cumulative projects; active engagements spanning six countries across the MENA region.</div>
            </div>
        </div>
    </div>
    
    <!-- Certificates Section -->
    <div style="margin-top: 100px; text-align: center;" class="reveal in">
        <div class="sl c">Accreditation</div>
        <h2 class="st c" style="margin-bottom: 20px;">Certificates & Accreditations</h2>
        <p style="color: var(--ink2); font-size: 18px; max-width: 800px; margin: 0 auto;">MetOcean is registered and accredited by Egypt's Ministry of Environment as a licensed House of Environmental Expertise.</p>
        <div class="cert-grid">
            <div class="cert-card reveal in">
                <div class="cert-icon">
                    <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 class="cert-title">Registered House of Environmental Expertise</h3>
                <p class="cert-desc">Egyptian Ministry of Environment — Environmental Affairs Agency</p>
            </div>
            <div class="cert-card reveal in">
                <div class="cert-icon">
                    <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                </div>
                <h3 class="cert-title">Accredited Environmental Consultants (Class A)</h3>
                <p class="cert-desc">Individually licensed consultants across EIA, biodiversity and carbon-footprint auditing.</p>
            </div>
            <div class="cert-card reveal in">
                <div class="cert-icon">
                    <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                </div>
                <h3 class="cert-title">Regulatory Compliance</h3>
                <p class="cert-desc">Certifications reviewed and renewed on a five-year cycle in line with national requirements.</p>
            </div>
        </div>
    </div>
</section>
'''

about_ar = '''
<section class="wrap" style="padding: 80px 40px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; margin-bottom: 80px;">
        <div class="reveal in">
            <div class="sl">رسالة الرئيس التنفيذي</div>
            <h2 class="st" style="margin-bottom: 24px;">أ. د. حسين عبد المجيد النجار</h2>
            <p style="color: var(--ink2); font-size: 18px; line-height: 1.8;">تأسست ميتوشيان لتلبية احتياجات عملائنا من خلال تقديم أفضل الحلول البيئية المتكاملة المتاحة. نحن نستثمر باستمرار في تطوير فريقنا وتزويدهم بأحدث التقنيات، بحيث لا تكون التنمية المستدامة مجرد هدف، بل ممارسة - مبنية على أفضل التقنيات المتاحة وأفضل الممارسات البيئية في كل مشروع نقوم به.</p>
        </div>
        <div class="reveal in" style="background: var(--off); padding: 40px; border-radius: 8px; border-right: 4px solid var(--brand);">
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">رؤيتنا</h3>
            <p style="color: var(--ink2); margin-bottom: 24px;">أن نكون قوة رائدة في القطاع البيئي في مصر - نساعد في تشكيل مجتمع واقتصاد مستدامين، والعمل بثبات نحو بيئة أنظف وأكثر خضرة.</p>
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">رسالتنا</h3>
            <p style="color: var(--ink2);">تلبية احتياجات كل عميل من خلال أفضل الحلول البيئية المتكاملة، وتطوير فريقنا باستمرار واعتماد أفضل التقنيات المتاحة (BAT) وأفضل الممارسات البيئية (BEP).</p>
        </div>
    </div>
    
    <!-- Timeline Section -->
    <div style="margin-top: 100px; text-align: center;" class="reveal in">
        <div class="sl c">رحلتنا</div>
        <h2 class="st c" style="margin-bottom: 60px;">الجدول الزمني للخبرات</h2>
        <div class="timeline">
            <div class="timeline-item reveal in">
                <div class="timeline-date">2011</div>
                <div class="timeline-content">أولى الارتباطات الدولية، بما في ذلك تقييم الأثر البيئي لمحطة طاقة في الكويت.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2014-16</div>
                <div class="timeline-content">توسع دراسات السياحة الساحلية والتنوع البيولوجي البحري عبر البحر الأحمر والأردن وعمان ولبنان.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2019</div>
                <div class="timeline-content">الدراسات الاستقصائية البحرية الأساسية تدعم الربط الكهربائي والمشاريع العملاقة في البحر الأحمر بالسعودية.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2021-22</div>
                <div class="timeline-content">توسيع محفظة تقييم الأثر البيئي الصناعي الوطني لتغطي مرافق النفايات والتصنيع والبتروكيماويات.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2023-24</div>
                <div class="timeline-content">البرامج الإقليمية للمراقبة البحرية لشركة JIGPC و WES في الكويت؛ وتدقيق امتثال مياه الصرف الصحي الوطني في المملكة العربية السعودية.</div>
            </div>
            <div class="timeline-item reveal in">
                <div class="timeline-date">2025</div>
                <div class="timeline-content">أكثر من 600 مشروع تراكمي؛ مشاركات نشطة تغطي ست دول في منطقة الشرق الأوسط وشمال أفريقيا.</div>
            </div>
        </div>
    </div>
    
    <!-- Certificates Section -->
    <div style="margin-top: 100px; text-align: center;" class="reveal in">
        <div class="sl c">الاعتمادات</div>
        <h2 class="st c" style="margin-bottom: 20px;">الشهادات والاعتمادات</h2>
        <p style="color: var(--ink2); font-size: 18px; max-width: 800px; margin: 0 auto;">تم تسجيل ميتوشيان واعتمادها من قبل وزارة البيئة المصرية كبيت خبرة بيئي مرخص.</p>
        <div class="cert-grid">
            <div class="cert-card reveal in">
                <div class="cert-icon">
                    <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 class="cert-title">بيت خبرة بيئي مسجل</h3>
                <p class="cert-desc">وزارة البيئة المصرية — جهاز شئون البيئة</p>
            </div>
            <div class="cert-card reveal in">
                <div class="cert-icon">
                    <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                </div>
                <h3 class="cert-title">مستشارون بيئيون معتمدون (الفئة أ)</h3>
                <p class="cert-desc">مستشارون مرخصون فردياً في مجالات تقييم الأثر البيئي والتنوع البيولوجي وتدقيق البصمة الكربونية.</p>
            </div>
            <div class="cert-card reveal in">
                <div class="cert-icon">
                    <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                </div>
                <h3 class="cert-title">الامتثال التنظيمي</h3>
                <p class="cert-desc">تتم مراجعة وتجديد الشهادات في دورة مدتها خمس سنوات تماشياً مع المتطلبات الوطنية.</p>
            </div>
        </div>
    </div>
</section>
'''

services_en = '''
<section class="wrap" style="padding: 80px 40px;">
    <div class="flip-grid">
        <!-- Service 1 -->
        <div class="flip-card reveal in" onclick="openSvcModal(0)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1466611653911-95081537e5b7?q=80&w=600" alt="Environmental Studies">
                    <div class="flip-card-front-content">
                        <h3>1. Environmental Studies</h3>
                        <p style="color: var(--ink2);">EIA, audits, compliance and risk-management plans.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">Environmental Studies</h3>
                    <p>Comprehensive baseline assessments, management plans, and environmental compliance audits.</p>
                    <button>Learn More</button>
                </div>
            </div>
        </div>
        
        <!-- Service 2 -->
        <div class="flip-card reveal in" onclick="openSvcModal(1)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1621255530635-c8e19574409b?q=80&w=600" alt="Environmental Measurements">
                    <div class="flip-card-front-content">
                        <h3>2. Environmental Measurements</h3>
                        <p style="color: var(--ink2);">Field monitoring of air, water, noise and emissions.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">Measurements</h3>
                    <p>Precise field monitoring for work environments, wastewater analysis, and stack emissions.</p>
                    <button>Learn More</button>
                </div>
            </div>
        </div>

        <!-- Service 3 -->
        <div class="flip-card reveal in" onclick="openSvcModal(2)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1541963463532-d68292c34b19?q=80&w=600" alt="Environmental Modeling">
                    <div class="flip-card-front-content">
                        <h3>3. Environmental Modeling</h3>
                        <p style="color: var(--ink2);">Air, noise, thermal and groundwater dispersion modeling.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">Modeling</h3>
                    <p>Simulating heat plumes and predicting the spread of airborne pollutants under real conditions.</p>
                    <button>Learn More</button>
                </div>
            </div>
        </div>

        <!-- Service 4 -->
        <div class="flip-card reveal in" onclick="openSvcModal(3)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1620509652597-9e4776e05bf1?q=80&w=600" alt="Sustainability">
                    <div class="flip-card-front-content">
                        <h3>4. Sustainability & Carbon</h3>
                        <p style="color: var(--ink2);">Carbon footprint auditing, ESG and green-building advisory.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">Sustainability</h3>
                    <p>Environmental design input for lower-impact, resource-efficient facilities.</p>
                    <button>Learn More</button>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Service Modals (Injected via JS) -->
<div class="svc-modal" id="svcModal">
    <div class="svc-modal-content">
        <button class="svc-modal-close" onclick="document.getElementById('svcModal').classList.remove('open')">&times;</button>
        <div class="svc-modal-header">
            <h2 id="svcTitle">Service Title</h2>
        </div>
        <div class="svc-modal-body" id="svcBody">
            <!-- Content -->
        </div>
        <div class="svc-modal-footer">
            <a href="contact.html" class="btn-primary" style="margin:0;">Book an Appointment</a>
        </div>
    </div>
</div>

<script>
const servicesData = [
    {
        title: "1. Environmental Studies",
        items: [
            "Environmental & Social Impact Assessment (EIA/ESIA)",
            "Environmental Audits (EA)",
            "Environmental Compliance Plans",
            "Baseline Environmental Component Assessment",
            "Environmental Response Plans (ERP)",
            "Environmental Management Plans (EMP)",
            "Hazardous Waste Management Plans",
            "Solid Waste Management Programs (SWMP)",
            "Environmental Risk Assessment (ERA)",
            "Biodiversity Action Plans (BAP)",
            "Environment, Health & Safety (EHS)",
            "Environmental Records & Registers"
        ]
    },
    {
        title: "2. Environmental Measurements",
        items: [
            "Ambient Air Quality",
            "Work Environment (Air, Water, Soil)",
            "Suspended & Inhalable Particulates",
            "Wastewater Analysis (Sanitary & Industrial)",
            "Stack Emissions",
            "Ambient Noise",
            "Water Quality",
            "Thermal Comfort / Heat Stress"
        ]
    },
    {
        title: "3. Environmental Modeling",
        items: [
            "Air Dispersion Modeling: Predicting the spread of airborne pollutants.",
            "Noise Dispersion Modeling: Mapping expected noise propagation.",
            "Thermal Dispersion Modeling: Simulating heat plumes.",
            "Groundwater Dispersion Modeling: Tracking potential migration of contaminants.",
            "Quantitative Risk Assessment: Numerically evaluating hazard likelihood.",
            "Surface Exposure & Illumination Studies"
        ]
    },
    {
        title: "4. Sustainability & Carbon Footprint",
        items: [
            "Carbon Footprint Auditing: Measurement and independent verification.",
            "ESG Advisory: Environmental, social and governance strategy.",
            "Green Building Guidance: Environmental design input for lower-impact facilities.",
            "Capacity Building: Training and awareness programs."
        ]
    }
];

function openSvcModal(index) {
    const data = servicesData[index];
    document.getElementById('svcTitle').innerText = data.title;
    let listHTML = '<ul>';
    data.items.forEach(i => listHTML += `<li>${i}</li>`);
    listHTML += '</ul>';
    document.getElementById('svcBody').innerHTML = listHTML;
    document.getElementById('svcModal').classList.add('open');
}

// Close on outside click
document.getElementById('svcModal').addEventListener('click', function(e) {
    if(e.target === this) this.classList.remove('open');
});
</script>
'''

services_ar = '''
<section class="wrap" style="padding: 80px 40px;">
    <div class="flip-grid">
        <!-- Service 1 -->
        <div class="flip-card reveal in" onclick="openSvcModal(0)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1466611653911-95081537e5b7?q=80&w=600" alt="Environmental Studies">
                    <div class="flip-card-front-content">
                        <h3>1. الدراسات البيئية</h3>
                        <p style="color: var(--ink2);">تقييم الأثر البيئي، التدقيق، وخطط الامتثال وإدارة المخاطر.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">الدراسات البيئية</h3>
                    <p>التقييمات الأساسية الشاملة، وخطط الإدارة، وعمليات تدقيق الامتثال البيئي.</p>
                    <button>اعرف المزيد</button>
                </div>
            </div>
        </div>
        
        <!-- Service 2 -->
        <div class="flip-card reveal in" onclick="openSvcModal(1)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1621255530635-c8e19574409b?q=80&w=600" alt="Environmental Measurements">
                    <div class="flip-card-front-content">
                        <h3>2. القياسات البيئية</h3>
                        <p style="color: var(--ink2);">المراقبة الميدانية للهواء والماء والضوضاء والانبعاثات.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">القياسات البيئية</h3>
                    <p>مراقبة ميدانية دقيقة لبيئات العمل، وتحليل مياه الصرف الصحي، وانبعاثات المداخن.</p>
                    <button>اعرف المزيد</button>
                </div>
            </div>
        </div>

        <!-- Service 3 -->
        <div class="flip-card reveal in" onclick="openSvcModal(2)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1541963463532-d68292c34b19?q=80&w=600" alt="Environmental Modeling">
                    <div class="flip-card-front-content">
                        <h3>3. النمذجة البيئية</h3>
                        <p style="color: var(--ink2);">نمذجة تشتت الهواء والضوضاء والحرارة والمياه الجوفية.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">النمذجة البيئية</h3>
                    <p>محاكاة الأعمدة الحرارية والتنبؤ بانتشار الملوثات المحمولة جواً في ظل ظروف التشغيل الحقيقية.</p>
                    <button>اعرف المزيد</button>
                </div>
            </div>
        </div>

        <!-- Service 4 -->
        <div class="flip-card reveal in" onclick="openSvcModal(3)">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <img src="https://images.unsplash.com/photo-1620509652597-9e4776e05bf1?q=80&w=600" alt="Sustainability">
                    <div class="flip-card-front-content">
                        <h3>4. الاستدامة والبصمة الكربونية</h3>
                        <p style="color: var(--ink2);">تدقيق البصمة الكربونية، الحوكمة البيئية والاجتماعية.</p>
                    </div>
                </div>
                <div class="flip-card-back">
                    <h3 style="font-family: var(--fd); font-size: 26px; margin-bottom: 15px;">الاستدامة</h3>
                    <p>مدخلات التصميم البيئي لمنشآت ذات تأثير أقل وكفاءة في استخدام الموارد.</p>
                    <button>اعرف المزيد</button>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Service Modals (Injected via JS) -->
<div class="svc-modal" id="svcModal">
    <div class="svc-modal-content" style="text-align: right;">
        <button class="svc-modal-close" onclick="document.getElementById('svcModal').classList.remove('open')">&times;</button>
        <div class="svc-modal-header">
            <h2 id="svcTitle">عنوان الخدمة</h2>
        </div>
        <div class="svc-modal-body" id="svcBody">
            <!-- Content -->
        </div>
        <div class="svc-modal-footer" style="justify-content: flex-start;">
            <a href="contact.html" class="btn-primary" style="margin:0;">احجز موعداً</a>
        </div>
    </div>
</div>

<script>
const servicesData = [
    {
        title: "1. الدراسات البيئية",
        items: [
            "تقييم الأثر البيئي والاجتماعي (EIA/ESIA)",
            "التدقيق البيئي (EA)",
            "خطط الامتثال البيئي",
            "تقييم مكونات البيئة الأساسية",
            "خطط الاستجابة البيئية (ERP)",
            "خطط الإدارة البيئية (EMP)",
            "خطط إدارة النفايات الخطرة",
            "برامج إدارة النفايات الصلبة (SWMP)",
            "تقييم المخاطر البيئية (ERA)",
            "خطط عمل التنوع البيولوجي (BAP)",
            "البيئة والصحة والسلامة (EHS)",
            "السجلات والدفاتر البيئية"
        ]
    },
    {
        title: "2. القياسات البيئية",
        items: [
            "جودة الهواء المحيط",
            "بيئة العمل (هواء، ماء، تربة)",
            "الجسيمات العالقة والقابلة للاستنشاق",
            "تحليل مياه الصرف (الصحي والصناعي)",
            "انبعاثات المداخن",
            "الضوضاء المحيطة",
            "جودة المياه",
            "الراحة الحرارية / الإجهاد الحراري"
        ]
    },
    {
        title: "3. النمذجة البيئية",
        items: [
            "نمذجة تشتت الهواء: التنبؤ بانتشار الملوثات المحمولة جواً.",
            "نمذجة تشتت الضوضاء: رسم خرائط انتشار الضوضاء المتوقعة.",
            "نمذجة التشتت الحراري: محاكاة الأعمدة الحرارية.",
            "نمذجة تشتت المياه الجوفية: تتبع الهجرة المحتملة للملوثات.",
            "التقييم الكمي للمخاطر: التقييم الرقمي لاحتمالية الخطر.",
            "دراسات التعرض السطحي والإضاءة"
        ]
    },
    {
        title: "4. الاستدامة والبصمة الكربونية",
        items: [
            "تدقيق البصمة الكربونية: القياس والتحقق المستقل.",
            "استشارات الحوكمة البيئية والاجتماعية (ESG): الاستراتيجية المتوافقة مع الأطر الدولية.",
            "إرشادات المباني الخضراء: مدخلات التصميم البيئي للمنشآت.",
            "بناء القدرات: برامج التدريب والتوعية."
        ]
    }
];

function openSvcModal(index) {
    const data = servicesData[index];
    document.getElementById('svcTitle').innerText = data.title;
    let listHTML = '<ul style="padding-inline-start: 0; padding-inline-end: 20px;">';
    data.items.forEach(i => listHTML += `<li>${i}</li>`);
    listHTML += '</ul>';
    document.getElementById('svcBody').innerHTML = listHTML;
    document.getElementById('svcModal').classList.add('open');
}

// Close on outside click
document.getElementById('svcModal').addEventListener('click', function(e) {
    if(e.target === this) this.classList.remove('open');
});
</script>
'''

contact_en = '''
<section class="wrap" style="padding: 80px 40px;">
    <div class="contact-layout">
        
        <!-- Contact Details -->
        <div class="reveal in">
            <h2 class="st" style="margin-bottom: 40px;">Offices & Locations</h2>
            
            <div style="margin-bottom: 30px; background: var(--off); padding: 30px; border-radius: 8px; border-left: 3px solid var(--brand);">
                <h3 style="font-family: var(--fd); font-size: 24px; color: var(--brand); margin-bottom: 8px;">Alexandria (Head Office)</h3>
                <p style="color: var(--ink2); font-size: 18px;">Bahari, El-Anfoushi, Alexandria, Egypt</p>
            </div>
            
            <div style="margin-bottom: 30px; background: var(--off); padding: 30px; border-radius: 8px; border-left: 3px solid var(--brand);">
                <h3 style="font-family: var(--fd); font-size: 24px; color: var(--brand); margin-bottom: 8px;">Amman / 10th of Ramadan</h3>
                <p style="color: var(--ink2); font-size: 18px;">Al-Hejaz Mall, Jordan &mdash; 10th of Ramadan City, Egypt</p>
            </div>
            
            <div style="margin-bottom: 40px; background: var(--off); padding: 30px; border-radius: 8px; border-left: 3px solid var(--brand);">
                <h3 style="font-family: var(--fd); font-size: 24px; color: var(--brand); margin-bottom: 8px;">Tanta Office</h3>
                <p style="color: var(--ink2); font-size: 18px;">Alexandria-Cairo Agricultural Road, Tanta, Gharbia, Egypt</p>
            </div>

            <div style="margin-top: 50px;">
                <h2 class="st" style="margin-bottom: 20px; font-size: 30px;">Direct Contact</h2>
                <p style="font-size: 18px; color: var(--ink); margin-bottom: 10px;"><strong>Phone:</strong> +20 100 308 4597 &nbsp;|&nbsp; +20 155 257 7665</p>
                <p style="font-size: 18px; color: var(--ink);"><strong>Email:</strong> hu_gar2000@azhar.edu.com</p>
                <p style="font-size: 18px; color: var(--ink);"><strong>Email:</strong> HuElnaggar@metoceanms.com</p>
            </div>
        </div>

        <!-- Contact Form -->
        <div class="reveal in">
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Thank you for reaching out. We will get back to you shortly.');">
                <h3 style="font-family: var(--fd); font-size: 32px; color: var(--brand); margin-bottom: 20px;">Send a Message</h3>
                <p style="color: var(--ink2); margin-bottom: 30px;">For inquiries, partnership requests, or training information, please fill out the form below.</p>
                
                <div class="form-group">
                    <label for="name">Full Name</label>
                    <input type="text" id="name" required placeholder="John Doe">
                </div>
                
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" required placeholder="john@company.com">
                </div>
                
                <div class="form-group">
                    <label for="subject">Subject</label>
                    <input type="text" id="subject" required placeholder="Project Inquiry">
                </div>
                
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" required placeholder="How can we help you?"></textarea>
                </div>
                
                <button type="submit" class="btn-primary" style="width: 100%; justify-content: center;">Send Message</button>
            </form>
        </div>

    </div>
</section>
'''

contact_ar = '''
<section class="wrap" style="padding: 80px 40px;">
    <div class="contact-layout">
        
        <!-- Contact Details -->
        <div class="reveal in">
            <h2 class="st" style="margin-bottom: 40px;">المكاتب والمواقع</h2>
            
            <div style="margin-bottom: 30px; background: var(--off); padding: 30px; border-radius: 8px; border-right: 3px solid var(--brand);">
                <h3 style="font-family: var(--fd); font-size: 24px; color: var(--brand); margin-bottom: 8px;">الإسكندرية (المقر الرئيسي)</h3>
                <p style="color: var(--ink2); font-size: 18px;">بحري، الأنفوشي، الإسكندرية، مصر</p>
            </div>
            
            <div style="margin-bottom: 30px; background: var(--off); padding: 30px; border-radius: 8px; border-right: 3px solid var(--brand);">
                <h3 style="font-family: var(--fd); font-size: 24px; color: var(--brand); margin-bottom: 8px;">عمان / العاشر من رمضان</h3>
                <p style="color: var(--ink2); font-size: 18px;">مول الحجاز، الأردن &mdash; مدينة العاشر من رمضان، مصر</p>
            </div>
            
            <div style="margin-bottom: 40px; background: var(--off); padding: 30px; border-radius: 8px; border-right: 3px solid var(--brand);">
                <h3 style="font-family: var(--fd); font-size: 24px; color: var(--brand); margin-bottom: 8px;">مكتب طنطا</h3>
                <p style="color: var(--ink2); font-size: 18px;">طريق الإسكندرية-القاهرة الزراعي، طنطا، الغربية، مصر</p>
            </div>

            <div style="margin-top: 50px;">
                <h2 class="st" style="margin-bottom: 20px; font-size: 30px;">تواصل مباشر</h2>
                <p style="font-size: 18px; color: var(--ink); margin-bottom: 10px;"><strong>الهاتف:</strong> <span dir="ltr">+20 100 308 4597</span> &nbsp;|&nbsp; <span dir="ltr">+20 155 257 7665</span></p>
                <p style="font-size: 18px; color: var(--ink);"><strong>البريد الإلكتروني:</strong> hu_gar2000@azhar.edu.com</p>
                <p style="font-size: 18px; color: var(--ink);"><strong>البريد الإلكتروني:</strong> HuElnaggar@metoceanms.com</p>
            </div>
        </div>

        <!-- Contact Form -->
        <div class="reveal in">
            <form class="contact-form" onsubmit="event.preventDefault(); alert('شكراً لتواصلك معنا. سنقوم بالرد عليك قريباً.');">
                <h3 style="font-family: var(--fd); font-size: 32px; color: var(--brand); margin-bottom: 20px;">أرسل رسالة</h3>
                <p style="color: var(--ink2); margin-bottom: 30px;">للاستفسارات أو طلبات الشراكة أو معلومات التدريب، يرجى ملء النموذج أدناه.</p>
                
                <div class="form-group">
                    <label for="name">الاسم الكامل</label>
                    <input type="text" id="name" required placeholder="أحمد محمد">
                </div>
                
                <div class="form-group">
                    <label for="email">البريد الإلكتروني</label>
                    <input type="email" id="email" required placeholder="ahmed@company.com">
                </div>
                
                <div class="form-group">
                    <label for="subject">الموضوع</label>
                    <input type="text" id="subject" required placeholder="استفسار عن مشروع">
                </div>
                
                <div class="form-group">
                    <label for="message">الرسالة</label>
                    <textarea id="message" required placeholder="كيف يمكننا مساعدتك؟"></textarea>
                </div>
                
                <button type="submit" class="btn-primary" style="width: 100%; justify-content: center;">إرسال الرسالة</button>
            </form>
        </div>

    </div>
</section>
'''

courses_en = '''
<section class="wrap" style="padding: 80px 40px; text-align: center;">
    <div style="max-width: 800px; margin: 0 auto;" class="reveal in">
        <h2 class="st" style="margin-bottom: 24px;">Training & Capacity Building</h2>
        <p style="color: var(--ink2); font-size: 18px; line-height: 1.8;">MetOcean offers comprehensive training and awareness programs that embed sustainability within client teams. Detailed course schedules and syllabus information will be updated soon. Please contact us directly for corporate training inquiries.</p>
        <a href="contact.html" class="btn-primary" style="margin-top: 30px;">Contact for Training</a>
    </div>
</section>
'''
courses_ar = '''
<section class="wrap" style="padding: 80px 40px; text-align: center;">
    <div style="max-width: 800px; margin: 0 auto;" class="reveal in">
        <h2 class="st" style="margin-bottom: 24px;">التدريب وبناء القدرات</h2>
        <p style="color: var(--ink2); font-size: 18px; line-height: 1.8;">تقدم ميتوشيان برامج تدريبية وتوعوية شاملة لترسيخ الاستدامة داخل فرق العملاء. سيتم تحديث جداول الدورات التفصيلية ومعلومات المناهج الدراسية قريباً. يرجى الاتصال بنا مباشرة للاستفسارات المتعلقة بالتدريب للشركات.</p>
        <a href="contact.html" class="btn-primary" style="margin-top: 30px;">تواصل معنا للتدريب</a>
    </div>
</section>
'''

login_en = '''
<section class="wrap" style="padding: 120px 40px; text-align: center;">
    <div style="max-width: 400px; margin: 0 auto;" class="reveal in">
        <h2 class="st" style="margin-bottom: 24px;">Client Portal</h2>
        <p style="color: var(--ink2); font-size: 18px; margin-bottom: 30px;">Please enter your credentials to access your project dashboard.</p>
        <input type="text" placeholder="Username or Email" style="width: 100%; padding: 15px; margin-bottom: 15px; border: 1px solid var(--lg); border-radius: 4px; font-family: var(--fb);">
        <input type="password" placeholder="Password" style="width: 100%; padding: 15px; margin-bottom: 25px; border: 1px solid var(--lg); border-radius: 4px; font-family: var(--fb);">
        <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="alert('Portal login coming soon.')">Login</button>
    </div>
</section>
'''

login_ar = '''
<section class="wrap" style="padding: 120px 40px; text-align: center;">
    <div style="max-width: 400px; margin: 0 auto;" class="reveal in">
        <h2 class="st" style="margin-bottom: 24px;">بوابة العملاء</h2>
        <p style="color: var(--ink2); font-size: 18px; margin-bottom: 30px;">يرجى إدخال بيانات الاعتماد الخاصة بك للوصول إلى لوحة معلومات مشروعك.</p>
        <input type="text" placeholder="اسم المستخدم أو البريد الإلكتروني" style="width: 100%; padding: 15px; margin-bottom: 15px; border: 1px solid var(--lg); border-radius: 4px; font-family: var(--fb);">
        <input type="password" placeholder="كلمة المرور" style="width: 100%; padding: 15px; margin-bottom: 25px; border: 1px solid var(--lg); border-radius: 4px; font-family: var(--fb);">
        <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="alert('سيتم إطلاق بوابة العملاء قريباً.')">تسجيل الدخول</button>
    </div>
</section>
'''

create_page('about.html', 'en', 'About Us', 'من نحن', about_en, about_ar)
create_page('about.html', 'ar', 'About Us', 'من نحن', about_en, about_ar)

create_page('services.html', 'en', 'Our Services', 'خدماتنا', services_en, services_ar)
create_page('services.html', 'ar', 'Our Services', 'خدماتنا', services_en, services_ar)

create_page('contact.html', 'en', 'Contact Us', 'اتصل بنا', contact_en, contact_ar)
create_page('contact.html', 'ar', 'Contact Us', 'اتصل بنا', contact_en, contact_ar)

create_page('courses.html', 'en', 'Courses', 'الدورات', courses_en, courses_ar)
create_page('courses.html', 'ar', 'Courses', 'الدورات', courses_en, courses_ar)

create_page('login.html', 'en', 'Client Login', 'تسجيل دخول العملاء', login_en, login_ar)
create_page('login.html', 'ar', 'Client Login', 'تسجيل دخول العملاء', login_en, login_ar)
