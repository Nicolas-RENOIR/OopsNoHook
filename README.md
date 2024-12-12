# 📧 Phishing Email Detector (LSTM)

## Overview
This project is a Python-based application that detects phishing emails using a **Long Short-Term Memory (LSTM)** machine learning model. The application analyzes the email content and predicts whether the email is "Phishing" or "Legitimate."

## 🚀 Features
- **LSTM Model:** Utilizes an advanced deep learning model for email classification.
- **Interactive Console Application:** Users can input email content directly into the console.
- **Real-time Prediction:** Provides instant feedback on email classification.

## 🛠 Prerequisites
- Python 3.8+

### Required Libraries
Install the required libraries using `pip`:
```bash
pip install tensorflow scikit-learn numpy
```

## 📝 Usage
### 1. Clone the Repository
```bash
git clone https://github.com/Nicolas-RENOIR/phishing-email-detector.git
cd phishing-email-detector
```

### 2. Add Your Trained Model and Vectorizer
Ensure the following files are in the project directory:
- `lstm_model.h5`: Trained LSTM model.
- `vectorizer.pkl`: TF-IDF vectorizer used for preprocessing.

### 3. Run the Application
Execute the script to start the console application:
```bash
python app.py
```

### 4. Predict Email Classification
- Enter the email content when prompted.
- View the LSTM model's prediction.
- Type `exit` to quit the application.

## 📊 Example Output
```plaintext
=== Phishing Email Detector ===
Enter email content (or type 'exit' to quit): Congratulations! You've won a prize. Click here to claim.
Prediction: Phishing

Enter email content (or type 'exit' to quit): Meeting at 3 PM today in the conference room.
Prediction: Legitimate

Enter email content (or type 'exit' to quit): Your bank account is locked. Please update your information.
Prediction: Phishing
```

## 📂 File Structure
```
phishing-email-detector/
├── app.py                # Main application script
├── lstm_model.h5         # Trained LSTM model
├── vectorizer.pkl        # TF-IDF vectorizer
├── README.md             # Project documentation
```

## 📬 Contact
For inquiries, please contact [Nicolas](mailto:rnicolas1202@gmail.com).
