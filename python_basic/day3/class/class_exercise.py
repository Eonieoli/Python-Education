##################################################
# 실습 1: 클래스 기본
##################################################

# 실습 1-1: Book 클래스 (+ 타입 힌트)
# 책 정보를 담는 클래스를 만드세요
# 속성: title(제목), author(저자), pages(페이지 수)
# 메서드: get_info() - "제목: {}, 저자: {}, {}페이지" 형식으로 반환

class Book:
    # 여기에 코드 작성
    pass

# 테스트
book = Book("파이썬", "홍길동", 300)
print(book.get_info())


# 실습 1-2: BankAccount 클래스 (+ 타입 힌트)
# 은행 계좌 클래스를 만드세요
# 속성: owner(예금주), balance(잔액, 초기값 0)
# 메서드: 
#   deposit(amount) - 입금
#   withdraw(amount) - 출금
#   get_balance() - 잔액 반환

class BankAccount:
    # 여기에 코드 작성
    pass

# 테스트
account = BankAccount("김철수")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000


# 실습 1-3: Rectangle 클래스 (+ 타입 힌트)
# 직사각형 클래스를 만드세요
# 속성: width(가로), height(세로)
# 메서드:
#   area() - 넓이 반환
#   perimeter() - 둘레 반환

class Rectangle:
    # 여기에 코드 작성
    pass

# 테스트
rect = Rectangle(5, 10)
print(rect.area())       # 50
print(rect.perimeter())  # 30


# 실습 1-4: Counter 클래스 (+ 타입 힌트)
# 카운터 클래스를 만드세요
# 속성: count(초기값 0)
# 메서드:
#   increment() - count를 1 증가
#   decrement() - count를 1 감소
#   reset() - count를 0으로
#   get_count() - 현재 count 반환

class Counter:
    # 여기에 코드 작성
    pass


##################################################
# 실습 2: 클래스 활용
##################################################

# 실습 2-1: Movie 클래스와 영화 목록
# 영화 정보를 담는 Movie 클래스를 만들고,
# 여러 영화를 리스트로 관리하세요
# 속성: title(제목), director(감독), year(개봉년도), rating(평점)
# 메서드: get_info() - 영화 정보 반환

class Movie:
    # 여기에 코드 작성
    pass

# 영화 3개 만들어서 리스트에 담기
movies = [
    # 여기에 Movie 객체들
]

# 전체 영화 출력
# 2020년 이후 영화만 필터링


# 실습 2-2: Student 클래스와 성적 관리
# 학생 정보를 담는 Student 클래스를 만드세요
# 속성: name, korean, english, math
# 메서드: 
#   get_average() - 평균 점수 반환
#   get_grade() - 평균이 90이상 A, 80이상 B, 그 외 C

class Student:
    # 여기에 코드 작성
    pass

# 학생 5명 만들기
students = [
    Student("김철수", 85, 90, 88),
    Student("이영희", 92, 95, 98),
    # 3명 더 추가
]

# 전체 학생의 평균과 등급 출력
# A 학생만 필터링


# 실습 2-3: 쇼핑 카트 시스템
# CartItem 클래스: 장바구니 아이템
# 속성: product_name, price, quantity
# 메서드: get_total() - 가격 * 수량

# ShoppingCart 클래스: 장바구니
# 속성: items (CartItem 리스트)
# 메서드:
#   add_item(item) - 아이템 추가
#   get_total_price() - 전체 금액 계산

class CartItem:
    # 여기에 코드 작성
    pass

class ShoppingCart:
    def __init__(self):
        self.items = []
    # 메서드 작성
    pass

# 테스트
cart = ShoppingCart()
cart.add_item(CartItem("노트북", 1000000, 1))
cart.add_item(CartItem("마우스", 30000, 2))
print(cart.get_total_price())  # 1060000


##################################################
# 실습 2: 클래스 활용
##################################################

# 실습 3-1: 고양이 클래스 만들기
# Animal 클래스는 이미 있다고 가정
# Cat 클래스를 만들어서:
# - Animal을 상속받기
# - color 속성 추가하기
# - speak() 메서드를 "야옹!"으로 재정의하기

class Cat(Animal):
    # 여기에 코드 작성
    pass

# 테스트
cat = Cat("나비", "흰색")
print(cat.speak())  # 야옹! 이 나와야 함


# 실습 3-2: 전기차 클래스 만들기
# Car 부모 클래스
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# ElectricCar 자식 클래스를 만드세요
# - Car를 상속받기
# - battery_capacity 속성 추가 (배터리 용량)
# - info() 재정의: "Tesla Model 3 (75kWh)" 형식으로

class ElectricCar(Car):
    # 여기에 코드 작성
    pass


# 실습 3-3: 여러 자식 클래스
# Shape 부모 클래스
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0

# Rectangle, Circle 클래스를 만드세요
# 각각 area() 메서드를 재정의하여 넓이를 계산

class Rectangle(Shape):
    # width, height 속성 추가
    # area() 재정의
    pass

class Circle(Shape):
    # radius 속성 추가
    # area() 재정의 (3.14 * r * r)
    pass