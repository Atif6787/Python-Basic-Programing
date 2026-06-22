# separate even and odd

a = [1, 3, 4, 3, 5, 5, 6, 6, 7, 8, 9, 10]

even = []
odd = []

for i in a:
  if i % 2 ==0:
    even.append(i)
  else:
    odd.append(i)

print(f"The even numbers are {even}")
print(f"The odd numbers are {odd}")
