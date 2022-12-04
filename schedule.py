import csv
class CreateTask:
    def __init__(self,taskNo,  category, description, deadline, isComplete = False):
        self.category = category
        self.description = description
        self.deadline = deadline
        self.taskNo = taskNo
        self.isComplete = isComplete
    
    def __repr__(self):
        return str(self.taskNo) + " " + self.description 

with open('tasks.csv', 'r') as file:
    reader = csv.DictReader(file)

    task_list = []

    for row in reader:
        taskNo = row['TaskNo.'].strip()
        category = row['Category'].strip()
        description = row['Description'].strip()
        deadline = row['Deadline'].strip()

        task_list.append(CreateTask(taskNo, category, description, str(deadline)))

# print(task_list)
personal = []
school = []

for task in task_list:
    if task.category == "Personal":
        personal.append(task)
    if task.category == "School":
        school.append(task)

def personal_tasks():
    for task in personal:
        print(task)

def school_tasks():
    for task in school:
        print(task)

def all_tasks():
    for tasks in task_list:
        print(tasks)

def pending_task():
    for tasks in task_list:
        if tasks.isComplete == False:
            print(tasks)


