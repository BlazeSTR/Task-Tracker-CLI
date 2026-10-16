import sys
import json
import datetime as dt


def print_task(task):
    updated = "Never" if task["updated_at"] is None else task["updated_at"]
    print(f"ID: {task['id']}, Name: {task['name']}, Status: {task['status']}, "
          f"Created at: {task['created_at']}, Updated at: {updated}")

def todo(command):

    with open("data.json", "r+") as file:
        data = json.load(file)

        match command:
        
            case "add":
                if len(sys.argv) < 3:
                    print("you need another argument for add")
                else: 
                    task_name = sys.argv[2]
                    next_id = data["next_id"]
                    data["tasks"].append({
                        "id":next_id,
                        "name":task_name,
                        "status":"todo",
                        "created_at":dt.datetime.now().strftime('%I:%M %p, %Y-%m-%d'),
                        "updated_at":None
                        }
                    )
                    print(f"Task added successfully (ID: {data['next_id']})")
                    data["next_id"] += 1
                    
                    file.seek(0)
                    json.dump(data, file, indent=2)
                    file.truncate()
                    
            case "list":
                if len(sys.argv) < 3:
                    if data["tasks"]:
                        for task in data["tasks"]:
                            print_task(task)
                    else:
                        print("No task to list.")
                else:
                    list_arg = sys.argv[2].lower()
                    if list_arg in ("done", "todo", "in-progress"):
                        filtered_tasks = [task for task in data["tasks"] if task.get('status') == list_arg]
                        if filtered_tasks:
                            for task in filtered_tasks:
                                print_task(task)
                        else:
                            print(f"No {list_arg} tasks are available")
                            
                    else:
                        print("Allowed arguments for list: done, todo, in-progress")
            
            case "update":
                if data["tasks"]:
                    print("Which one do you want to update?")
                    for task in data["tasks"]:
                        print_task(task)
                    try:
                        task_id = int(input("Enter ID: "))
                        filtered_task = [task for task in data["tasks"] if task.get('id') == task_id]
                        if filtered_task:
                            status_change = input("What status do you want to change it to? (done,todo,in-progress)\n")
                            if status_change.lower() not in ("done", "todo", "in-progress"):
                                print("Only (done, todo, in-progress) allowed! ")
                            else:
                                task = filtered_task[0]
                                task["status"] = status_change.lower()
                                task["updated_at"] = dt.datetime.now().strftime('%I:%M %p, %Y-%m-%d')
                                print(f"Task (ID: {task_id}) updated successfully!")
                                file.seek(0)
                                json.dump(data, file, indent=2)
                                file.truncate()
                        else:
                            print("No task has that ID")
                    except ValueError: print("Only numbers allowed!")
                else:
                    print("There are no tasks to update..")
                

        
            case "delete":
                if len(sys.argv) < 3:
                    print("you need another argument for delete")
                else:
                    try:
                        task_id = int(sys.argv[2])
                        data["tasks"] = [task for task in data["tasks"] if task.get('id') != task_id]
                        file.seek(0)
                        json.dump(data, file, indent=2)
                        file.truncate()
                    except ValueError: print("Expected integer as an argument for delete..")
            

            case _:
                print(f"command {command} is not included")

