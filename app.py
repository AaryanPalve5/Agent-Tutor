from flask import Flask, render_template, request
from agents.mentor_agent import MentorAgent
import markdown

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
mentor_agent = MentorAgent()

import re

def simple_format_markdown(text):
    # Convert **bold** to <strong> and *italic* to <em>
    # Handle bold first, then italic
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Convert `code` to <code>
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # Convert newlines to <br> (optional for better spacing)
    text = text.replace('\n', '<br>')
    return text


@app.route('/', methods=['GET', 'POST'])
def index():
    answer_html = ""
    subject = ""
    if request.method == 'POST':
        question = request.form.get('question')
        answer, subject = mentor_agent.handle_question(question)
        answer_html = simple_format_markdown(answer)
    return render_template('index.html', answer=answer_html, subject=subject)
 
if __name__ == "__main__":
    app.run(debug=True)
