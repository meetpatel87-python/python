l = []
n = int(input("enter the lengh of list : "))

for i in range(1,n+1):
    n1 =int(input("enter value : "))
    l.append(n1) 

print(l)
l1 = len(l)
l.sort

for i in range(0,l1):        # 0 index 
    for j in range(i+1,l1):   # 1 index
        if (l[i]>l[j]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            
for i in range(0,l1):     
    print("asc order : ",l[i])