print("LOOPS : ")

# print("\n While Loop")
# c=True
# while(c):
#     n1 = int(input("Enter num 1 : "))
#     n2= int (input("Enter 2nd num : "))
#     print("Sum : ", n1+n2,"\n")
#     choice = input("Would you like to run again (y/n) : ")
#     if(choice=='N' or choice == 'n'):
#         c=False
#         print("Thank You for using 'The BEST CAl in world ' ")
#     elif(choice !='y' and choice!='Y' and choice!='n' and choice !='N'):
#         print("You have entered a wrong choice .... ")
    

print("\n For Loop")
print("Table of a number")
n= int(input("Enter the number of the table you want : "))
r = int(input("Enter the range upto which you want the table : "))
for i in range(r):
    print(n, " x " , i+1 , " = " , n* (i+1))