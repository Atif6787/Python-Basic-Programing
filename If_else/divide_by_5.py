# Divisible by 5

while True:
  a = int(input("Enter the number: "))
  if a == 1:
    print("The loop is stoped")
    break

  if a % 5 == 0:
    print("The number is divisible by 5")

  else:
    print("The number is not divisible by 5")