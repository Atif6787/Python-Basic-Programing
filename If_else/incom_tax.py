# Icom tax


while True:
  incom = int(input("Enter your incom: "))
  if incom == 0:
    print("The loop is stoped")
    break
  elif incom <= 50000:
    print("Don't pay tax")

  elif incom <= 100000:
    print(f"Pay {(incom - 50000) * 0.10} Tax")

  elif incom > 100000:
    print(f"Pay {(incom - 50000) * 0.20} Tax")
  else:
    print("Invaild incom")