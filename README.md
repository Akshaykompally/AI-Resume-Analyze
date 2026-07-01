# 🤖 AI Resume ATS Analyzer

An AI-powered Resume Analyzer built with **Streamlit**, **LangChain**, and **Mistral AI** that evaluates a candidate's resume against a Job Description (JD) and generates a detailed ATS (Applicant Tracking System) compatibility report.

The application extracts structured information from a PDF resume, compares it with the provided job description, and produces an AI-generated hiring assessment including ATS score, strengths, missing skills, interview questions, and a preparation roadmap.

---

## 🚀 Features

* 📄 Upload Resume in PDF format
* 📝 Paste any Job Description
* 🤖 AI-powered resume parsing using Mistral AI
* 📊 ATS Match Score
* ✅ Hiring Recommendation
* 💻 Technical Skills Analysis
* ❌ Missing Skills Detection
* 🎓 Education Evaluation
* 💼 Experience Evaluation
* 📜 Certification Evaluation
* 🚀 Project Evaluation
* 💪 Candidate Strengths
* 📈 Improvement Suggestions
* 🎤 AI-generated Interview Questions
* 📚 Interview Preparation Topics
* 🛣️ Personalized Interview Roadmap
* 📥 Download the analysis report in Markdown format

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* PyPDFLoader
* python-dotenv

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py                 # Streamlit Web Application
├── main.py                # Console-based Resume Analyzer
├── requirements.txt
├── .env                   # Environment Variables (Not Recommended to Commit)
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Akshaykompally/AI-Resume-Analyze.git
cd AI-Resume-Analyze
```

Create a virtual environment (recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Get your API key from the Mistral AI platform.

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 💻 Run the Console Version

```bash
python main.py
```

The console version asks for a Job Description and prints the ATS analysis in the terminal.

---

## 📄 How It Works

1. Upload a PDF resume.
2. Enter or paste the Job Description.
3. The application extracts text from the resume using `PyPDFLoader`.
4. Mistral AI converts the resume into a structured summary.
5. The AI compares the resume against the Job Description.
6. A detailed ATS report is generated with hiring insights and interview preparation guidance.

---

## 📊 Sample Report

The generated report includes:

* ATS Match Score
* Hiring Decision
* Overall Summary
* Matching Technical Skills
* Missing Skills
* Experience Evaluation
* Education Evaluation
* Certification Evaluation
* Project Evaluation
* Candidate Strengths
* Major Improvements
* Technical Interview Questions
* Project-based Interview Questions
* Experience-based Questions
* Behavioral Questions
* Topics to Prepare
* Interview Preparation Roadmap

---

## 📦 Dependencies

* streamlit
* python-dotenv
* langchain
* langchain-core
* langchain-community
* langchain-mistralai
* pypdf

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Enhancements

* Resume keyword optimization
* Multi-resume comparison
* Support for DOCX resumes
* Resume rewriting suggestions
* Cover letter generation
* ATS score visualization with charts
* Export reports as PDF
* Authentication and user history
* Multiple LLM provider support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Akshay Kompally**

GitHub: https://github.com/Akshaykompally
