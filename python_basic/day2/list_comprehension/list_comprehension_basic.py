# 일반 for문
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# 리스트 컴프리헨션
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 숫자에 10 곱하기
numbers = [1, 2, 3, 4, 5]
result = [n * 10 for n in numbers]
print(result)  # [10, 20, 30, 40, 50]

# 문자열 리스트 가공
words = ["hello", "world", "python"]

# 일반 for문
upper_words = []
for word in words:
    upper_words.append(word.upper())

# 리스트 컴프리헨션
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']


# 짝수만 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 일반 for문 + if
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

# 리스트 컴프리헨션 + if
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 60점 이상만
scores = [85, 45, 92, 30, 78, 95, 55]
passing = [score for score in scores if score >= 60]
print(passing)  # [85, 92, 78, 95]

# 특정 문자 포함
words = ["apple", "banana", "grape", "orange"]
has_a = [word for word in words if 'a' in word]
print(has_a)  # ['apple', 'banana', 'grape', 'orange']


# 딕셔너리 리스트에서 특정 값 추출 (FastAPI에서 자주!)
users = [
    {"name": "김철수", "age": 25},
    {"name": "이영희", "age": 30},
    {"name": "박민수", "age": 28}
]

# 이름만 추출
names = [user["name"] for user in users]
print(names)  # ['김철수', '이영희', '박민수']

# 나이만 추출
ages = [user["age"] for user in users]
print(ages)  # [25, 30, 28]

# 조건부 추출: 25세 이상인 사람의 이름
adults = [user["name"] for user in users if user["age"] >= 25]
print(adults)  # ['김철수', '이영희', '박민수']

# 실용 예제: 상품명 리스트
products = [
    {"id": 1, "name": "노트북", "price": 1500000},
    {"id": 2, "name": "마우스", "price": 30000},
    {"id": 3, "name": "키보드", "price": 80000}
]

# 50만원 이상 상품명
expensive = [p["name"] for p in products if p["price"] >= 500000]
print(expensive)  # ['노트북']