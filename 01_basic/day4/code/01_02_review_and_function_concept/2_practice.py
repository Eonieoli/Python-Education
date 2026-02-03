# 2_practice.py

"""
Day 4 - 2교시: 함수 기본
Practice (강사와 함께 실습)

학습 목표:
- 계산 함수 만들기
- 문자열 처리 함수 만들기
- 여러 값 반환하는 함수 만들기
"""


# ============================================
# 실습 1: 계산 함수 (처음부터 끝까지)
# ============================================
# 함수가 처음이므로 전체를 함께 타이핑합니다

# 사칙연산 함수들을 만들어봅시다
def multiply(a, b):
    """두 숫자를 곱하는 함수"""
    return a * b

def divide(a, b):
    """두 숫자를 나누는 함수"""
    return a / b

# 함수 호출 및 테스트
print("=== 계산 함수 테스트 ===")
print(f"5 × 3 = {multiply(5, 3)}")  # 출력: 5 × 3 = 15
print(f"10 ÷ 2 = {divide(10, 2)}")  # 출력: 10 ÷ 2 = 5.0


# ============================================
# 실습 2: 문자열 처리 함수 (TODO)
# ============================================

# TODO: 문자열을 대문자로 변환하고 느낌표를 붙이는 함수를 작성하세요
# 함수명: make_excited
# 매개변수: text (문자열)
# 반환값: 대문자로 변환 + "!" 추가
# 힌트: text.upper() + "!"
def make_excited(text):
    return text.upper() + "!"

print("\n=== 문자열 처리 함수 테스트 ===")
print(make_excited("hello"))  # 출력: HELLO!
print(make_excited("python"))  # 출력: PYTHON!


# TODO: 이름과 나이를 받아서 소개 문자열을 반환하는 함수를 작성하세요
# 함수명: create_profile
# 매개변수: name (문자열), age (정수)
# 반환값: "이름: {name}, 나이: {age}세" 형식의 문자열
# 힌트: f-string 사용
def create_profile(name, age):
    return f"이름: {name}, 나이: {age}세"

print(create_profile("홍길동", 25))  # 출력: 이름: 홍길동, 나이: 25세
print(create_profile("김철수", 30))  # 출력: 이름: 김철수, 나이: 30세


# ============================================
# 실습 3: 여러 값 반환 함수 (TODO)
# ============================================

# TODO: 리스트에서 최댓값과 최솟값을 동시에 반환하는 함수를 작성하세요
# 함수명: get_min_max
# 매개변수: numbers (리스트)
# 반환값: (최솟값, 최댓값) 튜플
# 힌트: min(numbers), max(numbers)를 return
def get_min_max(numbers):
    return min(numbers), max(numbers)

scores = [85, 92, 78, 95, 88]
minimum, maximum = get_min_max(scores)
print(f"\n=== 최솟값/최댓값 테스트 ===")
print(f"최저 점수: {minimum}")  # 출력: 최저 점수: 78
print(f"최고 점수: {maximum}")  # 출력: 최고 점수: 95


# TODO: 직사각형의 넓이와 둘레를 동시에 반환하는 함수를 작성하세요
# 함수명: calculate_rectangle
# 매개변수: width (가로), height (세로)
# 반환값: (넓이, 둘레) 튜플
# 힌트: 넓이 = width * height, 둘레 = 2 * (width + height)
def calculate_rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

rect_area, rect_perimeter = calculate_rectangle(10, 5)
print(f"\n=== 직사각형 계산 테스트 ===")
print(f"가로 10, 세로 5")
print(f"넓이: {rect_area}")  # 출력: 넓이: 50
print(f"둘레: {rect_perimeter}")  # 출력: 둘레: 30
