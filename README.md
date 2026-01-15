# 🤖 GenAI Chatbot (ChatGPT-like Assistant)

GenAI is a Python-based AI chatbot inspired by ChatGPT.  
It uses **Groq LLM (LLaMA 3)** along with a modular agent-based architecture to generate intelligent responses and support tool-based reasoning.

---

## 🚀 Features

- 💬 ChatGPT-like conversational interface (backend logic)
- 🧠 Powered by **Groq LLaMA 3 (8B Instant)**
- 🛠️ Tool calling support (e.g. date & time tool)
- 🧩 Modular, scalable project structure
- 🔐 Secure API key handling using `.env`
- 🐍 Built with Python

---

## 🗂️ Project Structure

```text
GenAi/
│
├── src/
│   ├── agents/
│   │   └── chat_agent/
│   │       ├── nodes/
│   │       │   └── chat_node.py
│   │       ├── states/
│   │       │   └── chat_agent_state.py
│   │       └── tools/
│   │           └── date_time.py
│   │
│   ├── handlers/
│   │   └── chat_handlers.py
│   │
│   ├── routes/
│   │   └── chat_route.py
│
├── app.py
├── main.py
├── main.ipynb
├── .env          # ignored (contains API key)
├── .gitignore
└── README.md
