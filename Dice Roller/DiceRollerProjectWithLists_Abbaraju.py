from random import *

amountofRolls = int(raw_input("Enter how many dice to roll: ")) #user input for the amount of dice to roll
diceRolls = [] #empty array that will store the dice roll values
  
def firstAndLastRow(amountofRolls): #prints the rows of the top and bottom of dice based on the amount of dice
  print ""
  for x in range(0, amountofRolls):
    print "-------",

def secondRow(amountofRolls):
  print ""
  for x in range(0, len(diceRolls)): #goes through the array of dice roll values and prints the second line 
  									 #(first row of the dice faces) based on dice value in the array
    if diceRolls[x] == 1:
      print "|     |",
    elif diceRolls[x] == 2:
      print "|  o  |",
    elif diceRolls[x] == 3:
      print "|  o  |",
    elif diceRolls[x] == 4:
      print "| o o |",
    elif diceRolls[x] == 5:
      print "| o o |",
    elif diceRolls[x] == 6:
      print "| o o |",
      
def thirdRow(amountofRolls, score):
  print ""
  for x in range(0, len(diceRolls)):#goes through the array of dice roll values and prints the third line 
  									#(second row of the dice faces) based on each dice value in the array
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
  print ""
  for x in range(0, len(diceRolls)):#goes through the array of dice roll values and prints the fourth line 
  									#(third row of the dice faces) based on each dice value in the array
    if diceRolls[x] == 1:
      print "|     |",
    elif diceRolls[x] == 2:
      print "|  o  |",
    elif diceRolls[x] == 3:
      print "|  o  |",
    elif diceRolls[x] == 4:
      print "| o o |",
    elif diceRolls[x] == 5:
      print "| o o |",
    elif diceRolls[x] == 6:
      print "| o o |",
      
      
      


def diceRoller(amountofRolls, diceRolls): #this is the main method that includes the method calls for
										  #the other methods that print the dice line by line
  newRoll = 0#stores the randomly generated dice value
  score = 0
  for x in range(0, amountofRolls):#repeats this process of adding a random value into a variable, adding
  								   # that value to the score, and adding that value into the array also
								   #"amountofRolls" times
    newRoll = randint(1, 6)#random int generated between 1 and 6, then stored in variable newRoll
    score = score + newRoll#the newRoll value is added to the array 
    diceRolls.append(newRoll)#the value is added to the array
    
  firstAndLastRow(amountofRolls)
  secondRow(diceRolls)
  thirdRow(diceRolls, score)
  fourthRow(diceRolls)
  firstAndLastRow(amountofRolls)#printing methods are called      
  
    
diceRoller(amountofRolls, diceRolls)#passes the raw input variable and the empty array 
									#declared earlier through the parameter


