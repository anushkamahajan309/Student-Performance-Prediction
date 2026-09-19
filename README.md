# 🎓 Student Performance Prediction

A Machine Learning project that predicts a student's final score based on their study hours, attendance, assignments completed, and previous score.

## 📌 About the Project

This project uses **Linear Regression** to predict a student's Final Score.

The model takes four inputs:

- 📚 Study Hours
- 📅 Attendance
- 📝 Assignments Completed
- 📊 Previous Score

A simple **Streamlit web application** is also created so users can enter student details and get a predicted final score.

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

## 🤖 Machine Learning Model

**Linear Regression**

The model was trained using:

- 80% training data
- 20% testing data

### Model Performance

- **Mean Absolute Error (MAE):** 2.76
- **Mean Squared Error (MSE):** 12.33
- **R² Score:** 0.79

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
└── .venv/```

🎯 Project Goal

The goal of this project is to learn the complete Machine Learning workflow:

Dataset → Training → Prediction → Evaluation → Streamlit App

👩‍💻 Author

Anushka Mahajan