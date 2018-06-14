import re
import subprocess


def is_running(process):
    s = subprocess.Popen(["ps", "-faux"], stdout=subprocess.PIPE)

    for x in s.stdout:
        if re.search(process, x):
            print("Process " + str(process) + " Is running")

        elif not re.search:
            print(str(process) + " not running")


is_running(b"code")
