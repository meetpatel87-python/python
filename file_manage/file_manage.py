# file = open("test_1.txt","w")
# file.write("hello write method!!")
# file.close()


# file = open("test_1.txt","a")
# file.write("\nthis method is append!!")
# file.close()

# file = open("test_1.txt","r")
# print(file.read())
# file.close()

# l = []

# for i in range(1,31):
#     l.append(i)
#     print(  i  )

# file = open("test_2.txt","w")
# file.write(str(l))
# file.close()

# n = int(input("enter number : "))
# with open("demofile.txt","a") as f:
#     for i in range(1,n+1):
#         f.write(str(i))


# d ={}
# #with open("demofile_2.txt","a") as f:
# for i in range(1,5):
#     d[i]=i*i 
# #        f.write(str(d))
    
# file = open("demofile_2.txt.txt","w")
# file.write(str(d))
# file.close()


# file = open("test_3.txt","w+")
# file.write("w+ method!!")
# print(file.tell()) #cersur where position
# file.seek(0)   #use by position change 
# print(file.read())
# file.close()



# with open('test_3.txt', 'r+') as file:
#     content = file.read()
#     print(content)
#     file.write('Appending new content')


with open('test_3.txt', 'a+') as file:
    file.write('Appended text\n')
    file.seek(0)  # Move the pointer to the beginning
    content = file.read()
    print(content)