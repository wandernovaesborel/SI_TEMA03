const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const trainForm = document.getElementById("train-form");
const trainMessage = document.getElementById("train-message");

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    appendMessage("Você", userMessage);

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `mensagem=${encodeURIComponent(userMessage)}`,
    });

    const botMessage = await response.text();
    appendMessage("Bot", botMessage);

    userInput.value = "";
});

trainForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const question = document.getElementById("new-question").value.trim();
    const answer = document.getElementById("new-answer").value.trim();

    if (!question || !answer) {
        trainMessage.textContent = "Preencha ambos os campos!";
        return;
    }

    const response = await fetch("/treinar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pergunta: question, resposta: answer }),
    });

    const result = await response.json();
    trainMessage.textContent = result.mensagem;
    trainMessage.style.color = result.status === "sucesso" ? "green" : "red";

    trainForm.reset();
});

function appendMessage(sender, message) {
    const messageElement = document.createElement("div");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
