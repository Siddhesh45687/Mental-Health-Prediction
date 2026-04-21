# 🧠 Mental Health Prediction Using Machine Learning

## 📌 Project Overview

This project focuses on predicting **teen mental health (depression levels)** using Machine Learning techniques. By analyzing behavioral and lifestyle factors such as social media usage, sleep patterns, and physical activity, the model identifies patterns that contribute to mental health conditions.

---

## 📊 Dataset Information

* **Total Records:** 1200
* **Features:**

  * Age
  * Gender
  * Daily Social Media Usage
  * Platform Usage (Instagram, TikTok, Both)
  * Sleep Hours
  * Screen Time Before Sleep
  * Academic Performance
  * Physical Activity
  * Social Interaction Level
  * Stress Level
  * Anxiety Level
  * Addiction Level
* **Target Variable:** `depression_label`

---

## 🔍 Exploratory Data Analysis (EDA)

Key insights discovered:

* 📱 Higher social media usage is linked to increased **stress, anxiety, and depression**
* 😴 Lower sleep hours correlate with higher depression levels
* 🌙 Increased screen time before sleep negatively impacts mental health
* 🏃‍♂️ Physical activity reduces stress levels
* 💬 Low social interaction increases the likelihood of depression

---

## ⚙️ Feature Engineering

* Converted categorical variables into numerical values
* Created a new feature:
  **`screen_exposure = sleep_hours + screen_time_before_sleep`**

---

## 🤖 Machine Learning Models Used

* Logistic Regression
* Random Forest Classifier
* Decision Tree Classifier
* XGBoost Classifier

---

## 🏆 Model Performance

| Model               | Accuracy   |
| ------------------- | ---------- |
| Logistic Regression | 99.16%     |
| Random Forest       | 97.91%     |
| Decision Tree       | 99.16%     |
| XGBoost             | **99.58%** |

---

## 📈 Results & Insights

* XGBoost performed the best with the highest accuracy
* Strong correlation found between:

  * High screen time + Low sleep → Higher depression
  * Low physical activity → Higher stress
* Behavioral data can effectively predict mental health conditions

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries Used:**

  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn
  * Scikit-learn
  * XGBoost

---

## 🚀 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/mental-health-prediction.git

# Navigate to project folder
cd mental-health-prediction

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py
```

---

## 📌 Future Improvements

* Improve model generalization (handle class imbalance)
* Deploy as a web application
* Add real-time prediction system
* Use deep learning models for better insights

---

## 💡 Conclusion

This project demonstrates how Machine Learning can be used to **analyze and predict mental health conditions** based on everyday lifestyle habits. It highlights the importance of balanced digital usage, proper sleep, and physical activity for better mental well-being.

---

