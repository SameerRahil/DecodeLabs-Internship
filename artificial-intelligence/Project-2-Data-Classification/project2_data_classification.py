#Week 2 - Sameer
import sys
from collections import Counter

try:
    import numpy as np
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import f1_score
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
except ImportError:
    print()
    print("Required libraries are missing.")
    print("Install them by running this command:")
    print("pip install scikit-learn numpy")
    print()
    sys.exit()


def print_section(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


#loads the iris dataset
def load_dataset():
    iris = load_iris()
    features = iris.data
    labels = iris.target
    feature_names = iris.feature_names
    class_names = iris.target_names
    return features, labels, feature_names, class_names


#basic dataset info
def show_dataset_information(features, labels, feature_names, class_names):
    print_section("Dataset Overview")

    print("Dataset used: Iris flower dataset")
    print("Number of samples:", features.shape[0])
    print("Number of features:", features.shape[1])
    print("Number of classes:", len(class_names))

    print()
    print("Feature names:")
    for index, name in enumerate(feature_names, start=1):
        print(str(index) + ".", name)

    print()
    print("Class names:")
    for index, name in enumerate(class_names):
        print(str(index) + ":", name)

    print()
    print("Class distribution:")
    class_counts = Counter(labels)
    for class_index, count in class_counts.items():
        print(class_names[class_index] + ":", count, "samples")

    print()
    print("First five rows of data:")
    for index in range(5):
        print("Features:", features[index], "Label:", class_names[labels[index]])


# splits the dataset into training and testing data
def split_dataset(features, labels):
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=0.2,
        random_state=42,
        shuffle=True,
        stratify=labels
    )

    return x_train, x_test, y_train, y_test


#scale the feature values
def scale_features(x_train, x_test):
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    return x_train_scaled, x_test_scaled, scaler


#train
def train_knn_model(x_train, y_train, k_value):
    model = KNeighborsClassifier(n_neighbors=k_value)
    model.fit(x_train, y_train)

    return model


#eval
def evaluate_model(model, x_test, y_test, class_names):
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted")
    recall = recall_score(y_test, predictions, average="weighted")
    f1 = f1_score(y_test, predictions, average="weighted")
    matrix = confusion_matrix(y_test, predictions)
    print_section("Model Evaluation")
    print("Accuracy:", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall:", round(recall, 4))
    print("F1 Score:", round(f1, 4))
    print()
    print("Confusion Matrix:")
    print(matrix)
    print()
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=class_names))
    return predictions, accuracy, precision, recall, f1, matrix


#compares different k values
def compare_k_values(x_train, x_test, y_train, y_test):
    print_section("K Value Comparison")
    best_k = None
    best_score = 0

    for k_value in range(1, 16):
        model = KNeighborsClassifier(n_neighbors=k_value)
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        score = f1_score(y_test, predictions, average="weighted")

        print("K =", k_value, "| F1 Score =", round(score, 4))

        if score > best_score:
            best_score = score
            best_k = k_value

    print()
    print("Best K value from this test:", best_k)
    print("Best F1 score from this test:", round(best_score, 4))


#predicts the class for a new flower sample
def predict_new_sample(model, scaler, class_names):
    print_section("New Sample Prediction")

    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    scaled_sample = scaler.transform(sample)
    prediction = model.predict(scaled_sample)

    print("New flower measurements:")
    print("Sepal length:", sample[0][0])
    print("Sepal width:", sample[0][1])
    print("Petal length:", sample[0][2])
    print("Petal width:", sample[0][3])
    print()
    print("Predicted class:", class_names[prediction[0]])


#runs the full classification pipeline
def main():
    print_section("DecodeLabs Project 2")
    print("Data Classification Using AI")
    print("Algorithm: K-Nearest Neighbors")
    print("Dataset: Iris")

    features, labels, feature_names, class_names = load_dataset()

    show_dataset_information(features, labels, feature_names, class_names)

    x_train, x_test, y_train, y_test = split_dataset(features, labels)

    print_section("Train Test Split")
    print("Training samples:", x_train.shape[0])
    print("Testing samples:", x_test.shape[0])
    print("Split ratio: 80 percent training and 20 percent testing")

    x_train_scaled, x_test_scaled, scaler = scale_features(x_train, x_test)

    print_section("Feature Scaling")
    print("StandardScaler applied")
    print("Training data mean after scaling:", np.round(x_train_scaled.mean(axis=0), 4))
    print("Training data standard deviation after scaling:", np.round(x_train_scaled.std(axis=0), 4))

    k_value = 5
    model = train_knn_model(x_train_scaled, y_train, k_value)

    print_section("Model Training")
    print("KNN model trained successfully")
    print("K value used:", k_value)

    evaluate_model(model, x_test_scaled, y_test, class_names)

    compare_k_values(x_train_scaled, x_test_scaled, y_train, y_test)

    predict_new_sample(model, scaler, class_names)

    print_section("Project Completed")
    print("The Iris classification model was trained, tested, and evaluated successfully.")


#start
if __name__ == "__main__":
    main()