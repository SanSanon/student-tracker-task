tasks = []
while True:
    print("Student Task Tracker")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
    elif choice == "2":
        print("Tasks:")
        for task in tasks:
            print(task)
    if choice == "3":
      break
    