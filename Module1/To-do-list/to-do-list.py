#to-do list lesson
print("Let's get our life togeather, \nEnter some tasks so we can keep track on a nice to-do list:")

task_list = ["Give Chris an A+ 🤣"]

def add_task():
    task = input("Please enter a task to add to the to-do list: ")
    task_list.append(task)
    print(f"Task '{task}' added. ")

def remove_task():
    task = input("Enter the task you would like to remove from the to-do list: ")
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed from the to-do list. ")
    else:
        print(f"Task '{task}' not found in the to-do list. ")

def show_menu():
    print("\nMenu:")
    print("1. Add a task to the to-do list. ")
    print("2. Remove a task from the to-do list")
    print("3. View the to-do list, and the task you currently have. ")
    print("4. Quit")

def task_input():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            print("\nYour task list: ")
            if task_list:
                for idx, task in enumerate(task_list, start=1):
                    #idx to make the list look better,start=1 to make 123 vs 012
                    print(f"{idx}. {task} ")
            else:
                print("You have no tasks currently in your to-do list. ")
        elif choice == '4':
            print("Thanks for using this to-do list app. ")
            break
        else:
            print("\nInvalid choice, please try again. ")

task_input()
