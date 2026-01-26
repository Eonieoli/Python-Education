##################################################
# 실습 1: 딕셔너리 생성
##################################################

# 실습 1-1: 도서 정보
book = {
    "title": "파이썬 정복",
    "author": "홍길동",
    "year": 2024,
    "price": 25000
}
print("도서 정보:", book)
print()

# 실습 1-2: 음식점 정보
restaurant = {
    "name": "맛있는 집",
    "cuisine": "한식",
    "rating": 4.5,
    "is_open": True
}
print("음식점 정보:", restaurant)
print()

# 실습 1-3: 학생 성적
student = {
    "name": "김철수",
    "korean": 85,
    "english": 90,
    "math": 88
}
# 평균 계산
average = (student["korean"] + student["english"] + student["math"]) / 3
print(f"{student['name']}의 평균 점수: {average:.2f}점")
print()


##################################################
# 실습 2: 딕셔너리 CRUD
##################################################

# 실습 2-1: 프로필 관리
profile = {"name": "김철수", "age": 25}
print("초기 프로필:", profile)

# 1. "city": "서울" 추가
profile["city"] = "서울"

# 2. age를 26으로 수정
profile["age"] = 26

# 3. "job": "엔지니어" 추가
profile["job"] = "엔지니어"

# 4. 전체 출력
print("최종 프로필:", profile)
print()

# 실습 2-2: 상품 관리
product = {
    "name": "노트북",
    "price": 1500000,
    "stock": 5,
    "on_sale": True
}
print("초기 상품:", product)

# 1. 할인 종료: on_sale을 False로 변경
product["on_sale"] = False

# 2. 재고 3개 증가
product["stock"] = product["stock"] + 3  # 또는 product["stock"] += 3

# 3. "category": "전자제품" 추가
product["category"] = "전자제품"

# 4. 전체 출력
print("최종 상품:", product)
print()

# 실습 2-3: 임시 데이터 정리
data = {
    "id": 1,
    "name": "테스트",
    "temp": "임시",
    "cache": "캐시"
}
print("초기 데이터:", data)

# 1. temp 삭제 (del 사용)
del data["temp"]

# 2. cache 삭제 (pop 사용, 삭제된 값 출력)
removed_value = data.pop("cache")
print("삭제된 cache 값:", removed_value)

# 3. "status": "active" 추가
data["status"] = "active"

print("최종 데이터:", data)
print()


##################################################
# 실습 3: 딕셔너리 메서드
##################################################

# 실습 3-1: 설정 정보 확인
config = {
    "theme": "dark",
    "language": "ko",
    "notifications": True,
    "auto_save": True
}

# 1. 모든 설정 항목(Key) 출력
print("설정 항목들:", list(config.keys()))

# 2. 모든 설정 값(Value) 출력
print("설정 값들:", list(config.values()))

# 3. "language" 설정이 있는지 확인
if "language" in config:
    print("language 설정이 존재합니다")

# 4. "font_size" 설정이 있는지 확인
if "font_size" in config:
    print("font_size 설정이 존재합니다")
else:
    print("font_size 설정이 없습니다")
print()

# 실습 3-2: 사용자 검증
user_input = {
    "username": "hong",
    "email": "hong@test.com"
}

# 필수 필드 확인
# 방법 1: 각각 확인
if "username" in user_input and "email" in user_input and "password" in user_input:
    print("검증 성공")
else:
    print("필수 정보 누락")

# 방법 2: 더 자세한 검증
required_fields = ["username", "email", "password"]
missing_fields = []
for field in required_fields:
    if field not in user_input:
        missing_fields.append(field)

if len(missing_fields) == 0:
    print("검증 성공")
else:
    print(f"필수 정보 누락: {missing_fields}")
print()

# 실습 3-3: 메뉴 정보
menu = {"김치찌개": 8000, "된장찌개": 7000, "순두부": 7500}

# 1. 모든 메뉴 이름 출력
print("메뉴 이름들:", list(menu.keys()))

# 2. 모든 가격 출력
print("가격들:", list(menu.values()))

# 3. "불고기"가 메뉴에 있는지 확인
if "불고기" in menu:
    print("불고기가 메뉴에 있습니다")
else:
    print("불고기가 메뉴에 없습니다")
print()


##################################################
# 실습 4: 복합 자료구조
##################################################

# 실습 4-1: 학생 목록
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78}
]

# 1. 두 번째 학생의 이름 출력
print("두 번째 학생:", students[1]["name"])

# 2. 첫 번째 학생의 점수 출력
print("첫 번째 학생 점수:", students[0]["score"])

# 3. 새 학생 추가
students.append({"name": "최지은", "score": 88})

# 4. 전체 학생 수 출력
print("전체 학생 수:", len(students))
print("전체 학생 목록:", students)
print()

# 실습 4-2: 메뉴 목록
menu = [
    {"name": "아메리카노", "price": 4000, "hot": True},
    {"name": "라떼", "price": 4500, "hot": True}
]

# 1. 아이스 아메리카노 추가
menu.append({"name": "아이스 아메리카노", "price": 4500, "hot": False})

# 2. 첫 번째 메뉴의 가격을 3500으로 변경
menu[0]["price"] = 3500

# 3. 모든 메뉴의 이름만 리스트로 만들기
menu_names = []
for item in menu:
    menu_names.append(item["name"])
print("메뉴 이름들:", menu_names)

# 또는 리스트 컴프리헨션 사용 (배운 경우)
# menu_names = [item["name"] for item in menu]

print("전체 메뉴:", menu)
print()

# 실습 4-3: API 응답 형태
response = {
    "status": "success",
    "data": [
        {"id": 1, "title": "첫 게시글"},
        {"id": 2, "title": "두 번째 게시글"}
    ]
}

# 1. status 값 출력
print("상태:", response["status"])

# 2. data의 첫 번째 게시글 제목 출력
print("첫 번째 게시글 제목:", response["data"][0]["title"])

# 3. 전체 게시글 수 출력
print("전체 게시글 수:", len(response["data"]))