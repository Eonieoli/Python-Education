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


# 인덱시 실용 예제
email = "user@example.com"
first_char = email[0]
last_char = email[-1]
print("첫 글자:", first_char)  # u
print("마지막 글자:", last_char)  # m


# 슬라이싱 실용 예제
email = "user@example.com"
username = email[0:4]      # user
domain = email[5:]         # example.com
print("아이디:", username)
print("도메인:", domain)


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