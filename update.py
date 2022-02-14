#v1.0.0
import requests



repo = requests.get("https://raw.githubusercontent.com/thegamebegins25/scratchcloud/main/main.py")



file = open("main.py", "r")
if file.read() != repo.text:
    print("Hack is not updated. Updating file.")
    file2 = open("main.py", "w")
    lines = repo.text.splitlines(True)
    file2.writelines(lines)
    file2.close()
    print("Hack updated. Please reload your python interpreter.")
file.close()
