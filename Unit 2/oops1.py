class Car:
    def __init__(self,make,model,year,reading):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Reading = reading
    def start(self):
        print(f"{self.Make} {self.Model} has started.")
    def stop(self):
        print(f"{self.Make} {self.Model} has stopped.")
    def reading(self):
        print(f"{self.Make} {self.Model} has {self.Reading} kms on it")
    def update_reading(self,kms):
        self.Reading = kms
    def drive(self):
        print(f"{self.Make} {self.Model} is a fossil fuel car.")

class ElectricCar(Car):
    def __init__(self, make, model, year,reading):
        super().__init__(make, model, year,reading)
        self.battery = "120"
    def des_battery(self):
        print(f"The Car {self.Model} has a {self.battery} kwh battery.")
    def drive(self):
        print(f"{self.Make} {self.Model} is an electric fuel car.")
        
car1 = Car("Maruti","800","2000","0")
car2 = Car("Toyata","Innova","2010","0")

# print(car1.Make)
# print(car1.Model)
# print(car1.Year)
# print(car1.__dict__)
# print(car2.__dict__)
# car1.start()
# car2.start()
# car1.stop()
# car2.stop()
# Initial Reading
# car1.reading()
# car2.reading()
# print("\n")
# # Updated Reading
# car1.update_reading("20")
# car1.reading()
# car2.update_reading("200")
# car2.reading()

# Inheritence
e1 = ElectricCar("Tesla","Cybertruck","2023","0")
e1.start()
e1.des_battery()

car1.drive()
e1.drive()

