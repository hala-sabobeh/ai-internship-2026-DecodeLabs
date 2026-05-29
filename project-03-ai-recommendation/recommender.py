from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

JOBS = [
    {
        "title": "Data Scientist",
        "skills": "python sql machine learning data analysis statistics numpy pandas scikit-learn"
    },
    {
        "title": "Machine Learning Engineer",
        "skills": "python machine learning deep learning tensorflow pytorch neural networks scikit-learn"
    },
    {
        "title": "Data Analyst",
        "skills": "sql excel data analysis visualization power bi tableau statistics reporting"
    },
    {
        "title": "Backend Developer",
        "skills": "python java sql apis rest django flask databases postgresql"
    },
    {
        "title": "DevOps Engineer",
        "skills": "aws docker kubernetes linux git ci cd automation cloud infrastructure"
    },
    {
        "title": "Frontend Developer",
        "skills": "javascript html css react vue ui ux web design responsive"
    },
    {
        "title": "Cloud Architect",
        "skills": "aws azure cloud docker kubernetes infrastructure automation devops networking"
    },
    {
        "title": "AI Engineer",
        "skills": "python machine learning deep learning nlp transformers llm pytorch tensorflow"
    },
    {
        "title": "Cybersecurity Analyst",
        "skills": "networking linux security encryption firewalls penetration testing risk analysis"
    },
    {
        "title": "Full Stack Developer",
        "skills": "python javascript html css react django rest apis postgresql databases"
    },
]

def build_corpus():
    return [job["skills"] for job in JOBS]

def get_user_profile():
    print("=" * 50)
    print("  Project 3: AI Tech Stack Recommender")
    print("=" * 50)
    print("\nEnter 3 skills you know (press Enter after each):")

    skills = []
    for i in range(1, 4):
        skill = input(f"  Skill {i}: ").strip().lower()
        skills.append(skill)

    return " ".join(skills)

def recommend(user_profile, top_n=3):
    corpus = build_corpus()
    corpus_with_user = corpus + [user_profile]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus_with_user)

    user_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    scores = cosine_similarity(user_vector, job_vectors).flatten()

    ranked = sorted(
        zip(scores, JOBS),
        key=lambda x: x[0],
        reverse=True
    )

    return ranked[:top_n]

def display_results(results):
    print("\n-- Top Recommended Career Paths --\n")
    for rank, (score, job) in enumerate(results, 1):
        print(f"  {rank}. {job['title']}")
        print(f"     Match Score : {score:.2f}")
        print(f"     Key Skills  : {job['skills']}\n")

def main():
    user_profile = get_user_profile()

    print(f"\n-- User Profile Vector Built --")
    print(f"  Input Skills : {user_profile}")

    results = recommend(user_profile)
    display_results(results)

    print("=" * 50)

if __name__ == "__main__":
    main()