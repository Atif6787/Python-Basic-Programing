# Type of Character

while True:
  ch = input("Enter the Charator: ")

  if ch.lower() == 'stop':
    print("The loop is stop")
    print("_" *20)
    break

  if len(ch) != 1:
    print("Invalid input. Please enter a single character.")
    continue

  if ch.isalpha():
    print(f"{ch} is a Alphabet")
  elif ch.isdigit():
    print(f"{ch} is a Digit")
  else:
    print(f"{ch} is a Special character")
  print("_" *20)
  print(" ")
