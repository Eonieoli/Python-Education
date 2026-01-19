# None 할당
profile_image = None
print(profile_image)  # None
print(type(profile_image))  # <class 'NoneType'>

# None 체크하기
if profile_image is None:
    print("프로필 사진이 없습니다")
else:
    print("프로필 사진:", profile_image)

# 함수가 아무것도 반환하지 않으면 None
def greet():
    print("안녕하세요!")

result = greet()  # 안녕하세요! 출력
print(result)     # None