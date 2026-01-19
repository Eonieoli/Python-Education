# 자기 정보로 딕셔너리 만들기
my_info = {
    "name": "홍길동",
    "age": 30,
    "city": "서울",
    "job": "엔지니어"
}

# 값 출력하기
print(f"이름: {my_info['name']}")
print(f"나이: {my_info['age']}살")
print(f"직업: {my_info['job']}")

# 영화 정보
movie = {
    "title": "파이썬 마스터",
    "director": "코드감독",
    "year": 2026,
    "rating": 9.5
}

print(f"{movie['title']}({movie['year']})")


# API 응답 예시 (FastAPI에서 이렇게 옵니다!)
response = {
    "status": "success",
    "data": {
        "user_id": 123,
        "username": "김철수"
    },
    "message": "로그인 성공"
}

# 상태 확인
status = response["status"]
print(f"상태: {status}")

# 사용자 정보 (중첩된 딕셔너리)
user_data = response["data"]
print(f"사용자 ID: {user_data['user_id']}")
print(f"사용자명: {user_data['username']}")

# 직접 접근도 가능
username = response["data"]["username"]
print(username)  # 김철수

# 안전한 접근
error = response.get("error", "에러 없음")
print(error)  # 에러 없음


# 사용자 정보 점진적으로 추가
user = {
    "id": 1,
    "name": "김철수"
}

# 로그인 시 정보 추가
user["email"] = "kim@test.com"
user["login_time"] = "2024-01-16 09:00"

# 프로필 완성 시 추가
user["phone"] = "010-1234-5678"
user["address"] = "서울시 강남구"

print(user)

# 실전: 장바구니
cart = {}
cart["item_count"] = 0
cart["total_price"] = 0

# 상품 추가
cart["item_count"] = 1
cart["total_price"] = 15000

print(f"장바구니: {cart['item_count']}개, {cart['total_price']}원")


# 사용자 세션 정보
session = {
    "user_id": 123,
    "username": "김철수",
    "login_time": "2026-01-19 09:00",
    "temp_data": "임시정보",
    "cache": "캐시데이터"
}

print("로그인 상태:", session)

# 로그아웃 시 민감 정보 삭제
del session["temp_data"]
del session["cache"]

print("정리 후:", session)

# 캐시 삭제 (없어도 에러 안 남)
removed_cache = session.pop("cache", None)
print(f"삭제된 캐시: {removed_cache}")  # None

# 세션 완전 종료
session.clear()
print("로그아웃:", session)  # {}


# 상품 정보
product = {
    "id": 1,
    "name": "노트북",
    "price": 1500000,
    "stock": 10,
    "brand": "삼성"
}

# 모든 속성 이름 확인
print("상품 속성:", list(product.keys()))

# 모든 값 확인
print("상품 정보:", list(product.values()))

# Key-Value 쌍으로 확인
print("\n상품 상세:")
for key, value in product.items():
    print(f"{key}: {value}")

# 출력:
# id: 1
# name: 노트북
# price: 1500000
# stock: 10
# brand: 삼성


# 사용자 목록 (FastAPI 응답 형태!)
users = [
    {"id": 1, "name": "김철수", "age": 25},
    {"id": 2, "name": "이영희", "age": 30},
    {"id": 3, "name": "박민수", "age": 28}
]

# 첫 번째 사용자
first_user = users[0]
print(first_user)  # {'id': 1, 'name': '김철수', 'age': 25}

# 첫 번째 사용자의 이름
first_name = users[0]["name"]
print(first_name)  # 김철수

# 두 번째 사용자의 나이
second_age = users[1]["age"]
print(second_age)  # 30

# 전체 사용자 수
print(f"총 {len(users)}명의 사용자")  # 총 3명의 사용자


# 상품 목록
products = [
    {
        "id": 1,
        "name": "노트북",
        "price": 1500000,
        "stock": 10
    },
    {
        "id": 2,
        "name": "마우스",
        "price": 30000,
        "stock": 50
    },
    {
        "id": 3,
        "name": "키보드",
        "price": 80000,
        "stock": 25
    }
]

# 상품 정보 접근
print(f"첫 번째 상품: {products[0]['name']}")
print(f"가격: {products[0]['price']}원")

# 새 상품 추가
new_product = {
    "id": 4,
    "name": "모니터",
    "price": 350000,
    "stock": 15
}
products.append(new_product)

print(f"총 상품 수: {len(products)}개")