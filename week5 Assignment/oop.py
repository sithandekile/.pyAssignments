class House:
    def __init__(self, address):
        self.__address = address  # private attribute

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def house_info(self):
        print(f"This house is located at: {self.__address}")

myhouse = House("12A JT St")
myhouse.house_info()
print("Old address:", myhouse.get_address())
myhouse.set_address("15B JT St")
print("New address:", myhouse.get_address())

# inheritance
class Apartment(House):
    def __init__(self, address, floor):
        super().__init__(address)
        self.__floor = floor  # private attribute

    def get_floor(self):
        return self.__floor

    def set_floor(self, floor):
        self.__floor = floor

    def apartment_info(self):
        print(f"This apartment is located on the {self.__floor} floor of the building at: {self.get_address()}")

myapartment = Apartment("112A JT St", 'first floor')
myapartment.apartment_info()
print("Old floor:", myapartment.get_floor())
myapartment.set_floor("second floor")
print("New floor:", myapartment.get_floor())
myapartment.apartment_info()

#activity 2
class Employee:
    def work(self):
        print("Employee is working.")

class Teacher(Employee):
    def work(self):
        print("Teaching students.")

class Chef(Employee):
    def work(self):
        print("Cooking food.")

class Driver(Employee):
    def work(self):
        print("Driving a vehicle.")

# Demonstrate polymorphism
employees = [Teacher(), Chef(), Driver()]

for employee in employees:
    employee.work()