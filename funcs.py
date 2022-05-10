def is_even(num):
  return num % 2 == 0

def sluggify(string):
  return string.strip().lower().replace(' ', '-')

def count_vowels(string):
  vowels = ['a', 'e', 'i', 'o', 'u']
  count = 0
  string = string.lower()

  for char in string:
    if char in vowels:
      count += 1
  return count

print(is_even(4))
print(sluggify('   hello world I am reaDY  '))
print(count_vowels('I love you too'))