import joblib
import pandas as pd

class ChatBot:
    def __init__(self):
        self.name = "Personal Medic"
        self.model = joblib.load("Brain/disease_model.pkl")  # Load trained model
        self.mlb = joblib.load("Brain/mlb.pkl")  # Load MultiLabelBinarizer
        self.df = pd.read_csv("Brain/disease_symptom.csv")  # Load dataset for advice

    def greet(self):
        return "Hello! I am your Personal Medic. How can I assist you with your health today?"

    def predict_disease(self, symptoms):
        # Convert user input into binary symptom presence
        symptoms_list = symptoms.split(", ")
        symptoms_vector = self.mlb.transform([symptoms_list])
        
        # Predict Disease
        predicted_disease = self.model.predict(symptoms_vector)[0]
        return predicted_disease

    def get_advice(self, disease):
        row = self.df[self.df["Possible Disease"] == disease]
        if not row.empty:
            precautions = row["Precautions"].values[0]
            treatment = row["Treatment"].values[0]
            return f"Precautions: {precautions} | Treatment: {treatment}"
        return "No specific advice available."

    def respond(self, user_input):
        user_input = user_input.lower()
        if "symptom" in user_input:
            symptoms = input("Tell me your symptoms (comma-separated): ")
            predicted_disease = self.predict_disease(symptoms)
            print(f"Based on your symptoms, you may have: {predicted_disease}.")
            advice_needed = input("Do you want advice on precautions or treatment? (yes/no): ").lower()
            if advice_needed == "yes":
                print(f"Advice: {self.get_advice(predicted_disease)}")
        else:
            return "I didn't understand. You can ask me about symptoms."

# Test the chatbot
if __name__ == "__main__":
    bot = ChatBot()
    print(bot.greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Take care.")
            break
        bot.respond(user_input)
