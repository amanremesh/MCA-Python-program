numbers = list(map(int, input("Enter numbers: ").split()))
result = [x for x in numbers if x % 2 != 0]
print(result)
