##################################################
# 첫 번째 클래스 만들기
##################################################

# 가장 간단한 클래스
class Student:
    pass  # 일단 비워두기

# 클래스로 객체 만들기
student1 = Student()  # ← 괄호 붙여야 함!
student2 = Student()

print(student1)  # <__main__.Student object at ...>
print(student2)  # <__main__.Student object at ...>
print(type(student1))  # <class '__main__.Student'>

# 📌 포인트
# - class 키워드로 클래스 정의
# - 클래스명은 대문자로 시작 (PascalCase)
# - 클래스() 하면 객체(인스턴스) 생성


##################################################
# __init__ 사용하기
##################################################

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성 (자동으로 __init__ 실행됨)
student1 = Student("김철수", 25)
student2 = Student("이영희", 30)

# 속성에 접근하기
print(student1.name)  # 김철수
print(student1.age)   # 25
print(student2.name)  # 이영희
print(student2.age)   # 30


##################################################
# User 클래스 만들기
##################################################

class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

# 여러 사용자 만들기
user1 = User("김철수", "kim@example.com", 25)
user2 = User("이영희", "lee@example.com", 30)
user3 = User("박민수", "park@example.com", 28)

# 정보 확인하기
print(f"사용자1: {user1.username}, {user1.email}, {user1.age}세")
print(f"사용자2: {user2.username}, {user2.email}, {user2.age}세")

# 속성 수정하기
user1.age = 26  # 나이 수정 가능!
print(f"수정 후: {user1.age}세")

# 📌 클래스 하나로 객체 여러 개!


##################################################
# 메서드 만들기
##################################################

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    # 메서드 정의
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."
    
    def get_grade_info(self):
        return f"{self.name}의 성적: {self.grade}"

# 객체 생성
student1 = Student("김철수", 25, "A")
student2 = Student("이영희", 30, "B")

# 메서드 호출
print(student1.introduce())      # 안녕하세요, 저는 김철수이고 25세입니다.
print(student2.introduce())      # 안녕하세요, 저는 이영희이고 30세입니다.
print(student1.get_grade_info()) # 김철수의 성적: A


##################################################
# self의 의미
##################################################

class Student:
    def __init__(self, name, age):
        self.name = name                # self = 이 객체 자신
        self.age = age

# 객체를 만들 때
student1 = Student("김철수", 25)
# 내부적으로는 이렇게 동작
# Student.__init__(student1, "김철수", 25)
#                       └→ self가 student1을 가리킴

student2 = Student("이영희", 30)
# Student.__init__(student2, "이영희", 30)
#                       └→ self가 student2를 가리킴


##################################################
# Product 클래스 만들기
##################################################

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def get_info(self):
        return f"{self.name}: {self.price}원 (재고: {self.stock})"
    
    def is_available(self):
        return self.stock > 0
    
    def apply_discount(self, discount_rate):
        """할인율을 적용 (예: 0.1 = 10% 할인)"""
        self.price = int(self.price * (1 - discount_rate))
        return self.price

# 상품 만들기
laptop = Product("노트북", 1500000, 5)
mouse = Product("마우스", 30000, 0)

# 사용하기
print(laptop.get_info())  # 노트북: 1500000원 (재고: 5)

if laptop.is_available():
    print("구매 가능!")

laptop.apply_discount(0.1)  # 10% 할인
print(laptop.get_info())  # 노트북: 1350000원 (재고: 5)


##################################################
# 클래스 상속 기본 문법
##################################################

# 부모 클래스
class 부모클래스:
    def __init__(self):
        pass

# 자식 클래스
class 자식클래스(부모클래스):  # ← 괄호 안에 부모 이름!
    def __init__(self):
        super().__init__()  # ← 부모의 __init__ 호출
        pass