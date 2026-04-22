🔧 Machine Predictive Maintenance using Machine Learning

📌 Project Overview
This project focuses on building a Machine Learning-based Predictive Maintenance system for industrial machines. The goal is to predict whether a machine is likely to fail or operate normally based on sensor and operational data. This enables industries to shift from reactive maintenance to predictive maintenance, reducing downtime and financial losses.

🎯 Objective
To develop a classification model that predicts:
0 → Machine is Healthy (No Failure)
1 → Machine is Likely to Fail
The system helps in early detection of machine failures to improve operational efficiency and reduce unexpected breakdowns.

📊 Dataset
Source: Kaggle Predictive Maintenance Dataset
Contains sensor readings and operational parameters of industrial machines
Target variable: Machine failure status (binary classification)

⚙️ Workflow

1. Data Preprocessing
Feature-target separation
Train-test split
Handling categorical variables using Label Encoding
Feature scaling using RobustScaler (to handle outliers)

2. Handling Class Imbalance
Applied SMOTE (Synthetic Minority Oversampling Technique)
Balanced failure and non-failure classes to improve model learning

3. Model Training
Multiple classification models were trained:
Logistic Regression
K-Nearest Neighbors
Support Vector Classifier
Naive Bayes
Decision Tree Classifier
Random Forest Classifier
Gradient Boosting Classifier

4. Model Evaluation
Models were evaluated using:
Confusion Matrix
Classification Report (Precision, Recall, F1-score, Accuracy)

Focus was placed on reducing:
❗ False Negatives (critical failure cases missed)
⚠️ False Positives (false alarms)

5. Hyperparameter Tuning
Applied GridSearchCV
Used 5-Fold Cross Validation
Evaluation metric: F1-Weighted Score
Selected best model based on performance consistency

🏆 Final Model
Random Forest Classifier
Achieved ~97% accuracy
Best balance between precision and recall
Lowest false negative rate among tested models

🚀 Deployment
Final model saved along with:
Label Encoder
RobustScaler
Web application built using:
Backend: Django
Frontend: HTML Forms
Deployment Flow:

User Input → Preprocessing (Scaler + Encoder) → ML Model → Prediction Output

📈 Impact
Enables predictive maintenance strategy
Reduces machine downtime and operational cost
Improves machine lifecycle and production efficiency
Helps industries plan maintenance schedules proactively

🔮 Future Enhancements
Predict type of failure (multi-class classification)
Reduce false negatives further through advanced tuning
Integrate IoT sensors for real-time predictions
Deploy as a fully automated industrial monitoring system
Improve real-time data streaming and model retraining

🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
Imbalanced-learn (SMOTE)
Django (Deployment)
HTML/CSS

📌 Author
Krithiksha
Machine Learning & Data Science Enthusiast