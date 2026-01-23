##################################################
# import 기본
##################################################

# 방법 1: 모듈 전체 import
import random

# 모듈명.함수명으로 사용
number = random.randint(1, 10)
print(f"랜덤 숫자: {number}")

choice = random.choice(["사과", "바나나", "오렌지"])
print(f"선택: {choice}")

# 방법 2: 특정 기능만 import
from random import randint, choice

# 모듈명 없이 바로 사용
number = randint(1, 100)
fruit = choice(["딸기", "수박", "포도"])

# 방법 3: 별칭 사용
import random as rd

num = rd.randint(1, 6)  # 주사위
print(f"주사위: {num}")

# 방법 4: 전체 import (비권장)
from random import *
# 모든 기능을 가져옴 (충돌 위험)