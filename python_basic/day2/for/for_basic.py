##################################################
# 리스트 순회하기
##################################################

# 리스트의 모든 요소 출력
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# 출력:
# apple
# banana
# orange

# 리스트 요소로 작업하기
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    result = num * 2
    print(f"{num} x 2 = {result}")

# 출력:
# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6
# 4 x 2 = 8
# 5 x 2 = 10


##################################################
# 문자열 순회하기
##################################################

# 문자열도 순회 가능!
text = "Python"

for char in text:
    print(char)

# 출력:
# P
# y
# t
# h
# o
# n

# 실용 예제: 문자 개수 세기
word = "hello"
count = 0

for char in word:
    if char == 'l':
        count += 1

print(f"'l'의 개수: {count}개")  # 2개

##################################################
# 딕셔너리와 for 문 (keys 순회)
##################################################


user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# 방법 1: Key만 순회 (기본)
for key in user:
    print(key)

# 출력:
# name
# age
# city

# 방법 2: keys() 명시적 사용
for key in user.keys():
    print(key)
    
# Key로 Value 접근
for key in user:
    value = user[key]
    print(f"{key}: {value}")

# 출력:
# name: 김철수
# age: 25
# city: 서울


##################################################
# 딕셔너리와 for 문 (values 순회)
##################################################

user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# Value만 순회
for value in user.values():
    print(value)

# 출력:
# 김철수
# 25
# 서울

# 실용 예제: 상품 가격 합계
products = {
    "노트북": 1500000,
    "마우스": 30000,
    "키보드": 80000
}

total = 0
for price in products.values():
    total += price

print(f"총 가격: {total}원")  # 총 가격: 1610000원


##################################################
# 딕셔너리와 for 문 (items 순회)
##################################################

user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# Key와 Value를 동시에! (가장 많이 사용)
for key, value in user.items():
    print(f"{key}: {value}")

# 출력:
# name: 김철수
# age: 25
# city: 서울

# 실용 예제: 설정 정보 출력
config = {
    "theme": "dark",
    "language": "ko",
    "notifications": True,
    "auto_save": True
}

print("===== 설정 =====")
for setting, value in config.items():
    print(f"{setting}: {value}")


##################################################
# range 함수
##################################################

# range(n): 0부터 n-1까지
for i in range(5):
    print(i)

# 출력: 0 1 2 3 4

# range(start, end): start부터 end-1까지
for i in range(2, 6):
    print(i)

# 출력: 2 3 4 5

# range(start, end, step): 간격 지정
for i in range(0, 10, 2):
    print(i)

# 출력: 0 2 4 6 8

# 역순 (큰 수에서 작은 수로)
for i in range(5, 0, -1):
    print(i)

# 출력: 5 4 3 2 1

# 실용 예제: 구구단
dan = 3
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")


##################################################
# enumerate로 인덱스와 값 동시에
##################################################

# enumerate: 인덱스와 값을 동시에
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 출력:
# 0: apple
# 1: banana
# 2: orange

# 시작 인덱스 지정 가능
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}번째: {fruit}")

# 출력:
# 1번째: apple
# 2번째: banana
# 3번째: orange

# 실용 예제: 순위 매기기
scores = [92, 85, 98, 78]

for rank, score in enumerate(sorted(scores, reverse=True), start=1):
    print(f"{rank}등: {score}점")


##################################################
# 중첩 for 문 기본
##################################################

# 간단한 중첩 for문
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 출력 결과:
# i=0, j=0
# i=0, j=1    ← i가 0일 때 j가 0, 1
# i=1, j=0
# i=1, j=1    ← i가 1일 때 j가 0, 1
# i=2, j=0
# i=2, j=1    ← i가 2일 때 j가 0, 1


##################################################
# for + if 조합
##################################################

# for문 안에 if문
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 출력
for num in numbers:
    if num % 2 == 0:
        print(f"{num}은(는) 짝수")

# 조건부 처리
scores = [85, 92, 78, 95, 60, 88]

for score in scores:
    if score >= 90:
        print(f"{score}점 - 우수")
    elif score >= 80:
        print(f"{score}점 - 양호")
    else:
        print(f"{score}점 - 보통")

# 실용 예제: 재고 확인
products = [
    {"name": "노트북", "stock": 5},
    {"name": "마우스", "stock": 0},
    {"name": "키보드", "stock": 10}
]

for product in products:
    if product["stock"] > 0:
        print(f"{product['name']}: 재고 있음 ({product['stock']}개)")
    else:
        print(f"{product['name']}: 품절")


##################################################
# break로 반복 중단
##################################################

# break: 반복문 즉시 종료
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        print("5를 찾았습니다!")
        break
    print(num)

# 출력:
# 1
# 2
# 3
# 4
# 5를 찾았습니다!

# 실용 예제: 사용자 검색
users = [
    {"id": 1, "name": "김철수"},
    {"id": 2, "name": "이영희"},
    {"id": 3, "name": "박민수"}
]

search_id = 2

for user in users:
    if user["id"] == search_id:
        print(f"찾음: {user['name']}")
        break
else:
    print("사용자를 찾을 수 없습니다")


##################################################
# continue로 건너뛰기
##################################################

# continue: 다음 반복으로 건너뛰기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 홀수는 건너뛰고 짝수만 출력
for num in numbers:
    if num % 2 != 0:
        continue
    print(num)

# 출력: 2 4 6 8 10

# 실용 예제: 유효한 이메일만 처리
emails = [
    "user1@test.com",
    "invalid",
    "user2@test.com",
    "",
    "user3@test.com"
]

for email in emails:
    if "@" not in email or len(email) == 0:
        continue
    print(f"유효한 이메일: {email}")

# 출력:
# 유효한 이메일: user1@test.com
# 유효한 이메일: user2@test.com
# 유효한 이메일: user3@test.com