# 사용자 목록 (딕셔너리의 리스트!)
users = [
    {"name": "김철수", "age": 25, "city": "서울"},
    {"name": "이영희", "age": 30, "city": "부산"},
    {"name": "박민수", "age": 28, "city": "대구"}
]

# 모든 사용자 정보 출력
for user in users:
    print(f"이름: {user['name']}, 나이: {user['age']}, 도시: {user['city']}")

# 출력:
# 이름: 김철수, 나이: 25, 도시: 서울
# 이름: 이영희, 나이: 30, 도시: 부산
# 이름: 박민수, 나이: 28, 도시: 대구

# 각 사용자 상세 정보
for user in users:
    print(f"\n{user['name']}님의 정보:")
    for key, value in user.items():
        print(f"  {key}: {value}")


# 1부터 10까지 출력
for i in range(1, 11):
    print(i)

# 짝수만 출력 (0부터 10까지)
for i in range(0, 11, 2):
    print(i)

# 출력: 0 2 4 6 8 10

# 카운트다운
print("카운트다운!")
for i in range(10, 0, -1):
    print(i)
print("발사!")

# 별 피라미드
for i in range(1, 6):
    print("*" * i)

# 출력:
# *
# **
# ***
# ****
# *****