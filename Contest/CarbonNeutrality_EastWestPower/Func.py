import random

month = random.randint(1, 12)
day = 0
day2 = ""

def Month_day():
    global day

    if month == 1 or  month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 4 or  month == 6 or month == 9 or month == 11:
        day = 30
    elif month == 2:
        day = 28

    return day

def Five_VehicleSystem(car_num):
    global day2

    day2 = input("오늘은 몇일인가요? ")

    if month == 1 or  month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        for i in range(1, 31):
           if (car_num == 1 or car_num == 6) and (day2=="1" or day2=="6" or day2=="11" or day2=="16" or day2=="21" or day2=="26" or day2=="31"):
               print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
           elif(car_num == 2 or car_num == 7) and (day2=="2" or day2=="7" or day2=="12" or day2=="17" or day2=="22" or day2=="27"):
               print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
           elif(car_num == 3 or car_num == 8) and (day2=="3" or day2=="8" or day2=="13" or day2=="18" or day2=="23" or day2=="28"):
               print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
           elif(car_num == 4 or car_num == 9) and (day2=="4" or day2=="9" or day2=="14" or day2=="19" or day2=="24" or day2=="29"):
               print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
           elif(car_num == 5 or car_num == 0) and (day2=="5" or day2=="10" or day2=="15" or day2=="20" or day2=="25" or day2=="30"):
               print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
           break

    elif month == 4 or  month == 6 or month == 9 or month == 11:
        for i in range(1, 30):
            if (car_num == 1 or car_num == 6) and (
                    day2 == "1" or day2 == "6" or day2 == "11" or day2 == "16" or day2 == "21" or day2 == "26"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 2 or car_num == 7) and (
                    day2 == "2" or day2 == "7" or day2 == "12" or day2 == "17" or day2 == "22" or day2 == "27"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 3 or car_num == 8) and (
                    day2 == "3" or day2 == "8" or day2 == "13" or day2 == "18" or day2 == "23" or day2 == "28"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 4 or car_num == 9) and (
                    day2 == "4" or day2 == "9" or day2 == "14" or day2 == "19" or day2 == "24" or day2 == "29"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 5 or car_num == 0) and (
                    day2 == "5" or day2 == "10" or day2 == "15" or day2 == "20" or day2 == "25" or day2 == "30"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            break

    elif month == 2:
        for i in range(1, 28):
            if (car_num == 1 or car_num == 6) and (
                    day2 == "1" or day2 == "6" or day2 == "11" or day2 == "16" or day2 == "21" or day2 == "26"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 2 or car_num == 7) and (
                    day2 == "2" or day2 == "7" or day2 == "12" or day2 == "17" or day2 == "22" or day2 == "27"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 3 or car_num == 8) and (
                    day2 == "3" or day2 == "8" or day2 == "13" or day2 == "18" or day2 == "23" or day2 == "28"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 4 or car_num == 9) and (
                    day2 == "4" or day2 == "9" or day2 == "14" or day2 == "19" or day2 == "24"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            elif (car_num == 5 or car_num == 0) and (
                    day2 == "5" or day2 == "10" or day2 == "15" or day2 == "20" or day2 == "25"):
                print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
            break



