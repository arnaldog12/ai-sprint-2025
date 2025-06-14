# 🤖 Resume Agent

An AI Agent to maximize your chances of getting a job by matching your resume with a job description.

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/arnaldog12/ai-sprint-2025.git
cd ai-sprint-2025
```

Create the virtual environment, activate it, and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install google-adk
```

Finally, create a `.env` file inside the `resume_agent` directory with the following content:

```bash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

> 💡 You can get a Google API key in the [Google AI Studio][ai-studio]

## 🚀 Run

You can chat with the agent using the UI interface:

```bash
adk web
```

You can use the `resume.md` and `job_description.md` files as examples.

Your adapted resume will be saved in the `output.md` file.

## 🎉 Acknowledgments

This project was created during the AI Sprint 2025, organized by GDE Program. Google Cloud credits were provided for this project

[ai-studio]: https://aistudio.google.com/apikey
