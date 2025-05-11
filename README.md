# Multi agent system Using CrewAI

This project implements an AI-powered blog post generator system using CrewAI, which automates the process of researching and writing content based on specific topics. The system uses a multi-agent approach where specialized AI agents work together to create high-quality content.

## 🚀 Features

- **Research Agent**: Analyzes topics and identifies key trends, pros, cons, and market opportunities
- **Writer Agent**: Transforms research into well-structured, engaging content
- **Customizable Tasks**: Flexible task definitions for different types of content
- **Output File Generation**: Automatically saves generated content to markdown files

## Explanation
This AI-powered blog post generator was built using CrewAI, and it uses two agetns which is mainly responible for the blog post generator ,
- **Research Agent**
- **Writer Agent**
  
These two agents work sequentially to perform their own tasks with the specified tools,

Tools used:
- **Serper Tool**: Serper is the fastest Google search api helps to provide the fastest search results.
  
When a user gives a topic to this system, the research agent utilizes the Serp web search tool to provide the required data and information for the writer agent to generate the blog post.

Then the write agent executes its part of generating the desired blog post with the given data from the research agent.

The Agents use **Google Gemini-2.0-flash** LLM model for the generation.


## 📋 Prerequisites

- Python 3.11

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/vikrantvikaasa27/Spritle_task.git
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the python script:
```
python crew.py
```

## 📦 Dependencies

- crewai: Core framework for AI agent orchestration
- crewai_tools: Additional tools for CrewAI agents

## 🏗️ Project Structure

```
├── agent.py         # Agent definitions and configurations
├── task.py          # Task definitions for research and writing
├── tools.py         # Custom tools for agents
├── requirements.txt # Project dependencies
└── blog_post.md     # Generated content output
```

The system will:
1. Research the topic using the research agent
2. Generate content using the writer agent
3. Save the output to `blog_post.md`
