import wikipediaapi
import random
import json

class ChatBot:
    def __init__(self):
        self.name = "Personal Medic"
        self.user_memory = {}  # Stores user’s last symptoms & reminders
        self.health_data = self.load_health_data()  # Loads predefined health responses
        self.wiki = wikipediaapi.Wikipedia(user_agent="PersonalMedicBot", language="en")  # Wikipedia API setup

    def load_health_data(self):
        """Loads health-related responses from a JSON file."""
        try:
            with open("Brain/health_data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"post_conversation": ["Take care!"], "symptoms_responses": {}, "general_responses": {}}

    def remember(self, key, value):
        """Stores user details (e.g., last symptom or last reminder)."""
        self.user_memory[key] = value

    def retrieve_memory(self, key):
        """Retrieves stored user details."""
        return self.user_memory.get(key, None)

    def fetch_symptom_info(self, symptom):
        """Fetches symptom details from Wikipedia (500 words)."""
        page = self.wiki.page(symptom)
        if page.exists():
            return page.summary[:1000] + "..."  # Limit to 500 words
        else:
            return "I couldn't find reliable information on that symptom. Please consult a doctor."

    def respond(self, user_input):
        """Processes user input and provides a relevant response."""
        user_input = user_input.lower()

        # Check for predefined responses in health_data.json
        if user_input in self.health_data["general_responses"]:
            return self.health_data["general_responses"][user_input]

        # Check for symptoms and return pre-defined responses
        for symptom, response in self.health_data["symptoms_responses"].items():
            if symptom in user_input:
                return response

        # Fetch symptom details from Wikipedia
        if "symptom" in user_input or "feel" in user_input or "sick" in user_input:
            last_symptom = self.retrieve_memory("last_symptom")
            if last_symptom:
                return f"Last time, you mentioned '{last_symptom}'. Still experiencing it?"

            symptom = input("Enter your symptoms: ").lower()
            self.remember("last_symptom", symptom)
            return f"Noted your symptom: {symptom}.\nHere's what I found:\n{self.fetch_symptom_info(symptom)}"

        elif "reminder" in user_input:
            medicine = input("Enter medicine name: ")
            time = input("Enter reminder time (HH:MM format, 24-hour clock): ")
            self.remember("last_medicine", medicine)
            return f"Reminder set for {medicine} at {time}."

        elif "last symptom" in user_input:
            last_symptom = self.retrieve_memory("last_symptom")
            return f"Your last mentioned symptom was '{last_symptom}'." if last_symptom else "You haven't mentioned any symptoms yet."

        elif "health tip" in user_input:
            return random.choice(self.health_data.get("post_conversation", ["Take care!"]))

        else:
            return "I didn't understand. Can you be more specific?"

# Test the chatbot
if __name__ == "__main__":
    bot = ChatBot()
    print("Hello! I am your Personal Medic. How can I assist you?")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye"]:
            print(random.choice(bot.health_data.get("post_conversation", ["Take care!"])))
            break
        print("Bot:", bot.respond(user_input))
