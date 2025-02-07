# ATS Resume Optimizer - LLM Project
ATS Resume Optimizer is an AI-powered tool designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). By leveraging Google's Gemini Pro model, this tool analyzes your resume against a specific job description, providing actionable insights to improve your resume and increase your chances of landing interviews.

## Features
Resume-Job Description Matching: Calculate the percentage match between your resume and a job description.

Missing Keywords: Identify keywords from the job description that are missing in your resume.

Optimization Suggestions: Get tailored suggestions to improve your resume and achieve a 100% match.

Candidate Summary: A summary of why you’re a great fit for the role.

PDF Resume Support: Upload your resume in PDF format for analysis.

## How It Works
Paste the Job Description: Copy and paste the job description into the app.

Upload Your Resume: Upload your resume in PDF format.

Analyze: Click the "Analyze" button to get detailed insights.

Optimize: Use the feedback to improve your resume and achieve a perfect match.

### Built With
Streamlit: For building the interactive web app.

Google Gemini Pro: For AI-powered analysis and insights.

PyPDF2: For extracting text from uploaded PDF resumes.

Python: The backbone of the entire application.

## Getting Started
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or higher

A Google API key for Gemini Pro (follow Google's documentation to get your API key).

Installation
Clone the repository:

bash
Copy
git clone https://github.com/yourusername/ATSResumeOptimizer_LLM_Project.git
cd ATSResumeOptimizer_LLM_Project
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Set up your Google API key:

Create a .env file in the project root directory.

Add your Google API key to the .env file:

plaintext
Copy
GOOGLE_API_KEY=your_api_key_here
Running the App
Start the Streamlit app:

bash
Copy
streamlit run app.py
Open your browser and navigate to the URL provided in the terminal (usually http://localhost:8501).

Use the app:

Paste the job description in the text area.

Upload your resume in PDF format.

Click the "Analyze" button to get insights.

