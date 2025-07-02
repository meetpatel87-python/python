i = 1
od = 0
ev = 0
sumod = 0
sumev = 0
sum = 0


while(i>=5):
    n=int(input(f"enter number {i} : ",i))
    if n%2==0:
        print("even number",n)
        ev+=i
        sumev+=n

    else:
        print("odd number",n)
        od+=i
        sumod+=n

    
    sum+=n
    i=i+1

print("total even number : ",ev)
print("total odd number : ",od)
print("total sum even number : ",sumev)
print("total sum odd number : ",sumod)
print("total sum number : ",sum)

