# 3_exercise_solution.py

"""
Day 4 - 2교시: 함수 기본
Exercise - 정답

문제 1: 온도 변환 함수
문제 2: 인사말 함수
보너스: 할인 계산 함수
"""


# ============================================
# 문제 1: 온도 변환 함수 (정답)
# ============================================

def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환하는 함수"""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환하는 함수"""
    return (fahrenheit - 32) * 5/9


# 테스트 코드
print("=== 온도 변환 테스트 ===")
print(f"섭씨 25도 = 화씨 {celsius_to_fahrenheit(25)}도")  # 출력: 77.0
print(f"섭씨 0도 = 화씨 {celsius_to_fahrenheit(0)}도")  # 출력: 32.0
print(f"화씨 77도 = 섭씨 {fahrenheit_to_celsius(77)}도")  # 출력: 25.0
print(f"화씨 32도 = 섭씨 {fahrenheit_to_celsius(32)}도")  # 출력: 0.0


# ============================================
# 문제 2: 인사말 함수 (정답)
# ============================================

def get_greeting(hour):
    """시간대에 따른 인사말을 반환하는 함수"""
    if 5 <= hour <= 11:
        return "좋은 아침입니다!"
    elif 12 <= hour <= 17:
        return "좋은 오후입니다!"
    elif 18 <= hour <= 21:
        return "좋은 저녁입니다!"
    else:
        return "안녕하세요!"


# 테스트 코드
print("\n=== 인사말 테스트 ===")
print(f"7시: {get_greeting(7)}")  # 출력: 좋은 아침입니다!
print(f"14시: {get_greeting(14)}")  # 출력: 좋은 오후입니다!
print(f"19시: {get_greeting(19)}")  # 출력: 좋은 저녁입니다!
print(f"23시: {get_greeting(23)}")  # 출력: 안녕하세요!


# ============================================
# 보너스 문제: 할인 계산 함수 (정답)
# ============================================

def calculate_discount(price, discount_rate):
    """할인 금액과 최종 가격을 반환하는 함수"""
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price


# 테스트 코드
print("\n=== 할인 계산 테스트 ===")
discount_amount, final_price = calculate_discount(10000, 0.2)
print(f"원가: 10000원, 할인율: 20%")
print(f"할인 금액: {discount_amount}원")  # 출력: 2000.0
print(f"최종 가격: {final_price}원")  # 출력: 8000.0


# ============================================
# 추가 테스트: 다양한 케이스
# ============================================

print("\n=== 추가 테스트 ===")

# 온도 변환 추가 테스트
print(f"섭씨 100도 = 화씨 {celsius_to_fahrenheit(100)}도")  # 출력: 212.0 (물의 끓는점)
print(f"화씨 98.6도 = 섭씨 {fahrenheit_to_celsius(98.6):.1f}도")  # 출력: 37.0 (사람 체온)

# 인사말 추가 테스트
print(f"새벽 3시: {get_greeting(3)}")  # 출력: 안녕하세요!
print(f"정오 12시: {get_greeting(12)}")  # 출력: 좋은 오후입니다!

# 할인 계산 추가 테스트
discount_amount, final_price = calculate_discount(50000, 0.15)
print(f"\n원가: 50000원, 할인율: 15%")
print(f"할인 금액: {discount_amount}원")  # 출력: 7500.0
print(f"최종 가격: {final_price}원")  # 출력: 42500.0
