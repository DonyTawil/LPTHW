# cars is equal to 100
cars = 100
#space... is equal to 4
space_in_car = 4
#drivers is defined as 30
drivers = 30
#passengers as 90
passengers = 90
#cars... is defined as 100-30
cars_not_driven = cars - drivers
#cars...=drivers =30
cars_driven = drivers
#carpool... is the operation 30*4
carpool_capacity = cars_driven * space_in_car
#average...=90/30
average_passengers_per_car = passengers/cars_driven


print ("there are", cars, "cars available.")
print ('there are', drivers,'drivers available.')
print ('there will be', cars_not_driven,'empty cars today.')
print ("we can transport", carpool_capacity,"people today.")
print ("we have", passengers, "to carpool today.")
print ("we need to put about", average_passengers_per_car,"in each car.")
