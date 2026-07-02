# 🤖 AI Prompt Grader

An AI-powered Prompt Evaluation tool built with **Python**, **Streamlit**, and **Google Gemini AI**. The application analyzes user prompts and provides a detailed quality assessment based on prompt engineering best practices.

---

## 📌 Overview

Writing high-quality prompts is essential for obtaining accurate and reliable responses from Large Language Models (LLMs). This project evaluates prompts using an AI model and scores them across multiple dimensions.

The application provides actionable feedback to help users improve their prompts for better AI performance.

---

## ✨ Features

* 📝 Enter any prompt through a clean Streamlit interface
* 🤖 AI-powered prompt evaluation using Google Gemini
* 📊 Overall score out of 10
* 📈 Individual scores for:

  * Clarity
  * Context
  * Specificity
  * Constraints
  * Output Format
* ✅ Highlights prompt strengths
* ❌ Identifies weaknesses
* 💡 Suggests improvements
* ⚡ Fast and interactive UI

---

## 📂 Project Structure

```text
PromptGrader/
│
├── app.py                 # Streamlit User Interface
├── grader.py              # Gemini Prompt Evaluation Logic
├── .env                   # Gemini API Key
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend Development             |
| Streamlit         | Web Interface                   |
| Google Gemini API | Prompt Evaluation               |
| python-dotenv     | Environment Variable Management |
| JSON              | Structured AI Output            |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/prompt-grader.git
```

Navigate to the project:

```bash
cd prompt-grader
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📋 Evaluation Criteria

Each prompt is evaluated on the following criteria:

| Criterion     | Maximum Score |
| ------------- | ------------: |
| Clarity       |             2 |
| Context       |             2 |
| Specificity   |             2 |
| Constraints   |             2 |
| Output Format |             2 |

**Maximum Score:** **10/10**

---

## 📷 Example

### User Prompt

```text
Explain Artificial Intelligence.
```

### Evaluation

```text
Overall Score: 5/10

Clarity: 2/2
Context: 1/2
Specificity: 1/2
Constraints: 0/2
Output Format: 1/2

Strengths
• Clear topic

Weaknesses
• Missing audience
• No constraints
• Output format not specified

Suggestions
• Specify the target audience.
• Mention the desired response format.
• Add length or content constraints.
```

---

## 🔄 Workflow

```text
User Prompt
      │
      ▼
Streamlit UI
      │
      ▼
Gemini API
      │
      ▼
Prompt Evaluation
      │
      ▼
JSON Response
      │
      ▼
Interactive Dashboard
```

---

## 📚 Dependencies

```text
streamlit
google-genai
python-dotenv
```

Install them using:

```bash
pip install streamlit google-genai python-dotenv
```

---

## 🚀 Future Improvements

* Prompt rewriting and optimization
* Prompt comparison
* Prompt history
* PDF report generation
* Authentication
* Dark mode
* Export evaluation results
* Multiple LLM support (Gemini, Claude, OpenAI, Llama)
* Advanced prompt engineering metrics
* Prompt benchmarking

---

## 🎯 Use Cases

* Prompt Engineering Practice
* AI Application Development
* Chatbot Prompt Testing
* LLM Evaluation
* Research Projects
* Student Learning
* AI Developer Tooling

---

## 👨‍💻 Author

Developed as a Prompt Engineering utility to evaluate and improve prompts for Large Language Models using Google's Gemini API.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

* Google Gemini API
* Streamlit
* Python Community
