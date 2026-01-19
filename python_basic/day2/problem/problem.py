"""
요구사항:
- 학생 정보를 딕셔너리로 저장 (이름, 국어, 영어, 수학)
- 여러 학생을 리스트에 저장
- for문, if문, 리스트 컴프리헨션 활용

기초 문제 (15분)
1. 학생 정보 딕셔너리 3개 만들기
2. 학생 리스트에 추가하기
3. 모든 학생 정보 출력 (for 사용)

응용 문제 (25분)
4. 특정 학생 찾기 (이름으로 검색)
5. 각 학생의 평균 점수 계산
6. 80점 이상 학생만 필터링

도전 문제 (20분)
7. 평균 점수순으로 정렬 (힌트 제공)
8. 리스트 컴프리헨션으로 우등생 목록
   (평균 90점 이상)
9. 과목별 전체 평균 계산
"""


# 힌트
##################################################
"""
# 기초 3번: 학생 정보 출력
for student in students:
    print(f"이름: {student['name']}")
    print(f"국어: {student['korean']}")
    # ...

# 응용 4번: 학생 찾기
for student in students:
    if student['name'] == search_name:
        print("찾음!", student)
        break

# 응용 5번: 평균 계산
for student in students:
    avg = (student['korean'] + student['english'] + student['math']) / 3
    print(f"{student['name']}: {avg:.1f}점")

# 도전 8번: 우등생 목록
honor_students = [
    student['name'] 
    for student in students 
    if (student['korean'] + student['english'] + student['math']) / 3 >= 90
]
"""
##################################################