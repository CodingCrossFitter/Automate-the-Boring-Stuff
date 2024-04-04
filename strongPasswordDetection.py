# Regular Expression to detect if a password is strong or weak
# A strong password contains:
### at least 8 characters
### both uppercase and lowercase characters
### at least one digit

import re, sys

## Write REGEX here
passwordRegex = re.compile(r'[a-zA-Z0-9]{8,}+\S?') # Matches inputs containing at least 8 characters, uppercase and lowercase letters, and digits
userInput = passwordRegex.search(input('Input new password: '))
print(userInput.group())
## Function to call
def checkPassword(passwordInput):
  strongOrWeak = passwordInput.group()
  # Check that the input contains only letters and digits
  if strongOrWeak.isalnum():
    print('This contains only letters and numbers')
  else:
    print('Passwords can only have letters and numbers. Please enter a valid password.')
    sys.exit()

 # Check for uppercase and lowercase
  upperCounter = 0
  lowerCounter = 0
  for i in strongOrWeak:
    if i.isupper():
      upperCounter += 1
    if i.islower():
      lowerCounter += 1
  if upperCounter > 0:
      if lowerCounter > 0:
        print('Strong your password is.')
  else:
    print('Weak your password is.')
    sys.exit()


checkPassword(userInput)