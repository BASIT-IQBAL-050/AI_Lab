
class Resturant:
    def __init__(self):
        self.menu={}
        
    def addItems(self,item, price, rating):
        self.menu[item] = {'price': price, 'rating': rating}
        print(f"{item} added with price : {price} and rating : {rating}")
        
    def removeItem(self, item):
        if item in self.menu:
            print(f" the self.menu[item] is : ", self.menu[item])
            del self.menu[item]
            print(f"{item} Removed from the menu")
        else:
            print(f"{item} Not in the menu")
            
    def averageRating(self):
        sumRating = 0
        length = 0
        for itm in self.menu.values():
            sumRating += itm['rating']
            length+=1
        print("Resturant : ", self.menu)   
        print("Average of Rating is : ",sumRating/length)
        
        
        
#adding two in advance for just testing and all that stuff....
rest = Resturant()
rest.addItems("Sushi", 100, 5)
rest.addItems("Mango", 101, 4)


# now dynamically taking input from the user so that user can chose what action he wants to perfom
while True:
    print("Select the Option to perform the action: ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Average Rating ")
    ch = int(input("Enter Your Choice : "))
    
    match ch:
        case 1:
            nameOfItem = input("Enter the Name of Item : ")
            price = int(input(f"Enter the price of {nameOfItem} : "))
            rating = int(input(f"plz Rate {nameOfItem} : "))
            
            rest.addItems(nameOfItem, price, rating)
        case 2:
            nameOfItem = input("Enter the Name of Item You want to remove : ")
            rest.removeItem(nameOfItem)
        
        case 3:
            rest.averageRating()
            
        case _:
            print("invalid Input")
            
    choice = input("Would You like to exit (y) : ")
    if(choice in ['y', 'Y']):
        break
            

        