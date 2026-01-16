# None: "값이 없음"을 나타내는 특별한 값
result = None
print(result)  # None
print(type(result))  # <class 'NoneType'>

# 언제 사용하나요?
# 1. 초기값
user_name = None  # 아직 입력 안 됨

# 2. 함수에서 반환값이 없을 때
def say_hello():
    print("Hello")
    # return이 없으면 None 반환

result = say_hello()  # Hello
print(result)  # None

# 3. 값이 있는지 확인
user_name = None

if user_name is None:
    print("이름을 입력해주세요")
else:
    print(f"안녕하세요, {user_name}님!")

# None 체크는 is 사용 (==도 되지만 is 권장)
print(user_name is None)  # True