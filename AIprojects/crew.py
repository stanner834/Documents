import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = ""

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

# Define your agents with roles and goals
researcher = Agent(
    role='Cybersecurity Researcher',
    goal="""Conduct thorough research to gather today's latest news and insights on 
    cybersecurity, including specific vulnerabilities, patches, new malware, data breaches, 
    emerging trends, in technology, AI, threat intelligence, and cybersecurity tools, technologies, and products. Utilize 
    reputable sources such as 'HackerNews.com' and 
    https://www.cisa.gov/known-exploited-vulnerabilities-catalog to ensure 
    accuracy and reliability. Delve into deep detail, providing comprehensive 
    information for the content writer to analyze and incorporate into their articles.""",
    backstory="""You are a cybersecurity expert tasked with staying at 
    the forefront of developments in the cybersecurity landscape. Your 
    responsibilities include monitoring for the latest vulnerabilities, 
    patches, data breaches, malware, emerging technologies and trends. You excel in gathering 
    intricate details and understanding their significance, enabling you 
    to provide valuable insights to the content writer for further analysis and synthesis.""",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)


# Define your agents with roles and goals
content_writer = Agent(
    role='Content Writer',
    goal="""Analyze and synthesize the gathered information from the 
    cybersecurity researcher, incorporating insights on cybersecurity, 
    vulnerabilities, patches, emerging AI, tech trends, and business 
    updates into a comprehensive news article format. Ensure that all 
    critical details, including specific stories, vulnerabilities, and 
    AI developments from the current week, are covered extensively. 
    Additionally, add lessons learned and actionable items based on 
    the research, providing technical solutions to mitigate identified 
    threats. The article should be at least a page long, maintaining 
    accuracy and clarity throughout.""",
    backstory="""You are an expert cybersecurity content writer 
    entrusted with transforming the insights provided by the 
    cybersecurity researcher into a coherent and informative news article. 
    Your task is to distill complex information into clear and understandable 
    content, ensuring that all critical details, including specific vulnerabilities, 
    AI news, emerging trends, data breaches, malware, and threat intelligence
    are covered comprehensively. Additionally, 
    incorporate direct lessons learned and actionable insights from the 
    research, offering readers valuable guidance on addressing cybersecurity 
    challenges. Your expertise lies in creating engaging and informative 
    content that educates and empowers readers with actionable knowledge.""",
    verbose=True,
    allow_delegation=False
)


# Create tasks for your agents
task1 = Task(description="""Research and gather this week's news on cybersecurity, 
             including hacks, new malware, threat intelligence, data breaches,
             vulnerabilities, patches, emerging AI, tech, 
             and cybersecurity trends, alongside notable business updates. 
             Delve into specific stories and developments within the realm 
             of artificial intelligence, providing insights into cutting-edge 
             advancements and noteworthy events from reputable sources. 
             Explore recent vulnerabilities disclosed this week, focusing 
             on their CVE identifiers, affected systems, and available patches. 
             Utilize platforms such as 'HackerNews.com' 
             and https://www.cisa.gov/known-exploited-vulnerabilities-catalog 
             for comprehensive updates. Offer detailed analyses of emerging 
             trends, technological breakthroughs, and potential implications 
             within the cybersecurity landscape.""", agent=researcher)

task2 = Task(description="""Write a comprehensive news article based on the 
             information gathered by the researcher, ensuring it 
             encompasses all aspects of cybersecurity, including 
             new malware, threat intelligence, data breaches, 
             vulnerabilities, patches, emerging AI, tech trends, 
             and significant business updates. Incorporate detailed 
             coverage of specific stories and developments within the 
             field of artificial intelligence, highlighting cutting-edge 
             advancements and notable events from the current week. 
             Include thorough analyses of recent vulnerabilities 
             disclosed, providing in-depth information such as 
             CVE identifiers, affected systems, and recommended patches. 
             Additionally, ensure the article offers actionable insights 
             and lessons learned, including technical solutions to mitigate 
             identified threats. Maintain a high level of detail and accuracy 
             throughout the content, covering all relevant information provided 
             by the researcher.""", agent=content_writer)


# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, content_writer],
    tasks=[task1, task2],
    verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

filepath = "/Users/stann/Documents/cybernews.txt"
print("######################")
with open(filepath, "w") as file:
    file.write(result)

# Print a message indicating that the result has been written to the file
print(result)
print("Result has been written to:", filepath)
