try:
    l1 = [8,12,78,32,21]

    n = int(input("enter index :"))

    print("value of index is :",l1[n])

except ValueError as e:
    print(e)

except IndexError as e:
    print(e)

# try:
#     l1 = [8,12,78,32,21]

#     n = int(input("enter index : "))

#     print("value of index is : ",l1[n])

# except:
#     print("invalid input!!")

