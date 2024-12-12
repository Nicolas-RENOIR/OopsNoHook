import pickle
from tensorflow.keras.models import load_model  # For LSTM models
from sklearn.feature_extraction.text import TfidfVectorizer

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

model = load_model("LSTM.h5")

def predict_email(email_text):
    """Predict whether an email is phishing or legitimate."""
    email_vectorized = vectorizer.transform([email_text])
    
    prediction = model.predict(email_vectorized.toarray())
    predicted_class = (prediction > 0.5).astype(int)[0][0]
    
    result = "Phishing" if predicted_class == 1 else "Legitimate"
    return result

def main():
    print("=== Phishing Email Detector ===")
    while True:
        email_text = input("Enter email content (or type 'exit' to quit): ")
        if email_text.lower() == 'exit':
            print("Goodbye!")
            break

        result = predict_email(email_text)
        print(f"Prediction: {result}")

if __name__ == "__main__":
    main()