"""
요구사항:
- 학생 이름과 점수를 별도의 리스트로 관리
- 이름과 점수는 인덱스로 매칭

기초 문제 (10분)
1. 학생 이름 리스트 만들기 (3명)
2. 학생 점수 리스트 만들기 (3명)
3. 특정 학생 점수 찾기 (인덱스 활용)

응용 문제 (15분)
4. 새 학생 추가하기 (이름과 점수 둘 다)
5. 평균 점수 계산하기
6. 최고 점수 찾기 (max 함수)

도전 문제 (15분)
7. 60점 이상 학생만 필터링
8. f-string으로 성적표 출력
   (이름: 점수 형식)
"""


# 힌트
##################################################
"""
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
"""
##################################################