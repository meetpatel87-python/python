l = []
n = int(input("enter the lengh of list : "))

for i in range(1,n+1):
    n1 =int(input("enter value : "))
    l.append(n1) 

print(l)
l1 = []
l2 = []

for i in l:
    if i not in l1:
        l1.append(i)

    else:
        l2.append(i)


print("uniqe number : ",l1)
print("duplicate number : ",l2)  