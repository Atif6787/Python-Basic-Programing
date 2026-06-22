# Create a function that returns the square of a number.

while True:
  n = int(input("Enter the number: "))
  if n == 0:
    break

  def squre():
    return n*n

  print(squre())