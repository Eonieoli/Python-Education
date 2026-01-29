##################################################
# 실습 1: 함수 기본
##################################################

# 실습 1-1: 인사 함수
def say_hello(name):
    print(f"안녕하세요, {name}님!")

# 테스트
say_hello("김철수")  # 안녕하세요, 김철수님!
say_hello("이영희")  # 안녕하세요, 이영희님!


# 실습 1-2: 제곱 함수
def square(n):
    return n * n

# 테스트
print(square(5))   # 25
print(square(10))  # 100
result = square(7)
print(result)      # 49


# 실습 1-3: 짝수 판별 함수
def is_even(num):
    return num % 2 == 0

# 테스트
print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(10))  # True

# if문과 함께 사용
if is_even(8):
    print("짝수입니다")


# 실습 1-4: 최댓값 찾기 함수
def find_max(numbers):
    return max(numbers)

# 테스트
nums = [3, 7, 2, 9, 1]
print(find_max(nums))  # 9

scores = [85, 92, 78, 95, 88]
print(find_max(scores))  # 95


##################################################
# 실습 2: 매개변수
##################################################

# 실습 2-1: 할인가 계산
def calculate_price(price, discount=0):
    return price * (1 - discount)

# 테스트
print(calculate_price(10000))         # 10000 (할인 없음)
print(calculate_price(10000, 0.1))    # 9000 (10% 할인)
print(calculate_price(50000, 0.2))    # 40000 (20% 할인)
print(calculate_price(20000, 0.15))   # 17000 (15% 할인)


# 실습 2-2: 사용자 정보 생성
def create_profile(name, age, city="서울", job="미정"):
    return {
        "name": name,
        "age": age,
        "city": city,
        "job": job
    }

# 테스트
profile1 = create_profile("김철수", 25)
print(profile1)
# {"name": "김철수", "age": 25, "city": "서울", "job": "미정"}

profile2 = create_profile("이영희", 30, "부산", "개발자")
print(profile2)
# {"name": "이영희", "age": 30, "city": "부산", "job": "개발자"}

profile3 = create_profile("박민수", 28, job="디자이너")
print(profile3)
# {"name": "박민수", "age": 28, "city": "서울", "job": "디자이너"}


# 실습 2-3: 인사 메시지
def greet(name, time="아침"):
    if time == "아침":
        print(f"좋은 아침입니다, {name}님!")
    elif time == "저녁":
        print(f"좋은 저녁입니다, {name}님!")
    else:
        print(f"안녕하세요, {name}님!")

# 테스트
greet("김철수")           # 좋은 아침입니다, 김철수님!
greet("이영희", "저녁")   # 좋은 저녁입니다, 이영희님!
greet("박민수", "오후")   # 안녕하세요, 박민수님!


# 실습 2-4: 상품 필터링
def filter_products(products, max_price=100000):
    result = []
    for product in products:
        if product["price"] <= max_price:
            result.append(product)
    return result

# 테스트
products = [
    {"name": "노트북", "price": 1500000},
    {"name": "마우스", "price": 30000},
    {"name": "키보드", "price": 80000}
]

print(filter_products(products))
# [{"name": "마우스", "price": 30000}, {"name": "키보드", "price": 80000}]

print(filter_products(products, 50000))
# [{"name": "마우스", "price": 30000}]

print(filter_products(products, 2000000))
# 모든 상품

# 리스트 컴프리헨션 버전 (참고)
def filter_products_v2(products, max_price=100000):
    return [p for p in products if p["price"] <= max_price]


##################################################
# 실습 3: 함수 응용
##################################################

# 실습 3-1: 학생 정보 반환
def get_student_info(name, korean, english, math):
    # 평균 계산
    average = (korean + english + math) / 3
    
    # 등급 계산
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # 딕셔너리로 반환
    return {
        "name": name,
        "korean": korean,
        "english": english,
        "math": math,
        "average": round(average, 2),  # 소수점 2자리
        "grade": grade
    }

# 테스트
student1 = get_student_info("김철수", 85, 90, 88)
print(student1)
# {"name": "김철수", "korean": 85, "english": 90, 
#  "math": 88, "average": 87.67, "grade": "B"}

student2 = get_student_info("이영희", 95, 92, 98)
print(student2)
# {"name": "이영희", ..., "average": 95.0, "grade": "A"}


# 실습 3-2: 상품 검색
def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return {
                "found": True,
                "product": product
            }
    
    # 못 찾은 경우
    return {
        "found": False,
        "product": None
    }

# 테스트
products = [
    {"id": 1, "name": "노트북", "price": 1500000},
    {"id": 2, "name": "마우스", "price": 30000},
    {"id": 3, "name": "키보드", "price": 80000}
]

result1 = find_product(products, 2)
print(result1)
# {"found": True, "product": {"id": 2, "name": "마우스", "price": 30000}}

result2 = find_product(products, 999)
print(result2)
# {"found": False, "product": None}

# 사용 예시
result = find_product(products, 1)
if result["found"]:
    print(f"상품 찾음: {result['product']['name']}")
else:
    print("상품을 찾을 수 없습니다")


# 실습 3-3: 비밀번호 검증
def validate_password(password):
    if len(password) >= 8:
        return {
            "valid": True,
            "message": "안전한 비밀번호입니다"
        }
    else:
        return {
            "valid": False,
            "message": "8자 이상 필요합니다"
        }

# 테스트
result1 = validate_password("abc123")
print(result1)
# {"valid": False, "message": "8자 이상 필요합니다"}

result2 = validate_password("abcd1234")
print(result2)
# {"valid": True, "message": "안전한 비밀번호입니다"}

# 사용 예시
pw = "test"
result = validate_password(pw)
if result["valid"]:
    print("비밀번호 설정 완료!")
else:
    print(f"오류: {result['message']}")


# 실습 3-4: 통계 계산
def calculate_statistics(numbers):
    # 정렬된 리스트
    sorted_numbers = sorted(numbers)
    
    # 최소, 최대
    minimum = min(numbers)
    maximum = max(numbers)
    
    # 평균
    average = sum(numbers) / len(numbers)
    
    # 중앙값 계산
    n = len(sorted_numbers)
    if n % 2 == 1:
        # 홀수 개: 중간값
        median = sorted_numbers[n // 2]
    else:
        # 짝수 개: 중간 두 값의 평균
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    
    return {
        "min": minimum,
        "max": maximum,
        "average": round(average, 2),
        "median": median
    }

# 테스트
numbers1 = [1, 2, 3, 4, 5]
print(calculate_statistics(numbers1))
# {"min": 1, "max": 5, "average": 3.0, "median": 3}

numbers2 = [10, 20, 30, 40]
print(calculate_statistics(numbers2))
# {"min": 10, "max": 40, "average": 25.0, "median": 25.0}

scores = [85, 92, 78, 95, 88, 76]
print(calculate_statistics(scores))
# {"min": 76, "max": 95, "average": 85.67, "median": 86.5}


##################################################
# 실습 4: 타입 힌트
##################################################

# 실습 4-1: 두 문자열을 받아서 합친 문자열을 반환하는 함수
def concat_strings(s1: str, s2: str) -> str:
    return s1 + s2

# 테스트
result = concat_strings("Hello", "World")
print(result)  # HelloWorld

result2 = concat_strings("안녕", "하세요")
print(result2)  # 안녕하세요

# 공백 포함 버전
def concat_strings_v2(s1: str, s2: str) -> str:
    return s1 + " " + s2

print(concat_strings_v2("Hello", "World"))  # Hello World


# 실습 4-2: 숫자 리스트를 받아서 최댓값과 최솟값의 차이를 반환
def get_range(numbers: list) -> int:
    return max(numbers) - min(numbers)

# 테스트
nums = [3, 7, 2, 9, 1]
print(get_range(nums))  # 8 (9 - 1)

scores = [85, 92, 78, 95, 88]
print(get_range(scores))  # 17 (95 - 78)

# 더 정확한 타입 힌트 버전 (참고)
from typing import List

def get_range_v2(numbers: List[int]) -> int:
    return max(numbers) - min(numbers)


# 실습 4-3: 이름과 나이를 받아서 딕셔너리로 반환
def create_person(name: str, age: int) -> dict:
    is_adult = age >= 18
    
    return {
        "name": name,
        "age": age,
        "is_adult": is_adult
    }

# 테스트
person1 = create_person("김철수", 25)
print(person1)
# {"name": "김철수", "age": 25, "is_adult": True}

person2 = create_person("이영희", 16)
print(person2)
# {"name": "이영희", "age": 16, "is_adult": False}

# 더 정확한 타입 힌트 버전 (참고)
from typing import Dict, Any

def create_person_v2(name: str, age: int) -> Dict[str, Any]:
    return {
        "name": name,
        "age": age,
        "is_adult": age >= 18
    }