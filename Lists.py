from loguru import logger

# labour_name = ["Mahesh","Ramesh","Mithilesh","Manish"]
# logger.info(f"Elements of a list{labour_name}")
# logger.info(f"First element in the list is {labour_name[0]}")

# # List Methods

# labour_name.append("Ram")

# logger.info(labour_name)


# new_labour = ["Mohan","Salman"]
# labour_name.extend(new_labour)

# logger.info(labour_name)

# labour_name.insert(0,"Mara")
# logger.info(f"Inserted labour {labour_name}")

# labour_with_wage = [["Mahesh",500],["Ramesh",400]]
# logger.info(f"Labour {labour_with_wage[0][0]} is charging total of {labour_with_wage[0][1]} per day")


# labour_name = ["Mahesh","Ramesh","Mithilesh","Manish"]
# new_labour = ["Amir","Salman"]

# labours = labour_name + new_labour
# print(labours)

# labour_total = ["Ramesh","Sumesh","Mithilesh",200,300,400]
# print(labour_total[0:1])
# print(labour_total[::-1])
# print(len(labour_total))

# labour_total.insert(3,"Ram")
# print(labour_total)

# pop method - used to delete element from the list Returns the values whichever has deleted

# print(labour_total.pop(4))
# print(labour_total)

labour_total = ["Ramesh","Sumesh","Mihilesh","Manish",200,300,400,400]
# print(labour_total.remove(400))
# print(labour_total)

labour_total[2] = "Mithilesh"
print(labour_total)
