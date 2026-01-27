##################################################
# 실습 1: 클래스 기본
##################################################

# 실습 1-1: Book 클래스
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self) -> str:
        return f"제목: {self.title}, 저자: {self.author}, {self.pages}페이지"

# 테스트
print("=== 실습 1-1: Book 클래스 ===")
book1 = Book("파이썬", "홍길동", 300)
print(book1.get_info())

book2 = Book("FastAPI 입문", "김개발", 450)
print(book2.get_info())

# 여러 책 관리
books = [
    Book("파이썬 기초", "홍길동", 300),
    Book("FastAPI 실전", "김개발", 450),
    Book("웹 개발", "이코딩", 520)
]

print("\n전체 책 목록:")
for book in books:
    print(f"  {book.get_info()}")
print()


# 실습 1-2: BankAccount 클래스
class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: int) -> None:
        """입금"""
        self.balance += amount
        print(f"{amount}원 입금 완료. 잔액: {self.balance}원")
    
    def withdraw(self, amount: int) -> None:
        """출금"""
        if amount > self.balance:
            print(f"잔액 부족! 현재 잔액: {self.balance}원")
        else:
            self.balance -= amount
            print(f"{amount}원 출금 완료. 잔액: {self.balance}원")
    
    def get_balance(self) -> int:
        """잔액 조회"""
        return self.balance

# 테스트
print("=== 실습 1-2: BankAccount 클래스 ===")
account = BankAccount("김철수")
print(f"초기 잔액: {account.get_balance()}원")

account.deposit(10000)
account.withdraw(3000)
account.withdraw(8000)  # 잔액 부족!
print(f"최종 잔액: {account.get_balance()}원")

# 추가 예시: 여러 계좌
accounts = [
    BankAccount("김철수", 10000),
    BankAccount("이영희", 50000),
    BankAccount("박민수", 30000)
]

print("\n전체 계좌 잔액:")
total = 0
for acc in accounts:
    balance = acc.get_balance()
    print(f"  {acc.owner}: {balance:,}원")
    total += balance
print(f"총 잔액: {total:,}원")
print()


# 실습 1-3: Rectangle 클래스
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def area(self) -> int:
        """넓이 계산"""
        return self.width * self.height
    
    def perimeter(self) -> int:
        """둘레 계산"""
        return 2 * (self.width + self.height)

# 테스트
print("=== 실습 1-3: Rectangle 클래스 ===")
rect1 = Rectangle(5, 10)
print(f"가로: {rect1.width}, 세로: {rect1.height}")
print(f"넓이: {rect1.area()}")
print(f"둘레: {rect1.perimeter()}")

rect2 = Rectangle(8, 6)
print(f"\n가로: {rect2.width}, 세로: {rect2.height}")
print(f"넓이: {rect2.area()}")
print(f"둘레: {rect2.perimeter()}")

# 추가 예시: 여러 사각형 비교
rectangles = [
    Rectangle(5, 10),
    Rectangle(8, 6),
    Rectangle(3, 12)
]

print("\n넓이 비교:")
for i, rect in enumerate(rectangles, 1):
    print(f"  사각형 {i}: {rect.width}x{rect.height} = {rect.area()}")

# 가장 큰 넓이 찾기
max_rect = max(rectangles, key=lambda r: r.area())
print(f"\n가장 큰 사각형: {max_rect.width}x{max_rect.height}, 넓이: {max_rect.area()}")
print()


# 실습 1-4: Counter 클래스
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self) -> None:
        """1 증가"""
        self.count += 1
    
    def decrement(self) -> None:
        """1 감소"""
        self.count -= 1
    
    def reset(self) -> None:
        """0으로 초기화"""
        self.count = 0
    
    def get_count(self) -> int:
        """현재 값 반환"""
        return self.count

# 테스트
print("=== 실습 1-4: Counter 클래스 ===")
counter = Counter()
print(f"초기값: {counter.get_count()}")

counter.increment()
counter.increment()
counter.increment()
print(f"3번 증가: {counter.get_count()}")

counter.decrement()
print(f"1번 감소: {counter.get_count()}")

counter.reset()
print(f"초기화: {counter.get_count()}")

# 추가 예시: 방문자 수 카운터
print("\n방문자 수 카운터:")
visitor_counter = Counter()
for i in range(5):
    visitor_counter.increment()
    print(f"  방문자 {i+1}명 입장. 현재: {visitor_counter.get_count()}명")
print()


##################################################
# 실습 2: 클래스 활용
##################################################

# 실습 2-1: Movie 클래스와 영화 목록
class Movie:
    def __init__(self, title: str, director: str, year: int, rating: float):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
    
    def get_info(self) -> str:
        return f"{self.title} ({self.year}) - 감독: {self.director}, 평점: {self.rating}"

# 영화 3개 만들어서 리스트에 담기
print("=== 실습 2-1: Movie 클래스 ===")
movies = [
    Movie("인터스텔라", "크리스토퍼 놀란", 2014, 9.1),
    Movie("기생충", "봉준호", 2019, 8.6),
    Movie("오펜하이머", "크리스토퍼 놀란", 2023, 8.5),
    Movie("듄", "드니 빌뇌브", 2021, 8.0),
    Movie("탑건: 매버릭", "조셉 코신스키", 2022, 8.3)
]

# 전체 영화 출력
print("전체 영화 목록:")
for movie in movies:
    print(f"  {movie.get_info()}")

# 2020년 이후 영화만 필터링
print("\n2020년 이후 영화:")
recent_movies = [m for m in movies if m.year >= 2020]
for movie in recent_movies:
    print(f"  {movie.get_info()}")

# 추가: 평점 8.5 이상 영화
print("\n평점 8.5 이상 영화:")
high_rated = [m for m in movies if m.rating >= 8.5]
for movie in high_rated:
    print(f"  {movie.get_info()}")

# 추가: 감독별 영화 수
print("\n크리스토퍼 놀란 감독 영화:")
nolan_movies = [m for m in movies if m.director == "크리스토퍼 놀란"]
for movie in nolan_movies:
    print(f"  {movie.title} ({movie.year})")
print()


# 실습 2-2: Student 클래스와 성적 관리
class Student:
    def __init__(self, name: str, korean: int, english: int, math: int):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
    
    def get_average(self) -> float:
        """평균 점수 계산"""
        return (self.korean + self.english + self.math) / 3
    
    def get_grade(self) -> str:
        """등급 계산"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        else:
            return "C"
    
    def get_info(self) -> str:
        """학생 정보 반환"""
        avg = self.get_average()
        grade = self.get_grade()
        return f"{self.name}: 국어{self.korean}, 영어{self.english}, 수학{self.math}, 평균{avg:.1f}, 등급{grade}"

# 학생 5명 만들기
print("=== 실습 2-2: Student 클래스 ===")
students = [
    Student("김철수", 85, 90, 88),
    Student("이영희", 92, 95, 98),
    Student("박민수", 78, 82, 75),
    Student("최지은", 95, 92, 96),
    Student("정수진", 88, 85, 90)
]

# 전체 학생의 평균과 등급 출력
print("전체 학생 성적:")
for student in students:
    print(f"  {student.get_info()}")

# A 학생만 필터링
print("\nA 등급 학생:")
a_students = [s for s in students if s.get_grade() == "A"]
for student in a_students:
    print(f"  {student.name}: 평균 {student.get_average():.1f}")

# 추가: 전체 평균
print("\n통계:")
total_avg = sum(s.get_average() for s in students) / len(students)
print(f"  전체 평균: {total_avg:.1f}")

# 추가: 최고 점수 학생
best_student = max(students, key=lambda s: s.get_average())
print(f"  최고 점수: {best_student.name} ({best_student.get_average():.1f})")

# 추가: 과목별 평균
korean_avg = sum(s.korean for s in students) / len(students)
english_avg = sum(s.english for s in students) / len(students)
math_avg = sum(s.math for s in students) / len(students)
print(f"  과목별 평균: 국어{korean_avg:.1f}, 영어{english_avg:.1f}, 수학{math_avg:.1f}")
print()


# 실습 2-3: 쇼핑 카트 시스템
class CartItem:
    def __init__(self, product_name: str, price: int, quantity: int):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    
    def get_total(self) -> int:
        """아이템 총 가격 계산"""
        return self.price * self.quantity
    
    def get_info(self) -> str:
        """아이템 정보 반환"""
        return f"{self.product_name} - {self.price:,}원 x {self.quantity}개 = {self.get_total():,}원"


class ShoppingCart:
    def __init__(self):
        self.items: list[CartItem] = []
    
    def add_item(self, item: CartItem) -> None:
        """아이템 추가"""
        self.items.append(item)
        print(f"'{item.product_name}' 추가됨")
    
    def get_total_price(self) -> int:
        """전체 금액 계산"""
        return sum(item.get_total() for item in self.items)
    
    def show_cart(self) -> None:
        """장바구니 내역 출력"""
        print("\n=== 장바구니 내역 ===")
        if not self.items:
            print("장바구니가 비어있습니다.")
            return
        
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.get_info()}")
        print(f"\n총 금액: {self.get_total_price():,}원")

# 테스트
print("=== 실습 2-3: 쇼핑 카트 시스템 ===")
cart = ShoppingCart()

cart.add_item(CartItem("노트북", 1000000, 1))
cart.add_item(CartItem("마우스", 30000, 2))
cart.add_item(CartItem("키보드", 80000, 1))

cart.show_cart()

# 추가 예시: 할인 적용
print("\n\n=== 할인 적용 예시 ===")

class DiscountCartItem(CartItem):
    def __init__(self, product_name: str, price: int, quantity: int, discount_rate: float = 0):
        super().__init__(product_name, price, quantity)
        self.discount_rate = discount_rate
    
    def get_total(self) -> int:
        """할인 적용된 총 가격"""
        original = self.price * self.quantity
        return int(original * (1 - self.discount_rate))
    
    def get_info(self) -> str:
        """할인 정보 포함"""
        if self.discount_rate > 0:
            original = self.price * self.quantity
            discount = int(self.discount_rate * 100)
            return f"{self.product_name} - {self.price:,}원 x {self.quantity}개 ({discount}% 할인) = {self.get_total():,}원"
        return super().get_info()

cart2 = ShoppingCart()
cart2.add_item(DiscountCartItem("노트북", 1000000, 1, 0.1))  # 10% 할인
cart2.add_item(DiscountCartItem("마우스", 30000, 2, 0.2))   # 20% 할인
cart2.add_item(CartItem("키보드", 80000, 1))  # 할인 없음

cart2.show_cart()
print()


##################################################
# 실습 3: 클래스 상속
##################################################

# 실습 3-1: 고양이 클래스 만들기
# Animal 부모 클래스 (문제에서 "있다고 가정"했으므로 먼저 정의)
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return "동물 소리"

class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)  # 부모 클래스 초기화
        self.color = color
    
    def speak(self) -> str:
        """speak 메서드 재정의"""
        return "야옹!"
    
    def get_info(self) -> str:
        return f"{self.color} 고양이 {self.name}"

# 테스트
print("=== 실습 3-1: Cat 클래스 ===")
cat = Cat("나비", "흰색")
print(f"이름: {cat.name}")
print(f"색깔: {cat.color}")
print(f"소리: {cat.speak()}")
print(f"정보: {cat.get_info()}")

# 추가 예시: 여러 고양이
cats = [
    Cat("나비", "흰색"),
    Cat("치즈", "주황색"),
    Cat("먹구름", "검은색")
]

print("\n고양이 목록:")
for cat in cats:
    print(f"  {cat.get_info()}: {cat.speak()}")
print()


# 실습 3-2: 전기차 클래스 만들기
class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def info(self) -> str:
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand: str, model: str, battery_capacity: int):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def info(self) -> str:
        """info 메서드 재정의"""
        return f"{self.brand} {self.model} ({self.battery_capacity}kWh)"
    
    def charge(self, amount: int) -> None:
        """충전 기능 (추가 메서드)"""
        print(f"{amount}kWh 충전 중...")

# 테스트
print("=== 실습 3-2: ElectricCar 클래스 ===")
car1 = Car("현대", "아반떼")
print(f"일반 차량: {car1.info()}")

ev1 = ElectricCar("Tesla", "Model 3", 75)
print(f"전기차: {ev1.info()}")

ev2 = ElectricCar("현대", "아이오닉5", 72)
print(f"전기차: {ev2.info()}")

# 추가 예시: 전기차 목록
electric_cars = [
    ElectricCar("Tesla", "Model 3", 75),
    ElectricCar("Tesla", "Model S", 100),
    ElectricCar("현대", "아이오닉5", 72),
    ElectricCar("기아", "EV6", 77)
]

print("\n전기차 목록:")
for ev in electric_cars:
    print(f"  {ev.info()}")

# 배터리 용량별 정렬
print("\n배터리 용량 순:")
sorted_evs = sorted(electric_cars, key=lambda x: x.battery_capacity, reverse=True)
for ev in sorted_evs:
    print(f"  {ev.info()}")
print()


# 실습 3-3: 여러 자식 클래스
class Shape:
    def __init__(self, name: str):
        self.name = name
    
    def area(self) -> float:
        return 0

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        super().__init__("직사각형")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """넓이 계산 재정의"""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__("원")
        self.radius = radius
    
    def area(self) -> float:
        """넓이 계산 재정의"""
        return 3.14 * self.radius * self.radius

# 테스트
print("=== 실습 3-3: Shape 상속 ===")

rect = Rectangle(5, 10)
print(f"{rect.name}: {rect.width} x {rect.height}")
print(f"넓이: {rect.area()}")

circle = Circle(7)
print(f"\n{circle.name}: 반지름 {circle.radius}")
print(f"넓이: {circle.area():.2f}")

# 추가 예시: 여러 도형을 하나의 리스트로 관리
print("\n도형 목록:")
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Rectangle(3, 8),
    Circle(5)
]

for shape in shapes:
    print(f"  {shape.name}: 넓이 = {shape.area():.2f}")

# 전체 넓이 합계
total_area = sum(shape.area() for shape in shapes)
print(f"\n전체 넓이 합: {total_area:.2f}")
print()