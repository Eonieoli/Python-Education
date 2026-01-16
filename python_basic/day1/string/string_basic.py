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