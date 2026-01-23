##################################################
# 연습 1: 매개변수가 있는 메서드
##################################################

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = None  # 처음엔 성적 없음
    
    # 성적을 설정하는 메서드
    def set_grade(self, grade):
        self.grade = grade
        print(f"{self.name}의 성적이 {grade}로 설정되었습니다.")
    
    # 나이를 확인하는 메서드
    def is_adult(self):
        return self.age >= 20

# 사용하기
student = Student("김철수", 20)

# 성적 설정
student.set_grade("A")  # self 외에 grade를 받음!

# 성인 여부 확인
if student.is_adult():
    print(f"{student.name}은 성인입니다.")

##################################################
# 연습 2: self 이해하기
##################################################

class Student:
    def __init__(self, name, age):
        print(f"self는: {self}")  # 객체 자신 출력
        self.name = name
        self.age = age

# 실행해보기
print("student1 만들기:")
student1 = Student("김철수", 20)
print(f"student1은: {student1}")

print("\nstudent2 만들기:")
student2 = Student("이영희", 21)
print(f"student2는: {student2}")

# 결과
# student1 만들기:
# self는: <__main__.Student object at 0x...>
# student1은: <__main__.Student object at 0x...>
# ↑ 주소가 같음! self = student1


##################################################
# 연습 3: 여러 인스턴스 생성하기
##################################################

# 같은 클래스로 여러 객체 만들기

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def get_info(self):
        return f"{self.name}: {self.price}원 (재고: {self.stock})"

# 여러 상품 만들기
product1 = Product("노트북", 1500000, 5)
product2 = Product("마우스", 30000, 20)
product3 = Product("키보드", 80000, 15)

# 모두 출력
print(product1.get_info())
print(product2.get_info())
print(product3.get_info())

# 📌 클래스 하나로 객체 무한대!
# 📌 각 객체는 독립적인 데이터 보유


##################################################
# 연습 4: 인스턴스 리스트 관리하기
##################################################

# 객체들을 리스트로 관리하기
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def get_info(self):
        return f"{self.name}: {self.price}원"

# 상품들을 리스트에 담기
products = [
    Product("노트북", 1000000, 5),
    Product("마우스", 30000, 20),
    Product("키보드", 80000, 15)
]

# for 문으로 순회
print("=== 전체 상품 목록 ===")
for product in products:
    print(product.get_info())

# 조건 검색
print("\n=== 10만원 이하 상품 ===")
for product in products:
    if product.price <= 100000:
        print(product.get_info())

# 리스트 컴프리헨션
cheap_products = [p for p in products if p.price < 100000]
print(f"\n저렴한 상품 {len(cheap_products)}개")


##################################################
# 연습 5: 클래스 상속 기본
##################################################

# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "소리를 냅니다"

# 자식 클래스
class Dog(Animal):  # ← Animal을 상속!
    def __init__(self, name, breed):
        super().__init__(name)  # 부모의 __init__ 호출
        self.breed = breed  # Dog만의 속성 추가
    
    def speak(self):  # 메서드 재정의
        return "멍멍!"

# 사용해보기
dog = Dog("바둑이", "진돗개")
print(dog.name)   # 바둑이 (Animal에서 물려받음)
print(dog.breed)  # 진돗개 (Dog에서 추가)
print(dog.speak()) # 멍멍! (Dog에서 재정의)


##################################################
# 연습 6: FastAPI 스타일 미리보기
##################################################

from pydantic import BaseModel

# BaseModel을 상속받아 사용!
class User(BaseModel):  # ← 상속!
    name: str
    age: int
    email: str

# 왜 상속을 쓸까?
# BaseModel이 이미 가지고 있는 기능:
# ✅ 자동 데이터 검증
# ✅ JSON 변환 (model_dump())
# ✅ 타입 체크
# 이 모든 걸 User가 물려받음!

user = User(name="김철수", age=25, email="kim@example.com")
print(user.model_dump())  # ← BaseModel에서 물려받은 메서드!