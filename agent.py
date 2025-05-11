from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from crewai import LLM
import os


## call the gemini models
llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5,
    verbose=True
)

# Creating a senior researcher agent with memory and verbose mode

researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
