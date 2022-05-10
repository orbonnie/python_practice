
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
  print(char)

# Write a while loop that does the same thing!
count = 0
while count < len(word):
  print(word[count])
  count += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
count = 100

while count < 141:
  print(count)
  count += 2



# Write a for loop that does the same thing (with range())
nums = range(100, 141, 2)

for even in nums:
  print(even)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
pwd = input('Please enter the passphrase "sillygoose" ')

while pwd != 'sillygoose':
  pwd = input('Please enter the passphrase "sillygoose" ')

print('Thank you!!')