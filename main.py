from Brain.chatbot import ChatBot
from Brain.symptom_checker import SymptomChecker
from Brain.reminder import Reminder

def main():
    bot = ChatBot()
    checker = SymptomChecker()
    reminder = Reminder()

    print(bot.greet())

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Goodbye! Take care. 🏥")
            break

        elif "symptom" in user_input or "feel" in user_input or "feeling" in user_input:
            symptom = input("Enter your symptoms: ")
            print("A.I:", checker.search_symptom(symptom))

        elif "reminder" in user_input:
            medicine = input("Enter medicine name: ")
            reminder_time = input("Enter reminder time (HH:MM format, 24-hour clock): ")

            while not reminder.validate_time_format(reminder_time):
                print("❌ Invalid time format! Please enter time as HH:MM (24-hour format).")
                reminder_time = input("Enter reminder time (HH:MM format): ")

            days = int(input("Enter for how many days you need a reminder: "))
            print("A.I:", reminder.add_reminder(medicine, reminder_time, days))
            print("📅 Reminder system running in the background...")

        else:
            print("A.I:", bot.respond(user_input))

if __name__ == "__main__":
    main()
