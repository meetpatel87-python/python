
od = 0
ev = 0
sumod = 0
sumev = 0
sum = 0


for i in range(1,6):
    
    n=int(input(f"enter number {i} : "))
    if n%2==0:
        print("even number",n)
        ev+=1
        sumev+=n

    else:
        print("odd number",n)
        od+=1
        sumod+=n

    
    sum+=n
    

print("total even number : ",ev)
print("total odd number : ",od)
print("total sum even number : ",sumev)
print("total sum odd number : ",sumod)
print("total sum number : ",sum)

