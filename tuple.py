l = (1,2,"hello",3,"welcome",200,True,1)


print(l.count(1))

print(l.index(200))

l1 = list(l)
print(l1)
l1.append(100)

t1 = tuple(l1)
print(t1)