# 기초 문제
# 1. 학생 이름 리스트 (최소 3명)
students = []  # 여기에 이름 채우기

# 2. 점수 리스트 (이름과 순서 맞추기)
scores = []  # 여기에 점수 채우기

# 3. 특정 학생 점수 찾기
# "김철수"의 점수를 출력하세요
# 힌트: index() 사용

# 응용 문제
# 4. 새 학생 추가
# "최지은", 88점 추가
# 힌트: append() 두 번

# 5. 평균 점수
# 힌트: sum(scores) / len(scores)

# 6. 최고 점수
# 힌트: max(scores)
# 최고 점수 학생 이름도 출력 (도전!)

# 도전 문제
# 7. 60점 이상 학생 (for문 없이는 어려움)
# 힌트: 일단 건너뛰어도 OK

# 8. 성적표 출력
# f-string으로 예쁘게
# 예: 
# ===== 성적표 =====
# 김철수: 85점
# 이영희: 90점
# ...


# 힌트
##################################################
# 기초 3번: 특정 학생 점수 찾기
name = "김철수"
index = students.index(name)
score = scores[index]

# 응용 5번: 평균 계산
total = sum(scores)
count = len(scores)
average = total / count

# 응용 6번: 최고 점수 학생
max_score = max(scores)
max_index = scores.index(max_score)
top_student = students[max_index]

# 도전 8번: 성적표 출력 (for문 버전)
print("===== 성적표 =====")
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}점")
##################################################