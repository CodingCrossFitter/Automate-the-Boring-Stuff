### COMMA CODE ###
spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(useListVariable):
  newPrintOfList = ''
  for item in useListVariable:
    if item == useListVariable[-1]:
      newPrintOfList += f'and {item}'
      break
    newPrintOfList += f'{item}, '
  return newPrintOfList

print(commaCode(spam))