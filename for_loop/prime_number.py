# Prime number
while True:
  num = int(input('Enter the number: '))
  if num == 00:
    print('The loop is stop')
    break

  if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5 + 1)):
      if num % 2 == 0:
        is_prime = False
        break
    if is_prime:
      print(f"{num} is a prime number")
    else:
      print(f"{num} is not a prime number")
  else:
    print(f"{num} is not a prime number")