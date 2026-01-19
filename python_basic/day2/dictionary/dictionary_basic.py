# 빈 딕셔너리
empty_dict = {}

# 사용자 정보
user = {
    "name": "김철수",
    "age": 25,
    "email": "kim@example.com"
}

print(user)
# {'name': '김철수', 'age': 25, 'email': 'kim@example.com'}

# 상품 정보
product = {
    "id": 1,
    "name": "노트북",
    "price": 1500000,
    "stock": 10
}

print(product["name"])   # 노트북
print(product["price"])  # 1500000


user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# 대괄호로 접근
print(user["name"])  # 김철수
print(user["age"])   # 25

# 없는 Key는 에러!
# print(user["phone"])  # ❌ KeyError!

# get() 메서드 (안전한 접근)
print(user.get("name"))   # 김철수
print(user.get("phone"))  # None (에러 안 남!)

# 기본값 지정
phone = user.get("phone", "번호 없음")
print(phone)  # 번호 없음


# 빈 딕셔너리로 시작
user = {}

# 값 추가하기
user["name"] = "김철수"
user["age"] = 25
user["email"] = "kim@example.com"

print(user)
# {'name': '김철수', 'age': 25, 'email': 'kim@example.com'}

# 기존 딕셔너리에 추가
product = {
    "name": "노트북",
    "price": 1500000
}

product["stock"] = 10
product["brand"] = "삼성"

print(product)
# {'name': '노트북', 'price': 1500000, 'stock': 10, 'brand': '삼성'}


user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# 값 수정 (이미 있는 Key에 할당)
user["age"] = 26  # 나이 업데이트
user["city"] = "부산"  # 도시 변경

print(user)
# {'name': '김철수', 'age': 26, 'city': '부산'}

# 실전: 상품 재고 관리
product = {
    "name": "노트북",
    "stock": 10,
    "price": 1500000
}

# 판매 시 재고 감소
product["stock"] = product["stock"] - 1
# 또는 간단하게
product["stock"] -= 1

print(f"남은 재고: {product['stock']}개")


user = {
    "name": "김철수",
    "age": 25,
    "email": "kim@test.com",
    "temp_token": "abc123"
}

# del로 삭제
del user["temp_token"]
print(user)  # temp_token 사라짐

# pop()으로 삭제 (삭제된 값 반환)
email = user.pop("email")
print(f"삭제된 이메일: {email}")
print(user)  # email 사라짐

# pop() 기본값 지정 (없어도 에러 안 남)
phone = user.pop("phone", "없음")
print(phone)  # 없음

# clear(): 전체 삭제
user.clear()
print(user)  # {}


user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# keys(): 모든 Key 가져오기
keys = user.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

# values(): 모든 Value 가져오기
values = user.values()
print(values)  # dict_values(['김철수', 25, '서울'])

# items(): Key-Value 쌍 가져오기
items = user.items()
print(items)  
# dict_items([('name', '김철수'), ('age', 25), ('city', '서울')])

# 리스트로 변환
key_list = list(user.keys())
print(key_list)  # ['name', 'age', 'city']


user = {
    "name": "김철수",
    "age": 25,
    "email": "kim@test.com"
}

# Key 존재 확인
print("name" in user)   # True
print("phone" in user)  # False

# 안전한 접근 패턴
if "email" in user:
    print(f"이메일: {user['email']}")
else:
    print("이메일 정보 없음")

# Value 확인 (비효율적)
print("김철수" in user.values())  # True

# 실전 예시: 선택 필드 처리
if "phone" in user:
    contact = user["phone"]
else:
    contact = user.get("email", "연락처 없음")
    
print(f"연락처: {contact}")