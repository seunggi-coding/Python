# datetime 모듈은 날짜와 시간을 다루기 위한 다양한 '클래스'를 갖추고 있습니다.
# 클래스의 개념을 잘 모르셔도 이 모듈을 사용하는 데에는 문제없습니다.

import datetime

# 현재 시간과 날짜
today = datetime.datetime.now()
print(today)

# 출력값을 "요일, 월 일 연도"로 포매팅
print(today.strftime("%A, %B %dth %Y"))

# 특정 시간과 날짜
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)

# 두 datetime의 차이
print(today - pi_day)