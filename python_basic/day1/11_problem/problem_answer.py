##################################################
# 초기 데이터
##################################################
students = ["김철수", "이영희", "박민수", "최지훈", "한소미"]
scores = [85, 92, 78, 88, 90]

print("=== 학생 성적 관리 시스템 ===")
print(f"학생: {students}")
print(f"점수: {scores}")
print()


##################################################
# 기초 1: 특정 학생의 점수 출력하기
##################################################
print("=== 기초 1: 이영희의 점수 찾기 ===")

# 방법 1: 단계별로
student_name = "이영희"
student_index = students.index(student_name)
student_score = scores[student_index]
print(f"{student_name}의 점수: {student_score}점")

# 방법 2: 한 줄로
print(f"이영희의 점수: {scores[students.index('이영희')]}점")

# 출력: 이영희의 점수: 92점
print()


##################################################
# 기초 2: 새 학생 추가하기
##################################################
print("=== 기초 2: 새 학생 추가 ===")

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
# 기초 4: 처음 3명의 성적표 출력
##################################################
print("=== 기초 4: 처음 3명 성적표 ===")

# 하나씩 출력 (for문 없이!)
print(f"{students[0]}: {scores[0]}점")
print(f"{students[1]}: {scores[1]}점")
print(f"{students[2]}: {scores[2]}점")

# 출력:
# 김철수: 85점
# 이영희: 92점
# 박민수: 78점
print()


##################################################
# 응용 1: 평균 점수 계산
##################################################
print("=== 응용 1: 평균 점수 ===")

# 방법 1: 그냥 계산
average = sum(scores) / len(scores)
print(f"평균 점수: {average}점")

# 방법 2: f-string으로 소수점 둘째자리까지
print(f"평균 점수: {sum(scores) / len(scores):.2f}점")

# 출력:
# 평균 점수: 88.0점
# 평균 점수: 88.00점
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

# 한 줄로 표현 (심화)
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

print(f"삭제 전 학생: {students}")
print(f"삭제 전 점수: {scores}")

# 박민수의 위치 찾기
student_to_remove = "박민수"
remove_index = students.index(student_to_remove)

# 이름 삭제
students.pop(remove_index)
# 점수 삭제
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
# 도전 1: 점수 정렬하여 상위 3개 출력
##################################################
print("=== 도전 1: 점수 정렬 ===")

print(f"정렬 전: {scores}")

# 내림차순 정렬 (원본이 바뀜!)
scores.sort(reverse=True)

print(f"정렬 후: {scores}")

# 상위 3개
top_3 = scores[:3]
print(f"상위 3개: {top_3}")

# 출력:
# 정렬 전: [85, 92, 88, 90, 95]
# 정렬 후: [95, 92, 90, 88, 85]
# 상위 3개: [95, 92, 90]
print()


##################################################
# 도전 2: 특정 점수 개수와 점수 차이
##################################################
print("=== 도전 2: 점수 분석 ===")

# 1) 90점이 몇 개?
count_90 = scores.count(90)
print(f"90점 개수: {count_90}개")

# 2) 최고점과 최저점의 차이
highest = max(scores)
lowest = min(scores)
difference = highest - lowest

print(f"최고점: {highest}점")
print(f"최저점: {lowest}점")
print(f"점수 차이: {difference}점")

# 한 줄로
print(f"\n점수 차이 (한 줄): {max(scores) - min(scores)}점")

# 출력:
# 90점 개수: 1개
# 최고점: 95점
# 최저점: 85점
# 점수 차이: 10점
print()


##################################################
# 최종 정리
##################################################
print("=== 최종 성적 정리 ===")
print(f"학생 명단: {students}")
print(f"점수 목록: {scores}")
print(f"총 학생 수: {len(students)}명")
print(f"평균 점수: {sum(scores) / len(scores):.2f}점")
print(f"최고점: {max(scores)}점")
print(f"최저점: {min(scores)}점")