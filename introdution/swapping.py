a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

#a=30 b=20

#a=20 b=30

temp=a  #temp=30 a=blank
a=b     #a=20 b=blank
b=temp  #b=30 temp=blank

# a=a+b  #30+20 = 50 = a  
# b=a-b  #50-20 = 30 =b
# a=a-b  #50-30 a=20 value got override

#a,b = b,a

print("after swapping value of A : ",a)
print("after swapping value of B : ",b)

