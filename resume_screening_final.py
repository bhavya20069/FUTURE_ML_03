import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- LOAD DATA --------------------
df = pd.read_csv("resumes.csv")

# -------------------- JOB DESCRIPTION --------------------
job_description = "Python SQL Machine Learning Data Analysis"

# -------------------- CLEAN TEXT --------------------
def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', '', str(text))
    return text.lower()

# -------------------- SKILLS --------------------
skills = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "react", "deep learning", "nlp"
]

# -------------------- SKILL EXTRACTION --------------------
def extract_skills(text):
    found = []
    for skill in skills:
        if skill in text:
            found.append(skill)
    return found

# -------------------- PROCESS JOB --------------------
clean_job = clean_text(job_description)
job_skills = extract_skills(clean_job)

# Optional: Names for candidates
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen"]

results = []

# -------------------- PROCESS RESUMES --------------------
for i, row in df.iterrows():
    resume = clean_text(row["resume_text"])
    resume_skills = extract_skills(resume)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([clean_job, resume])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    missing = list(set(job_skills) - set(resume_skills))

    results.append({
        "Name": names[i] if i < len(names) else f"Candidate_{i+1}",
        "Score": round(score, 2),
        "Skills": resume_skills,
        "Missing Skills": missing
    })

# -------------------- CREATE DATAFRAME --------------------
df_result = pd.DataFrame(results)
df_result = df_result.sort_values(by="Score", ascending=False)

# -------------------- ADD EXPLANATION --------------------
def get_explanation(missing):
    if len(missing) == 0:
        return "Good Fit"
    else:
        return "Missing: " + ", ".join(missing)

df_result["Explanation"] = df_result["Missing Skills"].apply(get_explanation)

# -------------------- FORMAT OUTPUT --------------------
df_result["Skills"] = df_result["Skills"].apply(lambda x: ", ".join(x))
df_result["Missing Skills"] = df_result["Missing Skills"].apply(
    lambda x: ", ".join(x) if x else "None"
)

# -------------------- PRINT CLEAN OUTPUT --------------------
print("\n🏆 FINAL CANDIDATE REPORT 🏆\n")

for _, row in df_result.iterrows():
    print(f"Name: {row['Name']}")
    print(f"Score: {row['Score']}")
    print(f"Skills: {row['Skills']}")
    print(f"Missing Skills: {row['Missing Skills']}")
    print(f"Explanation: {row['Explanation']}")
    print("-" * 40)

# -------------------- SAVE CSV --------------------
df_result.to_csv("final_ranking.csv", index=False)