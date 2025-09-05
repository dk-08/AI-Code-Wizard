# 🧙 AI Code Wizard

AI Code Wizard is a Python project that converts natural language prompts into runnable Python code using Google’s Gemini API.
It provides both a **Command-Line Interface (CLI)** and a **Gradio-powered Web App** with safe code execution, real-time results, and flexible API key management.

---

## ✨ Features

* 🔹 Generate Python code from plain text prompts
* 🔹 Edit and run code safely inside the app
* 🔹 View clean execution results or error messages
* 🔹 CLI and Web interface included
* 🔹 Secure API key management with environment variables

---

## 📂 Project Structure

```
ai-code-wizard/
│-- cli_app.py         # Command-line interface
│-- web.py             # Web app with Gradio UI
│-- gemini_helper.py   # Core logic (Gemini API + code execution)
│-- requirements.txt   # Python dependencies
│-- .gitignore         # Ignore cache, env, etc.
```

---

## ⚡ Installation

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/ai-code-wizard.git
cd ai-code-wizard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Gemini API key:

```powershell
# On Windows (PowerShell)
setx GEMINI_API_KEY "your_real_key_here"

# On Mac/Linux
export GEMINI_API_KEY="your_real_key_here"
```

---

## 🚀 Usage

### Run CLI

```bash
python cli_app.py
```

Example:

```
>>> write a bubble sort program
```

### Run Web App

```bash
python web.py
```

* Enter a prompt in the textbox
* Generated code appears (editable)
* Click **Run Code** to execute and see results

---

## 📦 Requirements

* Python 3.9+
* [Google Gemini API Key](https://ai.google.dev/gemini-api)

Dependencies:

```
google-generativeai
gradio
python-dotenv   # optional
```

---

## 🔒 Security

* **Never hardcode your API key**.
* Use environment variables or a `.env` file.

---

Feel free to contribute :))
-Disha Kaushik
