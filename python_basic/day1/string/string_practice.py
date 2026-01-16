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


# 자기소개 문자열 만들기
name = "김철수"
age = "25"
job = "개발자"

# 문자열 이어붙이기
intro = "안녕하세요. 제 이름은 " + name + "이고, 나이는 " + age + "살입니다."
print(intro)

# 여러 줄로
profile = "이름: " + name + "\n나이: " + age + "\n직업: " + job
print(profile)
# \n은 줄바꿈을 의미해요!


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

# 실용 예제
email = "user@example.com"
first_char = email[0]
last_char = email[-1]
print("첫 글자:", first_char)  # u
print("마지막 글자:", last_char)  # m


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

# 실용 예제
email = "user@example.com"
username = email[0:4]      # user
domain = email[5:]         # example.com
print("아이디:", username)
print("도메인:", domain)


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


# 실전 예제 1: 사용자 입력 정제
user_input = "  HELLO@EXAMPLE.COM  "
clean_email = user_input.strip().lower()
print(clean_email)  # "hello@example.com"

# 실전 예제 2: 연락처 정보 파싱
contact = "이름:김철수,전화:010-1234-5678,이메일:kim@test.com"
parts = contact.split(",")
for part in parts:
    print(part)

# 실전 예제 3: URL 생성
base_url = "https://api.example.com"
endpoint = "users"
user_id = "123"
full_url = f"{base_url}/{endpoint}/{user_id}"
print(full_url)  # https://api.example.com/users/123