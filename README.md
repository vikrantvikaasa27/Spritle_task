# AI-Powered Content Generation System

This project implements an AI-powered content generation system using CrewAI, which automates the process of researching and writing content based on specific topics. The system uses a multi-agent approach where specialized AI agents work together to create high-quality content.

## 🚀 Features

- **Research Agent**: Analyzes topics and identifies key trends, pros, cons, and market opportunities
- **Writer Agent**: Transforms research into well-structured, engaging content
- **Automated Content Generation**: Streamlines the process of creating blog posts and articles
- **Customizable Tasks**: Flexible task definitions for different types of content
- **Output File Generation**: Automatically saves generated content to markdown files

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 📦 Dependencies

- crewai: Core framework for AI agent orchestration
- crewai_tools: Additional tools for CrewAI agents

## 🏗️ Project Structure

```
├── agent.py          # Agent definitions and configurations
├── task.py          # Task definitions for research and writing
├── tools.py         # Custom tools for agents
├── requirements.txt # Project dependencies
└── blog_post.md     # Generated content output
```

## 💻 Usage

1. Import the necessary components:
```python
from task import research_task, write_task
```

2. Define your topic and run the tasks:
```python
topic = "Your Topic Here"
research_task.execute(topic=topic)
write_task.execute(topic=topic)
```

The system will:
1. Research the topic using the research agent
2. Generate content using the writer agent
3. Save the output to `blog_post.md`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- CrewAI framework for providing the foundation for AI agent orchestration
- All contributors who have helped shape this project

## 📧 Contact

For any questions or suggestions, please open an issue in the repository. 