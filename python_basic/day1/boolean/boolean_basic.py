# 비교 연산자
print(10 == 10)   # True  (같다)
print(10 != 5)    # True  (다르다)
print(10 > 5)     # True  (크다)
print(10 < 5)     # False (작다)
print(10 >= 10)   # True  (크거나 같다)
print(10 <= 5)    # False (작거나 같다)

# 문자열도 비교 가능
print("A" == "A")  # True
print("A" < "B")   # True (사전순)


# and: 둘 다 True여야 True
print(True and True)    # True
print(True and False)   # False

# or: 하나라도 True면 True
print(True or False)    # True
print(False or False)   # False

# not: 반대로
print(not True)         # False
print(not False)        # True

# 실용 예제
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(can_drive)  # True