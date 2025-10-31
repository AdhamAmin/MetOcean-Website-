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

// --- App Initialization ---
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

/**
 * Updates the "Login" link to "Logout" if the user is signed in.
 * This is a simple check and only works if the element exists on the page.
 */
function updateLoginState(user) {
    // This function is a bit of a placeholder.
    // In a real multi-page app, you'd check this on each page load.
    // We'll just log it for now.
    if (user && user.email) {
        console.log(`User ${user.email} is logged in.`);
        // Example: if you have a nav link with id="login-link"
        const loginLink = document.getElementById('login-link');
        if (loginLink) {
            loginLink.innerHTML = `<i class="fas fa-sign-out-alt"></i> Logout`;
            loginLink.href = "#"; // Prevent navigation
            loginLink.onclick = (e) => {
                e.preventDefault();
                signOut(auth).catch(err => console.error("Logout error:", err));
            };
        }
    } else {
         const loginLink = document.getElementById('login-link');
         if (loginLink) {
            loginLink.innerHTML = `<i class="fas fa-user"></i> Login`;
            loginLink.href = "login.html";
            loginLink.onclick = null; // Clear any previous onclick
         }
    }
}


// --- Search Function ---
window.performSearch = function() {
    const query = document.getElementById('searchInput').value;
    if (query.trim()) {
        // Use a modal for alerts
        showInfoModal('Search', 'Searching for: ' + query + '\n\nSearch results page would display here.');
    }
}

// Enter key search
// Add event listener only if the element exists
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

// --- Modal Functions ---
window.showSignUp = function() {
    const modal = document.getElementById('signupModal');
    if (modal) modal.classList.add('active');
}

window.showForgotPassword = function() {
    const modal = document.getElementById('forgotPasswordModal');
    if (modal) modal.classList.add('active');
}

window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove('active');
}

window.toggleChat = function() {
    const modal = document.getElementById('chatModal');
    if (modal) modal.classList.toggle('active');
}

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.classList.remove('active');
    }
}

/**
 * A simple, non-blocking modal for showing information or errors.
 * Replaces alert().
 */
function showInfoModal(title, message) {
    // Check if an info modal already exists
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
    
    // Set the content
    document.getElementById('infoModalTitle').textContent = title;
    document.getElementById('infoModalMessage').textContent = message;
    
    // Show the modal
    infoModal.classList.add('active');
}

// --- Form Handlers (Now with Firebase!) ---

/**
 * Handles the login form submission.
 */
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
        showInfoModal("Success", `Welcome back, ${email}!`);
        // Redirect to home page
        window.location.href = 'index.html';
    } catch (error) {
        console.error("Login failed:", error);
        showInfoModal("Login Failed", error.message);
    }
}

/**
 * Handles the sign-up form submission.
 * Creates a user in Firebase Auth and a document in Firestore.
 */
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
        // 1. Create user in Firebase Authentication
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        console.log("User created in Auth:", user);

        // 2. Create user document in Firestore
        const userDocRef = doc(db, "users", user.uid);
        await setDoc(userDocRef, {
            firstName: firstName,
            lastName: lastName,
            email: email,
            createdAt: serverTimestamp()
        });

        console.log("User document created in Firestore");
        showInfoModal("Account Created!", "Welcome to OceanSustain! Your account has been created successfully.");
        closeModal('signupModal');
        // Log the user in (they are already logged in, but just in case)
        window.location.href = 'index.html';

    } catch (error) {
        console.error("Sign-up failed:", error);
        showInfoModal("Sign-up Failed", error.message);
    }
}

/**
 * Handles the contact form submission.
 * Saves the message to the Firestore 'messages' collection.
 */
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
            read: false, // You can use this field in your dashboard
            userId: auth.currentUser ? auth.currentUser.uid : 'anonymous'
        });
        
        console.log("Contact message saved with ID: ", docRef.id);
        showInfoModal("Message Sent!", "Thank you for contacting us. Your message has been received and we will get back to you shortly.");
        event.target.reset(); // Clear the form

    } catch (error)
        {
        console.error("Error sending message:", error);
        showInfoModal("Error", "There was a problem sending your message. Please try again.");
    }
}

/**
 * Handles the "I need help!" button in the chat.
 * Saves a high-priority message to the 'messages' collection.
 */
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
            priority: true, // Mark as high priority
            userId: user.uid,
            email: user.email || 'N/A' // Include email if available
        });
        
        showInfoModal("Help Request Sent", "We've received your urgent request. Someone from our team will reach out to you as soon as possible.");
        closeModal('chatModal');

    } catch (error) {
        console.error("Error sending help request:", error);
        showInfoModal("Error", "There was a problem sending your request. Please try again.");
    }
}


// --- Other Form Handlers ---
window.handleForgotPassword = function(event) {
    event.preventDefault();
    // This functionality requires Firebase Auth, but it's
    // sendPasswordResetEmail(auth, email)
    // For now, we'll just show a message.
    showInfoModal("Password Reset", "Password reset functionality is being set up. For now, please contact support.");
    closeModal('forgotPasswordModal');
}

window.handleNewsletter = function(event) {
    event.preventDefault();
    const email = event.target.email.value;
    // In a real app, you'd save this to a 'newsletter' collection in Firestore
    console.log("Newsletter subscription for:", email);
    showInfoModal("Subscribed!", "Thank you for subscribing to our newsletter!");
    event.target.reset();
}

window.handleChatMessage = function(event) {
    event.preventDefault();
    const input = event.target.querySelector('input');
    if (input.value.trim()) {
        // In a real app, this would save to a 'chat' collection in Firestore
        console.log("Chat message:", input.value);
        
        // Add message to UI (demo)
        const messageBox = document.querySelector('.chat-message-box');
        const userMessage = document.createElement('div');
        userMessage.className = 'chat-message';
        userMessage.style.background = '#e1f5fe'; // User's message
        userMessage.innerHTML = `<strong>You</strong><p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">${input.value}</p>`;
        messageBox.appendChild(userMessage);
        messageBox.scrollTop = messageBox.scrollHeight; // Scroll to bottom

        input.value = '';
        
        // Simulate a reply
        setTimeout(() => {
            const replyMessage = document.createElement('div');
            replyMessage.className = 'chat-message';
            replyMessage.innerHTML = `<strong>OceanSustain Support</strong><p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Thanks for your message! This is a demo chat. For help, click the 'I need help!' button.</p>`;
            messageBox.appendChild(replyMessage);
            messageBox.scrollTop = messageBox.scrollHeight;
        }, 1000);
    }
}
