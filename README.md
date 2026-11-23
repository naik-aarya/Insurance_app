# Insurance Premium Price Prediction Using Machine Learning

## 1. Project Overview

This project focuses on predicting insurance premium prices using Machine Learning regression algorithms.

The model analyzes customer information such as age, gender, BMI, smoking habits, number of dependents, and other relevant features to estimate insurance premium costs.

The objective is to build an accurate predictive model that helps understand the factors influencing insurance premium prices.

## 2. Problem Statement

Insurance premium prices vary depending on several factors, including customer demographics, health conditions, and lifestyle habits.

Estimating insurance costs manually can be challenging due to the involvement of multiple variables.

This project applies Machine Learning regression techniques to predict insurance premium prices based on customer information and historical insurance data.

## 3. Project Objectives

- Perform Exploratory Data Analysis (EDA).
- Understand factors influencing insurance premium prices.
- Clean and preprocess the dataset.
- Perform feature engineering and encoding.
- Apply feature scaling where required.
- Train multiple Machine Learning regression models.
- Evaluate and compare model performance.
- Select the best-performing regression model.
- Predict insurance premium prices for new customers.

## 4. Dataset Description

The project uses an insurance dataset containing customer demographic, health, and lifestyle information.

**Common dataset features include:**

- Age: Age of the customer.
- Gender: Gender of the customer.
- BMI: Body Mass Index.
- Children: Number of dependents.
- Smoker: Smoking status.
- Region: Residential region.
- Charges: Insurance premium amount (Target Variable).

*Note: Adjust these features according to your actual dataset.*

## 5. Technologies and Libraries Used

- **Programming Language:** Python
- **Data Manipulation:** NumPy, Pandas
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Model Saving:** Joblib, Pickle
- **Deployment:** Streamlit

## 6. Machine Learning Algorithms

The following regression algorithms are implemented:

1. Linear Regression
2. K-Nearest Neighbors (KNN) Regressor
3. Decision Tree Regressor
4. Random Forest Regressor
5. Gradient Boosting Regressor
6. Support Vector Regressor (SVR)
7. XGBoost Regressor

## 7. Project Workflow

1. Data Collection
2. Data Loading
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Handling Missing Values
6. Categorical Feature Encoding
7. Feature Scaling
8. Train-Test Split
9. Model Training
10. Hyperparameter Tuning
11. Model Evaluation
12. Model Comparison
13. Best Model Selection
14. Model Serialization
15. Insurance Premium Prediction

## 8. Model Evaluation Metrics

The regression models are evaluated using:

- **R² Score:** Measures how well the model explains variations in the target variable.
- **Adjusted R²:** Evaluates model fit while accounting for the number of predictors.
- **RMSE (Root Mean Squared Error):** Measures the average magnitude of prediction errors, with greater penalty for larger errors.

These metrics help compare regression models and identify the most suitable model.

## 9. Best Model Selection

Support Vector Regressor (SVR) achieved the best performance in the previous model evaluation, with an R² score of approximately 0.867.

The final model selection should be based on the evaluation results obtained from the same test dataset.

## 10. Deployment

The selected Machine Learning model is saved using Joblib/Pickle and integrated into a Streamlit web application.

The application allows users to enter customer details and receive predicted insurance premium estimates.

## 11. Real-World Applications

- Insurance premium estimation.
- Customer risk assessment.
- Insurance pricing analysis.
- Data-driven insurance decision-making.
- Understanding factors affecting insurance costs.

## 12. Project Structure

```text
Insurance-Premium-Price-Prediction/
│
├── README.md
├── requirements.txt
├── app.py
├── main.py
├── insurance.csv
│
├── models/
│   └── insurance_model.pkl
│
└── images/
    ├── correlation_matrix.png
    ├── model_comparison.png
    └── prediction_results.png
```

*Include only the files and folders that are actually present in your project.*

## 13. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/naik-aarya/Insurance-Premium-Price-Prediction.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Insurance-Premium-Price-Prediction
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

## 14. Conclusion

This project demonstrates the application of Machine Learning regression algorithms to predict insurance premium prices.

By implementing and comparing multiple regression models, the project identifies an effective approach for estimating insurance costs based on customer characteristics.

It provides practical experience in data preprocessing, exploratory data analysis, feature engineering, regression modelling, model evaluation, and deployment using Streamlit.

---

**Author:** Aarya Naik

**GitHub:** https://github.com/naik-aarya
