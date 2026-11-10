list1 = input("Enter color-list1: ").split()
list2 = input("Enter color-list2: ").split()
result = [x for x in list1 if x not in list2]
print(result)
