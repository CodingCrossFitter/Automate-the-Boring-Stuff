tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
  # initialize the list "colWidths" with zeroes equal to the length of the input list
  colWidths = [0] * len(tableData)
  
  # iterate over the input list to find the longest word in each inner list
  # if it is larger than the current value, set it as the new value
  for i in range(len(tableData)):
    for j in range(len(tableData[i])):
      if len(tableData[i][j]) > colWidths[i]:
        colWidths[i] = len(tableData[i][j])
  
  print(colWidths)
  # assuming each inner list is the same length as the first, iterate over the input list
  # printing the x value from each inner list, right justified to its corresponding value in colWidths
  for x in range(len(tableData[0])):
    for y in range(len(tableData)):
      print(tableData[y][x].rjust(colWidths[y]), end=' ')
    print('')


printTable(tableData)