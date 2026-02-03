# 1_basic.py

"""
Day 2 - 5교시: 튜플 + 집합
Basic (강사 시연용)

학습 목표:
- 튜플의 불변성과 언패킹 이해
- 함수에서 여러 값 리턴하기
- 집합으로 중복 제거 및 빠른 검색
"""

# ============================================
# 1. 튜플 생성과 인덱싱
# ============================================

# 튜플은 소괄호 ()로 생성합니다 (리스트와 비슷하지만 수정 불가)
point = (10, 20)
print(point)  # 출력: (10, 20)
print(type(point))  # 출력: <class 'tuple'>

# tuple() 함수로도 생성 가능
colors = tuple(["red", "green", "blue"])
print(colors)  # 출력: ('red', 'green', 'blue')

# 인덱싱은 리스트와 동일
print(point[0])  # 출력: 10
print(point[1])  # 출력: 20
print(colors[-1])  # 출력: blue

# 수정 시도하면 에러 발생!
# point[0] = 30  # TypeError: 'tuple' object does not support item assignment


# ============================================
# 2. 튜플 언패킹 (중요!)
# ============================================

# 언패킹: 튜플의 값을 여러 변수에 한 번에 할당
coordinates = (100, 200)
x, y = coordinates  # 튜플 언패킹!
print(f"x: {x}, y: {y}")  # 출력: x: 100, y: 200

# 소괄호 없이도 가능
name, age = "홍길동", 25
print(f"이름: {name}, 나이: {age}")  # 출력: 이름: 홍길동, 나이: 25

# 여러 변수 동시 할당
a, b, c = 1, 2, 3
print(a, b, c)  # 출력: 1 2 3


# ============================================
# 3. 함수에서 여러 값 리턴 (핵심!)
# ============================================

# 함수는 여러 값을 튜플로 리턴할 수 있습니다
def get_user_info():
    """사용자 정보를 튜플로 리턴"""
    name = "김철수"
    age = 28
    email = "kim@example.com"
    return name, age, email  # 튜플로 리턴!

# 리턴값을 언패킹하여 받기
user_name, user_age, user_email = get_user_info()
print(f"이름: {user_name}")  # 출력: 이름: 김철수
print(f"나이: {user_age}")  # 출력: 나이: 28
print(f"이메일: {user_email}")  # 출력: 이메일: kim@example.com


def calculate(a, b):
    """두 수의 합과 곱을 리턴"""
    return a + b, a * b  # 여러 값 리턴

sum_result, product_result = calculate(5, 3)
print(f"합: {sum_result}, 곱: {product_result}")  # 출력: 합: 8, 곱: 15


# ============================================
# 4. 집합 (set) - 중복 제거
# ============================================

# set()으로 집합 생성 - 중복 자동 제거!
tags = set(["python", "coding", "python", "study", "coding"])
print(tags)  # 출력: {'python', 'coding', 'study'} (순서 랜덤)

# 리스트에서 중복 제거
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # 출력: {1, 2, 3, 4, 5}

# 다시 리스트로 변환
unique_list = list(unique_numbers)
print(unique_list)  # 출력: [1, 2, 3, 4, 5] (순서 랜덤)


# ============================================
# 5. 집합 - 빠른 검색 (in 연산자)
# ============================================

# 집합은 in 연산자로 매우 빠르게 검색!
# in 연산자는 True 또는 False를 반환합니다
allowed_users = set(["admin", "user1", "user2"])

# 사용자가 허용된 사용자인지 확인
is_admin = "admin" in allowed_users
print(f"admin이 허용된 사용자인가? {is_admin}")  # 출력: admin이 허용된 사용자인가? True

is_hacker = "hacker" in allowed_users
print(f"hacker가 허용된 사용자인가? {is_hacker}")  # 출력: hacker가 허용된 사용자인가? False

# 다양한 검색 예시
print("user1" in allowed_users)  # 출력: True
print("guest" in allowed_users)  # 출력: False


# ============================================
# 6. 집합 메서드 (간단히)
# ============================================

# 빈 집합 생성
fruits = set()

# add() - 요소 추가
fruits.add("사과")
fruits.add("바나나")
fruits.add("사과")  # 중복은 무시됨
print(fruits)  # 출력: {'사과', '바나나'}

# remove() - 요소 제거
fruits.remove("바나나")
print(fruits)  # 출력: {'사과'}
