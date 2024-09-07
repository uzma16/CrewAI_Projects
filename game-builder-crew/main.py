# from dotenv import load_dotenv
# load_dotenv()

# from crewai import Crew

# from tasks import GameTasks
# from agents import GameAgents

# tasks = GameTasks()
# agents = GameAgents()

# print("## Welcome to the Game Crew")
# print('-------------------------------')
# game = input("What is the game you would like to build? What will be the mechanics?\n")

# # Create Agents
# senior_engineer_agent = agents.senior_engineer_agent()
# qa_engineer_agent = agents.qa_engineer_agent()
# chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# # Create Tasks
# code_game = tasks.code_task(senior_engineer_agent, game)
# review_game = tasks.review_task(qa_engineer_agent, game)
# approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# # Create Crew responsible for Copy
# crew = Crew(
# 	agents=[
# 		senior_engineer_agent,
# 		qa_engineer_agent,
# 		chief_qa_engineer_agent
# 	],
# 	tasks=[
# 		code_game,
# 		review_game,
# 		approve_game
# 	],
# 	verbose=True
# )

# game = crew.kickoff()


# # Print results
# print("\n\n########################")
# print("## Here is the result")
# print("########################\n")
# print("final code for the game:")
# print(game)


from dotenv import load_dotenv
from crewai import Crew, Agent

from tasks import GameTasks
from agents import GameAgents

# Load environment variables
load_dotenv()

# Define a function to gather structured feedback from the user
def gather_structured_feedback():
    print("Please rate the following aspects of the output on a scale from 1 to 5:")
    feedback = {
        'code_quality': int(input("Code Quality: ")),
        'task_completion': int(input("Task Completion: ")),
        'agent_performance': int(input("Agent Performance: "))
    }
    return feedback

# Define a function to adjust an agent based on structured feedback
def adjust_agent_based_on_feedback(agent, feedback):
    # Example: Adjusting the role and goal of an agent based on feedback
    if feedback['code_quality'] < 3:
        agent.role = 'Senior Software Engineer with a focus on code quality'
        agent.goal = 'Create high-quality software and improve code quality'
    # we can add more conditions based on different types of feedback
    return agent

# Initialize your agents and tasks
tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
game = input("What is the game you would like to build? What will be the mechanics?\n")

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

# Iterate through each task, generate output, collect feedback, and adjust agents
for task in crew.tasks:
    # Generate output for the current task
    game = crew.kickoff()
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("final code for the game:")
    print(game)
    
    # Skip feedback collection on the first iteration
    if task == crew.tasks[0]:
        continue
    
    # Gather structured feedback
    feedback = gather_structured_feedback()
    
    # Adjust agents based on feedback
    senior_engineer_agent = adjust_agent_based_on_feedback(senior_engineer_agent, feedback)
    qa_engineer_agent = adjust_agent_based_on_feedback(qa_engineer_agent, feedback)
    chief_qa_engineer_agent = adjust_agent_based_on_feedback(chief_qa_engineer_agent, feedback)
    
    # Optionally, add a condition to break the loop if the user decides to stop
    continue_feedback = input("Would you like to provide more feedback? (yes/no): ")
    if continue_feedback.lower() != 'yes':
        break

# from dotenv import load_dotenv
# from crewai import Crew, Agent

# from tasks import GameTasks
# from agents import GameAgents

# # Load environment variables
# load_dotenv()

# # Define a function to gather structured feedback from the user
# def gather_structured_feedback():
#     print("Please rate the following aspects of the output on a scale from 1 to 5:")
#     feedback = {
#         'code_quality': int(input("Code Quality: ")),
#         'task_completion': int(input("Task Completion: ")),
#         'agent_performance': int(input("Agent Performance: "))
#     }
#     return feedback

# # Define a function to adjust an agent based on structured feedback
# def adjust_agent_based_on_feedback(agent, feedback):
#     # Example: Adjusting the role and goal of an agent based on feedback
#     if feedback['code_quality'] < 3:
#         agent.role = 'Senior Software Engineer with a focus on code quality'
#         agent.goal = 'Create high-quality software and improve code quality'
#     # Add more conditions based on different types of feedback
#     return agent

# # Initialize your agents and tasks
# tasks = GameTasks()
# agents = GameAgents()

# print("## Welcome to the Game Crew")
# print('-------------------------------')
# game = input("What is the game you would like to build? What will be the mechanics?\n")

# # Create Agents
# senior_engineer_agent = agents.senior_engineer_agent()
# qa_engineer_agent = agents.qa_engineer_agent()
# chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# # Create Tasks
# code_game = tasks.code_task(senior_engineer_agent, game)
# review_game = tasks.review_task(qa_engineer_agent, game)
# approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# # Create Crew responsible for Copy
# crew = Crew(
#     agents=[
#         senior_engineer_agent,
#         qa_engineer_agent,
#         chief_qa_engineer_agent
#     ],
#     tasks=[
#         code_game,
#         review_game,
#         approve_game
#     ],
#     verbose=True
# )

# # Iterate through each task, generate output, collect feedback, and adjust agents
# for task in crew.tasks:
#     # Generate output for the current task
#     game = crew.kickoff()
#     print("\n\n########################")
#     print("## Here is the result")
#     print("########################\n")
#     print("final code for the game:")
#     print(game)
    
#     # Gather structured feedback
#     feedback = gather_structured_feedback()
    
#     # Adjust agents based on feedback
#     senior_engineer_agent = adjust_agent_based_on_feedback(senior_engineer_agent, feedback)
#     qa_engineer_agent = adjust_agent_based_on_feedback(qa_engineer_agent, feedback)
#     chief_qa_engineer_agent = adjust_agent_based_on_feedback(chief_qa_engineer_agent, feedback)
    
#     # Optionally, add a condition to break the loop if the user decides to stop
#     continue_feedback = input("Would you like to provide more feedback? (yes/no): ")
#     if continue_feedback.lower() != 'yes':
#         break

