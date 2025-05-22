from agents.gemini_api import ask_gemini

class PhysicsAgent:
    def answer(self, question):
        return ask_gemini("physics", question)
