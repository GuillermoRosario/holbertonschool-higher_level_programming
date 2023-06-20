#!/usr/bin/python3
from Motor import Motorcycle
from Motor import drive
from Motor import stop

def drive(self):
    print("vrumm")

def stop(self):
    print("Stop!")

bike_1 = Motorcycle("Honda", "Shadow", 1999, "Red")

print(bike_1.make)
print(bike_1.model)
print(bike_1.year)
print(bike_1.color)

bike_2 = Motorcycle("Honda", "CRF", 2023, "Red")

print(bike_2.make)
print(bike_2.model)
print(bike_2.year)
print(bike_2.color)

bike_1.drive()
bike_2.drive()

