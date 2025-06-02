# Rule-Based Chatbot with Journey, Topic, and Subtopic

This project is a **rule-based chatbot** that scopes conversations based on selected parameters: journey, topic, and subtopic. It uses the Groq LLM API to generate conversational responses limited to these themes, and provides a clean, interactive UI inspired by ChatGPT/OpenWebUI.

---

## Features

- Selectable **Journey**, **Topic**, and **Subtopic** to constrain chatbot responses  
- Interactive setup page to choose conversation context  
- Streaming chat interface with user and bot message bubbles  
- Dark-themed responsive UI with animated thinking indicator  
- Markdown-supported bot message rendering  
- Easy to extend with new journeys, topics, and subtopics  

---

## Demo

![Chatbot UI Screenshot](./docs/chatbot_ui.png)

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Groq SDK Python client (or other LLM client)  
- Flask or FastAPI (depending on your backend choice)  
- Basic web browser  

### Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/yourusername/your-chatbot-repo.git
   cd your-chatbot-repo
Install dependencies:

bash
Salin
Edit
pip install -r requirements.txt
Set up your Groq API key as environment variable:

bash
Salin
Edit
export GROQ_API_KEY="your_api_key_here"
Running the App
bash
Salin
Edit
python app.py
Then open your browser and navigate to:

arduino
Salin
Edit
http://localhost:8000
Usage
On the setup page, select a Journey, Topic, and Subtopic from dropdown menus.

Click Mulai Chat to start the conversation scoped to your selection.

Enter your messages in the chat interface and receive context-aware responses from the bot.

Configuration
Edit config.py to customize journeys, topics, and subtopics. Example format:

python
Salin
Edit
journeys = {
    "Customer Support": {
        "topics": {
            "Refund": {
                "subtopics": {
                    "Delayed Refund": {},
                    "Partial Refund": {},
                }
            },
            ...
        }
    },
    ...
}
Project Structure
bash
Salin
Edit
/project-root
├─ static/
│  ├─ chat.css        # Chat UI styles
│  ├─ index.html      # Setup page
│  └─ chat.html       # Chat interface page
├─ app.py             # Backend server
├─ config.py          # Journey/topic/subtopic config
├─ chat_logic.py      # Chat session and Groq API handling
├─ requirements.txt   # Python dependencies
└─ README.md          # This documentation
Future Enhancements
Persistent session and user management

Support for multiple LLM providers

Enhanced prompt engineering for stricter rule adherence

UI improvements including themes and accessibility

Analytics and monitoring dashboard

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, please contact Your Name.

Acknowledgments
Groq AI for the LLM platform

Inspiration from ChatGPT and OpenWebUI

Open-source community and contributors