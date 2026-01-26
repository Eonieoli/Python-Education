##################################################
# 실습 1: while 활용
##################################################

# 실습 1-1: 1부터 10까지 합
# while을 사용해서 1+2+3+...+10 계산

num = 1
total = 0

while num <= 10:
    total += num
    num += 1

print(f"1부터 10까지의 합: {total}")

# 비교: for 문 방식
total_for = 0
for i in range(1, 11):
    total_for += i
print(f"for 문 방식: {total_for}")
print()


# 실습 1-2: 구구단 (5단)
# while을 사용해서 5단 출력

print("=== 5단 ===")
i = 1
while i <= 9:
    result = 5 * i
    print(f"5 x {i} = {result}")
    i += 1

# 비교: for 문 방식
print("\n=== 5단 (for문) ===")
for i in range(1, 10):
    print(f"5 x {i} = {5 * i}")
print()


# 실습 1-3: 목표 금액 모으기
# 매달 10만원씩 저축
# 목표 금액 50만원을 모으는 데 몇 개월 걸리는지 계산

saved = 0
months = 0
monthly_saving = 100000
goal = 500000

while saved < goal:
    months += 1
    saved += monthly_saving
    print(f"{months}개월: {saved:,}원")

print(f"\n목표 달성! 총 {months}개월 소요")
print(f"최종 저축액: {saved:,}원")
print()


# 실습 1-4: 배수 찾기
# 1부터 시작해서 3의 배수를 5개 찾기

count = 0
num = 1

print("3의 배수 5개:")
while count < 5:
    if num % 3 == 0:
        print(num, end=" ")
        count += 1
    num += 1

print()
print()

# 방법 2: 3씩 증가
print("3의 배수 5개 (방법 2):")
count = 0
num = 3
while count < 5:
    print(num, end=" ")
    num += 3
    count += 1

print()