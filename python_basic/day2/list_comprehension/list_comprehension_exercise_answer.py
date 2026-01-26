##################################################
# 실습 1: 리스트 컴프리헨션
##################################################

# 실습 1-1: 제곱 리스트
numbers = [1, 2, 3, 4, 5]
# 각 숫자의 제곱으로 이루어진 리스트 만들기
# 결과: [1, 4, 9, 16, 25]

# 리스트 컴프리헨션
squared = [num ** 2 for num in numbers]
print("제곱 리스트:", squared)

# 비교: for 문 방식
squared_for = []
for num in numbers:
    squared_for.append(num ** 2)
print("for 문 방식:", squared_for)
print()


# 실습 1-2: 길이 리스트
words = ["hello", "world", "python", "programming"]
# 각 단어의 길이로 이루어진 리스트 만들기

# 리스트 컴프리헨션
lengths = [len(word) for word in words]
print("단어 길이:", lengths)
print()


# 실습 1-3: 양수만 필터링
numbers = [-5, 3, -2, 8, -1, 6, -7, 10]
# 양수만 담은 리스트 만들기

# 리스트 컴프리헨션
positive = [num for num in numbers if num > 0]
print("양수만:", positive)

# 비교: for 문 방식
positive_for = []
for num in numbers:
    if num > 0:
        positive_for.append(num)
print("for 문 방식:", positive_for)
print()


# 실습 1-4: 가격 인상
prices = [1000, 2000, 3000, 4000]
# 모든 가격에 10% 인상 (각 가격 * 1.1)

# 리스트 컴프리헨션
increased_prices = [price * 1.1 for price in prices]
print("인상된 가격:", increased_prices)

# 정수로 변환하고 싶다면
increased_prices_int = [int(price * 1.1) for price in prices]
print("인상된 가격 (정수):", increased_prices_int)
print()


# 실습 1-5: 학생 이름 추출
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78},
    {"name": "최지은", "score": 95}
]
# 90점 이상 학생의 이름만 추출

# 리스트 컴프리헨션
high_scorers = [student["name"] for student in students if student["score"] >= 90]
print("90점 이상 학생:", high_scorers)

# 비교: for 문 방식
high_scorers_for = []
for student in students:
    if student["score"] >= 90:
        high_scorers_for.append(student["name"])
print("for 문 방식:", high_scorers_for)
print()


# 실습 1-6: 짝수 제곱
# 1부터 10까지 중 짝수의 제곱으로 이루어진 리스트

# 방법 1: if로 짝수 필터링
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("짝수 제곱 (방법 1):", even_squares)

# 방법 2: range의 step 활용
even_squares2 = [i ** 2 for i in range(2, 11, 2)]
print("짝수 제곱 (방법 2):", even_squares2)

# 비교: for 문 방식
even_squares_for = []
for i in range(1, 11):
    if i % 2 == 0:
        even_squares_for.append(i ** 2)
print("for 문 방식:", even_squares_for)