# Project 3: Tech Stack Recommender

This is my Week 3 Artificial Intelligence project for the DecodeLabs internship.

## Description

This project builds a simple AI recommendation system based on user preferences. It recommends the most relevant tech career paths by matching the user's skills or interests with predefined career role profiles.

The system uses content-based filtering, TF-IDF vectorization, and cosine similarity to rank recommendations.

## Project Goal

Create a simple recommendation system based on user preferences.

## How It Works

| Step | Description |
|---|---|
| Input | The user enters at least three skills or interests |
| Vector Mapping | User preferences and career role profiles are converted into TF-IDF vectors |
| Scoring | Cosine similarity is calculated between the user profile and each career role |
| Sorting | Roles are sorted based on similarity score |
| Filtering | The system returns the Top 3 most relevant career paths |

## Recommendation Method

| Component | Method Used |
|---|---|
| Recommendation Type | Content-Based Filtering |
| Feature Extraction | TF-IDF |
| Similarity Metric | Cosine Similarity |
| Output | Top 3 Career Recommendations |

## Example Input

```text
Python, Machine Learning, Data Analysis