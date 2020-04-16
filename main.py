from __future__ import division
from datetime import datetime
import random
import math
import os

# We create a folder to a relative path.
# This folder has the name of the date of the day
dirname = os.path.dirname(__file__)
folder = datetime.date(datetime.now())
dateFolder = 'pastTeams/' + folder.strftime("%Y-%m-%d")
filename = os.path.join(dirname, dateFolder)
if not os.path.exists(filename):
  os.makedirs(filename)

# Input ask
nbPeoplePerTeam = int(input("How many people in each team do you want? "))

# For each line we get the name of the people and put them into an array
line = []
with open('list.txt') as my_file:
  for row in my_file:
    line.append(row.rstrip('\n'))

nbTeams = int(math.ceil(len(line) / nbPeoplePerTeam))
print "You have", len(line), "people in your company and you want", nbPeoplePerTeam, "people per team. You will have", nbTeams, "teams.\n",

# For each team we get random people
teams = []
while len(line) > 0 and nbTeams > 0:
  team = random.sample(line, int(len(line) / nbTeams))

  for x in team:
    line.remove(x)

  nbTeams -= 1
  teams.append(team)

i = 0
globalFileName = filename + "/global.txt"
globalFile = open(globalFileName, "w+")

for people in teams:
  i += 1
  fileName = filename + "/" + str(i) + ".txt"
  globalFile.write("TEAM " + str(i) + "\n\n ")

  f = open(fileName,"w+")
  for person in people:
    f.write(person + "\n")
    globalFile.write(person + "\n")

  globalFile.write("\n---------\n")
  globalFile.write("\n")
