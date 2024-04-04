### CHARACTER PICTURE GRID ###
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print('\n'.join(map(''.join, zip(*grid))))
rows = len(grid) # Number of elements in the list
cols = len(grid[0]) # Number of elements in every single element in the list

for j in range(cols):
  for i in range(rows):
    print(grid[i][j], end='')
  print()