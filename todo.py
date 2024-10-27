def task():
    tasks = []
    print("-- WELCOME TO TODO APP--")

    totalTask = int(input("How many tasks do you want to add: "))
    for i in range(1, totalTask+1):
        taskName = input(f"Enter your task {i}: ")
        tasks.append(taskName)

    print(f"Toady's tasks are:\n{tasks}")

    while True:
        operation = int(input("Please enter the operation you want to perform:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"{add} has been added successfully")

        elif operation == 2:
            updated = input("Enter the task you want to update: ")
            if updated in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated)
                tasks[ind] = up
                print(f"Updated task is: {up}")

        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Deleted task is: {del_val}")

        elif operation == 4:
            print(f"Tasks are: {tasks}")        

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input")


task()