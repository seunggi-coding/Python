# OS는 Operating System, 즉 운영체제의 약자입니다.
# os 모듈을 통해서 파이썬으로 운영체제를 조작하거나 운영체제에 대한 정보를 가져올 수 있습니다.

import os

# 현재 어떤 계정으로 로그인 돼있는지 확인
print(os.getlogin())

# 현재 파일의 디렉토리 확인
print(os.getcwd())

# 현재 프로세스 ID 확인
print(os.getpid())