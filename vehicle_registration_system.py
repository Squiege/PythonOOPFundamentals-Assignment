# Task 1
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
    
    def print_vehicle_information(self):
        print(f"Registration number: {self.registration_number}, Type: {self.type}, Owner: {self.owner}")

car1 = Vehicle(123, "Sedan", "Harry")
car2 = Vehicle(234, "SUV", "Josie")
car3 = Vehicle(432, "Van", "Bob")

new_owner1 = input("Please enter the name of the new owner for car 1: ")
car1.update_owner(new_owner1)
car1.print_vehicle_information()

new_owner2 = input("Please enter the name of the new owner for car 2: ")
car2.update_owner(new_owner2)
car2.print_vehicle_information()

new_owner3 = input("Please enter the name of the new owner for car 3: ")
car3.update_owner(new_owner3)
car3.print_vehicle_information()

