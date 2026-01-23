##################################################
# 간단한 함수 만들기
##################################################

# 가장 간단한 함수
def say_hello():
    print("안녕하세요!")

# 함수 호출
say_hello()  # 안녕하세요!
say_hello()  # 안녕하세요!

# 매개변수가 있는 함수
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("김철수")  # 안녕하세요, 김철수님!
greet("이영희")  # 안녕하세요, 이영희님!

# 반환값이 있는 함수
def add(a, b):
    result = a + b
    return result

sum_result = add(10, 20)
print(sum_result)  # 30

# 한 줄로도 가능
def multiply(a, b):
    return a * b

print(multiply(5, 6))  # 30


##################################################
# 위치 인자와 키워드 인자
##################################################

# 위치 인자 (Positional Arguments)
def introduce(name, age, city):
    print(f"{name}님은 {age}살이고 {city}에 살아요")

# 순서대로 전달
introduce("김철수", 25, "서울")

# 키워드 인자 (Keyword Arguments)
introduce(name="이영희", age=30, city="부산")

# 순서 바꿔도 OK
introduce(city="대구", name="박민수", age=28)

# 섞어서 사용 (위치 인자가 먼저!)
introduce("최지은", age=27, city="인천")

# ❌ 이건 에러 (키워드 뒤에 위치 인자)
# introduce(name="홍길동", 25, "광주")

# 할인가 계산
def calculate_discount(price, discount_rate, is_member):
    if is_member:
        discount_rate += 0.05  # 회원 추가 5% 할인
    
    final_price = price * (1 - discount_rate)
    return final_price

# 명확하게 호출
result = calculate_discount(
    price=10000,
    discount_rate=0.1,
    is_member=True
)
print(f"최종 가격: {result}원")


##################################################
# 기본값 설정
##################################################

# 기본값이 있는 매개변수
def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님!")

greet("김철수")                # 안녕하세요, 김철수님!
greet("이영희", "반갑습니다")   # 반갑습니다, 이영희님!

# 여러 개의 기본값
def create_user(username, email, age=0, is_active=True):
    user = {
        "username": username,
        "email": email,
        "age": age,
        "is_active": is_active
    }
    return user

# 필수 값만 전달
user1 = create_user("hong", "hong@test.com")
print(user1)
# {'username': 'hong', 'email': 'hong@test.com', 
#  'age': 0, 'is_active': True}

# 선택적으로 전달
user2 = create_user("kim", "kim@test.com", age=25)
print(user2)

# FastAPI 스타일 (이렇게 많이 씀!)
items = [1, 2, 3, 4, 5]
def get_items(skip=0, limit=10):
    # skip부터 limit개만 가져오기
    return items[skip:skip+limit]

# 기본값으로 호출
result = get_items()  # skip=0, limit=10

# 필요시 변경
result = get_items(skip=10, limit=5)