line=(input("enter a line =>"))
words=line.split()
for word in set(words):
 	print(word,"=",words.count(word))
