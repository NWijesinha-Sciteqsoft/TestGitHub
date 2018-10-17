'''
Created on Oct 17, 2018

@author: nwijesinha
'''
# Create cars variable and assign 100 
cars = 100
# Create space_in_a_car variable and assign 4
space_in_a_car = 4.0
# Create car_drivers variable and assign 30
car_drivers = 30
# Create car+passenger variable and assign 90
car_passengers = 90
# Create variable cars_not_drive and assign the value from deducting car_drivers from cars
cars_not_driven = cars - car_drivers
# Create variable cars_driven and assign number of car_drivers
cars_driven = car_drivers
# Create carpool_capacity and calculate the carpool capacity by multiplying cars driven by space in a car
carpool_capacity = cars_driven * space_in_a_car
# Create variable average_passengers_per_car and calculate average passengers per car by dividing car passengers by cars driven
average_passaengers_per_car = car_passengers / cars_driven

# Print the available cars
print("There are", cars, "cars available.")
# Print the cars available
print("There are only", car_drivers, "drivers available.")
# Print the cars not driven
print("There will be", cars_not_driven, "empty cars today.")
# print the car pool capacity
print("We can transport", carpool_capacity, "people today.")
# Print the car pool for today
print("We have", car_passengers, "to carpool today.")
# Print the average passengers per car for today
print("We need to put about", average_passaengers_per_car, "in each car")


