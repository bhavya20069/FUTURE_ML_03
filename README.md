🚀Overview
Recruiters often receive a large number of resumes for a single job role, making manual screening time-consuming and inconsistent.
This project presents a Machine Learning–based Resume Screening System that automates the process of evaluating and ranking candidates based on job requirements.
The system uses Natural Language Processing (NLP) techniques to analyze resume content, extract relevant skills, and compare them with a given job description.
🎯 Objective
The primary objective of this project is to:
Process unstructured resume data
Extract key skills and keywords
Compare resumes with job descriptions
Score and rank candidates based on relevance
Identify missing or weak skills
🛠️ Tech Stack
Programming Language:
Python
Libraries & Tools:
spaCy (NLP processing)
NLTK (text preprocessing)
Scikit-learn (TF-IDF, similarity scoring)
Pandas & NumPy (data handling)
⚙️ Key Features
Resume text cleaning and preprocessing
Skill extraction using NLP techniques
Job description parsing
Resume-to-job similarity scoring
Candidate ranking based on role fit
Skill gap identification
🔄 Workflow
Data Preprocessing
Clean and normalize resume text by removing stopwords, punctuation, and irrelevant content.
Skill Extraction
Extract important keywords and skills using NLP techniques.
Job Description Analysis
Identify required skills and key terms from the job description.
Similarity Scoring
Convert text into numerical vectors using TF-IDF and compute similarity using cosine similarity.
Candidate Ranking
Rank candidates based on similarity scores.
Skill Gap Analysis
Highlight missing skills for each candidate.
📊 Example Output
🏆 FINAL CANDIDATE REPORT 🏆
Name: Alice  
Score: 0.78  
Skills: Python, SQL, Machine Learning  
Missing Skills: None  
Explanation: Good Fit  
----------------------------------------
Name: Charlie  
Score: 0.63  
Skills: Python, Machine Learning  
Missing Skills: SQL  
Explanation: Missing: SQL
