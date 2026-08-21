def show_menu():
    print("Student Task Tracker")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task(tasks):
  task = input("Enter task name: ")
  tasks.append(task)

def view_tasks(tasks):
  print("Tasks:")
  for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
  if not tasks:
    print("No tasks found.")


def delete_task(tasks):
  if not tasks:
    print("No tasks found.")
    return

  for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
  try:
    delete = int(input("Which number you want to delete: "))
  except ValueError:
    print("Please enter a valid number.")
    return

  if 1 <= delete <= len(tasks):
    removed_task = tasks.pop(delete - 1)
    print(f"Deleted: {removed_task}")
  else:
    print("Invalid task number.")
  
tasks=[]
while True:
  show_menu()
  choice = input("Choose an option: ")

  if choice == "1":
      add_task(tasks)

  elif choice == "2":
    view_tasks(tasks)
  elif choice == "3":
    delete_task(tasks)
  elif choice == "4":
    break
  else:
    print("Invalid choice. Please choose a valid option.")