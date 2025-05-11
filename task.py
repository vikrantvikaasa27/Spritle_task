from crewai import Task
from tools import tool
from agent import researcher,writer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} video, including key points, insights, and any relevant details that would be useful for writing a blog post.',
  tools=[tool],
  agent=researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A well-structured blog post that effectively communicates the key points and insights from the video {topic}, tailored for an audience interested in technology.',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='blog_post.md'  
)