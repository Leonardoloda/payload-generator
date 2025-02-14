class Prompts:
    def __init__(self):
        self.prompts = {
            "welcome": "Welcome to the payload generator! Please select an application to start?",
        }

        self.applications = {
            "crew": "Crew",
            "hotels": "Hotels",
            "monthly": "Monthly Block Limits"
        }

    def get_prompt(self, key):
        return self.prompts.get(key)