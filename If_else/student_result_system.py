# Student result system

while True:
  sub_1 = int(input("Enter your Maths paper marks: "))
  if sub_1 == 0:
    print("The loop is stoped")
    break

  sub_2 = int(input("Enter your Physics paper marks: "))
  sub_3 = int(input("Enter your Chemistry paper marks: "))
  sub_4 = int(input("Enter your Biology paper marks: "))
  sub_5 = int(input("Enter your English paper marks: "))


  total_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
  calculate_Persentage = (total_marks/500) * 100



  if sub_1 < 33 or sub_2 < 33 or sub_3 < 33 or sub_4 < 33 or sub_5 < 33:
    print("The student has Fail")

  if total_marks > 200:
    print("The student has Pass")
    print(f"Total marks: {total_marks}")
    print(f"Persentage: {calculate_Persentage}")
  else:
    print("The student has Fail")


  if total_marks > 200 and total_marks <= 250:
    print('The student has D grade')

  elif total_marks > 250 and total_marks <= 300:
    print("The students has C grade")

  elif total_marks > 300 and total_marks <= 350:
    print('The student has B grade')

  elif total_marks >350 and total_marks <=400:
    print("The student has A grade")

  elif total_marks > 400 and total_marks <= 500:
    print('The student has A+ grade')

  else:
    print("The sudent has No grade")


  print('--' * 20)