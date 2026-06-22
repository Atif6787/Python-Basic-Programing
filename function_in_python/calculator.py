# calcultor
while True:
  def add(a, b):
    return a+b

  def sub(a, b):
    return a-b

  def mul(a, b):
    return a*b

  def div(a, b):
    if b == 0:
      return "Error: Division by zero"
    return a/b


  # Get input from the User
  print("==== Simple Calculator ====")

  a = float(input("Enter the first number: "))
  if a == 00:
    print("The program execution is stop")
    break

  op = input("Enter the operator (+, -, *, /): ")
  b = float(input("Enter the second number: "))

  print(f"You entered: {a} {op} {b}")


  # Route to the Right Function
  if op == "+":
    result = add(a, b)
  elif op == "-":
    result = sub(a, b)
  elif op == "*":
    result = mul(a, b)
  elif op == "/":
    result = div(a, b)
  else:
    result = "Unknown Operator"
  print(f"Result : {result}")
  print()
