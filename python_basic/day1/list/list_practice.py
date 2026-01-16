# 빈 리스트
empty_list = []

# 숫자 리스트
numbers = [1, 2, 3, 4, 5]

# 문자열 리스트 (가장 많이 사용!)
fruits = ["apple", "banana", "orange"]
students = ["김철수", "이영희", "박민수"]

# 혼합 (권장하지 않음)
mixed = [1, "hello", 3.14, True]

print(fruits)  # ['apple', 'banana', 'orange']
print(len(students))  # 3


# 리스트 인덱싱
fruits = ["apple", "banana", "orange", "grape"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # grape (마지막)

# 리스트 슬라이싱
print(fruits[0:2])   # ['apple', 'banana']
print(fruits[1:])    # ['banana', 'orange', 'grape']
print(fruits[:3])    # ['apple', 'banana', 'orange']

# 실용 예제
students = ["김철수", "이영희", "박민수", "최지은", "정수진"]
top_3 = students[:3]  # 상위 3명
print(top_3)  # ['김철수', '이영희', '박민수']


# 할 일 목록 관리
todo_list = []

# 할 일 추가
todo_list.append("Python 공부")
todo_list.append("운동하기")
todo_list.append("저녁 약속")

print("현재 할 일:", todo_list)
# ['Python 공부', '운동하기', '저녁 약속']

# 급한 일 맨 앞에 추가
todo_list.insert(0, "긴급 회의")
print("업데이트:", todo_list)
# ['긴급 회의', 'Python 공부', '운동하기', '저녁 약속']

# 오늘 할 일 개수
print(f"할 일 {len(todo_list)}개")


# 할 일 목록 관리 계속
todo_list = ["회의", "Python 공부", "운동", "저녁 약속"]

# 완료한 일 삭제
todo_list.remove("회의")
print(todo_list)  # ['Python 공부', '운동', '저녁 약속']

# 마지막 할 일 완료
last_todo = todo_list.pop()
print(f"완료: {last_todo}")  # 완료: 저녁 약속
print("남은 할 일:", todo_list)  # ['Python 공부', '운동']

# 특정 위치 삭제
del todo_list[0]
print(todo_list)  # ['운동']

# 전부 완료!
todo_list.clear()
print("모든 할 일 완료!", todo_list)  # []


# 할 일 목록 수정
todo_list = ["영어 공부", "운동", "장보기"]

print("원래 계획:", todo_list)

# 운동 계획 변경
todo_list[1] = "요가 수업"
print("수정 1:", todo_list)

# 여러 개 변경
todo_list[0:2] = ["중국어 공부", "수영"]
print("수정 2:", todo_list)

# 특정 할 일 찾아서 수정
if "장보기" in todo_list:
    index = todo_list.index("장보기")
    todo_list[index] = "온라인 주문"
    
print("최종:", todo_list)


# 점수 정렬
scores = [85, 92, 78, 95, 88]
print("원본:", scores)

# 오름차순
scores.sort()
print("오름차순:", scores)  # [78, 85, 88, 92, 95]

# 내림차순 (높은 점수부터)
scores.sort(reverse=True)
print("내림차순:", scores)  # [95, 92, 88, 85, 78]

# 학생 이름 정렬
students = ["김철수", "이영희", "박민수", "최지은"]
students.sort()
print("가나다순:", students)
# ['김철수', '박민수', '이영희', '최지은']

# 역순으로
students.reverse()
print("역순:", students)


# 연락처 검색
contacts = [
    "김철수:010-1234-5678",
    "이영희:010-2345-6789",
    "박민수:010-3456-7890"
]

# 검색어
search = "이영희"

# 검색 실행
found = False
for contact in contacts:
    if search in contact:
        print(f"찾음: {contact}")
        found = True
        break

if not found:
    print("검색 결과 없음")

# 간단한 버전
print("영희" in str(contacts))  # True