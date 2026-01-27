##################################################
# 실습 1: 숫자 연산
##################################################

# 실습 1-1: 두 숫자의 평균 구하기
num1 = 80
num2 = 90
average = (num1 + num2) / 2
print(f"평균: {average}")
# 출력: 평균: 85.0


# 실습 1-2: 짝수 판별하기
number = 17
remainder = number % 2  # 2로 나눈 나머지
print(f"{number}를 2로 나눈 나머지: {remainder}")
print(f"{number}는 짝수인가? {remainder == 0}")
# 출력: 17를 2로 나눈 나머지: 1
# 출력: 17는 짝수인가? False

# 더 간결한 방법
is_even = number % 2 == 0
print(f"{number}는 짝수: {is_even}")


# 실습 1-3: 온도 변환
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"섭씨 {celsius}도 = 화씨 {fahrenheit}도")
# 출력: 섭씨 25도 = 화씨 77.0도


# 실습 1-4: 거스름돈 계산
price = 7800
payment = 10000

# 거스름돈 계산
change = payment - price
print(f"거스름돈: {change}원")

# 천원짜리 개수 계산
thousand_bills = change // 1000  # 몫만 구하기
remaining = change % 1000        # 나머지
print(f"천원짜리: {thousand_bills}장")
print(f"나머지: {remaining}원")

# 출력:
# 거스름돈: 2200원
# 천원짜리: 2장
# 나머지: 200원