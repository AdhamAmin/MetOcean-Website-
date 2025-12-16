# MetOcean Consulting - Website Project

A premium, fully responsive, and localized website for MetOcean Consulting, featuring high-end animations, a strict first-visit user experience, and a polished mobile interface.

## 🚀 Key Features

### 1. Localization & Defaults
*   **Bilingual Support**: Full English (LTR) and Arabic (RTL) definitions.
*   **Smart Defaults**: First-time visitors are forced to **English / Light Mode**.
*   **Persistence**: Language and Theme preferences are saved in `localStorage`.

### 2. User Experience (UX)
*   **Welcome Modal**: Appears **ONLY** on the Homepage (`index.html`) and **ONLY** on the very first visit.
*   **Interactive Tour**: Guided tour of the navigation and footer features, triggered immediately after selecting a language.
*   **Premium Animations**: "Text Reveal" buttons, "Slide Up" element entries, and counting stats.

### 3. Mobile Responsiveness / Phone View
*   **Glassmorphism Drawer**: A side-menu utilizing backdrop filters for a modern feel.
*   **Swipeable Cards**: "Key Sectors" display as a horizontal scrolling carousel (like an App Store) instead of a long vertical stack.
*   **Optimized Typography**: Headers and text scaled appropriately for small screens.
*   **Hidden Desktop Elements**: Video backgrounds or complex nav bars are simplified for mobile performance.

---

## 🛠 Recent Technical Changes & Fixes

### 1. Welcome Modal Logic (Strict Mode)
*   **Problem**: Users reported the Welcome Modal appearing on every page refresh or on sub-pages (e.g., Services).
*   **Root Cause**: Browser caching of old JavaScript and loose logic checking.
*   **Solution**: Implemented strict logic in `js/main.js`:
    ```javascript
    const isHomePage = path.endsWith('index.html') || path.endsWith('/');
    if (!hasVisited && isHomePage) { ... }
    ```
    *Note: Validated locally; strongly requires a Hard Refresh (Ctrl+Shift+R) to take effect.*

### 2. Mobile Hamburger Icon Visibility
*   **Problem**: Hamburger menu icon was missing on mobile devices.
*   **Root Cause**: The parent container `.nav-actions` was being hidden by CSS, which inadvertently hid the hamburger button inside it.
*   **Solution**: Adjusted `style.css` to only hide the *siblings* (`.btn`, `.icon-hover`) of the hamburger button, keeping the parent visible.

### 3. Key Sector Images "Compressed" on Mobile
*   **Problem**: Images in the "Key Sectors" carousel were squished/compressed on small screens.
*   **Root Cause**: A CSS class typo (`.destination-card` vs `.dest-card`) meant `min-width` wasn't applying.
*   **Solution**: Corrected the class name to `.dest-card` and verified `min-width: 280px` + `flex-shrink: 0`.

### 4. Clickable Cards
*   **Problem**: Key Sector cards were static `div` elements, confusing users who tried to click them.
*   **Solution**: Refactored `index.html` to wrap these cards in `<a href="services.html">` tags.

### 5. Footer Refinements
*   **Problem**: Footer bottom bar alignment was cluttered on desktop.
*   **Solution**:
    *   **Desktop**: Implemented a horizontal layout with a distinct separator line (Width: 90%) separating "Rights" (Left) and "Credits" (Right).
    *   **Mobile**: Stacked vertically for cleanliness.
    *   **Tweaks**: Increased top margin for better visual separation and reduced height for a slimmer profile.

---

## 📂 Project Structure

*   **/includes**: Contains `header.html` and `footer.html` components (loaded dynamically).
*   **/js**: `main.js` handles all logic (Localization, Modal, Loader, Component Injection).
*   **/style.css**: Single source of truth for all styles (Desktop, Mobile, Dark Mode, Animations).
*   **index.html**: The main entry point containing the unique Hero, Impact, and Sectors sections.

## ⚠️ Important for Testing
If you wish to re-test the "First Visit" experience:
1.  Open DevTools (F12) -> Application -> Local Storage.
2.  Delete keys: `metocean_visited`, `metocean_lang`, `metocean_theme`.
3.  **Hard Refresh** the page.
