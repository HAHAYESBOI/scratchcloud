#v1.0.0
import scratchclient as scratch
import time
import requests


repo = requests.get("https://raw.githubusercontent.com/thegamebegins25/scratchcloud/main/update.py")
file = open("update.py", "r")

if file.read()[:7] != repo.text[:7]:
    file.close()
    print("Update available. Updating now...")
    file2 = open("update.py", "w")
    lines = repo.text.split("\n")
    for i in range(0, len(lines)):
        lines[i] = lines[i] + "\n"
    file2.writelines(lines)
    time.sleep(3)
    file2.close()
    print("Update complete.")


repo = requests.get("https://raw.githubusercontent.com/thegamebegins25/scratchcloud/main/main.py")
print(repo)

module = __import__(__name__)
file = open(module.__file__, "r")
if file.read()[:7] != repo.text[:7]:
    print("Update available. Updating now...")
    import update
    time.sleep(3)
    print("Update complete. The program will now stop for the updates to process.")
    quit()


print("Project Id?")
id = input()
print("Name of variable?")
var = input()
print("Value?")
val = input()

session = scratch.ScratchSession("username", "password")


connection = session.create_cloud_connection(id)
time.sleep(3)

connection.set_cloud_variable(var, val)
valN = connection.get_cloud_variable(var)
if valN == val:
  print("Success")
else:
  print("Failed. Make sure you put in the correct variable (case sensitive)")
