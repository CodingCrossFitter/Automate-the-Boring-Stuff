## Program to ask users their sandwich preferences

import pyinputplus as pyip

# Overarching Sandwich Function
def makeTheSandwich():
  sandwichOptions = []
  sandwichPrice = 0
  # Step 1 -- use inputMenu() for a bread type
  # wheat, white, or sourdough
  # print('Please select a bread option: ')
  bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
  sandwichOptions.append(bread)
  if bread == 'wheat':
    sandwichPrice += 1
  if bread == 'white':
    sandwichPrice += 0
  if bread == 'sourdough':
    sandwichPrice += 2

  # Step 2 -- use inputMenu() for protein type
  # chicken, turkey, ham, or tofu
  # print('Please select a protein option: ')
  protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
  sandwichOptions.append(protein)
  if (protein == 'chicken') or (protein == 'turkey') or (protein == 'ham'):
    sandwichPrice += 3
  if protein == 'tofu':
    sandwichPrice += 5

  # Step 3 -- use inputYesNo() to ask if they want cheese
  ## If YES, use inputMenu() to ask cheese type
  ### cheddar, Swiss, or mozzarella
  print('Would you like cheese?')
  cheese = pyip.inputYesNo()
  if cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    sandwichOptions.append(cheese)
    if cheese == 'cheddar':
      sandwichPrice += 1
    if cheese == 'Swiss':
      sandwichPrice += 2
    if cheese == 'mozzarella':
      sandwichPrice += 3
  else:
    sandwichOptions.append('no cheese')
  
  # Step 4 -- use inputYesNo() to ask if they want mayo,
  # mustard, lettuce, or tomato
  print('Would you like mayo, mustard, lettuce, or tomato?')
  condiments = pyip.inputYesNo()
  if (condiments == 'yes') or (condiments == 'Yes') or (condiments == 'y') or (condiments == 'Y'):
    sandwichOptions.append(['mayo', 'mustard', 'lettuce', 'tomato'])
  else:
      sandwichOptions.append(', and no condiments')
  
  # Step 5 -- use inputInt() to ask how many sandwiches they want
  ## this number should be 1 or more -- use min=1
  print('How many sandwiches would you like?')
  totalSandwiches = pyip.inputInt(min=1)

  # Step 6 -- display the sandwich choices AND total price
  sandwichPrice *= totalSandwiches
  print(f'Your sandwiches will consist of {sandwichOptions}.')
  print(f'Your total today is ${sandwichPrice}.')

makeTheSandwich()