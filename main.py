#v1.0.0
import scratchclient as scratch
import time


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

run = True

while run == True:
  connection.set_cloud_variable(var, val)

  valN = connection.get_cloud_variable(var)

  if valN == val:
    print("Success")
  else:
    print("Failed. Make sure you put in the correct variable (case sensitive)")
  print("Run again? (y/n)")
  run = input()
  if run.lower() == "y":
    run = True
  else:
    run = False
print("Input cleared for privacy.")