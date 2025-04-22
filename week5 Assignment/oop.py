class House:
  def __init__(self, address):
    self.address = address

  def house_info(self):
      print(f"This house is located at: {self.address}")

myhouse=House("12A JT St")
print(myhouse.house_info())

# inheritance
class Apartment(House):
  def __init__(self, address, floor):
    super().__init__(address)
    self.floor = floor

  def apartment_info(self):
    print(f"This apartment is located on the {self.floor} floor of the building at: {self.address}")

myapartment=Apartment("112A JT St", 'first floor')
print(myapartment.apartment_info())

# polymophysm



