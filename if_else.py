from loguru import logger

length_of_land = int(input("Enter the length of your land: "))
if(length_of_land < 100):
    logger.info(f"Your land is not sufficient to build 4 BHK")
    logger.info("Second Line")
    if length_of_land > 80:
        logger.info("You can build 3 BHK")
    else:
        logger.info("Your land is not having enough space")
elif(length_of_land > 500):
    logger.info(f"You can build more than 2 buildings")
else:
    logger.info(f"Share more details with us!")


# How will you findout the given number is even or odd

# if length_of_land % 2 == 0:
#     logger.info("It is an even number")
# else:
#     logger.info("It is odd number")