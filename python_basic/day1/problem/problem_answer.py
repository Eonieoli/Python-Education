##################################################
# 초기 데이터
##################################################
students = ["김철수", "이영희", "박민수", "최지훈", "한소미"]
scores = [85, 92, 78, 88, 90]

print("=== 초기 데이터 ===")
print(f"학생: {students}")
print(f"점수: {scores}")
print()


##################################################
# 기초 1: 특정 학생의 점수 출력하기
##################################################
print("=== 기초 1: 이영희의 점수 찾기 ===")

# 방법 1: index() 사용
student_name = "이영희"
student_index = students.index(student_name)
student_score = scores[student_index]
print(f"{student_name}의 점수: {student_score}점")

# 방법 2: 한 줄로
print(f"{student_name}의 점수: {scores[students.index(student_name)]}점")

# 출력: 이영희의 점수: 92점
print()


##################################################
# 기초 2: 새 학생 추가하기
##################################################
print("=== 기초 2: 새 학생 추가 ===")

# 학생 추가
students.append("정수진")
scores.append(95)

print(f"추가 후 학생: {students}")
print(f"추가 후 점수: {scores}")

# 출력:
# 추가 후 학생: ['김철수', '이영희', '박민수', '최지훈', '한소미', '정수진']
# 추가 후 점수: [85, 92, 78, 88, 90, 95]
print()


##################################################
# 기초 3: 전체 학생 수와 점수 합계
##################################################
print("=== 기초 3: 통계 정보 ===")

total_students = len(students)
total_score = sum(scores)

print(f"전체 학생 수: {total_students}명")
print(f"전체 점수 합계: {total_score}점")

# 출력:
# 전체 학생 수: 6명
# 전체 점수 합계: 528점
print()


##################################################
# 기초 4: 성적표 출력
##################################################
print("=== 기초 4: 성적표 ===")

# 방법 1: 인덱스 사용
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}점")

print()

# 방법 2: enumerate 사용 (더 좋은 방법!)
for i, student in enumerate(students):
    print(f"{student}: {scores[i]}점")

# 출력:
# 김철수: 85점
# 이영희: 92점
# 박민수: 78점
# 최지훈: 88점
# 한소미: 90점
# 정수진: 95점
print()


##################################################
# 응용 1: 평균 점수 계산
##################################################
print("=== 응용 1: 평균 점수 ===")

average = sum(scores) / len(scores)

# 방법 1: round() 함수
average_rounded = round(average, 2)
print(f"평균 점수: {average_rounded}점")

# 방법 2: f-string 포맷팅
print(f"평균 점수: {average:.2f}점")

# 출력: 평균 점수: 88.00점
print()


##################################################
# 응용 2: 최고점과 최저점 학생 찾기
##################################################
print("=== 응용 2: 최고점/최저점 학생 ===")

# 최고점 학생
max_score = max(scores)
max_index = scores.index(max_score)
max_student = students[max_index]

print(f"최고점: {max_student} - {max_score}점")

# 최저점 학생
min_score = min(scores)
min_index = scores.index(min_score)
min_student = students[min_index]

print(f"최저점: {min_student} - {min_score}점")

# 한 줄로 표현
print(f"\n최고점: {students[scores.index(max(scores))]} - {max(scores)}점")
print(f"최저점: {students[scores.index(min(scores))]} - {min(scores)}점")

# 출력:
# 최고점: 정수진 - 95점
# 최저점: 박민수 - 78점
print()


##################################################
# 응용 3: 특정 학생 삭제
##################################################
print("=== 응용 3: 박민수 삭제 ===")

# 삭제 전 상태 저장
print(f"삭제 전 학생: {students}")
print(f"삭제 전 점수: {scores}")

# 박민수 위치 찾기
student_to_remove = "박민수"
remove_index = students.index(student_to_remove)

# 삭제 (이름과 점수 둘 다)
students.pop(remove_index)
removed_score = scores.pop(remove_index)

print(f"\n{student_to_remove} 삭제 완료 (점수: {removed_score}점)")
print(f"삭제 후 학생: {students}")
print(f"삭제 후 점수: {scores}")

# 출력:
# 박민수 삭제 완료 (점수: 78점)
# 삭제 후 학생: ['김철수', '이영희', '최지훈', '한소미', '정수진']
# 삭제 후 점수: [85, 92, 88, 90, 95]
print()


##################################################
# 도전 1: 점수 순으로 정렬된 명단 만들기
##################################################
print("=== 도전 1: 점수 정렬 ===")

# 원본 유지를 위해 복사
sorted_scores = scores.copy()

# 내림차순 정렬
sorted_scores.sort(reverse=True)

print(f"원본 점수: {scores}")
print(f"정렬 점수: {sorted_scores}")

# 상위 3명의 점수
top_3 = sorted_scores[:3]
print(f"상위 3명 점수: {top_3}")

# sorted() 함수 사용 (원본 유지, 한 줄로)
top_3_alt = sorted(scores, reverse=True)[:3]
print(f"상위 3명 점수 (sorted): {top_3_alt}")

# 출력:
# 원본 점수: [85, 92, 88, 90, 95]
# 정렬 점수: [95, 92, 90, 88, 85]
# 상위 3명 점수: [95, 92, 90]
print()


##################################################
# 도전 2: 80점대 학생 수 세기
##################################################
print("=== 도전 2: 80점대 학생 수 ===")

# 방법 1: for문과 if문 사용
count_80s = 0
for score in scores:
    if 80 <= score < 90:
        count_80s += 1

print(f"80점대 학생 수 (if 사용): {count_80s}명")

# 방법 2: if문 없이 - 리스트 컴프리헨션
count_80s_no_if = len([s for s in scores if 80 <= s < 90])
print(f"80점대 학생 수 (컴프리헨션): {count_80s_no_if}명")

# 방법 3: if문 없이 - 수동 카운트 (창의적!)
# 각 점수가 80점대인지 확인하고 True(1) / False(0)로 변환해서 합산
count_80s_creative = sum([80 <= score < 90 for score in scores])
print(f"80점대 학생 수 (창의적): {count_80s_creative}명")

# 80점대 학생들의 상세 정보
print("\n80점대 학생 목록:")
for i, score in enumerate(scores):
    if 80 <= score < 90:
        print(f"  {students[i]}: {score}점")

# 출력:
# 80점대 학생 수 (if 사용): 2명
# 
# 80점대 학생 목록:
#   김철수: 85점
#   최지훈: 88점
print()


##################################################
# 최종 정리
##################################################
print("=== 최종 성적 정리 ===")
print(f"학생 명단: {students}")
print(f"점수 목록: {scores}")
print(f"총 학생 수: {len(students)}명")
print(f"평균 점수: {sum(scores) / len(scores):.2f}점")
print(f"최고점: {max(scores)}점 ({students[scores.index(max(scores))]})")
print(f"최저점: {min(scores)}점 ({students[scores.index(min(scores))]})")