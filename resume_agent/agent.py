from google.adk.agents import Agent


def save_resume(resume: str):
    """
    Save the adapted resume to the file "output.md".
    """
    with open("output.md", "w") as file:
        file.write(resume)


root_agent = Agent(
    name="resume_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to adapt the resume to the job description provided by the user.",
    instruction="""
    You are a resume agent that will be used to adapt the resume to the job description provided by the user.
    You are highly skilled in the Human Resources domain.
    Ask the user for the job description and his/her resume. 
    Your goal is to adapt the resume to maximize the chances of getting the job.
    Your output should be a new resume that is adapted to the job description in markdown format.
    Save the output using the save_resume tool.
    """,
    tools=[save_resume],
)
