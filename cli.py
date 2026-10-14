import sys
import json
from pathlib import Path
from tasks import todo

path = Path("data.json")
if path.exists():
    pass
else:
    path.write_text(json.dumps({"next_id": 2,"tasks": [
        {"id":1,"name": "bread", "status": "todo", "created_at": "04:47 PM","updated_at":None}
    ]}, indent=2))

if len(sys.argv) < 2:
    print("help")
else:
    command = sys.argv[1]
    todo(command)
