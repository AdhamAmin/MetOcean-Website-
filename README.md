# MetOcean Consulting - Website Project

A premium, fully responsive, and localized website for MetOcean Consulting, featuring high-end interactions, a strict first-visit user experience, and a polished mobile interface.

## 🚀 Key Features

### 1. Localization & Defaults
*   **Bilingual Support**: Full English (LTR) and Arabic (RTL) support with RTL-aware layout adjustments.
*   **Smart Defaults**: First-time visitors are defaulted to **English / Light Mode**.
*   **Persistence**: Language and Theme preferences are saved in `localStorage`.

### 2. Advanced User Experience (UX)
*   **Welcome Modal**: Sophisticated portal on the Homepage for first-time visitors to choose their language.
*   **Interactive Tour**: Guided tour with **Progress Indicators** (Step X of Y) helping users discover key site controls.
*   **Skip Option**: Users can now bypass the tour entirely via the "Skip Tour" button in the welcome modal.
*   **Search Overlay**: A full-screen, blur-effect search system that allows real-time content discovery with keyboard support (**ESC** to close).
*   **Scroll-to-Top**: A persistent, smart-floating button that appears after scrolling down 300px for easy navigation.

### 3. Visuals & Themes
*   **Inverted Theme Toggles**: The theme toggle button intelligently inverts its colors (Dark background/Light icon in Light mode and vice-versa) to ensure maximum visibility.
*   **Polished Animations**: Clean "Text Reveal" buttons, "Slide Up" element entries, and counting stats without being overwhelming.
*   **Responsive Typography**: Fluid headers and text scaled perfectly for mobile, tablet, and desktop viewports.

### 4. Mobile Optimized
*   **Glassmorphism Drawer**: A modern mobile side-menu with backdrop filters.
*   **App-style Carousel**: "Key Sectors" displayed as horizontal scrolling cards on mobile for a native application feel.

---

## 🛠 Recent Technical Changes & Fixes

### 1. Search Logic Implementation
*   **Feature**: Implemented a dynamic search system in `js/main.js` that scans the site's structure (Home, Services, About, etc.) and provides instant navigation results.
*   **UI**: Added a full-viewport overlay with backdrop-blur in `style.css`.

### 2. Persistent Scroll-to-Top
*   **Problem**: Button was only appearing on the homepage or after the first visit.
*   **Fix**: Refactored `loadIncludes()` to inject the scroll-to-top button on every page, ensuring accessibility site-wide.

### 3. Theme Toggle Accessibility
*   **Feature**: Enhanced the `.circle-btn` in the footer to use inverse color values. 
*   **Contrast**: In Light mode, the button is dark; in Dark mode, the button is light/body-colored. This guarantees the theme/language controls are always prominent.

### 4. Tour Guide Progress
*   **Improvement**: Added a `tour-progress` element to the tooltip. 
*   **Localization**: Used translation templates like `Step {current} of {total}` to support bilingual numbering.

---

## 📂 Project Structure

*   **/includes**: Contains `header.html` and `footer.html` components (loaded dynamically).
*   **/js**: `main.js` handles all logic (Localization, Search, Tour, Scroll Logic, Component Injection).
*   **/style.css**: Single source of truth for all styles (Desktop, Mobile, Themes, Animations).
*   **index.html**: Main entry point with Hero, Impact, and Sectors sections.

## ⚠️ Important for Testing
If you wish to re-test the "First Visit" or "Tour" experience:
1.  Open DevTools (F12) -> Application -> Local Storage.
2.  Delete the key: `metocean_visited`.
3.  **Hard Refresh** (Ctrl+Shift+R).

