#ATM Withdarw

while True:
  balance = float(input("Enter the balance: "))
  if balance == 0:
    print("Your bank account is empty")
    break

  amount = float(input("Enter the amount that you want to withdraw: "))

  if amount <= balance:
    balance -= amount
    print(f"withdraw successful: {balance}")
  else:
    print("You have insufficient balance")

  print("-" * 25)
