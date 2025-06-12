from loguru import logger
# def final_cart_amount(discount, *args):
#     result = 0
#     for amount in args:
#         result += amount
#     print(result)

#     amount_after_discount = result - (result * discount)

#     return amount_after_discount
# final_amount_to_be_paid = final_cart_amount(0.5,100,500,120,300,500)
# logger.info(final_amount_to_be_paid)

# def sum_of_num(*args):
#     number = input("Enter number")
#     number_list = [float(num) for num in number.split()]
#     return sum(number_list)
     

# number_obj = sum_of_num()
# logger.info(f"Sum of numbers: {number_obj}")


def write_logs_to_file(**kwargs):
    filename = "user_logs.txt"
    with open(filename, "a") as file:
        for key, value in kwargs.items():
            file.write(f"{key}: {value}\n")
            print("Logs written successfully to", filename)
n = int(input("How many log entries do you want to make? "))
logs = {}

for i in range(n):
    key = input(f"Enter log key #{i+1} (e.g., ERROR, INFO): ")
    value = input(f"Enter log message for '{key}': ")
    logs[key] = value

# Calling the function with **kwargs
write_logs_to_file(**logs)