

while True:
    print("         press 1 prime number : ")
    print("         press 2 tringle : ")
    print("         press 3 factorial : ")
    print("         press 4 exit : ")


    choice = int(input("you choice number 1,2,3&4: "))

    if choice == 1:
        n = int(input("enter number  : "))

        if n<0:
            print("enter positive number!!")

        else:  

            if n==1 or n==2 or n==3:
                print(n,"is prime!!")

            else:
                 prime = 0
            for i in range(1,n+1):

                    if (n%i==0):
                        prime+=1

            if prime==2:
                    print(n,"is prime number!!")

            else:
                    print(n,"not a prime number!!")
          

    elif choice == 2:
        for i in range(1,6,1):
            print(" "*(6-i),"* "*i)

        for i in range(4,0,-1):
            print(" "*(6-i),"* "*i)




    elif choice == 3:
        n = int(input("enter number : "))
 
        sum=0
        for i in range(0,n+1):
    
            sum = sum + i
      
     
        print(sum)

    elif choice == 4:
        print("thank you!!")
        break

    else:
        print("invalid choice!!")
        break    

