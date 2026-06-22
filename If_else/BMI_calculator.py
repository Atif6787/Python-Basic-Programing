# BMI Calculator

# Input weight and height.
# Calculate BMI and classify:
# Underweight
# Normal
# Overweight
# Obese

while True:
  a = float(input("Enter the Weight: "))
  if a == 0:
    print("The loop is stoped")
    break
  b = float(input("Enter the Height: "))

  if a < 50 and b < 145:
    print("You are underweight")
    print("-" * 20)
  elif (a >= 50 and a <= 60) and (b >= 145 and b <= 155):
    print("Your body is normal")
    print("-" * 20)
  elif (a >= 60 and a <= 70) and (b >= 155 and b <= 165):
    print("You are overweight")
    print("-" * 20)
  else:
    print("You are obese")
    print("-" * 20)