import random
from Func import month, Month_day as md, Five_VehicleSystem as vs, People_car as pc

i = random.randint(0, 3)
list_park = pc()
pu_transport = ""

print("오늘은 {}월 입니다. {}월은 {}일까지 있습니다.\n".format(month, month, md()))
day2 = input("오늘은 몇일인가요? ")
print("\n")

for j in range(4) :
    ex_park = list_park[j]
    vs(day2, ex_park[0], ex_park[1], ex_park[2], pu_transport)