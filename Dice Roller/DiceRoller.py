from random import *

amountofRolls = int(raw_input("Enter how many dice to roll: "))
diceRolls = []
  
def firstAndLastRow(amountofRolls):
  print "\r"
  for x in range(0, amountofRolls):
    print "-------",

def secondRow(amountofRolls):
  print "\r"
  for x in range(0, len(diceRolls)):
    if diceRolls[x] == 1:
      print "|     |",
    elif diceRolls[x] == 2:
      print "|o    |",
    elif diceRolls[x] == 3:
      print "|o    |",
    elif diceRolls[x] == 4:
      print "| o o |",
    elif diceRolls[x] == 5:
      print "| o o |",
    elif diceRolls[x] == 6:
      print "| o o |",
      
def thirdRow(amountofRolls, score):
  print "\r"
  for x in range(0, len(diceRolls)):
    if diceRolls[x] == 1:
      print "|  o  |",
    elif diceRolls[x] == 2:
      print "|     |",
    elif diceRolls[x] == 3:
      print "|  o  |",
    elif diceRolls[x] == 4:
      print "|     |",
    elif diceRolls[x] == 5:
      print "|  o  |",
    elif diceRolls[x] == 6:
      print "| o o |",
  
  print "You rolled a", score,
  
def fourthRow(diceRolls):
  print "\r"
  for x in range(0, len(diceRolls)):
    if diceRolls[x] == 1:
      print "|     |",
    elif diceRolls[x] == 2:
      print "|    o|",
    elif diceRolls[x] == 3:
      print "|    o|",
    elif diceRolls[x] == 4:
      print "| o o |",
    elif diceRolls[x] == 5:
      print "| o o |",
    elif diceRolls[x] == 6:
      print "| o o |",
      
      
      


def diceRoller(amountofRolls, diceRolls):
  newRoll = 0
  score = 0
  for x in range(0, amountofRolls):
    newRoll = randint(1, 6)
    score = score + newRoll
    diceRolls.append(newRoll)
    
  firstAndLastRow(amountofRolls)
  secondRow(diceRolls)
  thirdRow(diceRolls, score)
  fourthRow(diceRolls)
  firstAndLastRow(amountofRolls)      
  
    
diceRoller(amountofRolls, diceRolls)


