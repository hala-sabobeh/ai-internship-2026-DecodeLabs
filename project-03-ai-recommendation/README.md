# Project 3 – AI Recommendation Logic

## Overview
A content-based recommendation engine that maps a user's skills to the
most relevant tech career paths. The system accepts three user inputs,
converts them into a weighted TF-IDF vector, and computes cosine
similarity against a dataset of job roles to return a ranked Top-3 list
of career recommendations.

## Architecture
This project follows the IPO (Input → Process → Output) model:

- **Input** — The user provides three skills via the terminal. All inputs
  are normalized to lowercase and joined into a single user profile string.
- **Process** — The user profile and all job role descriptions are
  transformed into TF-IDF vectors within a shared vocabulary space.
  Cosine similarity is then calculated between the user vector and every
  job vector in the dataset.
- **Output** — Results are sorted in descending order by similarity score
  and truncated to the Top 3 matches to prevent choice overload.

## Tech Stack
- Language: Python 3
- Libraries: scikit-learn
- Algorithm: TF-IDF Vectorization + Cosine Similarity
- Paradigm: Content-Based Filtering

## How to Run

Install dependencies:
```bash
pip install scikit-learn
```

Run the recommender:
```bash
python recommender.py
```

## Sample Interaction
Enter 3 skills you know (press Enter after each):
Skill 1: python
Skill 2: sql
Skill 3: machine learning
-- Top Recommended Career Paths --

Data Scientist
Match Score : 0.48
Key Skills  : python sql machine learning data analysis statistics...
AI Engineer
Match Score : 0.46
Key Skills  : python machine learning deep learning nlp transformers...
Machine Learning Engineer
Match Score : 0.45
Key Skills  : python machine learning deep learning tensorflow pytorch...


## Key Concepts

| Concept | Implementation |
|---------|----------------|
| Content-Based Filtering | Match user profile to item attributes directly |
| TF-IDF Vectorization | Converts skill text into weighted numerical vectors |
| Cosine Similarity | Measures angular alignment between user and job vectors |
| Top-N Filtering | Results truncated to Top 3 to prevent choice overload |
| Cold Start Bypass | User is prompted for skills on first run — no history needed |

## Why Cosine Similarity Over Euclidean Distance
Euclidean distance is sensitive to vector magnitude — a job role with
more listed skills would always appear more distant even if the direction
of skills aligns perfectly. Cosine similarity measures only the angle
between vectors, making it magnitude-invariant and far more accurate
for text-based matching.

## What I Learned
- How to transform qualitative text data into numerical vectors using TF-IDF
- Why cosine similarity is the industry standard for recommendation engines
- How the 4-step ranking pipeline works: Ingestion, Scoring, Sorting, Filtering
- The Cold Start problem and how onboarding input solves it
- How Netflix, Amazon, and Spotify recommendation engines are built on
  these same mathematical foundations