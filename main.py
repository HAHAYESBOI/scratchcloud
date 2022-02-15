#v1.0.0
import scratchclient as scratch
import time
from google.colab import output

#If you are not comfortable entering your username and password, make an alt account with the same email and different password (I get it)
print("Username? (Case sensitive)")
name = input()
print("Password?")
pword = input()
print("Project Id?")
id = input()
print("Name of variable?")
var = input()
print("Value?")
val = input()

session = scratch.ScratchSession(name, pword)


connection = session.create_cloud_connection(id)
time.sleep(3)

connection.set_cloud_variable(var, val)
time.sleep(3)
valN = connection.get_cloud_variable(var)
if valN == val:
  print("Success")
else:
  print("Failed. Make sure you put in the correct variable (case sensitive)")
output.clear()
print("Input cleared for privacy.")
