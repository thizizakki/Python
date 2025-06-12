# names = ["Manish","Ram","Shyam"]
# final_result = " "
# for name in names:
    # final_result += name
    # final_result = final_result + "-" + name
#     final_result = "-".join(names)
# print(final_result)

# labour_with_cost = {"Mahesh":500,"Ramesh":400,
#                     "Mithilesh":400,"Sumesh":300,
#                     "Jagmohan":1000,"Rampyare":800}
# result = " - ".join(labour_with_cost)
# print(result)

state_dept_info = [{"state":"Bihar","department":"IT"},
                   {"state":"Delhi","department":"Marketing"}]

query = """ select * from (
select e.employee_name, e.state, e.zip, e.salary, d.department
from employee_tble e
inner join department d
ON e.emp_id = d.emp_id
)a
where salary > 100000"""

final_filter_condition = []
for i in state_dept_info:
    for key,value in i.items():
        final_filter_condition.append(f"{key} = {value}")
print(final_filter_condition)

result = " Or ".join(final_filter_condition)

print(query + "AND" +result)