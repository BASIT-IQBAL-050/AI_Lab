

def task1(n1,n2):
    pr = n1*n2
    if(pr<=1000):
        print("Product is ")
        return pr
    else:
        print("Sum is ")
        return n1+n2

while True:
    n1 = int(input(("Enter 1st Num : ")))
    n2 = int(input(("Enter 2nd Num : ")))
    print(n1, " and ", n2 , " : ",task1(n1,n2))
    ch= input("Do you want to run again : (y/n)")

    if(ch !='Y' or ch !='y'):
        break
    

    