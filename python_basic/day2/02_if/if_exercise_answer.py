##################################################
# 실습 1: if 기본
##################################################

# 실습 1-1: 온도 확인
temperature = 28
# 온도가 25도 이상이면 "더워요" 출력
if temperature >= 25:
    print("더워요")
print()

# 실습 1-2: 비밀번호 길이 검증
password = "abc123"
# 비밀번호 길이가 8자 이상이면 "안전한 비밀번호" 출력
if len(password) >= 8:
    print("안전한 비밀번호")
# 현재 password는 6자이므로 아무것도 출력되지 않음
print()

# 실습 1-3: 할인 적용
total_price = 55000
# 총액이 50000원 이상이면 10% 할인된 가격 출력
if total_price >= 50000:
    discounted_price = total_price * 0.9  # 10% 할인 = 0.9 곱하기
    print(f"할인가: {int(discounted_price)}원")
    # 또는
    # discount = total_price * 0.1
    # print(f"할인가: {int(total_price - discount)}원")
print()

# 실습 1-4: 로그인 체크
is_logged_in = True
# 로그인 상태면 "환영합니다!" 출력
if is_logged_in:
    print("환영합니다!")
# Boolean 값은 == True 없이 바로 사용 가능
print()


##################################################
# 실습 2: 조건 분기
##################################################

# 실습 2-1: BMI 계산 및 판정
weight = 70  # kg
height = 1.75  # m
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

# BMI가 25 이상이면 "과체중", 18.5 이상이면 "정상", 미만이면 "저체중"
if bmi >= 25:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    print("저체중")
print()

# 실습 2-2: 로그인 검증
username = "admin"
password = "1234"

# username이 "admin"이고 password가 "1234"면 "로그인 성공"
# 아니면 "로그인 실패"
if username == "admin" and password == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")
print()

# 실습 2-3: 상품 구매 가능 여부
price = 15000
balance = 20000
stock = 5

# 잔액이 가격 이상이고, 재고가 1개 이상이면 "구매 가능"
# 아니면 "구매 불가" 및 이유 출력
if balance >= price and stock >= 1:
    print("구매 가능")
else:
    print("구매 불가")
    # 이유 상세 출력
    if balance < price:
        print(f"이유: 잔액 부족 (부족액: {price - balance}원)")
    if stock < 1:
        print("이유: 재고 없음")
print()

# 실습 2-4: 등급 판정
score = 76
attendance = 85  # 출석률

# 점수 80 이상이고 출석률 90 이상: "A"
# 점수 70 이상이고 출석률 80 이상: "B"  
# 그 외: "C"
if score >= 80 and attendance >= 90:
    print("등급: A")
elif score >= 70 and attendance >= 80:
    print("등급: B")
else:
    print("등급: C")