##################################################
# 실습 1: 함수 기본
##################################################

# 실습 1-1: 인사 함수
# say_hello(name) 함수를 만들어서
# "안녕하세요, {name}님!" 출력

# 실습 1-2: 제곱 함수
# square(n) 함수를 만들어서
# n의 제곱을 반환
# 예: square(5) → 25

# 실습 1-3: 짝수 판별 함수
# is_even(num) 함수를 만들어서
# 짝수면 True, 홀수면 False 반환
# 힌트: num % 2 == 0

# 실습 1-4: 최댓값 찾기 함수
# find_max(numbers) 함수를 만들어서
# 리스트에서 최댓값 반환
# 힌트: max(numbers) 사용


##################################################
# 실습 2: 매개변수
##################################################

# 실습 2-1: 할인가 계산
# calculate_price(price, discount=0) 함수 작성
# discount가 없으면 원가 그대로 반환
# 있으면 할인 적용 (price * (1 - discount))
# 예: calculate_price(10000, 0.1) → 9000

# 실습 2-2: 사용자 정보 생성
# create_profile(name, age, city="서울", job="미정") 함수
# 딕셔너리로 반환
# 예: create_profile("김철수", 25) 
#     → {"name": "김철수", "age": 25, "city": "서울", "job": "미정"}

# 실습 2-3: 인사 메시지
# greet(name, time="아침") 함수
# time이 "아침"이면 "좋은 아침입니다"
# "저녁"이면 "좋은 저녁입니다"
# 예: greet("김철수") → "좋은 아침입니다, 김철수님!"

# 실습 2-4: 상품 필터링
products = [
    {"name": "노트북", "price": 1500000},
    {"name": "마우스", "price": 30000},
    {"name": "키보드", "price": 80000}
]
# filter_products(products, max_price=100000) 함수
# max_price 이하 상품만 반환


##################################################
# 실습 3: 함수 응용
##################################################

# 실습 3-1: 학생 정보 반환
# get_student_info(name, korean, english, math) 함수
# 이름, 세 과목 점수, 평균, 등급을 딕셔너리로 반환
# 예: {"name": "김철수", "korean": 85, "english": 90, 
#      "math": 88, "average": 87.7, "grade": "B"}

# 실습 3-2: 상품 검색
products = [
    {"id": 1, "name": "노트북", "price": 1500000},
    {"id": 2, "name": "마우스", "price": 30000}
]
# find_product(products, product_id) 함수
# 찾으면 {"found": True, "product": {...}}
# 못 찾으면 {"found": False, "product": None}

# 실습 3-3: 비밀번호 검증
# validate_password(password) 함수
# 8자 이상이면 valid: True
# 아니면 valid: False, 이유 메시지도 포함
# 예: {"valid": True, "message": "안전한 비밀번호"}
#     {"valid": False, "message": "8자 이상 필요"}

# 실습 3-4: 통계 계산
# calculate_statistics(numbers) 함수
# 최소, 최대, 평균, 중앙값을 딕셔너리로 반환
# 힌트: 중앙값은 정렬 후 중간값


##################################################
# 실습 4: 타입 힌트
##################################################

# 실습 4-1: 두 문자열을 받아서 합친 문자열을 반환하는 함수
# 타입 힌트 필수!
def concat_strings(s1: str, s2: str) -> str:
    # 여기에 코드 작성
    pass

# 실습 4-2: 숫자 리스트를 받아서 최댓값과 최솟값의 차이를 반환
# 타입 힌트 필수!
def get_range(numbers: list) -> int:
    # 여기에 코드 작성
    pass

# 실습 4-3: 이름과 나이를 받아서 딕셔너리로 반환
# 딕셔너리 형식: {"name": "...", "age": ..., "is_adult": ...}
# is_adult는 나이가 18 이상이면 True
# 타입 힌트 필수!
def create_person(name: str, age: int) -> dict:
    # 여기에 코드 작성
    pass