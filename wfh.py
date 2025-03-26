#Define my conditions
my_wake_up_time=int(input('Please enter a integer >'))
if(my_wake_up_time<=6):
    #Leave for office by 7 am
    print('Leave for office by 7 am')
elif(my_wake_up_time==7):
    print('Leave for office by 8 am')
else:
    print('Today I WFH')