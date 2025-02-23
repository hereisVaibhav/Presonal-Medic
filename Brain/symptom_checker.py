import wikipediaapi

class SymptomChecker:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia(
            language="en", 
            user_agent="PersonalMedicBot/1.0 (vaibhav@personalmedic.com)"
        )

    def search_symptom(self, symptom):
        page = self.wiki.page(symptom)
        if page.exists():
            return f"Possible disease info:\n{page.summary[:500]}..."  # First 500 chars
        else:
            return "No reliable information found for this symptom."

# Test the symptom checker
if __name__ == "__main__":
    checker = SymptomChecker()
    symptom = input("Enter a symptom: ")
    print(checker.search_symptom(symptom))
