# 여러 가지 방법으로 문자열 만들기
name1 = "김철수"
name2 = '이영희'

# 따옴표 안에 따옴표 넣기
message1 = "I'm a student"  # 작은따옴표 포함
message2 = 'He said "Hello"'  # 큰따옴표 포함

# 여러 줄 문자열
intro = """안녕하세요.
저는 김철수입니다.
반갑습니다."""

print(name1)
print(message1)
print(intro)


# 문자열 더하기 (+)
last_name = "김"
first_name = "철수"
full_name = last_name + first_name
print(full_name)  # 김철수

# 문자열 곱하기 (*)
star = "*"
line = star * 10
print(line)  # **********

# 실용 예제
greeting = "안녕" * 3
print(greeting)  # 안녕안녕안녕


# len() 함수로 길이 구하기
text = "Hello"
length = len(text)
print(length)  # 5

# 한글도 똑같이
name = "김철수"
print(len(name))  # 3

# 공백도 포함
message = "Hello World"
print(len(message))  # 11 (공백도 센다!)


# 문자열 인덱싱
text = "Python"

# 양수 인덱스
print(text[0])  # P
print(text[1])  # y
print(text[5])  # n

# 음수 인덱스
print(text[-1])  # n (맨 뒤)
print(text[-2])  # o (뒤에서 두 번째)
print(text[-6])  # P (맨 앞)


# 문자열 슬라이싱
text = "Python Programming"

# 기본 슬라이싱
print(text[0:6])    # Python
print(text[7:18])   # Programming

# 시작/끝 생략
print(text[:6])     # Python (처음부터 6번째 전까지)
print(text[7:])     # Programming (7번째부터 끝까지)
print(text[:])      # Python Programming (전체)

# 음수 인덱스
print(text[-11:])   # Programming
print(text[:-12])   # Python


# f-string 사용하기
name = "김철수"
age = 25
city = "서울"

# 기본 사용
intro = f"안녕하세요. 저는 {name}입니다."
print(intro)

# 여러 변수
profile = f"이름: {name}, 나이: {age}살, 거주지: {city}"
print(profile)

# 표현식도 가능
price = 10000
quantity = 3
total = f"총 금액: {price * quantity}원"
print(total)  # 총 금액: 30000원

# 소수점 포맷팅
pi = 3.141592
print(f"파이: {pi:.2f}")  # 파이: 3.14 (소수점 2자리)


# 공백 제거
text = "  Hello World  "
print(text.strip())   # "Hello World" (양쪽 공백 제거)
print(text.lstrip())  # "Hello World  " (왼쪽만)
print(text.rstrip())  # "  Hello World" (오른쪽만)

# 문자열 분리 (split)
sentence = "Python is awesome"
words = sentence.split()  # 공백 기준 분리
print(words)  # ['Python', 'is', 'awesome']

email = "user@example.com"
parts = email.split("@")  # @ 기준 분리
print(parts)  # ['user', 'example.com']

# 문자열 결합 (join)
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # "Python is fun"


# 문자열 찾기
text = "Hello World"
print(text.find("World"))    # 6 (시작 위치)
print(text.find("Python"))   # -1 (없으면 -1)

# 포함 여부 확인
print("World" in text)       # True
print("Python" in text)      # False

# 문자열 치환
message = "Hello World"
new_message = message.replace("World", "Python")
print(new_message)  # Hello Python

# 여러 번 치환
text = "banana"
print(text.replace("a", "o"))  # bonono