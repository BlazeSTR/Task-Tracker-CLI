import sys
import json
from pathlib import Path
from tasks import todo

path = Path("data.json")
if path.exists():
    pass
else:
    path.write_text(json.dumps({"next_id": 1,"tasks": []}, indent=2))

if len(sys.argv) < 2:
    print("help")
else:
    command = sys.argv[1]
    todo(command)
