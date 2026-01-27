##################################################
# 초기 데이터 (수정하지 마세요!)
##################################################
students = [
    {"name": "김철수", "korean": 85, "english": 90, "math": 88},
    {"name": "이영희", "korean": 92, "english": 88, "math": 95},
    {"name": "박민수", "korean": 78, "english": 85, "math": 80}
]

print("=== 학생 성적 관리 시스템 (딕셔너리 버전) ===")
print(f"학생 수: {len(students)}명")
print()


##################################################
# 기초 1: 모든 학생 정보 출력
##################################################
print("=== 기초 1: 전체 학생 정보 ===")

for student in students:
    print(f"{student['name']}: 국어 {student['korean']}, 영어 {student['english']}, 수학 {student['math']}")

# 출력:
# 김철수: 국어 85, 영어 90, 수학 88
# 이영희: 국어 92, 영어 88, 수학 95
# 박민수: 국어 78, 영어 85, 수학 80
print()


##################################################
# 기초 2: 각 학생의 평균 점수 출력
##################################################
print("=== 기초 2: 평균 점수 계산 ===")

for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    print(f"{student['name']}: 평균 {avg:.2f}점")

# 출력:
# 김철수: 평균 87.67점
# 이영희: 평균 91.67점
# 박민수: 평균 81.00점
print()


##################################################
# 기초 3: 특정 학생 찾기
##################################################
print("=== 기초 3: 이영희 찾기 ===")

for student in students:
    if student['name'] == "이영희":
        print(f"이름: {student['name']}")
        print(f"국어: {student['korean']}점")
        print(f"영어: {student['english']}점")
        print(f"수학: {student['math']}점")
        break

# 출력:
# 이름: 이영희
# 국어: 92점
# 영어: 88점
# 수학: 95점
print()


##################################################
# 응용 1: 새 학생 추가
##################################################
print("=== 응용 1: 학생 추가 ===")

new_student = {
    "name": "최지은",
    "korean": 95,
    "english": 92,
    "math": 90
}
students.append(new_student)

print(f"추가 후 학생 수: {len(students)}명")

# 출력:
# 추가 후 학생 수: 4명
print()


##################################################
# 응용 2: 80점 이상 학생 필터링
##################################################
print("=== 응용 2: 평균 80점 이상 학생 ===")

for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    if avg >= 80:
        print(f"{student['name']}: {avg:.2f}점")

# 출력:
# 김철수: 87.67점
# 이영희: 91.67점
# 박민수: 81.00점
# 최지은: 92.33점
print()


##################################################
# 응용 3: 과목별 전체 평균
##################################################
print("=== 응용 3: 과목별 평균 ===")

korean_total = 0
english_total = 0
math_total = 0

for student in students:
    korean_total += student['korean']
    english_total += student['english']
    math_total += student['math']

korean_avg = korean_total / len(students)
english_avg = english_total / len(students)
math_avg = math_total / len(students)

print(f"국어 평균: {korean_avg:.2f}점")
print(f"영어 평균: {english_avg:.2f}점")
print(f"수학 평균: {math_avg:.2f}점")

# 출력:
# 국어 평균: 87.50점
# 영어 평균: 88.75점
# 수학 평균: 88.25점
print()


##################################################
# 응용 4: 최고 평균 학생 찾기
##################################################
print("=== 응용 4: 최고 평균 학생 ===")

max_avg = 0
top_student = ""

for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    if avg > max_avg:
        max_avg = avg
        top_student = student['name']

print(f"최고 평균: {top_student} - {max_avg:.2f}점")

# 출력:
# 최고 평균: 최지은 - 92.33점
print()


##################################################
# 도전 1: 리스트 컴프리헨션으로 우등생 목록
##################################################
print("=== 도전 1: 우등생 목록 (리스트 컴프리헨션) ===")

honor_students = [
    student['name'] 
    for student in students 
    if (student['korean'] + student['english'] + student['math']) / 3 >= 90
]

print(f"우등생 ({len(honor_students)}명): {honor_students}")

# 출력:
# 우등생 (2명): ['이영희', '최지은']
print()


##################################################
# 도전 2: 과목별 1등 찾기
##################################################
print("=== 도전 2: 과목별 1등 ===")

# 국어 1등
korean_scores = [s['korean'] for s in students]
max_korean = max(korean_scores)

for student in students:
    if student['korean'] == max_korean:
        print(f"국어 1등: {student['name']} ({max_korean}점)")
        break

# 영어 1등
english_scores = [s['english'] for s in students]
max_english = max(english_scores)

for student in students:
    if student['english'] == max_english:
        print(f"영어 1등: {student['name']} ({max_english}점)")
        break

# 수학 1등
math_scores = [s['math'] for s in students]
max_math = max(math_scores)

for student in students:
    if student['math'] == max_math:
        print(f"수학 1등: {student['name']} ({max_math}점)")
        break

# 출력:
# 국어 1등: 최지은 (95점)
# 영어 1등: 최지은 (92점)
# 수학 1등: 이영희 (95점)
print()


##################################################
# 도전 3: 성적순 정렬
##################################################
print("=== 도전 3: 성적순 정렬 ===")

# 1) (평균, 이름) 튜플 리스트 만들기
rankings = []
for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    rankings.append((avg, student['name']))

# 2) 내림차순 정렬
rankings.sort(reverse=True)

# 3) 출력
for rank, (avg, name) in enumerate(rankings, start=1):
    print(f"{rank}등: {name} ({avg:.2f}점)")

# 출력:
# 1등: 최지은 (92.33점)
# 2등: 이영희 (91.67점)
# 3등: 김철수 (87.67점)
# 4등: 박민수 (81.00점)