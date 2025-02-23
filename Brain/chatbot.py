class ChatBot:
    def __init__(self):
        self.name = "Personal Medic"

    def greet(self):
        return "Hello! I am your Personal Medic. How can I assist you with your health today?"

    def respond(self, user_input):
        user_input = user_input.lower()
        if "symptom" in user_input or "feel" or "feeling" in user_input:
            return "Please describe your symptoms, and I will check for possible diseases."
        elif "reminder" in user_input:
            return "Tell me the medicine name and time, and I'll set a reminder for you."
        else:
            return "I didn't understand. You can ask me about symptoms or set a reminder."

# Test the chatbot
if __name__ == "__main__":
    bot = ChatBot()
    print(bot.greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Take care.")
            break
        print("Bot:", bot.respond(user_input))
