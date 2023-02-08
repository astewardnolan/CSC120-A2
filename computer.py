class Computer:
    # What attributes will it need?
    computer_num= 0
    description= ""
    processor_type=" " 
    hard_drive_capacity= 0.0
    memory= 0.0
    OS = ""
    year = 0
    price = 0.0
    item_id= ""
    def __init__(self, computer_num, description, processor_type, hard_drive_capacity, memory, OS, year,price):
        self.computer_num= computer_num
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.OS = OS
        self.year = year
        self.price = price
     

    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def comp_details(self, c, computer_num, description, processor_type, hard_drive_capacity, memory, OS, year,price): 
        c= ("Computer number", computer_num, "description", description, "processor type", processor_type, "hard drive capacity", hard_drive_capacity, "memory", memory, "operating system", OS, "year", year, "price", price)
        return c

    def update_price(self, new_price):
        self.price = new_price
        return new_price
    def update_os(self, new_os):
        self.OS= new_os
        return new_os
    #put this in shop and update all sorts of stuff j for fun, but the if else statement works
    # def refurbish(self, c, new_os):
    #     if c in self.inventory:
    #         c.OS= new_os
    #     else:
    #         print("This computer is not in out inventory")
  
           
           
           
            #if self.year< 2000:
             #   self.new_price = 0

            #elif self.year < 2012:
             #   self.OS= new_os
              #  self.price= 250
                
           # elif self.year < 2018:
            #    self.price= 550
            #else:
             #   self.price= 1000
                
              


def main(): 
    computer= Computer(1, "new","p", 7, 8, "mac", 2013, 50)
    #print(computer.refurbish((1, "new","p", 7, 8, "mac", 2013, 50), "mac wo", ))

main()



#need to refurbish comp :
   


        
       
    #pass # You'll remove this when you fill out your constructor

    # What methods will you need?