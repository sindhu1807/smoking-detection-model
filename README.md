# 🚬 Smoking Prediction Web App using Linear Regression

This project uses machine learning to predict the likelihood of an individual being a smoker based on biometric and health signals. The application includes a trained model, a Flask web server, and a simple HTML frontend.

---

## 📌 Features

- 📊 Predicts smoking probability using 26 biometric and health metrics
- 🧠 Trained using `scikit-learn` Linear Regression
- 💾 Model serialized using `pickle`
- 🌐 Flask-powered web interface with user input form
- 🧼 Basic data preprocessing and encoding steps

---

## 🏗️ Project Structure

```

smoking-predictor/
├── app.py                 # Flask web server
├── model\_train.py         # ML training script
├── smoking.csv            # Dataset
├── mrs/
│   └── mr.pkl             # Saved trained model
├── templates/
│   └── index.html         # Web form interface
├── static/                # (Optional) CSS/JS assets
└── README.md              # Project documentation

````

---

## 🧠 Model Training

Run the training script to generate `mr.pkl`:

```bash
python model_train.py
````

This script:

* Loads and cleans the dataset
* Encodes categorical variables (gender, oral, tartar)
* Trains a Linear Regression model
* Saves the model in the `mrs/` directory

---

## 🌐 Running the Web App

Install required libraries:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
pandas
numpy
scikit-learn
flask
```

Start the Flask server:

```bash
python app.py
```

Then open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥️ Web Interface

The form takes in 26 numeric input values including:

* Gender (0 = Female, 1 = Male)
* Age, Height, Weight, Waist, Eyesight, Hearing
* Blood pressure, Sugar, Cholesterol levels, etc.
* Oral Health (Oral exam, Tartar, Dental Caries)

After submission, it displays the **predicted probability** of the person being a smoker.

> 📝 Note: All inputs are required and must be numerical.

---

## 🎯 Sample Output

```
Prediction of smoking is 0.83
```

---

## 💡 Future Improvements

* Switch from regression to classification (e.g., Logistic Regression or RandomForestClassifier)
* Add input validation and better UI/UX
* Deploy online using Render, Heroku, or Vercel
* Include real-world visuals or dashboard

---

## 📬 Contact

Contributions and questions are welcome!
Raise an issue or submit a pull request.

---

## 📝 License

Distributed under the [MIT License](LICENSE).

