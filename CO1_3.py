#generate positive list of numbers from a given list of numbers
numbers = [-2,-1,0,1,2,3,-3,-4,4]
positive = [n for n in numbers if n > 0]
print(positive)

#square of n numbers
square = [n**2 for n in numbers]
print(square)

#form a list of vovels from a given word
word = "hello world"
vowels = [char for char in word.lower() if char in "aeiou"]
print(vowels)

# ordinal value of each element in a word
ordinal_values = [ord(char) for char in word]
print(ordinal_values)



