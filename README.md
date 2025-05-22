
# 📚 Agent Tutor

## **Project URL**

Live Demo: [https://agent-tutor.onrender.com](https://agent-tutor.onrender.com)

---

## **System Overview**

Mentor Agent Tutor Bot is a multi-agent AI system designed to intelligently answer academic questions using agentic AI principles and Gemini LLMs.
Key features include:

* **Natural language subject classification (no hardcoded rules)**
* **Agent delegation and tool use**
* **Clean, mobile-friendly UI**
* **Fully deployable and scalable**

---

## **Core Components**

### 1. **MentorAgent (Orchestrator)**

* Receives the user’s question.
* Uses LLM-based classification (Gemini 1.5 Pro) to determine the academic subject (Math, Physics, Chemistry).
* Delegates the question to the corresponding SubjectAgent.

### 2. **SubjectAgents (Specialists)**

* **MathAgent:** Handles math questions. Uses CalculatorTool for arithmetic and Gemini for other math queries.
* **PhysicsAgent:** Handles physics questions via Gemini.
* **ChemistryAgent:** Handles chemistry questions via Gemini.

### 3. **Tools**

* **CalculatorTool:** For numeric/math expressions within MathAgent.

### 4. **Gemini API**

* Used both for subject classification and for generating subject-specific answers.

---

## **How It Works (Flow)**

1. **User Input:**
   User asks any academic question in the UI.

2. **Subject Classification:**
   MentorAgent invokes the Gemini LLM to classify the question into Math, Physics, Chemistry, or Unknown.

3. **Task Delegation:**
   MentorAgent routes the question to the appropriate SubjectAgent.

4. **Answer Generation:**

   * SubjectAgent invokes Gemini LLM (or CalculatorTool for math) to answer.
   * The answer and detected subject are shown to the user.

---

## **Endpoints**

### `/` (Home)

* **Method:** GET, POST
* **Description:** Main UI page. Accepts user question (POST), returns answer and detected subject.

---

## **File Structure**

```
├── app.py
├── agents/
│   ├── mentor_agent.py
│   ├── math_agent.py
│   ├── physics_agent.py
│   ├── chemistry_agent.py
│   ├── subject_classifier.py
│   └── gemini_api.py
├── tools/
│   └── calculator.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── Procfile
├── .env.example
├── README.md
└── DOCUMENTATION.md (this file)
```

---

## **Extending the System**

* **To add a new subject:**

  * Create a new SubjectAgent (e.g., `biology_agent.py`).
  * Update the LLM prompt in `subject_classifier.py` to include “biology”.
  * Add the new agent to `mentor_agent.py`.

* **To add more tools:**

  * Create a new tool in `tools/`.
  * Add logic to the appropriate SubjectAgent.

---

## **Deployment (on Render)**

**Deployed at:** [https://agent-tutor.onrender.com](https://agent-tutor.onrender.com)

* Render auto-installs all Python requirements.
* App reads `GEMINI_API_KEY` from Render environment variables.
* Flask server is bound to `0.0.0.0` and `PORT` for public access.

---

## **Agentic AI and ADK Principles**

* **Modularity:** Each agent is a distinct, reusable, and extendable class.
* **Autonomy:** SubjectAgents make independent decisions (tool use or LLM).
* **Orchestration:** MentorAgent routes requests based on LLM “reasoning”, not code rules.
* **Extendable:** Easily add new agents or tools for more subjects or tasks.

---

## **How to Run Locally**

1. Clone the repo:

   ```
   git clone https://github.com/yourusername/agent-tutor.git
   cd agent-tutor
   ```
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Add your Gemini API key to `.env`
4. Start the app:

   ```
   python app.py
   ```
5. Visit [http://localhost:5000](http://localhost:5000)

---

## **How to Deploy (Render.com)**

1. Push code to GitHub.
2. Create a new Web Service on Render.
3. Set Start Command: `python app.py`
4. Add environment variable: `GEMINI_API_KEY`
5. Deploy and share your live URL!

---
