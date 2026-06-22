# Largest of Three Numbers

while True:
  a = int(input("Enter the first number: "))
  if a == 0:
    print("The loop is stoped")
    break

  b = int(input("Enter the second number: "))
  c = int(input("Enter the third number: "))

  if a > b and a > c:
    print(f"{a} is greater than {b} and {c}")

  elif b > a and b > c:
    print(f"{b} is greater than {a} and {c}")

  else:
    print(f"{c} is greater than {a} and {b}")