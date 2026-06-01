# Project 2: Data Classification Using AI

This is my Week 2 Artificial Intelligence project for the DecodeLabs internship.

## Description

This project builds a basic supervised machine learning classification model using the Iris dataset. The model uses the K-Nearest Neighbors algorithm to classify flower samples into one of three Iris species.

The project follows a complete machine learning workflow: loading the dataset, understanding the data, splitting it into training and testing sets, applying feature scaling, training the model, evaluating performance, and testing the model on a new sample.

## Dataset

The project uses the Iris dataset.

| Property | Value |
|---|---|
| Dataset | Iris Flower Dataset |
| Total Samples | 150 |
| Features | 4 |
| Classes | 3 |
| Class Names | setosa, versicolor, virginica |
| Samples per Class | 50 |

## Features Used

| Feature Number | Feature Name |
|---|---|
| 1 | sepal length (cm) |
| 2 | sepal width (cm) |
| 3 | petal length (cm) |
| 4 | petal width (cm) |

## Model Details

| Item | Value |
|---|---|
| Algorithm | K-Nearest Neighbors |
| K Value Used | 5 |
| Train-Test Split | 80% training, 20% testing |
| Training Samples | 120 |
| Testing Samples | 30 |
| Feature Scaling | StandardScaler |

## Model Evaluation Results

| Metric | Score |
|---|---|
| Accuracy | 0.9333 |
| Precision | 0.9444 |
| Recall | 0.9333 |
| F1 Score | 0.9327 |

## Confusion Matrix

| Actual / Predicted | setosa | versicolor | virginica |
|---|---:|---:|---:|
| setosa | 10 | 0 | 0 |
| versicolor | 0 | 10 | 0 |
| virginica | 0 | 2 | 8 |

## Class Wise Performance

| Class | Precision | Recall | F1 Score | Support |
|---|---:|---:|---:|---:|
| setosa | 1.00 | 1.00 | 1.00 | 10 |
| versicolor | 0.83 | 1.00 | 0.91 | 10 |
| virginica | 1.00 | 0.80 | 0.89 | 10 |

## K Value Comparison

| K Value | F1 Score |
|---:|---:|
| 1 | 0.9666 |
| 2 | 0.9327 |
| 3 | 0.9327 |
| 4 | 0.9327 |
| 5 | 0.9327 |
| 6 | 0.9327 |
| 7 | 0.9666 |
| 8 | 0.9327 |
| 9 | 0.9666 |
| 10 | 0.9666 |
| 11 | 0.9666 |
| 12 | 0.9666 |
| 13 | 0.9666 |
| 14 | 0.9666 |
| 15 | 0.9666 |

Best K value from this test: **1**  
Best F1 score from this test: **0.9666**

## New Sample Prediction

| Feature | Value |
|---|---:|
| Sepal Length | 5.1 |
| Sepal Width | 3.5 |
| Petal Length | 1.4 |
| Petal Width | 0.2 |

Predicted class: **setosa**

## Concepts Used

- Supervised learning
- Classification
- Train-test split
- Feature scaling
- K-Nearest Neighbors
- Confusion matrix
- Precision
- Recall
- F1 score
- Model evaluation

## How to Run

Install the required libraries:

```bash
pip install scikit-learn numpy