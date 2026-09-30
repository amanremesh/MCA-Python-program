numbers=input("enter list of numbers =>").split()
result =[]
for number in numbers:
        number=int(number)
        if number>100:
                result.append("OVER")
        else:
                result.append(number)
print(result)
