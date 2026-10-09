import sys
import json

tasks: list[dict] = [{'id':1}, {'id':3}]


def todo(command):
    match command:
    
        case "--add":
            if len(sys.argv) < 3:
                print("you need another argument for add")
            else:
                try: 
                    task_name = str(sys.argv[2])
                    # tasks[0]["id"] = 1
                    next_id = max([num["id"] for num in tasks],default=0) + 1
                    tasks.append(dict(id=next_id, name=task_name))
                    print(tasks)
                except ValueError: print("Expected a string")

    
        case "--update":
            pass
    
        case "--delete":
            if len(sys.argv) < 3:
                print("you need another argument for delete")
            else:
                try:
                    task_id = int(sys.argv[2])
                    print(f"Delete task id {task_id}")
                except ValueError: print("Expected integer as an argument for delete..")
        
        case "--list":
            pass

        case _:
            print(f"command {command} is not included")

