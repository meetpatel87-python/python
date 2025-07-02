

while True:
    print("         press 1 tringle : ")
    print("         press 2 prime number  : ")
    print("         press 3 factorial : ")
    print("         press 4 prime number : ")
    print("         press 5 exit : ")


    choice = int(input("you choice number 1, 2, 3, 4&5: "))

    if choice == 1:
        def signup():

          for i in range(1,6):
            print("*"*i)
        signup()          

    elif choice == 2:
        def prime(n):   #parameters
          prime=0
          for i in range(1,n+1):
             if n%i==0:
               prime+=1

          if prime==2:
            print("prime!!")

          else:
            print("not prime!!")

        n = int(input("enter number : "))
        prime(n)



    elif choice == 3:
        def fun3():

         n =int(input("enter number : "))
         fac=1

         for i in range(1,n+1):
           fac*=i

         return fac
        
        print(fun3())

    elif choice == 4:
        def prime(n):   #parameters
         prime=0
         for i in range(1,n+1):
           if n%i==0:
            prime+=1

         if prime==2:
           print("prime!!")

         else:
          print("not prime!!")
         return prime

        n = int(input("enter number : "))

        prime(n) #argument
        print(n)   

    elif choice == 5:
        print("thank you!!")
        break

    else:
        print("invalid choice!!")
        break    

