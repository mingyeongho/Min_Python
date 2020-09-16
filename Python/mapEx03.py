ex = [1,2,3,4,5]
print(list(map(lambda x: x**2 if x % 2 == 0 else x, ex)))

print([x**2 if x % 2 == 0 else x for x in ex])