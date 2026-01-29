##################################################
# while 문 기본
##################################################

# 기본 while 문
count = 1

while count <= 5:
    print(count)
    count += 1

# 출력: 1 2 3 4 5

# 조건이 False가 되면 종료
number = 10

while number > 0:
    print(number)
    number -= 1

print("종료!")
# 출력: 10 9 8 7 6 5 4 3 2 1 종료!

# 무한 루프 (주의!)
# while True:
#     print("무한 반복")  # 절대 멈추지 않음!


##################################################
# while과 break
##################################################

# break로 while 종료
count = 1

while True:
    print(count)
    if count >= 5:
        break
    count += 1

# 출력: 1 2 3 4 5

# 실용 예제: 입력 받기 (개념만)
# while True:
#     answer = input("계속하시겠습니까? (y/n): ")
#     if answer == 'n':
#         break
#     print("계속합니다...")

# 재고 처리
stock = 10

while stock > 0:
    print(f"판매! 남은 재고: {stock}")
    stock -= 1
    if stock == 3:
        print("재고 부족 경고!")
        break

print("판매 종료")