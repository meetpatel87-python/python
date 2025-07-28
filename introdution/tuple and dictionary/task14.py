

while True:
    menu = """

        press 1 for square
        press 2 for merge dictonary
        press 3 for merge list
        press 4 for exit
        
        """
    
    print(menu)

    choice = int(input("enter choice : "))

    if choice==1 :
         
        n= int(input("enter number : "))
        d ={}
        for i in range(1,n+1):
              d[i]=i*i 
        print(n)     
         
        

    elif choice==2:
        d1 = {'p':1100, 'q':300, 'r':600}
        d2 = {'p':400, 'q':200, 'r':1200, 'm':1923}
        d3 = {}
        for i,j in d1.items():
            for k,l in d2.items():
                if i==k:
                    d3[i]=j+l

        print(d3)

        
    elif choice==3:
        l = [16,62,24]
        l1 = [32,89,62]

        ans = {}

        for i in range(len(l)):
            ans[l[i]] = l1[i]
    

        print(ans)
    elif choice==4:
         print("thank you!!")
         break
    else:
        print("invalid choice!!")
        break