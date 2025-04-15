# ASTRA - Your AI Terminal Companion 🤖

Welcome to **ASTRA**, your AI-powered chatbot companion that helps you with a variety of tasks, all from the comfort of your terminal. Whether you're online or offline, ASTRA has got you covered with pre-configured responses and powerful API integrations for an amazing experience.

---

## 🚀 Features

- **Real-Time AI Responses** using the **Gemini API** (powered by Google).
- **Offline Mode:** Gracefully fallback to predefined responses when offline.
- **Stylish CLI Interface** with rich terminal styling.
- **Easy-to-Use** command-line interface for seamless interaction.
- **Error Logging** to track bot activity and errors for debugging.

---

## 📋 Prerequisites

Before you can get started, make sure you have the following installed:

- **Python 3.8+**
- **pip** (Python package installer)
- **An Internet connection** (for API calls to work)

---

## 🛠️ Installation

To get your chatbot up and running, follow these simple steps:

### 1. Fork the Repository

### 2. Clone the Forked Repository

```bash
git clone https://github.com/your-username/astra-chatbot.git
cd astra-chatbot
```

### 3. Install Dependencies

Ensure that you have all the required Python libraries installed by running:

```bash
pip install -r requirements.txt
```

### 4. Create a copy of `.env.example` and rename it to `.env`

### 5. Set Up API Key

In order to connect to the Gemini API (for AI-powered responses), you'll need to obtain an API key.

- Go to the [https://ai.google.dev/gemini-api/docs/api-key](Gemini API documentation) and follow the steps to get your API key.
- Once you have the API Key paste the API Key in the `.env` file

### 6. Run the ASTRA

```bash
python main.py
```

