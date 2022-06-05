# 'cil'은 Codeit Imaging Library의 약자입니다.
#
# 코딩 창을 보시면 cil.py 파일이 있습니다.
# 파일 안에는 이미지를 읽어오고, 저장하고, 디스플레이하는데 쓰이는 유틸리티 함수들이 몇 개 있는데
# 이 함수들에 대해서 간단히 설명드리겠습니다.
#
# read_image(filepath), save_image(img, filepath) 함수
# 이 함수들은 비트맵 이미지 파일을 읽어와서 중첩된 리스트로 만들어 주고 중첩된 리스트를 비트맵 형식으로
# 저장해 주는 함수들입니다.
#
# display(img) 함수
# 이미지를 예쁘게 출력해 줍니다.

# 이미지를 파일에서 읽어오는 함수
def read_image(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])
    return img


# 이미지를 파일에 저장해 주는 함수
def save_image(img, filepath):
    with open(filepath, 'w') as f:
        for row in img:
            line = ''
            for bit in row:
                line += str(bit)
            line += '\n'
            f.write(line)


# 이미지를 디스플레이해 주는 함수
def display(img):
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width):
            print(img[i][j], end=' ')
        print()


# 이미지 색상 반전
def invert(img):
    # img 이미지 크기
    height, width = len(img), len(img[0])

#    ### 코드를 작성해 주세요 ###
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = invert_bit(img[i][j])

    return new_img


# -1로 채워진 새로운 이미지 생성
def empty_image(height, width):
    new_img = []
    for i in range(height):
        new_img.append([-1] * width)
    return new_img


# 비트 반전
def invert_bit(bit):
    return 1 - bit