# 학생 정보 생성
students = [
    {"name": "김철수", "korean": 85, "english": 90, "math": 88},
    {"name": "이영희", "korean": 92, "english": 95, "math": 98},
    {"name": "박민수", "korean": 78, "english": 82, "math": 75}
]

# 모든 학생 정보 출력
print("===== 전체 학생 =====")
for student in students:
    print(f"{student['name']}: 국어 {student['korean']}, "
          f"영어 {student['english']}, 수학 {student['math']}")

# 특정 학생 찾기
search_name = "이영희"
for student in students:
    if student['name'] == search_name:
        print(f"\n{search_name} 학생을 찾았습니다!")
        print(student)
        break

# 평균 점수 계산
print("\n===== 평균 점수 =====")
for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    print(f"{student['name']}: {avg:.1f}점")

# 80점 이상 학생
print("\n===== 80점 이상 학생 =====")
for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    if avg >= 80:
        print(f"{student['name']}: {avg:.1f}점")

# 우등생 목록 (리스트 컴프리헨션)
honor = [s['name'] for s in students 
         if (s['korean'] + s['english'] + s['math']) / 3 >= 90]
print(f"\n우등생: {honor}")

# 과목별 평균
korean_total = sum([s['korean'] for s in students])
english_total = sum([s['english'] for s in students])
math_total = sum([s['math'] for s in students])
count = len(students)

print(f"\n과목별 평균:")
print(f"국어: {korean_total / count:.1f}")
print(f"영어: {english_total / count:.1f}")
print(f"수학: {math_total / count:.1f}")