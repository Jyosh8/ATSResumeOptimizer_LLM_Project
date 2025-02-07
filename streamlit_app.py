import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables (Google API key)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini Pro
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    """
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume_with_gemini(job_description, resume_text):
    """
    Uses Gemini Pro to analyze the resume and job description.
    """
    prompt = f"""
    Job Description:
    {job_description}

    Resume Text:
    {resume_text}

    Task:
    1. Calculate the percentage match between the job description and the resume.
    2. Identify the missing keywords in the resume that are present in the job description.
    3. Suggest how to modify the resume to achieve a 100% match for the job description.
    4. Provide the output in the following format:
       - Match Percentage: X%
       - Missing Keywords: [list of missing keywords]
       - Suggestions: [suggestions for improving the resume]
    5. Provide a summary of why the candidate is a good fit for the job.
    """
    response = model.generate_content(prompt)
    return response.text
# Streamlit App
st.set_page_config(layout="wide", page_title="Resume Matcher Pro") 

# Streamlit App
st.title("🌟 Resume Matcher Pro 🚀")
st.markdown("""
    **Welcome to Resume Matcher Pro!**  
    This tool helps you analyze how well your resume matches a job description.  
    Simply paste the job description, upload your resume, and click **Analyze** to get detailed insights.  
    Optimize your resume to stand out and land your dream job!  
""")

# Input job description at the top
st.subheader("📝 Job Description")
job_description = st.text_area("Paste the job description here:", height=200)

# Upload PDF file below
st.subheader("📄 Upload Your Resume")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Analyze button
if st.button("🔍 Analyze Resume", type="primary"):
    if uploaded_file and job_description:
        # Extract text from the uploaded PDF
        resume_text = extract_text_from_pdf(uploaded_file)

        # Analyze the resume and job description using Gemini Pro
        with st.spinner("Analyzing your resume... Please wait."):
            analysis_result = analyze_resume_with_gemini(job_description, resume_text)

        # Display the results
        st.subheader("📊 Analysis Results")
        st.write(analysis_result)
    else:
        st.warning("⚠️ Please upload your resume and paste the job description to proceed.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center;">
        <p>Created by Shlaghana with ❤️</p>
        <p>Designed to assist candidates in navigating today's competitive job market, where resumes are often filtered out by Applicant Tracking Systems (ATS).</p>
    </div>
""", unsafe_allow_html=True)