

def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return number // 2
  else:
    result = 3 * number + 1
    print(result)
    return result
  
user_input = input("Enter a number: ")
while user_input != 1:
    user_input = collatz(int(user_input))


# collatz(42)
# collatz(27)
# collatz(37)
# collatz(40)

