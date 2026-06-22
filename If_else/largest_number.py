# Largest of Two Numbers

while True:
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))


  if a > b:
    print(f"{a} is greater than {b}")

  elif a == 0:
    print("The loop is stoped")
    break

  else:
    print(f"{b} is greater than {a}")