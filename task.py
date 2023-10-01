# hourly_wage = float(input("wages rate: "))
# total_hours = float(input("total hours: "))

# overtime = total_hours - 40
# normal_pay = total_hours * hourly_wage
# overtime_pay = hourly_wage * overtime

# total_wages = overtime_pay + normal_pay

# if total_hours > 40:
#     hours_overtime = float(input("enter hours: "))
#     overtime_pay = hours_overtime * hourly_wage
#     print("Overtime pay:", overtime_pay)
#     print("total pay :",total_wages)
# else:
#     print("Normal pay:" ,"{:.2f}".format(normal_pay))
# temp = 5
# if( temp in range(1,3)):
#     print("cold")
# elif (temp in range(4,7)):
#     print("hot")
# import functools
# numbers = ["S","E","M","E","S","T","E","R"]

# func = lambda x,y :x+y 
# reduced = functools.reduce(func,numbers)
# new_list = []
# for i in reduced:
#     # print(ord(i))
#     new_list.append(i)
#     print(new_list)
# nested loops

# rows = 10
# cols = 10
# sym = "X"
# for i in range(rows):
#     for j in range(i):
#         print(sym,end='')
#     print("")
# num = 1045.8957
# print(round(num,2))
# import math
# loops
# rows = 4
# cols = 2
# for i in range(rows):
#     for j in range(i):
#         print(" im alive", end="")
#     print()

print(list(range(1,6)))
print(list(range(10,0,-1)))