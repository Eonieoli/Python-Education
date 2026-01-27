##################################################
# 연습 1: 기본 예외 처리
##################################################

# 나이 입력 받기 (안전하게)
def get_age_safely(age_str):
    try:
        age = int(age_str)
        if age < 0:
            return None
        return age
    except ValueError:
        print("숫자를 입력해주세요!")
        return None

# 테스트
print(get_age_safely("25"))      # 25
print(get_age_safely("스물다섯"))  # 숫자를 입력해주세요! None
print(get_age_safely("-5"))      # None

# 딕셔너리 안전하게 접근
def get_value_safely(data, key, default=None):
    try:
        return data[key]
    except KeyError:
        print(f"'{key}' 키가 없습니다!")
        return default

user = {"name": "김철수", "age": 25}
print(get_value_safely(user, "name"))      # 김철수
print(get_value_safely(user, "email", "없음"))  # '이메일' 키가 없습니다! 없음

# 리스트 안전하게 접근
def get_item_safely(items, index):
    try:
        return items[index]
    except IndexError:
        print(f"인덱스 {index}는 범위를 벗어났습니다!")
        return None

fruits = ["apple", "banana", "orange"]
print(get_item_safely(fruits, 1))   # banana
print(get_item_safely(fruits, 10))  # 에러 메시지, None


##################################################
# 연습 2: 상품 검증
##################################################

# 상품 딕셔너리
products = {
    1: {"name": "노트북", "price": 1500000},
    2: {"name": "마우스", "price": 30000},
    3: {"name": "키보드", "price": 80000}
}

# 상품 조회 함수
def get_product(product_id):
    if product_id not in products:
        raise KeyError(f"상품 {product_id}가 존재하지 않습니다")
    return products[product_id]

# 사용 예시
try:
    product = get_product(1)
    print(f"상품명: {product['name']}")  # 상품명: 노트북
    
    product = get_product(999)  # 없는 상품!
    print("이 줄은 실행 안 됨")
    
except KeyError as e:
    print(f"에러: {e}")

# 출력:
# 상품명: 노트북
# 에러: 상품 999가 존재하지 않습니다