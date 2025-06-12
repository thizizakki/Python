from loguru import logger

#creating an empty sets
#set_var = set()

set_var = {1,2,7,8,4,12}
# print(set_var)

# for number in set_var:
#     print(number)

new_set_var = {2,4,6,5,15}

# print("Union ",set_var.union(new_set_var))

# print("Intersection ",set_var.intersection(new_set_var))

# print("Disjoint ",set_var.isdisjoint(new_set_var))

set_var.add(45)
print(set_var)
set_var.remove(12)
print(set_var)