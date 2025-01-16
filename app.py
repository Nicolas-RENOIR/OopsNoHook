import pickle
from tensorflow.keras.models import load_model
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
    print("""
   ____                   _   __      __  __            __  
  / __ \____  ____  _____/ | / /___  / / / /___  ____  / /__
 / / / / __ \/ __ \/ ___/  |/ / __ \/ /_/ / __ \/ __ \/ //_/
/ /_/ / /_/ / /_/ (__  ) /|  / /_/ / __  / /_/ / /_/ / ,<   
\____/\____/ .___/____/_/ |_/\____/_/ /_/\____/\____/_/|_|  
          /_/                                               
""")
    while True:
        email_text = input("Enter email content or \"exit\" : ")
        if email_text.lower() == 'exit':
            break

        result = predict_email(email_text)
        print(f"Prediction: {result}")

if __name__ == "__main__":
    main()
