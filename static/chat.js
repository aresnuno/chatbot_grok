const chatbox = document.getElementById("chatbox");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const thinkingIndicator = document.getElementById("thinking");
const toggleThinkingBtn = document.getElementById("toggleThinkingBtn");

function addMessage(text, sender) {
  const div = document.createElement("div");
  div.classList.add("message", sender);

  if (sender === "bot") {
    // Render Markdown
    div.innerHTML = marked.parse(text);
  } else {
    div.textContent = text;
  }

  chatbox.appendChild(div);
  chatbox.scrollTop = chatbox.scrollHeight;
}
// Toggle thinking indicator visibility
toggleThinkingBtn.addEventListener("click", () => {
  if (thinkingIndicator.hasAttribute("hidden")) {
    thinkingIndicator.removeAttribute("hidden");
  } else {
    thinkingIndicator.setAttribute("hidden", "");
  }
});

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const msg = messageInput.value.trim();
  if (!msg) return;

  addMessage(msg, "user");
  messageInput.value = "";
  thinkingIndicator.removeAttribute("hidden");

  try {
    const res = await fetch("/send_message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg }),
    });

    if (!res.ok) {
      throw new Error(`Error: ${res.statusText}`);
    }

    const data = await res.json();
    addMessage(data.answer, "bot");
  } catch (err) {
    addMessage("Terjadi kesalahan: " + err.message, "bot");
  } finally {
    thinkingIndicator.setAttribute("hidden", "");
  }
});
