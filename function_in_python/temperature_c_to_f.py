# Temperature through function

while True:
  c = float(input("Enter the temperature in celcius: "))
  if c == 00:
    print("The loop is stopped..")
    break
  def temp():
    f = c*9/5 +32
    return c*9/5+32

  print(temp())