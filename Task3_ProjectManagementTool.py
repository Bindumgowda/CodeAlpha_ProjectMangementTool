# Task 3: Project Management Tool - Bindu

projects = {}

def create_project(name):
    projects[name] = []
    print(f"Project '{name}' created!")

def add_task(project_name, task, person):
    projects[project_name].append({"task": task, "person": person})
    print(f"Task added: {task}")

def show_tasks(project_name):
    print(f"\n--- {project_name} BOARD ---")
    for i, t in enumerate(projects[project_name]):
        print(f"{i+1}. {t['task']} - Assigned to: {t['person']}")

# Testing
create_project("CodeAlpha Internship")
add_task("CodeAlpha Internship", "Task1: AI in Healthcare", "Bindu")
add_task("CodeAlpha Internship", "Task2: MEA Algorithm", "Bindu")
add_task("CodeAlpha Internship", "Task3: Project Tool", "Bindu")
show_tasks("CodeAlpha Internship")