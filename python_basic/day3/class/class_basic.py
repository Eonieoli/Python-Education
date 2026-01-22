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


# 같이 따라 쳐봅시다!

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


# 부모 클래스
class 부모클래스:
    def __init__(self):
        pass

# 자식 클래스
class 자식클래스(부모클래스):  # ← 괄호 안에 부모 이름!
    def __init__(self):
        super().__init__()  # ← 부모의 __init__ 호출
        pass