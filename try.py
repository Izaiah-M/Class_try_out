import datetime
import threading

class Task:
  def __init__(self, name, date, time):
    self.name = name
    self.date = date
    self.time = time

class Scheduler:
  def __init__(self):
    self.tasks = {}

  def add_task(self, name, date, time):
    # Check if the day already exists in the tasks dictionary
    if date not in self.tasks:
      self.tasks[date] = []

    # Create a new task and add it to the list for the specified day
    task = Task(name, date, time)
    self.tasks[date].append(task)

    # Start the alert thread for the task
    self.start_alert_thread(task)

  def remove_task(self, name, date):
    # Check if the day exists in the tasks dictionary
    if date not in self.tasks:
      return

    # Find the task with the specified name and remove it
    for i, task in enumerate(self.tasks[date]):
      if task.name == name:
        del self.tasks[date][i]

  def start_alert_thread(self, task):
    thread = threading.Timer((task.date - datetime.datetime.now()).total_seconds(), self.alert, [task])
    thread.start()

  def alert(self, task):
    print(f"{task.name} is starting now!")

  def get_tasks_for_month(self, month):
    tasks = []
    for date, dayTasks in self.tasks.items():
      if date.month == month:
        tasks.extend(dayTasks)
    return tasks

  def get_tasks_for_day(self, date):
    if date not in self.tasks:
      return []
    return self.tasks[date]

  def search_tasks(self, query):
    query = query.lower()
    results = []
    for date, dayTasks in self.tasks.items():
      for task in dayTasks:
        if query in task.name.lower():
          results.append(task)
    return results

# Create a new scheduler
scheduler = Scheduler()

# Add some tasks
scheduler.add_task("Meeting with John", datetime.datetime(2022, 12, 10, 10, 30), None)
scheduler.add_task("Grocery shopping", datetime.datetime(2022, 12, 11), None)
scheduler.add_task("Dentist appointment", datetime.datetime(2022, 12, 12, 14, 30), None)

# Remove a task
scheduler.remove_task("Meeting with John", datetime.datetime(2022, 12, 10))

# Get all tasks for the current month
tasks = scheduler.get_tasks_for_month(datetime.datetime.now().month)
