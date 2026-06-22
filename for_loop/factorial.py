# factorial of a number
while True:
  n = int(input("Enter the number: "))
  if n == 00:
    print('The loop is stop')
    break
  result = 1
  for i in range(n, 0, -1):
    result *= i
  print(result)