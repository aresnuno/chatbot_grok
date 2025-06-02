# Rule-Based Chatbot with Journey, Topic, and Subtopic

A focused chatbot system using **Groq's LLM** to simulate scoped and rule-bound conversations based on predefined **journey**, **topic**, and **subtopic** selections. Inspired by platforms like Yellow and OpenWebUI, this project includes a clean UI and modular code for easy customization.

---

## ✨ Features

- ✅ Interactive UI for selecting journey, topic, and subtopic
- ✅ Groq-powered LLM response streaming
- ✅ Markdown and code block support in bot messages
- ✅ Easy to update through `config.py` without touching business logic
- ✅ Toggleable "thinking" indicator
- ✅ Responsive dark theme

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.10+
- Groq API Key (https://console.groq.com)
- `pip` installed

### 🛠 Installation

```bash
git clone https://github.com/yourusername/chatbot-journey.git
cd chatbot-journey
pip install -r requirements.txt
Set your Groq API Key:

bash
export GROQ_API_KEY=your_api_key_here
▶️ Run the App
bash
python app.py
Then go to http://localhost:8000 in your browser.

🧠 Configuration
Open config.py and edit the JOURNEYS dictionary:

python
JOURNEYS = {
    "Onboarding": {
        "topics": {
            "Account Creation": {
                "subtopics": {
                    "Email Verification": "Help with email verification steps",
                    "Username Rules": "Explaining username criteria"
                }
            },
            ...
        }
    }
}
These will populate the dropdowns in the setup UI.

🗂 Project Structure
chatbot-journey/
├── static/
│   ├── chat.css         # UI styles
│   ├── chat.html        # Main chat interface
│   └── index.html       # Journey/topic/subtopic selection
├── app.py               # Flask backend server
├── config.py            # Static journey/topic/subtopic configuration
├── chat_logic.py        # LLM interaction and rule-based filtering
├── requirements.txt     # Python dependencies
└── README.md
📜 License
This project is licensed under the MIT License.

🤝 Contributions
Feel free to fork and PR improvements!