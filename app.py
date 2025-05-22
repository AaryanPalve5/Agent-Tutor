from flask import Flask, render_template, request
from agents.mentor_agent import MentorAgent

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
mentor_agent = MentorAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    subject = ""
    if request.method == 'POST':
        question = request.form.get('question')
        answer, subject = mentor_agent.handle_question(question)
    return render_template('index.html', answer=answer, subject=subject)

if __name__ == "__main__":
    app.run(debug=True)
