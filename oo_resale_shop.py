from computer import*
class ResaleShop:
    
    inventory = [] #list to hold computer details
   
    def __init__(self ):
        self.inventory = []
       
            
    def inventory_buy(self, c:Computer):# adds computer to inventory when bought
        self.inventory.append(c)
       
    
    def inventory_sell(self, c:Computer): #removes sold computer from inventory
        if c in self.inventory:
            self.inventory.remove(c)
        else:
            print("No computer found in inventory")
        


    def refurbish(self, c:Computer, new_os): # will update price based on computer year, and update computer's OS to new_os given.
        if c in self.inventory:
            if c.year < 2000:
                c.price = 0 # too old to sell, donation only
            elif c.year < 2012:
                c.price = 250 # heavily-discounted price on machines 10+ years old
            elif c.year < 2018:
                c.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                c.price = 1000 # recent stuff

            if new_os is not None:
                c.OS = new_os # update details after installing new OS
        else:
            print("Item", c.computer_name, "not found. Please select another item to refurbish.")



    def print_inventory(self): #Will print out detials for all computers in inventory
    # If the inventory is not empty
        if self.inventory != []:
        # For each item
            for i in self.inventory:
            # Print its details
                i.print_details()
                print("                           ")
        else:
            print("No inventory to display.")
    

def main():
    comp1= Computer("ashby", "h", "b", 3,3, "mac", 2000, 50)
    comp2= Computer("kat", "l", "b", 3,3, "dell", 2010, 50)
    comp3= Computer("kait", "l", "b", 3,3, "dell", 2010, 50)
    myShop= ResaleShop()
    myShop.inventory_buy(comp1)
    myShop.inventory_buy(comp2)
    myShop.refurbish(comp3, "mac 500")
    myShop.print_inventory()
    myShop.inventory_sell(comp1)
    myShop.print_inventory()
    
main()
            
            
            


