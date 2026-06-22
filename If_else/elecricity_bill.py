#Electricity Bill

while True:
  units = float(input("How many units are you used?: "))
  if units == 0:
    print("You have not used electricty, so your bill is zero")
    break

  bill = 0

  if units > 0 and units <= 100:
    bill = units * 5
    print(f"Your bill is {bill}")

  elif units > 100 and units <=200:
    bill = units * 10
    print(f"Your bill is {bill}")

  elif units > 200:
    bill = units * 15
    print(f"Your bill is {bill}")

  else:
    print("check error in your meter")

  print("-" *25)