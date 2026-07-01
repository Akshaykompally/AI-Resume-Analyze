from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI,MistralAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

Loader = PyPDFLoader("Documents loader/Kompally_Akshay_Resume.pdf")
docs = Loader.load()

resume_text = "\n\n".join(doc.page_content for doc in docs)

llm = ChatMistralAI(
    model_name = "mistral-small-2506"
)

Job_description = input("Enter the Job Description : ")


extract_details_pdf = ChatPromptTemplate.from_messages([
    ("system",
        """
    You are an AI Resume Parser.

    Your task is to extract the key information from the resume provided below and return it in a structured JSON format.

    Instructions
    Extract only the information explicitly mentioned in the resume.
    Do not infer, guess, or generate any missing information.
    If a field is unavailable, return null for single values or [] for arrays.
    Preserve the original wording where appropriate.
    Return only the JSON object. Do not include explanations, notes, or markdown.
    Output Format
    {{
    "name": "",
    "email": "",
    "phone": "",
    "education": [
        {{
        "degree": "",
        "institution": "",
        "graduation_year": ""
        }}
    ],
    "experience": [
        {{
        "job_title": "",
        "company": "",
        "duration": ""
        }}
    ],
    "technical_skills": [],
    "projects": [
        {{
        "project_name": "",
        "technologies": []
        }}
    ],
    "certifications": []
    }}
    """
    ),
    ("human",
      """
        Resume:
        {docs}
      """
    )
])



chain =  extract_details_pdf | llm

response = chain.invoke({
    "docs": resume_text
})

resume_json = response.content




match = ChatPromptTemplate.from_messages([
    ("system",
    """
        You are an experienced Technical Recruiter, ATS Screening Expert, and Interview Preparation Assistant.

        You will receive two inputs:

        Candidate Resume (in structured JSON format)
        Job Description

        Your task is to analyze how well the candidate matches the job description and provide a complete hiring assessment.

        Instructions
        Compare the candidate's technical skills with the required skills in the job description.
        Compare the candidate's work experience with the required experience.
        Compare the candidate's education with the required qualifications.
        Compare the candidate's certifications with the preferred or required certifications.
        Compare the candidate's projects with the technologies, tools, and responsibilities mentioned in the job description.
        Identify the candidate's strengths based on the job description.
        Identify the candidate's missing skills or qualifications.
        Suggest major improvements the candidate should make to become a stronger fit for the role.
        Calculate an overall match percentage between 0 and 100.
        Recommend one of the following decisions:
        Shortlist
        Maybe
        Reject
        Clearly explain the reason for the recommendation.
        If the candidate is suitable, suggest interview questions based on:
        Technical Skills
        Projects
        Work Experience
        Job Description
        List the important topics the candidate should study before the interview.
        Provide a step-by-step roadmap for cracking the interview based on the job description.
        Return only valid JSON.

        Output Format:

        {{
        "match_percentage": 0,

        "decision": "",

        "reason": "",

        "technical_skill_match": {{
            "matching_skills": [],
            "missing_skills": []
        }},

        "experience_evaluation": "",

        "education_evaluation": "",

        "certification_evaluation": "",

        "project_evaluation": "",

        "strengths": [],

        "major_improvements": [],

        "interview_questions": {{
            "technical": [],
            "projects": [],
            "experience": [],
            "behavioral": []
        }},

        "topics_to_prepare": [],

        "interview_roadmap": [
            "Step 1",
            "Step 2",
            "Step 3",
            "Step 4"
        ]
        }}
    """
    ),
    ("human",
     """
        Candidate Resume: {candidate_resume}
        Job Description: {Job_description}
     """)
])


analyze = match | llm



result = analyze.invoke({
    "candidate_resume": resume_json,
    "Job_description": Job_description
})

print(result.content)