ex = [1,2,3,4,5]
f = lambda x,y : x + y
print(list(map(f,ex,ex)))

print([x+y for x,y in zip(ex,ex)])