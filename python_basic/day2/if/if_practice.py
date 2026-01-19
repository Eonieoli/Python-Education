# 영화 관람 등급 확인
age = 17
movie_rating = 15

if age >= movie_rating:
    print(f"{movie_rating}세 관람가 영화를 볼 수 있습니다")

# 할인 적용
price = 10000
is_student = True

if is_student:
    discount_price = price * 0.8
    print(f"학생 할인가: {discount_price}원")

# 재고 확인
stock = 5

if stock > 0:
    print("구매 가능")
    stock = stock - 1
    print(f"남은 재고: {stock}개")


# 재고 상태
stock = 0

if stock > 0:
    print(f"재고 있음: {stock}개")
else:
    print("품절")

# 합격/불합격
score = 55
passing_score = 60

if score >= passing_score:
    print("합격입니다!")
    print(f"점수: {score}")
else:
    print("불합격입니다")
    print(f"점수: {score}")
    print(f"{passing_score - score}점 부족")


# 성적 등급 계산기
score = 78

if score >= 90:
    print("A 등급 - 우수합니다!")
elif score >= 80:
    print("B 등급 - 잘했습니다!")
elif score >= 70:
    print("C 등급 - 보통입니다")
elif score >= 60:
    print("D 등급 - 노력하세요")
else:
    print("F 등급 - 많은 노력이 필요합니다")

# 계절 판별
month = 7

if month in [12, 1, 2]:
    season = "겨울"
elif month in [3, 4, 5]:
    season = "봄"
elif month in [6, 7, 8]:
    season = "여름"
else:
    season = "가을"

print(f"{month}월은 {season}입니다")


# 입장 조건 확인
age = 22
has_ticket = True
is_member = False

if age >= 18 and has_ticket:
    print("입장 가능")
    if is_member:
        print("회원 혜택 적용")
else:
    print("입장 불가")

# 할인 조건 (복잡한 예시)
price = 50000
is_weekend = True
is_member = True

if is_weekend and is_member:
    final_price = price * 0.7  # 30% 할인
    print(f"주말 회원 할인: {final_price}원")
elif is_weekend:
    final_price = price * 0.9  # 10% 할인
    print(f"주말 할인: {final_price}원")
elif is_member:
    final_price = price * 0.8  # 20% 할인
    print(f"회원 할인: {final_price}원")
else:
    print(f"정상가: {price}원")