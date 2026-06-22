from typing_extensions import final
# Discount system

while True:
  shopping_amount = float(input("Please enter your shopping amount: "))
  if shopping_amount < 2000:
    print("Sorry, This offer is not for you")
    break

  Discount = 0
  final = 0

  if shopping_amount >= 2000 and shopping_amount < 5000:
    Discount = shopping_amount * 0.10
    final = shopping_amount - Discount
    print("-"* 20)

  elif shopping_amount >= 5000:
    Discount = shopping_amount * 0.20
    final = shopping_amount - Discount
    print("-"* 20)

  else:
    print('error')

  print(f"Orignal Bill: {bill}")
  print(f"Discount: {Discount}")
  print(f"Final Bill: {final}")