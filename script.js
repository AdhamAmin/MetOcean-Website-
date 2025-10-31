// Import Firebase modules
// This script must be loaded *after* the Firebase SDKs are imported in the HTML
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";
import { 
    getAuth, 
    signInAnonymously, 
    signInWithCustomToken, 
    onAuthStateChanged,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    signOut
} from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";
import { 
    getFirestore, 
    doc, 
    setDoc, 
    addDoc, 
    collection,
    serverTimestamp
} from "https://www.gstatic.com/firebasejs/11.6.1/firebase-firestore.js";

// --- Global Firebase Variables ---
let auth;
let db;
let userId;

/**
 * Loads HTML content from a file into an element.
 * @param {string} url - The URL of the HTML file to fetch.
 * @param {string} elementId - The ID of the element to inject the HTML into.
 */
async function loadHTML(url, elementId) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Failed to fetch ${url}: ${response.statusText}`);
        }
        const text = await response.text();
        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = text;
        } else {
            console.warn(`Element with ID '${elementId}' not found.`);
        }
    } catch (error) {
        console.error(`Error loading HTML into ${elementId}:`, error);
    }
}

/**
 * Loads the header and footer, then initializes the main app logic.
 */
async function loadHeaderAndFooter() {
    await Promise.all([
        loadHTML('header.html', 'header-placeholder'),
        loadHTML('footer.html', 'footer-placeholder')
    ]);
    
    // After HTML is loaded, initialize the rest of the app logic
    initializeAppLogic();
}

/**
 * Main function to initialize Firebase and attach event handlers.
 * This runs *after* the header and footer are loaded.
 */
function initializeAppLogic() {
    try {
        // Get Firebase config from global variable (must be set in HTML)
        const firebaseConfig = JSON.parse(__firebase_config);
        const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        auth = getAuth(app);
        db = getFirestore(app);

        console.log("Firebase Initialized Successfully");

        // --- Authentication ---
        onAuthStateChanged(auth, async (user) => {
            if (user) {
                // User is signed in
                userId = user.uid;
                console.log("User is signed in:", userId);
                updateLoginState(user);
            } else {
                // User is signed out
                userId = null;
                console.log("User is signed out.");
                updateLoginState(null);
                
                // Try to sign in with custom token if available, else sign in anonymously
                if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) {
                    try {
                        await signInWithCustomToken(auth, __initial_auth_token);
                        console.log("Signed in with custom token.");
                    } catch (error) {
                        console.error("Custom token sign-in failed, trying anonymous:", error);
                        await signInAnonymously(auth);
                        console.log("Signed in anonymously after token fail.");
                    }
                } else {
                    await signInAnonymously(auth);
                    console.log("Signed in anonymously.");
                }
            }
        });

    } catch (e) {
        console.error("Firebase initialization error:", e);
        console.error("Please make sure your Firebase config is set up correctly.");
    }

    // --- Active Nav Link ---
    // This code finds the current page and adds the 'active' class to the matching nav link
    try {
        let currentPage = window.location.pathname.split("/").pop();
        if (currentPage === "") { // Handle root (index.html)
            currentPage = "index.html";
        }
        const navLinks = document.querySelectorAll("nav a");
        navLinks.forEach(link => {
            const linkHref = link.getAttribute("href");
            if (linkHref === currentPage) {
                link.classList.add("active");
            }
        });
    } catch (e) {
        console.warn("Could not set active nav link:", e);
    }


    // --- Attach all window functions to make them globally accessible ---
    // This ensures onclick attributes in the loaded HTML can find them.

    window.performSearch = function() {
        const query = document.getElementById('searchInput').value;
        if (query.trim()) {
            showInfoModal('Search', 'Searching for: ' + query + '\n\nSearch results page would display here.');
        }
    }

    // Enter key search
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }

    window.showSignUp = function() {
        const modal = document.getElementById('signupModal');
        if (modal) modal.classList.add('active');
    }

    // NEW: Function to show the login modal
    window.showLogin = function() {
        const modal = document.getElementById('loginModal');
        if (modal) modal.classList.add('active');
    }

    // NEW: Function to switch between modals
    window.switchModals = function(fromModalId, toModalId) {
        closeModal(fromModalId);
        
        // Use a slight delay to make the switch feel smoother
        setTimeout(() => {
            if (toModalId === 'loginModal') {
                showLogin();
            } else if (toModalId === 'signupModal') {
                showSignUp();
            }
        }, 300); // 300ms matches the animation speed
    }

    // NEW: Function to toggle password visibility
    window.togglePasswordVisibility = function(inputId) {
        const input = document.getElementById(inputId);
        const icon = input.nextElementSibling; // Get the icon
        if (input.type === "password") {
            input.type = "text";
            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");
        } else {
            input.type = "password";
            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");
        }
    }


    window.showForgotPassword = function() {
        const modal = document.getElementById('forgotPasswordModal');
        if (modal) modal.classList.add('active');
    }

    window.closeModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('active');

            // If closing the video modal, stop the video
            if (modalId === 'videoModal') {
                const videoIframe = document.getElementById('videoModalIframe');
                if (videoIframe) {
                    videoIframe.src = ''; // This stops the video from playing
                }
            }
        }
    }
    
    /**
     * Shows the video modal and sets the YouTube video source.
     * @param {string} youtubeId - The ID of the YouTube video (e.g., '5Gq-L1soS7s')
     */
    window.showVideoModal = function(youtubeId) {
        const modal = document.getElementById('videoModal');
        const iframe = document.getElementById('videoModalIframe');
        
        if (modal && iframe) {
            iframe.src = `https://www.youtube.com/embed/${youtubeId}?autoplay=1&rel=0`;
            modal.classList.add('active');
        } else {
            console.error('Video modal or iframe not found.');
        }
    }


    window.toggleChat = function() {
        const modal = document.getElementById('chatModal');
        if (modal) modal.classList.toggle('active');
    }

    // Close modal when clicking outside
    window.onclick = function(event) {
        if (event.target.classList.contains('modal')) {
            window.closeModal(event.target.id);
        }
    }

    window.handleLogin = async function(event) {
        event.preventDefault();
        const email = event.target.email.value;
        const password = event.target.password.value;

        if (!auth) {
            showInfoModal("Error", "Authentication service is not ready. Please try again in a moment.");
            return;
        }

        try {
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            console.log("User logged in:", userCredential.user);
            closeModal('loginModal');
            showInfoModal("Success", `Welcome back, ${email}!`);
            // No redirect needed, state will update
        } catch (error) {
            console.error("Login failed:", error);
            showInfoModal("Login Failed", error.message);
        }
    }

    window.handleSignUp = async function(event) {
        event.preventDefault();
        const firstName = event.target.firstName.value;
        const lastName = event.target.lastName.value;
        const email = event.target.email.value;
        const password = event.target.password.value;

        if (!auth || !db) {
            showInfoModal("Error", "Database service is not ready. Please try again in a moment.");
            return;
        }

        try {
            const userCredential = await createUserWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;
            console.log("User created in Auth:", user);

            const userDocRef = doc(db, "users", user.uid);
            await setDoc(userDocRef, {
                firstName: firstName,
                lastName: lastName,
                email: email,
                createdAt: serverTimestamp()
            });

            console.log("User document created in Firestore");
            closeModal('signupModal');
            showInfoModal("Account Created!", "Welcome to OceanSustain! Your account has been created successfully.");

        } catch (error) {
            console.error("Sign-up failed:", error);
            showInfoModal("Sign-up Failed", error.message);
        }
    }

    window.handleContactForm = async function(event) {
        event.preventDefault();
        const inquiryType = event.target.inquiryType.value;
        const name = event.target.name.value;
        const email = event.target.email.value;
        const phone = event.target.phone.value;
        const message = event.target.message.value;

        if (!db) {
            showInfoModal("Error", "Database service is not ready. Please try again in a moment.");
            return;
        }

        try {
            const docRef = await addDoc(collection(db, "messages"), {
                type: "Contact Inquiry",
                inquiryType: inquiryType,
                name: name,
                email: email,
                phone: phone,
                message: message,
                timestamp: serverTimestamp(),
                read: false,
                userId: auth.currentUser ? auth.currentUser.uid : 'anonymous'
            });
            
            console.log("Contact message saved with ID: ", docRef.id);
            showInfoModal("Message Sent!", "Thank you for contacting us. Your message has been received and we will get back to you shortly.");
            event.target.reset();

        } catch (error) {
            console.error("Error sending message:", error);
            showInfoModal("Error", "There was a problem sending your message. Please try again.");
        }
    }

    window.handleHelpRequest = async function() {
        if (!db || !auth.currentUser) {
            showInfoModal("Error", "You must be logged in to request help. If this persists, please contact us directly.");
            return;
        }

        const user = auth.currentUser;

        try {
            await addDoc(collection(db, "messages"), {
                type: "HELP_REQUEST",
                message: "User clicked the 'I need help!' button.",
                timestamp: serverTimestamp(),
                read: false,
                priority: true,
                userId: user.uid,
                email: user.email || 'N/A'
            });
            
            showInfoModal("Help Request Sent", "We've received your urgent request. Someone from our team will reach out to you as soon as possible.");
            closeModal('chatModal');

        } catch (error) {
            console.error("Error sending help request:", error);
            showInfoModal("Error", "There was a problem sending your request. Please try again.");
        }
    }

    window.handleForgotPassword = function(event) {
        event.preventDefault();
        showInfoModal("Password Reset", "Password reset functionality is being set up. For now, please contact support.");
        closeModal('forgotPasswordModal');
    }

    window.handleNewsletter = function(event) {
        event.preventDefault();
        const email = event.target.email.value;
        console.log("Newsletter subscription for:", email);
        showInfoModal("Subscribed!", "Thank you for subscribing to our newsletter!");
        event.target.reset();
    }

    window.handleChatMessage = function(event) {
        event.preventDefault();
        const input = event.target.querySelector('input');
        if (input.value.trim()) {
            console.log("Chat message:", input.value);
            
            const messageBox = document.querySelector('.chat-message-box');
            const userMessage = document.createElement('div');
            userMessage.className = 'chat-message';
            userMessage.style.background = '#e1f5fe';
            userMessage.innerHTML = `<strong>You</strong><p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">${input.value}</p>`;
            messageBox.appendChild(userMessage);
            messageBox.scrollTop = messageBox.scrollHeight;

            input.value = '';
            
            setTimeout(() => {
                const replyMessage = document.createElement('div');
                replyMessage.className = 'chat-message';
                replyMessage.innerHTML = `<strong>OceanSustain Support</strong><p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Thanks for your message! This is a demo chat. For help, click the 'I need help!' button.</p>`;
                messageBox.appendChild(replyMessage);
                messageBox.scrollTop = messageBox.scrollHeight;
            }, 1000);
        }
    }
}

/**
 * Updates the "Get Started" button to "Logout" if the user is signed in.
 */
function updateLoginState(user) {
    const getStartedLink = document.getElementById('get-started-link');
    if (!getStartedLink) return; // Happens if header hasn't loaded yet

    if (user && !user.isAnonymous) {
        // User is logged in
        getStartedLink.innerHTML = `<i class="fas fa-sign-out-alt"></i> Logout`;
        getStartedLink.href = "#";
        getStartedLink.classList.remove('get-started-btn');
        getStartedLink.classList.add('logout-btn');
        getStartedLink.onclick = (e) => {
            e.preventDefault();
            signOut(auth).catch(err => console.error("Logout error:", err));
        };
    } else {
        // User is logged out
        getStartedLink.innerHTML = `Get Started`;
        getStartedLink.href = "#"; // It's a modal trigger, not a page link
        getStartedLink.classList.remove('logout-btn');
        getStartedLink.classList.add('get-started-btn');
        getStartedLink.onclick = (e) => {
            e.preventDefault();
            showSignUp();
        };
    }
}

/**
 * A simple, non-blocking modal for showing information or errors.
 * Replaces alert().
 */
function showInfoModal(title, message) {
    let infoModal = document.getElementById('infoModal');
    if (!infoModal) {
        // Create the modal HTML
        infoModal = document.createElement('div');
        infoModal.id = 'infoModal';
        infoModal.className = 'modal';
        infoModal.innerHTML = `
            <div class="modal-content" style="max-width: 400px;">
                <button class="modal-close" onclick="closeModal('infoModal')">&times;</button>
                <h2 id="infoModalTitle" style="color: var(--deep-blue); margin-bottom: 1rem;"></h2>
                <p id="infoModalMessage" style="line-height: 1.6;"></p>
                <button class="submit-button" style="margin-top: 1.5rem;" onclick="closeModal('infoModal')">OK</button>
            </div>
        `;
        document.body.appendChild(infoModal);
    }
    
    document.getElementById('infoModalTitle').textContent = title;
    document.getElementById('infoModalMessage').textContent = message;
    infoModal.classList.add('active');
}

// --- App Entry Point ---
// Start loading header/footer as soon as the DOM is ready.
document.addEventListener('DOMContentLoaded', loadHeaderAndFooter);

