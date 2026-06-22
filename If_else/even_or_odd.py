# Even or Odd

while True:
  a = int(input("Enter the number: "))

  if a % 2 == 0:
    print(f"The number {a} is even")

  elif a == 1:
    print("The loop is stop")
    break

  else:
    print(f"The number {a} is odd")