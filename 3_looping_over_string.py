# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.

word = input("Type in your word: ")
for letter in word:
    print(letter)

# Challenge:
# Count how many vowels are in the word.

vowels = "aeiouAEIOU"
count = 0
word1 = input("Type in your word: ")
for letter in range(len(word1)):
    if letter in vowels:
        count+=1
    else:
        continue
print(count)
