# 🎓 Student Performance Prediction

This is a Machine Learning project that predicts a student's final score based on their study hours, attendance, assignments completed, and previous score.

## 📌 About

The model predicts the **Final Score** using:

- 📚 Study Hours
- 📅 Attendance
- 📝 Assignments Completed
- 📊 Previous Score

A Streamlit web application is also created where users can enter student details and get a predicted final score.

## 🤖 Machine Learning Model

I used **Linear Regression** for prediction.

### Model Performance

- **Mean Absolute Error (MAE):** 2.76
- **Mean Squared Error (MSE):** 12.33
- **R² Score:** 0.79

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── Data/
│   └── Student_Data.csv
│
├── student_model.ipynb
├── student_model.pkl
├── AI_Page.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application

```bash
streamlit run AI_Page.py
```

## 🎯 Project Goal

The goal of this project is to understand the complete Machine Learning workflow:

**Dataset → Data Analysis → Train/Test Split → Model Training → Prediction → Evaluation → Model Saving → Streamlit App**

## 📚 What I Learned

- Loading and exploring datasets using Pandas
- Data preprocessing
- Feature and target selection
- Train-test splitting
- Linear Regression
- Model evaluation using MAE, MSE and R²
- Saving ML models using Joblib
- Building a Streamlit application
- Connecting a trained ML model to a web application

## 👩‍💻 Author

**Anushka Mahajan**