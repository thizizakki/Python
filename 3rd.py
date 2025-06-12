length_of_land = 100
bricks_cost_per_Piece = 10.5
labor_mistri1 = "Jagmohan"
labor_mistri2 = "Rampyare"
is_home = True

# print("Length of the land is",length_of_land)
# print("Labour name is",labor_mistri1)

# print("my home is of 4 BHK Length of the total land is 100")

#For new line we have to use \n
# print("my home is of 4 BHK \nLength of the total land is 100"

# print('''My home is of 4 BHK 
# Length of the total land is 100''')

# print(length_of_land,bricks_cost_per_Piece,labor_mistri1,is_home)

#print(type(length_of_land),type(bricks_cost_per_Piece),type(labor_mistri1),type(is_home))

# f string, .format method

# print(f"cost of bricks per unit is  {bricks_cost_per_Piece}")

# print("Cost of bricks per unit is {} {} {}".format(bricks_cost_per_Piece,length_of_land,labor_mistri2))

#logging
import logging
from loguru import logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

logging.info(f"cost of bricks per unit is {bricks_cost_per_Piece}")

logger.info(f"cost of bricks per unit is {bricks_cost_per_Piece}")