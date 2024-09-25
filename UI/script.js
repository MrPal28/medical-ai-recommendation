const chatBox = document.querySelector(".chat-box");
const chatInput = document.querySelector(".chat-input");
const sendButton = document.querySelector(".send-button");
const dropdownLinks = document.querySelectorAll(".dropdown-content a");

// Function to create a message
function createMessage(message, isUser = true) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add(isUser ? "user-message" : "bot-message");
  
  const messageContent = document.createElement("p");
  messageContent.classList.add("message-content");
  messageContent.textContent = message;
  
  messageDiv.appendChild(messageContent);
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to send a message
function sendMessage() {
  const message = chatInput.value.trim();
  if (message) {
    createMessage(message, true);
    chatInput.value = "";
    setTimeout(() => createMessage("Bot response!", false), 1000);
  }
}

// Event listeners for send button and Enter key
sendButton.addEventListener("click", sendMessage);
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

// Event listener for dropdown suggestions
dropdownLinks.forEach(link => {
  link.addEventListener("click", (e) => {
    chatInput.value = e.target.textContent;
  });
});