import random

month = random.randint(1, 12)
day = 0

def Month_day():
    global day

    if month == 1 or  month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 4 or  month == 6 or month == 9 or month == 11:
        day = 30
    elif month == 2:
        day = 28

    return day

def Five_VehicleSystem(day2, people, car_num, point, pu_transport):

    if month == 1 or  month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        for i in range(1, 31):
            if(car_num == 1 or car_num == 6):
                if (day2=="1" or day2=="6" or day2=="11" or day2=="16" or day2=="21" or day2=="26" or day2=="31"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 1, 6, 11, 16, 21, 26, 31일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif(car_num == 2 or car_num == 7):
                if (day2=="2" or day2=="7" or day2=="12" or day2=="17" or day2=="22" or day2=="27"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 2, 7, 12, 17, 22, 27일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif(car_num == 3 or car_num == 8):
                if (day2=="3" or day2=="8" or day2=="13" or day2=="18" or day2=="23" or day2=="28"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 3, 8, 13, 18, 23, 28일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif(car_num == 4 or car_num == 9):
                if (day2=="4" or day2=="9" or day2=="14" or day2=="19" or day2=="24" or day2=="29"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 4, 9, 14, 19, 24, 29일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif(car_num == 5 or car_num == 0):
                if (day2=="5" or day2=="10" or day2=="15" or day2=="20" or day2=="25" or day2=="30"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 1, 6, 11, 16, 21, 26, 31일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            break

    elif month == 4 or  month == 6 or month == 9 or month == 11:
        for i in range(1, 30):
            if (car_num == 1 or car_num == 6):
                if (
                        day2 == "1" or day2 == "6" or day2 == "11" or day2 == "16" or day2 == "21" or day2 == "26"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 1, 6, 11, 16, 21, 26일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 2 or car_num == 7):
                if (day2 == "2" or day2 == "7" or day2 == "12" or day2 == "17" or day2 == "22" or day2 == "27"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 2, 7, 12, 17, 22, 27일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 3 or car_num == 8):
                if (day2 == "3" or day2 == "8" or day2 == "13" or day2 == "18" or day2 == "23" or day2 == "28"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 3, 8, 13, 18, 23, 28일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 4 or car_num == 9):
                if (day2 == "4" or day2 == "9" or day2 == "14" or day2 == "19" or day2 == "24" or day2 == "29"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 4, 9, 14, 19, 24, 29일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 5 or car_num == 0):
                if (day2 == "5" or day2 == "10" or day2 == "15" or day2 == "20" or day2 == "25" or day2 == "30"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 1, 6, 11, 16, 21, 26일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            break

    elif month == 2:
        for i in range(1, 28):
            if (car_num == 1 or car_num == 6):
                if (
                        day2 == "1" or day2 == "6" or day2 == "11" or day2 == "16" or day2 == "21" or day2 == "26"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 1, 6, 11, 16, 21, 26일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 2 or car_num == 7):
                if (day2 == "2" or day2 == "7" or day2 == "12" or day2 == "17" or day2 == "22" or day2 == "27"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 2, 7, 12, 17, 22, 27일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 3 or car_num == 8):
                if (day2 == "3" or day2 == "8" or day2 == "13" or day2 == "18" or day2 == "23" or day2 == "28"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 3, 8, 13, 18, 23, 28일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 4 or car_num == 9):
                if (day2 == "4" or day2 == "9" or day2 == "14" or day2 == "19" or day2 == "24"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 4, 9, 14, 19, 24일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            elif (car_num == 5 or car_num == 0):
                if (day2 == "5" or day2 == "10" or day2 == "15" or day2 == "20" or day2 == "25"):
                    while 1:
                        pu_transport = input("대중교통을 이용했습니까? ")
                        if pu_transport == "Yes" or pu_transport == "yes":
                            point += 1
                            print("{}님 차량5부제를 장려해주셔서 감사합니다. 복지포인트가 1p 적립되었습니다.".format(people))
                            print("현재 {}님의 총 복지포인트는 {}p 입니다.\n".format(people, point))
                            break
                        elif pu_transport == "No" or pu_transport == "no":
                            print("오늘은 {}일 이므로 차량번호 끝자리가 {}인 차량의 이용을 자제해 주시면 감사하겠습니다.".format(day2, car_num))
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                else:
                    print("{}님의 차량 5부제 날짜는 1, 6, 11, 16, 21, 26일 입니다. 해당 날짜에 대중교통 이용 부탁드립니다.".format(people))
                    print("현재 적립되어 있는 복지포인트는 {}포인트 입니다.\n".format(point))
            break


def People_car():
    people_car_list = [["A", 2, 0], ["B", 4, 0], ["C", 6, 0], ["D", 8, 0]]

    return people_car_list



