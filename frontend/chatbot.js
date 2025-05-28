async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value;

  if (!message) return;

  const chatDiv = document.getElementById("chat");
  chatDiv.innerHTML += `<p><strong>Tú:</strong> ${message}</p>`;

  try {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    chatDiv.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
  } catch (error) {
    chatDiv.innerHTML += `<p style="color:red;"><strong>Error:</strong> No se pudo conectar al servidor.</p>`;
    console.error(error);
  }

  input.value = "";
}
