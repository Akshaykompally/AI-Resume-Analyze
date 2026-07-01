
import streamlit as st
import tempfile

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

st.set_page_config(page_title="AI Resume ATS Analyzer", page_icon="🤖", layout="wide")

st.title("🤖 AI Resume ATS Analyzer")
st.write("Upload your resume and compare it with a Job Description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the complete Job Description here..."
)

analyze = st.button("🔍 Analyze Resume", use_container_width=True)

if analyze:
    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter the Job Description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        docs = PyPDFLoader(pdf_path).load()
        resume_text = "\n\n".join(doc.page_content for doc in docs)

        llm = ChatMistralAI(
            model_name="mistral-small-2506",
            temperature=0
        )

        extract_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are an AI Resume Parser. Convert the resume into a structured text summary. "
             "Preserve skills, experience, education, projects and certifications."),
            ("human", "Resume:\n\n{docs}")
        ])

        resume_summary = (extract_prompt | llm).invoke(
            {"docs": resume_text}
        ).content

        match_prompt = ChatPromptTemplate.from_messages([
            ("system", """
        You are an expert ATS Resume Analyzer.

        Compare the candidate's resume with the job description.

        Return ONLY a professional Markdown report.

        Use exactly these sections:

        # ATS Resume Analysis

        ## ATS Match Score
        Provide a percentage.

        ## Hiring Decision

        ## Overall Summary

        ## Technical Skills
        ### Matching Skills
        ### Missing Skills

        ## Experience Evaluation

        ## Education Evaluation

        ## Certification Evaluation

        ## Project Evaluation

        ## Candidate Strengths

        ## Major Improvements

        ## Interview Questions
        ### Technical
        ### Projects
        ### Experience
        ### Behavioral

        ## Topics to Prepare

        ## Interview Preparation Roadmap

        Do not return JSON.
        Do not wrap the response in markdown code fences.
        """),
            ("human",
             "Candidate Resume:\n\n{candidate_resume}\n\n"
             "Job Description:\n\n{job_description}")
        ])

        report = (match_prompt | llm).invoke(
            {
                "candidate_resume": resume_summary,
                "job_description": job_description,
            }
        ).content

    report = report.replace("```markdown", "").replace("```", "").strip()

    st.success("Analysis Completed!")

    st.markdown(report)

    st.download_button(
        "📄 Download Report",
        data=report,
        file_name="ATS_Resume_Analysis.md",
        mime="text/markdown",
        use_container_width=True
    )
