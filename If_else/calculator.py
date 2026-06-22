from re import sub
# calculator

while True:
  a = int(input("Enter the first number: "))
  if a == 0:
    print("The loop is stoped")
    break
  operator = input("Enter the Operator: ")
  b = int(input("Enter the second number: "))


  if operator == "+":
    print(f"{a} + {b} = {a + b}")
  elif operator == "-":
    print(f"{a} - {b} = {a - b}")
  elif operator == "*":
    print(f"{a} * {b} = {a * b}")
  elif operator == "/":
    print(f"{a} / {b} = {a / b}")
  else:
    print("Invaild Operator")