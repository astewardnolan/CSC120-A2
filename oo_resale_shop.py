from computer import*
class ResaleShop:
    
    inventory: list
    OS : str
    # What attributes will it need?


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self ):
        self.inventory= []
        #self.OS= OS

        #pass # You'll remove this when you fill out your constructor
    
    #def itemID(self, Computer): #counts num of computers in inventory
       # for item in self.inventory:
          #  self.item_ID += 1
   # pass 
    
            
    def inventory_buy(self, c:Computer):
        self.inventory.append(c)
       
    
    def inventory_sell(self, c:Computer):
        if c in self.inventory:
            self.inventory.pop(c)
        else:
            print("No computer found in inventory")
        

    def refurbish(self, c:Computer, new_os):
        if c in self.inventory:
            c.OS= new_os
        else:
            print("This computer is not in out inventory")


    def print_inventory(self, c):
    # If the inventory is not empty
        if self.inventory != []:
            print("abc")
        
        # For each item
            for c in self.inventory:
            # Print its details
                print(self.inventory)
        else:
            print("No inventory to display.")
    

    def main():
        c=Computer(1, "mac pro", "h", 4,4,"mac", 2000, 5)
        myShop= ResaleShop(3, "he", "he", 3, 4, "mac", 2000, 50 ) #question, how do i call a specific computer to this part of code!?!?!?!
        myShop.print_inventory(c)
        #c=Computer("mac pro", etc)
        #myShop.buy(c)
        #like how much info do i need to transfer over???
    main()
            
            
            


    # What methods will you need?