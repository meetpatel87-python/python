
def palindrome(s): #with parameter
    rev = s[::-1]

    if s==rev:
        print("palindrome!!")

    else:
        print("not palindrome!!")


s = input("ENTER NAME :")

palindrome(s)