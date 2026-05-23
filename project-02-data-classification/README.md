# Project 2 – Data Classification Using AI

## Overview
A supervised machine learning pipeline that trains a K-Nearest Neighbors
model to classify iris flowers into three species based on their physical
measurements. The model learns entirely from data — no rules are written
manually.

## Architecture
This project follows the IPO (Input → Process → Output) model:

- **Input** — The Iris dataset (150 samples, 4 features, 3 classes) loaded
  via scikit-learn. Features are normalized using StandardScaler to remove
  measurement bias before training.
- **Process** — Data is split 80/20 into training and testing sets with
  shuffling to remove order bias. A KNN classifier (K=5) is trained on
  the training set using the proximity principle: classify by majority
  vote of the 5 nearest neighbors.
- **Output** — Predictions are evaluated using a Confusion Matrix and
  F1 Score rather than raw accuracy, to ensure honest model validation.

## Tech Stack
- Language: Python 3
- Libraries: scikit-learn, numpy
- Algorithm: K-Nearest Neighbors (KNN)
- Paradigm: Supervised Learning

## How to Run

Install dependencies:
```bash
pip install scikit-learn numpy
```

Run the classifier:
```bash
python classifier.py
```

## Sample Output
-- Dataset Overview --
Total samples  : 150
Features       : 4
Classes        : [setosa, versicolor, virginica]
-- Train/Test Split --
Training samples : 120 (80%)
Testing samples  : 30  (20%)
-- Confusion Matrix --
[10  0  0]  <- Setosa
[ 0  9  0]  <- Versicolor
[ 0  0 11]  <- Virginica
-- Classification Report --
precision  recall  f1-score
setosa          1.00    1.00      1.00
versicolor      1.00    1.00      1.00
virginica       1.00    1.00      1.00
-- Single Prediction Example --
Input    : sepal=5.1cm x 3.5cm | petal=1.4cm x 0.2cm
Predicted: setosa

## Key Concepts

| Concept | Implementation |
|---------|----------------|
| Feature Scaling | StandardScaler — mean=0, variance=1 |
| Train/Test Split | 80% training, 20% testing, shuffle=True |
| KNN Algorithm | K=5, majority vote among nearest neighbors |
| Confusion Matrix | Per-class breakdown of correct and incorrect predictions |
| F1 Score | Harmonic mean of precision and recall — more honest than accuracy |

## Why F1 Score Over Accuracy
Raw accuracy can be misleading on imbalanced datasets. A model that always
predicts the majority class can score 99% accuracy while being completely
useless. F1 Score balances precision (trustworthiness) and recall
(sensitivity) to give a true measure of model performance.

## What I Learned
- How to build a complete supervised learning pipeline from scratch
- Why feature scaling is essential for distance-based algorithms like KNN
- How to choose K and why both extremes (K=1 and K=100) cause problems
- How to read a confusion matrix and interpret model errors
- Why F1 Score is a more reliable metric than raw accuracy