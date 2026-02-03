# 3_exercise.py

"""
Day 4 - 2교시: 함수 기본
Exercise - 혼자 풀어보기

문제 1: 온도 변환 함수
섭씨를 화씨로, 화씨를 섭씨로 변환하는 함수를 작성하세요.

문제 2: 인사말 함수
시간대에 따라 다른 인사말을 반환하는 함수를 작성하세요.

각 함수를 작성하고 테스트 코드로 검증하세요.
"""


# ============================================
# 문제 1: 온도 변환 함수
# ============================================

"""
요구사항:
1. celsius_to_fahrenheit 함수
   - 매개변수: celsius (섭씨 온도)
   - 반환값: 화씨 온도
   - 공식: 화씨 = (섭씨 × 9/5) + 32

2. fahrenheit_to_celsius 함수
   - 매개변수: fahrenheit (화씨 온도)
   - 반환값: 섭씨 온도
   - 공식: 섭씨 = (화씨 - 32) × 5/9
"""

# TODO: 섭씨를 화씨로 변환하는 함수를 작성하세요
def celsius_to_fahrenheit(celsius):
    # 여기에 코드를 작성하세요
    pass


# TODO: 화씨를 섭씨로 변환하는 함수를 작성하세요
def fahrenheit_to_celsius(fahrenheit):
    # 여기에 코드를 작성하세요
    pass


# 테스트 코드
print("=== 온도 변환 테스트 ===")
print(f"섭씨 25도 = 화씨 {celsius_to_fahrenheit(25)}도")  # 예상: 77.0
print(f"섭씨 0도 = 화씨 {celsius_to_fahrenheit(0)}도")  # 예상: 32.0
print(f"화씨 77도 = 섭씨 {fahrenheit_to_celsius(77)}도")  # 예상: 25.0
print(f"화씨 32도 = 섭씨 {fahrenheit_to_celsius(32)}도")  # 예상: 0.0


# ============================================
# 문제 2: 인사말 함수
# ============================================

"""
요구사항:
1. get_greeting 함수
   - 매개변수: hour (시간, 0-23)
   - 반환값: 시간대에 맞는 인사말
   - 조건:
     * 5시 ~ 11시: "좋은 아침입니다!"
     * 12시 ~ 17시: "좋은 오후입니다!"
     * 18시 ~ 21시: "좋은 저녁입니다!"
     * 그 외: "안녕하세요!"
"""

# TODO: 시간대에 따른 인사말을 반환하는 함수를 작성하세요
def get_greeting(hour):
    # 여기에 코드를 작성하세요
    # 힌트: if-elif-else 사용
    pass


# 테스트 코드
print("\n=== 인사말 테스트 ===")
print(f"7시: {get_greeting(7)}")  # 예상: 좋은 아침입니다!
print(f"14시: {get_greeting(14)}")  # 예상: 좋은 오후입니다!
print(f"19시: {get_greeting(19)}")  # 예상: 좋은 저녁입니다!
print(f"23시: {get_greeting(23)}")  # 예상: 안녕하세요!


# ============================================
# 보너스 문제 (시간이 남으면 도전!)
# ============================================

"""
요구사항:
calculate_discount 함수를 작성하세요
- 매개변수: price (가격), discount_rate (할인율, 0~1 사이)
- 반환값: (할인 금액, 최종 가격) 튜플
- 예: price=10000, discount_rate=0.2
  → 할인 금액: 2000, 최종 가격: 8000
"""

# TODO: 할인 금액과 최종 가격을 반환하는 함수를 작성하세요
def calculate_discount(price, discount_rate):
    # 여기에 코드를 작성하세요
    pass


# 테스트 코드
print("\n=== 할인 계산 테스트 ===")
discount_amount, final_price = calculate_discount(10000, 0.2)
print(f"원가: 10000원, 할인율: 20%")
print(f"할인 금액: {discount_amount}원")  # 예상: 2000
print(f"최종 가격: {final_price}원")  # 예상: 8000
