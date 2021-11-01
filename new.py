import os
from datetime import datetime

now = datetime.now()

if __name__ == "__main__":
    readme = "/README.md"
    current_time = now.strftime("%H:%M:%S")
    name = "hi.txt"
    with open(name, 'w') as f:
        f.write(current_time)
