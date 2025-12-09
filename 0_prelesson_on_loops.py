# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc

# counts down from 10 until it reaches to 1, then prints Happy New Year
for x in range(1, 11):
    print(x)
print("HAPPY NEW YEAR")

# counts up from 1 until 20, skips when reaches 13, or else prints number
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
