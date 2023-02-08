class Computer:
    # What attributes will it need?
    computer_name= ""
    description= ""
    processor_type=" " 
    hard_drive_capacity= 0.0
    memory= 0.0
    OS = ""
    year = 0
    price = 0.0
    item_id= ""
    def __init__(self, computer_name, description, processor_type, hard_drive_capacity, memory, OS, year,price):
        self.computer_name= computer_name
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.OS = OS
        self.year = year
        self.price = price
     
    def print_details(self): #will print detials of computer
        print("Computer name; ", self.computer_name) 
        print("description; ", self.description) 
        print("processor type; ", self.processor_type) 
        print("hard drive capacity; ", self.hard_drive_capacity) 
        print("memory; ", self.memory) 
        print("operating system; ", self.OS) 
        print("year; ", self.year) 
        print("price; ", self.price, "$")
        

    def update_price(self, new_price):#will update the price of computer
        self.price = new_price
        
    def update_os(self, new_os):#will update operating system of the computer
        self.OS= new_os
            

def main(): 
    computer= Computer(1, "new","p", 7, 8, "mac", 2013, 50)

main()


