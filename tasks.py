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
                    task_name = str(sys.argv[2])
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
                    list_arg = sys.argv[2]
                    if list_arg in ("done", "todo", "in-progress"):
                        for task in data["tasks"]:
                            if task["status"] == list_arg:
                                print_task(task)
                    else:
                        print("Allowed arguments for list: done, todo, in-progress")
            case "update":
                pass
        
            case "delete":
                if len(sys.argv) < 3:
                    print("you need another argument for delete")
                else:
                    try:
                        task_id = int(sys.argv[2])
                        print(f"Delete task id {task_id}")
                    except ValueError: print("Expected integer as an argument for delete..")
            

            case _:
                print(f"command {command} is not included")

