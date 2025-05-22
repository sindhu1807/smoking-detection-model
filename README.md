# 🚬 Smoking Prediction Using Linear Regression

This repository contains a machine learning project focused on predicting an individual's smoking status using health-related metrics from the **National Health Insurance Service (NHIS)** dataset. The primary goal is to apply **Linear Regression** to model the relationship between biometric indicators and smoking behavior.


## 📁 Dataset

The dataset (`smoking.csv`) includes medical examination data such as:

- Demographics: Age, Gender, Height, Weight, Waist Circumference
- Vision & Hearing Tests
- Blood Pressure
- Blood Tests: Cholesterol, Triglycerides, Glucose, etc.
- Dental Health: Presence of Oral Disease and Tartar

**Target Variable:**  
- `smoking` — 0 (Non-smoker), 1 (Smoker)

---

## 🔧 Project Workflow

1. **Data Cleaning**
   - Dropped unnecessary or excessive records to limit processing scope.
   - Removed missing values to ensure model integrity.

2. **Feature Encoding**
   - Categorical features like `gender`, `oral`, and `tartar` were label-encoded using `LabelEncoder`.

3. **Model Training**
   - Applied **Linear Regression** using `scikit-learn`.
   - Dataset split into 80% training and 20% testing.

4. **Model Evaluation**
   - Evaluated with **Mean Squared Error (MSE)** and **R² Score**.

5. **Model Persistence**
   - Saved the trained model using `pickle` for future inference.

---

## 🧠 Model Details

**Algorithm:** Linear Regression  
**Train/Test Split:** 80% / 20%  
**Evaluation Metrics:**
- `Mean Squared Error (MSE)`
- `R² Score`

---

## 💻 Dependencies

- `pandas`
- `numpy`
- `scikit-learn`
- `pickle`

Install required libraries:
```bash
pip install pandas numpy scikit-learn
````

---

## 📊 Features Used

Below are the input features used for prediction:

```
['gender', 'oral', 'tartar', 'age', 'height', 'weight', 'waist',
 'eyesight_left', 'eyesight_right', 'hearing_left', 'hearing_right',
 'systolic', 'relaxation', 'fasting_blood_sugar', 'Cholesterol',
 'triglyceride', 'HDL', 'LDL', 'hemoglobin', 'urine_protein',
 'serum_creatinine', 'AST', 'ALT', 'Gtp', 'dental_caries']
```

---

## 📈 Results (Sample Output)

```
Model Intercept: <insert_value>
Model Coefficients: <insert_values>
Mean Squared Error: <insert_value>
R² Score: <insert_value>
```

---

## 🔮 Example: Making Predictions

```python
import pickle

# Load model
model = pickle.load(open('mr.pkl', 'rb'))

# Predict using new data (replace values accordingly)
sample_input = [[0.0, 0.0, 40.0, 155.0, 60.0, 81.3, 1.2, 1.0, 1.0,
                 1.0, 114.0, 73.0, 94.0, 215.0, 82.0, 73.0, 126.0,
                 12.9, 1.0, 0.7, 18.0, 19.0, 27.0, 0.0, 0.0, 1.0]]

prediction = model.predict(sample_input)
print("Smoking prediction:", prediction)
```

---

## 📌 Notes

* This model is a basic regression approach. Smoking prediction is inherently a **classification** problem, and future work could explore models like **Logistic Regression**, **Random Forest**, or **XGBoost** for improved accuracy.
* Ensure data scaling and domain-specific validations for production-grade deployment.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

