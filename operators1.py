from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = 'Jagmohan'
labour_mistri2 = 'Rampyare'

# calculate the total area of the land
total_area_Of_land = length_of_land * breadth_of_land

perimeter_of_land = 2 * (length_of_land + breadth_of_land)

#Modulo operator
result = 15 % 6
result1 = math.ceil(15 // 7)

result2 = math.floor(15 / 7)
logger.info(f"Total area of my land is {total_area_Of_land}")
logger.info(f"Perimeter of land is {perimeter_of_land}")
logger.info(f"Result of the modulo {result}")
logger.info(f"Result of the floor division {result1}")
logger.info(f"Result of division {result2}")


#concatenation
a="aks"
b="hay"
logger.info(f"Name is concated and it is {a+b}")

c="25"
d=5
logger.info(f"Concatenated {c + str(d)}")

e=1.5
f=7
logger.info(f"sum is {e+f}")
logger.info(f"sum without decimal point is {int(e)+f}")

land_length = float(input("Please enter the length of the land: "))
land_breadth = input("Please enter the breadth of the land: ")


total_area = int(land_length * float(land_breadth))

logger.info(f"Total area of your land is {abs(total_area)} sq ft")