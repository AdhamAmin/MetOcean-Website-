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
        .dl-close:hover {{ color: var(--red); }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        @keyframes popIn {{ from {{ transform: scale(0.9); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}
        .page-header {{ padding: 160px 40px 80px; text-align: center; background: var(--warm); border-bottom: 1px solid var(--lg); }}
    </style>
</head>
<body>
    <!-- NAV -->
    <nav id="navbar" class="scrolled">
        <a href="index.html" class="nav-logo">
            <span style="font-family:var(--fd);font-weight:900;font-size:32px;letter-spacing:1px;color:var(--red)">{'ميتوشيان' if is_ar else 'MetOcean'}</span>
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
        <div class="reveal in" style="background: var(--off); padding: 40px; border-radius: 8px; border-left: 4px solid var(--red);">
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">Vision</h3>
            <p style="color: var(--ink2); margin-bottom: 24px;">To be a leading force in Egypt's environmental sector — helping shape a sustainable community and economy, and working steadily toward a cleaner, greener environment.</p>
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">Mission</h3>
            <p style="color: var(--ink2);">To meet every client's needs through the best integrated environmental solutions, continuously developing our team and adopting the Best Available Techniques (BAT) and Best Environmental Practices (BEP).</p>
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
        <div class="reveal in" style="background: var(--off); padding: 40px; border-radius: 8px; border-right: 4px solid var(--red);">
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">رؤيتنا</h3>
            <p style="color: var(--ink2); margin-bottom: 24px;">أن نكون قوة رائدة في القطاع البيئي في مصر - نساعد في تشكيل مجتمع واقتصاد مستدامين، والعمل بثبات نحو بيئة أنظف وأكثر خضرة.</p>
            <h3 style="font-family: var(--fd); font-size: 24px; margin-bottom: 12px;">رسالتنا</h3>
            <p style="color: var(--ink2);">تلبية احتياجات كل عميل من خلال أفضل الحلول البيئية المتكاملة، وتطوير فريقنا باستمرار واعتماد أفضل التقنيات المتاحة (BAT) وأفضل الممارسات البيئية (BEP).</p>
        </div>
    </div>
</section>
'''

services_en = '''
<section class="wrap" style="padding: 80px 40px;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;">
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">1. Environmental Studies</h3>
            <p style="color: var(--ink2); line-height: 1.8;">EIA, audits, compliance and risk-management plans. Includes Baseline Environmental Component Assessment, Environmental Management Plans (EMP), and Biodiversity Action Plans (BAP).</p>
        </div>
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">2. Environmental Measurements</h3>
            <p style="color: var(--ink2); line-height: 1.8;">Field monitoring of air, water, noise and emissions. Includes Work Environment (Air, Water, Soil), Wastewater Analysis, and Stack Emissions.</p>
        </div>
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">3. Environmental Modeling</h3>
            <p style="color: var(--ink2); line-height: 1.8;">Air, noise, thermal and groundwater dispersion modeling. Simulating heat plumes and predicting the spread of airborne pollutants under real operating conditions.</p>
        </div>
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">4. Sustainability & Carbon</h3>
            <p style="color: var(--ink2); line-height: 1.8;">Carbon footprint auditing, ESG and green-building advisory. Environmental design input for lower-impact, resource-efficient facilities.</p>
        </div>
    </div>
</section>
'''

services_ar = '''
<section class="wrap" style="padding: 80px 40px;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;">
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">1. الدراسات البيئية</h3>
            <p style="color: var(--ink2); line-height: 1.8;">تقييم الأثر البيئي، التدقيق، وخطط الامتثال وإدارة المخاطر. يشمل ذلك تقييم مكونات البيئة الأساسية، وخطط الإدارة البيئية، وخطط عمل التنوع البيولوجي.</p>
        </div>
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">2. القياسات البيئية</h3>
            <p style="color: var(--ink2); line-height: 1.8;">المراقبة الميدانية للهواء والماء والضوضاء والانبعاثات. يشمل ذلك بيئة العمل (الهواء، الماء، التربة)، تحليل مياه الصرف الصحي، وانبعاثات المداخن.</p>
        </div>
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">3. النمذجة البيئية</h3>
            <p style="color: var(--ink2); line-height: 1.8;">نمذجة تشتت الهواء والضوضاء والحرارة والمياه الجوفية. محاكاة الأعمدة الحرارية والتنبؤ بانتشار الملوثات المحمولة جواً في ظل ظروف التشغيل الحقيقية.</p>
        </div>
        <div class="reveal in" style="border: 1px solid var(--lg); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 28px; margin-bottom: 16px; color: var(--red);">4. الاستدامة والبصمة الكربونية</h3>
            <p style="color: var(--ink2); line-height: 1.8;">تدقيق البصمة الكربونية، الحوكمة البيئية والاجتماعية، واستشارات المباني الخضراء. مدخلات التصميم البيئي لمنشآت ذات تأثير أقل وكفاءة في استخدام الموارد.</p>
        </div>
    </div>
</section>
'''

contact_en = '''
<section class="wrap" style="padding: 80px 40px; text-align: center;">
    <div style="max-width: 800px; margin: 0 auto;" class="reveal in">
        <h2 class="st" style="margin-bottom: 40px;">Offices & Locations</h2>
        
        <div style="margin-bottom: 40px; text-align: left; background: var(--off); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 24px; color: var(--red); margin-bottom: 8px;">Alexandria (Head Office)</h3>
            <p style="color: var(--ink2); font-size: 18px;">Bahari, El-Anfoushi, Alexandria, Egypt</p>
        </div>
        
        <div style="margin-bottom: 40px; text-align: left; background: var(--off); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 24px; color: var(--red); margin-bottom: 8px;">Amman / 10th of Ramadan</h3>
            <p style="color: var(--ink2); font-size: 18px;">Al-Hejaz Mall, Jordan &mdash; 10th of Ramadan City, Egypt</p>
        </div>
        
        <div style="margin-bottom: 40px; text-align: left; background: var(--off); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 24px; color: var(--red); margin-bottom: 8px;">Tanta Office</h3>
            <p style="color: var(--ink2); font-size: 18px;">Alexandria-Cairo Agricultural Road, Tanta, Gharbia, Egypt</p>
        </div>

        <div style="margin-top: 60px;">
            <h2 class="st" style="margin-bottom: 20px;">Direct Contact</h2>
            <p style="font-size: 20px; color: var(--ink); margin-bottom: 10px;"><strong>Phone:</strong> +20 100 308 4597 &nbsp;|&nbsp; +20 155 257 7665</p>
            <p style="font-size: 20px; color: var(--ink);"><strong>Email:</strong> hu_gar2000@azhar.edu.com &nbsp;|&nbsp; HuElnaggar@metoceanms.com</p>
        </div>
    </div>
</section>
'''

contact_ar = '''
<section class="wrap" style="padding: 80px 40px; text-align: center;">
    <div style="max-width: 800px; margin: 0 auto;" class="reveal in">
        <h2 class="st" style="margin-bottom: 40px;">المكاتب والمواقع</h2>
        
        <div style="margin-bottom: 40px; text-align: right; background: var(--off); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 24px; color: var(--red); margin-bottom: 8px;">الإسكندرية (المقر الرئيسي)</h3>
            <p style="color: var(--ink2); font-size: 18px;">بحري، الأنفوشي، الإسكندرية، مصر</p>
        </div>
        
        <div style="margin-bottom: 40px; text-align: right; background: var(--off); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 24px; color: var(--red); margin-bottom: 8px;">عمان / العاشر من رمضان</h3>
            <p style="color: var(--ink2); font-size: 18px;">مول الحجاز، الأردن &mdash; مدينة العاشر من رمضان، مصر</p>
        </div>
        
        <div style="margin-bottom: 40px; text-align: right; background: var(--off); padding: 30px; border-radius: 8px;">
            <h3 style="font-family: var(--fd); font-size: 24px; color: var(--red); margin-bottom: 8px;">مكتب طنطا</h3>
            <p style="color: var(--ink2); font-size: 18px;">طريق الإسكندرية-القاهرة الزراعي، طنطا، الغربية، مصر</p>
        </div>

        <div style="margin-top: 60px;">
            <h2 class="st" style="margin-bottom: 20px;">تواصل مباشر</h2>
            <p style="font-size: 20px; color: var(--ink); margin-bottom: 10px;"><strong dir="rtl">الهاتف:</strong> <span dir="ltr">+20 100 308 4597</span> &nbsp;|&nbsp; <span dir="ltr">+20 155 257 7665</span></p>
            <p style="font-size: 20px; color: var(--ink);"><strong dir="rtl">البريد الإلكتروني:</strong> hu_gar2000@azhar.edu.com &nbsp;|&nbsp; HuElnaggar@metoceanms.com</p>
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
