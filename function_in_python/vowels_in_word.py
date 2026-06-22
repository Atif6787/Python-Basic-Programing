
# Create a function that counts the vowels in a string.
word = input("Enter the word: ")

def vowels():
  vowels = "aeiouAEIOU"
  count = 0
  for char in word:
    if char in vowels:
      count += 1
  return count
  count= word

vowels()
