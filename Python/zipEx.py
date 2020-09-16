alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a,b in zip(alist, blist) :
    print(a,b)

a,b,c = zip((1,2,3),(4,5,6),(7,8,9))
print(a,b,c)

print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])