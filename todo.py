class task:
    def __init__(self):
        self.tasks = {}

    def view_tasks(self):
        self.tasks.clear()

        try:
            with open("tasks.txt", "r") as tasks_file:
                for line in tasks_file:
                    if "," in line:
                        name, status = line.strip().split(",", 1)
                        self.tasks[name.strip().title()] = status.strip() == "True"
        except FileNotFoundError:
            open("tasks.txt", "w").close()  # create file if not exists

        if self.tasks:
            print("Here are all your tasks:\n")
            for index, task_name in enumerate(self.tasks, start=1):
                symbol = "✔" if self.tasks[task_name] else "❌"
                print(f"{index}. {task_name}   {symbol}")

            while True:
                try:
                    mark = input("Would you like to mark some tasks as done(y/n) : ").strip().lower()
                    if mark == "y":
                        mark_tasks = input("What tasks would you like to mark(separate by comma): ")
                        mark_tasks_list = [task.strip().title() for task in mark_tasks.split(",")]
                        for task_name in mark_tasks_list:
                            if task_name in self.tasks:
                                if self.tasks[task_name]:
                                    print(f"'{task_name}' is already marked as done.")
                                else:
                                    self.tasks[task_name] = True
                                    print(f"'{task_name}' marked as done.")
                            else:
                                print(f"'{task_name}' not found in your to-do list.")
                        break
                    elif mark == "n":
                        break
                    else:
                        print("Invalid Choice! Please enter 'y' or 'n'")
                except ValueError:
                    print("Invalid choice! Please enter a letter")
        else:
            print("You have no tasks yet!")

        # Save updated status back to file
        with open("tasks.txt", "w") as tasks_file:
            for task_name, status in self.tasks.items():
                tasks_file.write(f"{task_name},{status}\n")

    def add_tasks(self):
        task_add = input("What tasks would you like to add (separate multiple tasks by comma): ")
        task_add_list = [task.strip().title() for task in task_add.strip().split(",")]

        try:
            with open("tasks.txt", "r") as tasks_file:
                existing_lines = tasks_file.readlines()
        except FileNotFoundError:
            existing_lines = []

        existing_tasks = [line.split(",")[0].strip().title() for line in existing_lines if "," in line]

        with open("tasks.txt", "a") as tasks_file:
            for task_name in task_add_list:
                if task_name in existing_tasks:
                    print(f"'{task_name}' has already been added.")
                else:
                    tasks_file.write(f"{task_name},False\n")

    def remove_tasks(self):
        task_remove = input("What tasks would you like to remove (separate multiple tasks by comma): ")
        task_remove_list = [task.strip().title() for task in task_remove.strip().split(",")]

        try:
            with open("tasks.txt", "r") as tasks_file:
                lines = tasks_file.readlines()
        except FileNotFoundError:
            lines = []

        existing_tasks = [line.split(",")[0].strip().title() for line in lines if "," in line]

        for task_name in task_remove_list:
            if task_name not in existing_tasks:
                print(f"'{task_name}' is not present in your to-do list.")

        with open("tasks.txt", "w") as tasks_file:
            for line in lines:
                task_name = line.split(",")[0].strip().title()
                if task_name not in task_remove_list:
                    tasks_file.write(line)
                else:
                    print(f"'{task_name}' has been removed from your to-do list.")


my_tasks = task()

def show_menu(again):
    if not again:
        print("Welcome to your to-do list:\n")
    print(
        "\t1. View tasks\n"
        "\t2. Add tasks\n"
        "\t3. Remove tasks\n"
        "\t4. Exit\n"
    )

again = False
while True:
    show_menu(again)
    try:
        choice = int(input("Make a Choice (1/2/3/4): "))
        if choice == 1:
            my_tasks.view_tasks()
        elif choice == 2:
            my_tasks.add_tasks()
        elif choice == 3:
            my_tasks.remove_tasks()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 4.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    again = True
