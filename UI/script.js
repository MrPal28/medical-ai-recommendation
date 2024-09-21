// Select necessary DOM elements
const chatBox = document.querySelector('.chat-box');
const chatInput = document.querySelector('.chat-input');
const sendButton = document.querySelector('.send-button');

// Function to create a new message element
function createMessageElement(message, isUserMessage = true) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(isUserMessage ? 'user-message' : 'bot-message');

    const messageContent = document.createElement('p');
    messageContent.classList.add('message-content');
    messageContent.textContent = message;

    messageDiv.appendChild(messageContent);
    return messageDiv;
}

// Function to append the message to the chat box
function appendMessage(message, isUserMessage = true) {
    const messageElement = createMessageElement(message, isUserMessage);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

// Function to handle sending the message
function sendMessage() {
    const message = chatInput.value.trim();
    if (message) {
        appendMessage(message, true); // Append user message
        chatInput.value = ''; // Clear the input field

        // Simulate a bot response after 1 second
        setTimeout(() => {
            appendMessage('This is a bot response.', false); // Append bot message
        }, 1000);
    }
}

// Event listener for the send button
sendButton.addEventListener('click', sendMessage);

// Event listener for the "Enter" key
chatInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});