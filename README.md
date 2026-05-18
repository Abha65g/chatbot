# 🩺 MediCare AI Assistant

An AI-powered medical chatbot built using **Flask**, **Groq LLM**, and a **Medical Q&A Dataset**.

This chatbot provides short and readable medical responses using Retrieval-Augmented Generation (RAG).

---

# 🚀 Features

- AI-powered medical chatbot
- Medical dataset integration
- Groq LLM responses
- Modern responsive UI
- Markdown formatted answers
- Typing animation
- Flask backend
- Educational medical assistance

---

# 🛠 Technologies Used

- Python
- Flask
- Groq API
- Pandas
- HTML
- CSS
- JavaScript
- jQuery

---

# 📂 Project Structure

```bash
chatbot/
│
├── main.py
├── medical_data.csv
├── .env
├── .gitignore
│
└── templates/
    └── chat.html
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

---

## 2. Install Dependencies

```bash
pip install flask groq python-dotenv pandas
```

---

## 3. Create `.env` File

```env
GROQ_API_KEY=your_api_key_here
```

---

## 4. Run Application

```bash
python main.py
```

---

# 🌐 Open In Browser

```text
http://127.0.0.1:5000
```

---

# 🧠 Working Principle

1. User enters a medical query
2. Chatbot searches relevant medical context from dataset
3. Context is passed to Groq LLM
4. AI generates a readable response
5. Response is displayed in chatbot UI

---

# 📊 Dataset

The chatbot uses a medical question-answer dataset in CSV format.

Dataset contains:

* Symptoms
* Diseases
* Treatments
* Prevention
* Diagnosis

---

# ⚠ Disclaimer

This chatbot is for educational purposes only and should not be used for real medical diagnosis.

Always consult a healthcare professional for medical advice.

---

# 👨‍💻 Author

Abhay Singh
