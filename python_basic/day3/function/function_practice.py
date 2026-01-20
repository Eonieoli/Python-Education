# 평균 계산 함수
def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

# 사용
student_scores = [85, 90, 78, 92]
avg = calculate_average(student_scores)
print(f"평균: {avg}점")  # 평균: 86.25점

# 등급 계산 함수
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 사용
grade = get_grade(85)
print(f"등급: {grade}")  # 등급: B

# 여러 학생 처리
scores = [95, 78, 88]
for score in scores:
    grade = get_grade(score)
    print(f"{score}점 → {grade}등급")


# 검색 함수 (기본값 활용)
def search_users(users, name=None, min_age=0):
    results = []
    for user in users:
        # 이름 조건
        if name and user["name"] != name:
            continue
        # 나이 조건
        if user["age"] < min_age:
            continue
        results.append(user)
    return results

# 테스트 데이터
users = [
    {"name": "김철수", "age": 25},
    {"name": "이영희", "age": 30},
    {"name": "박민수", "age": 22}
]

# 전체 검색
all_users = search_users(users)
print("전체:", all_users)

# 이름으로 검색
kim = search_users(users, name="김철수")
print("김철수:", kim)

# 나이로 필터링
adults = search_users(users, min_age=25)
print("25세 이상:", adults)

# 복합 조건
result = search_users(users, name="이영희", min_age=20)
print("결과:", result)


# 여러 값 반환 (튜플)
def get_min_max(numbers):
    return min(numbers), max(numbers)

# 언패킹으로 받기
min_val, max_val = get_min_max([10, 5, 8, 12, 3])
print(f"최소: {min_val}, 최대: {max_val}")
# 최소: 3, 최대: 12

# 통계 정보 반환
def get_stats(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    
    return total, count, average

total, count, avg = get_stats([85, 90, 78])
print(f"합계: {total}, 개수: {count}, 평균: {avg:.1f}")

# 딕셔너리로 반환하는 게 더 명확!
def get_user_info(user_id):
    # 실제로는 DB에서 가져온다고 가정
    return {
        "id": user_id,
        "name": "김철수",
        "email": "kim@test.com",
        "age": 25
    }

user = get_user_info(1)
print(user["name"])  # 김철수

# 리스트 반환
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

evens = get_even_numbers([1, 2, 3, 4, 5, 6])
print(evens)  # [2, 4, 6]