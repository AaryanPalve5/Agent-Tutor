from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent
from agents.chemistry_agent import ChemistryAgent
from agents.subject_classifier import classify_subject

class MentorAgent:
    def __init__(self):
        self.subject_agents = {
            "math": MathAgent(),
            "physics": PhysicsAgent(),
            "chemistry": ChemistryAgent()
        }

    def handle_question(self, question):
        subject = classify_subject(question)
        if subject not in self.subject_agents:
            return "Sorry, I could not determine the subject of your question.", subject
        agent = self.subject_agents[subject]
        answer = agent.answer(question)
        return answer, subject

