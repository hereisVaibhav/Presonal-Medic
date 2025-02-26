import schedule
import time
from datetime import datetime, timedelta

class Reminder:
    def __init__(self):
        self.reminders = []

    def validate_time_format(self, reminder_time):
        """Checks if the given time is in the correct HH:MM format."""
        try:
            datetime.strptime(reminder_time, "%H:%M")  # Try parsing the time
            return True
        except ValueError:
            return False

    def add_reminder(self, medicine, reminder_time, days):
        """Adds a reminder if the time format is valid."""
        if not self.validate_time_format(reminder_time):
            return "❌ Invalid time format! Please enter time in HH:MM (24-hour format)."
        
        end_date = datetime.now() + timedelta(days=days)  # Calculate end date
        self.reminders.append({"medicine": medicine, "time": reminder_time, "end_date": end_date})
        schedule.every().day.at(reminder_time).do(self.notify, medicine, end_date)
        return f"✅ Reminder set for {medicine} at {reminder_time} for {days} days."

    def notify(self, medicine, end_date):
        """Triggers the reminder if within the valid period."""
        if datetime.now() <= end_date:
            print(f"🔔 Time to take your medicine: {medicine}")
        else:
            print(f"✅ Reminder for {medicine} is completed.")
            return schedule.CancelJob  # Stop scheduling once duration ends

    def run_scheduler(self):
        """Runs the scheduler in a loop."""
        print("📅 Reminder system started... Press Ctrl+C to stop.")
        while True:
            schedule.run_pending()
            time.sleep(30)  # Check every 30 seconds

# Test the reminder system
if __name__ == "__main__":
    reminder = Reminder()
    
    medicine = input("Enter medicine name: ")
    reminder_time = input("Enter reminder time (HH:MM format, 24-hour clock): ")

    # Validate the time format before proceeding
    while not reminder.validate_time_format(reminder_time):
        print("❌ Invalid time format! Please enter time as HH:MM (24-hour format).")
        reminder_time = input("Enter reminder time (HH:MM format): ")

    days = int(input("Enter for how many days you need a reminder: "))
    print(reminder.add_reminder(medicine, reminder_time, days))
    reminder.run_scheduler()

