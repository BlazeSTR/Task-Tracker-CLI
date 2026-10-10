import sys
import json
import datetime as dt

data = {
    "next_id": 2,
    "tasks": [
        {"id":1,"name": "bread", "status": "todo", "created_at": "04:47 PM","updated_at":None}
    ]
}



def todo(command):
    match command:
    
        case "add":
            if len(sys.argv) < 3:
                print("you need another argument for add")
            else: 
                task_name = str(sys.argv[2])
                next_id = data["next_id"]
                data["tasks"].append(dict(id=next_id,name=task_name,status="todo",created_at=dt.datetime.now().strftime('%I:%M %p'),updated_at=None))
                print(f"Task added successfully (ID: {data['next_id']})")
                data["next_id"] += 1
                

        case "list":
            if len(sys.argv) < 3:
                if data["tasks"]:
                    for task in data["tasks"]:
                        updated = "Never" if task["updated_at"] is None else task["updated_at"]
                        print(f"ID: {task["id"]}, Name: {task["name"]}, Status: {task["status"]}, Created at: {task["created_at"]}, Updated at: {updated}")
                else:
                    print("No task to list.")
            else:
                list_arg = sys.argv[2]
                if list_arg in ("done", "todo", "in-progress"):
                    for task in data["tasks"]:
                        if task["status"] == list_arg:
                            updated = "Never" if task["updated_at"] is None else task["updated_at"]
                            print(f"ID: {task['id']}, Name: {task['name']}, Status: {task['status']}, Created at: {task['created_at']}, Updated at: {updated}")    
    
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

