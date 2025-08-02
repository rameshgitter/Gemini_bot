const chatHistory = document.getElementById("chat-history");
const userMessage = document.getElementById("user_message");
const sendButton = document.getElementById("send_button");

sendButton.addEventListener("click", sendMessage);
userMessage.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    sendMessage();
  }
});

function sendMessage() {
  const message = userMessage.value.trim();
  if (message) {
    addMessageToChat("user", message);
    userMessage.value = "";

    fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_message: message }),
    })
      .then((response) => response.text())
      .then((botResponse) => {
        addMessageToChat("bot", botResponse);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}

function addMessageToChat(sender, message) {
  const messageElement = document.createElement("div");
  messageElement.classList.add(
    "mb-2",
    "p-2",
    "rounded",
    "max-w-md",
    "break-words"
  );
  if (sender === "user") {
    messageElement.classList.add("bg-gray-200", "ml-auto");
    messageElement.textContent = `You: ${message}`;
  } else {
    messageElement.classList.add("bg-blue-200", "mr-auto");
    messageElement.textContent = `Bot: ${message}`;
  }
  chatHistory.appendChild(messageElement);
  chatHistory.scrollTop = chatHistory.scrollHeight;
}
