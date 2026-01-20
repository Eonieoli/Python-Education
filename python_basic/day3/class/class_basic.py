# 딕셔너리로 사용자 관리 (불편함)
user1 = {"name": "김철수", "age": 25, "email": "kim@test.com"}
user2 = {"name": "이영희", "age": 30, "email": "lee@test.com"}

# 문제점 1: 오타 가능
user3 = {"naem": "박민수", "age": 28}  # naem으로 오타!

# 문제점 2: 구조 불일치
user4 = {"name": "최지은", "age": 27}  # email 누락

# 문제점 3: 타입 체크 없음
user5 = {"name": "정수진", "age": "서른"}  # 나이가 문자열!

# 클래스로 해결! (다음 슬라이드)


# 클래스 정의
class User:
    pass  # 일단 빈 클래스

# 객체(인스턴스) 생성
user1 = User()
print(user1)  # <__main__.User object at 0x...>

# 속성 추가 (동적으로 - 비권장)
user1.name = "김철수"
user1.age = 25

print(user1.name)  # 김철수
print(user1.age)   # 25

# 더 나은 방법: __init__ 생성자 (다음 슬라이드)


# __init__ 생성자로 초기화
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# 객체 생성 시 값 전달
user1 = User("김철수", 25, "kim@test.com")
user2 = User("이영희", 30, "lee@test.com")

# 속성 접근
print(user1.name)   # 김철수
print(user1.age)    # 25
print(user1.email)  # kim@test.com

print(user2.name)   # 이영희

# 여러 객체 생성
users = [
    User("박민수", 28, "park@test.com"),
    User("최지은", 27, "choi@test.com"),
    User("정수진", 32, "jung@test.com")
]

for user in users:
    print(f"{user.name} ({user.age}세)")


class User:
    def __init__(self, name, age):
        self.name = name  # 이 객체의 name
        self.age = age    # 이 객체의 age
        
    def introduce(self):
        print(f"안녕하세요, {self.name}입니다!")
        print(f"나이는 {self.age}살입니다.")

# user1 객체
user1 = User("김철수", 25)
user1.introduce()
# 안녕하세요, 김철수입니다!
# 나이는 25살입니다.

# user2 객체
user2 = User("이영희", 30)
user2.introduce()
# 안녕하세요, 이영희입니다!
# 나이는 30살입니다.

# self는 각 객체를 가리킴
# user1.introduce() 호출 시 self = user1
# user2.introduce() 호출 시 self = user2


# Product 클래스 (FastAPI Pydantic 모델과 유사!)
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    def to_dict(self):
        """딕셔너리로 변환 (API 응답용)"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
        
    def sell(self, quantity):
        """판매 처리"""
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

# 상품 목록 관리
products = [
    Product(1, "노트북", 1500000, 10),
    Product(2, "마우스", 30000, 50),
    Product(3, "키보드", 80000, 25)
]

# 모든 상품 정보 (API 응답 형태!)
product_list = [p.to_dict() for p in products]
print(product_list)

# 특정 상품 검색
def find_product(products, product_id):
    for product in products:
        if product.id == product_id:
            return product
    return None

# 판매 처리
product = find_product(products, 1)
if product and product.sell(1):
    print(f"{product.name} 판매 완료! 남은 재고: {product.stock}")