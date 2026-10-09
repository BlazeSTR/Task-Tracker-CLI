import sys
from tasks import todo
if len(sys.argv) < 2:
    print("help")
else:
    command = sys.argv[1]
    todo(command)
