d = {'a': 3, 'b': 1, 'c': 2}
ascending = dict(sorted(d.items()))
descending = dict(sorted(d.items(), reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)
