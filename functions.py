# def calculate_fencing_cost(length,breadth,cost_per_ft):
#     circumference = 2 * (length + breadth)
#     cost_for_fencing = circumference * cost_per_ft
#     return cost_for_fencing

# cost_for_fencing_land = calculate_fencing_cost(100,70,17)
# print(cost_for_fencing_land)

def cost_land(land_length,land_breadth,home_length,home_breadth,garden_length,garden_breadth,cost_per_ft):
    land_area = land_length * land_breadth
    home_area = home_length * home_breadth
    garden_area = garden_length * garden_breadth
    cost_of_garden_area = (land_area - home_area - garden_area) * cost_per_ft
    return cost_of_garden_area

result = cost_land(100,100,80,60,100,20,10) # type: ignore
print(result)