tasks = []

def show_menu():
    print('\n TODO LIST')
    print('1. Add Tasks')
    print('2. View Tasks')
    print('3. Remove Tasks')
    print('4. Exit')
        
def add_task():
    task = input("Enter your task")
    tasks.append(task)
    print(f"Task '{task}' added")

def view_task():
    if not tasks:
        print("No task yet")
    else:
        print("\nYour Tasks are:")
        for i,task in enumerate(tasks,1):
            print(f"{i}. {task}")

def remove_task():
    view_task()
    try:
        task_num = int(input("Enter the number to remove from the task"))-1
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task}' removed")
    except (IndexError, ValueError):
        print("Invalid")
    

while True:
    show_menu()
    choice = input('Enter your choice:')
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("GoodBYE")
        break
    else:
        print("Invalid Value")
    
