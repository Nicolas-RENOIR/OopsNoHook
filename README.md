# 📧 Phishing Email Detector (LSTM)

## 🌍 Overview
This project is a Python-based application that detects phishing emails using a **Long Short-Term Memory (LSTM)** machine learning model. The application analyzes the email content and predicts whether the email is "Phishing" or "Legitimate" using TensorFlow.

## 🚀 Features
- **LSTM Model:** Utilizes an advanced deep learning model for email classification.
- **Interactive Console Application:** Users can input email content directly into the console.
- **Real-time Prediction:** Provides instant feedback on email classification.

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

## 📬 Credits
[Nicolas](mailto:rnicolas1202@gmail.com) - [Killian](mailto:killianfournier2003@gmail.com) - [Lucas](mailto:lopeslucas0311@gmail.com)
