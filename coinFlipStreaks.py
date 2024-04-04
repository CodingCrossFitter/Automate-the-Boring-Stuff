### COIN FLIP STREAKS ###
import random
numberOfStreaks = 0
streak = 0
counter = 0
headsOrTails = []
for experimentNumber in range(10000):
  # Code that creates a list of 100 'heads' or 'tails' values

  while counter <= 100:
    randomNumber = random.randint(0,1)
    if randomNumber == 0:
      headsOrTails.append('H')
    else: headsOrTails.append('T')
    counter += 1

  # Code that checks if there is a streak of 6 heads or tails in a row.
  for i in range(len(headsOrTails)):
    if i == 0:
      pass
    elif headsOrTails[i] == headsOrTails[i-1]:
      streak += 1
    else:
      streak = 0
    
    if streak == 6:
      numberOfStreaks += 1
  headsOrTails = []
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))