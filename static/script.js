// Chat functionality
let chatHistory = [];
let isTyping = false;

// Initialize the chat
document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const welcomeTime = document.getElementById('welcomeTime');
    
    // Set welcome message time
    welcomeTime.textContent = formatTime(new Date());
    
    // Add event listeners
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    messageInput.addEventListener('input', function() {
        sendButton.disabled = this.value.trim() === '';
    });
    
    // Focus on input
    messageInput.focus();
});

// Send message function
async function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    
    if (!message || isTyping) return;
    
    // Clear input and disable send button
    messageInput.value = '';
    const sendButton = document.getElementById('sendButton');
    sendButton.disabled = true;
    
    // Add user message to chat
    addMessage(message, 'user');
    
    // Show typing indicator
    showTypingIndicator();
    
    try {
        // Send request to backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                history: chatHistory.slice(-6) // Send last 6 messages for context
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Hide typing indicator
        hideTypingIndicator();
        
        // Add bot response to chat
        addMessage(data.response, 'bot');
        
        // Update chat history
        chatHistory.push(
            { user: message, bot: data.response }
        );
        
        // Keep only last 10 exchanges in history
        if (chatHistory.length > 10) {
            chatHistory = chatHistory.slice(-10);
        }
        
    } catch (error) {
        console.error('Error sending message:', error);
        hideTypingIndicator();
        addMessage('I apologize, but I encountered an error. Please try again.', 'bot', true);
    }
    
    // Re-enable input
    messageInput.focus();
}

// Add message to chat
function addMessage(content, sender, isError = false) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message${isError ? ' error-message' : ''}`;
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    
    if (sender === 'user') {
        messageContent.innerHTML = `<strong>You:</strong> ${escapeHtml(content)}`;
    } else {
        messageContent.innerHTML = `<strong>Prakhar:</strong> ${formatBotMessage(content)}`;
    }
    
    const messageTime = document.createElement('div');
    messageTime.className = 'message-time';
    messageTime.textContent = formatTime(new Date());
    
    messageDiv.appendChild(messageContent);
    messageDiv.appendChild(messageTime);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Format bot message to handle line breaks and formatting
function formatBotMessage(content) {
    return escapeHtml(content)
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>');
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Format time
function formatTime(date) {
    return date.toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: true 
    });
}

// Show typing indicator
function showTypingIndicator() {
    isTyping = true;
    const typingIndicator = document.getElementById('typingIndicator');
    typingIndicator.style.display = 'flex';
    
    // Scroll to bottom to show typing indicator
    const chatMessages = document.getElementById('chatMessages');
    setTimeout(() => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 100);
}

// Hide typing indicator
function hideTypingIndicator() {
    isTyping = false;
    const typingIndicator = document.getElementById('typingIndicator');
    typingIndicator.style.display = 'none';
}

// Sample questions for demonstration
const sampleQuestions = [
    "What is your background?",
    "What technologies do you work with?",
    "Tell me about your experience with AI/ML",
    "What projects have you worked on?",
    "What are your achievements?",
    "How can I contact you?"
];

// Add sample questions as clickable suggestions (optional enhancement)
function addSampleQuestions() {
    const chatMessages = document.getElementById('chatMessages');
    const suggestionsDiv = document.createElement('div');
    suggestionsDiv.className = 'sample-questions';
    suggestionsDiv.innerHTML = `
        <div class="suggestions-title">Try asking:</div>
        ${sampleQuestions.map(q => 
            `<button class="suggestion-btn" onclick="askQuestion('${q}')">${q}</button>`
        ).join('')}
    `;
    chatMessages.appendChild(suggestionsDiv);
}

// Ask a sample question
function askQuestion(question) {
    const messageInput = document.getElementById('messageInput');
    messageInput.value = question;
    sendMessage();
}

// Health check function
async function checkHealth() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        console.log('Health check:', data);
        return data.bot_ready;
    } catch (error) {
        console.error('Health check failed:', error);
        return false;
    }
}

// Initialize health check
checkHealth();