##################################################
# 실습 1: 모듈 활용
##################################################

# 필요한 모듈 import
import random
from datetime import datetime
import json


# 실습 1-1: 랜덤 게임
print("=== 실습 1-1: 랜덤 게임 ===")

# 1부터 100까지 숫자 중 하나를 랜덤하게 선택
answer = random.randint(1, 100)
print("숫자를 맞춰보세요!")
print(f"정답: {answer}")  # 테스트용 (실제 게임에서는 보여주면 안됨!)

# 추가 예시: 여러 번 실행해보기
print("\n랜덤 숫자 5개 생성:")
for i in range(5):
    print(random.randint(1, 100), end=" ")
print("\n")


# 실습 1-2: 오늘 날짜
print("=== 실습 1-2: 오늘 날짜 ===")

# 현재 날짜와 시간 가져오기
now = datetime.now()
print(f"전체 정보: {now}")

# "2024년 01월 16일" 형식으로 출력
formatted_date = now.strftime('%Y년 %m월 %d일')
print(f"포맷팅된 날짜: {formatted_date}")

# 추가 예시: 다양한 날짜 포맷
print("\n다양한 날짜 형식:")
print(f"기본: {now.strftime('%Y-%m-%d')}")
print(f"시간 포함: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"요일 포함: {now.strftime('%Y년 %m월 %d일 (%A)')}")
print(f"12시간제: {now.strftime('%Y-%m-%d %I:%M %p')}")
print()


# 실습 1-3: D-day 계산
print("=== 실습 1-3: D-day 계산 ===")

# 현재 날짜
today = datetime.now()
print(f"오늘: {today.strftime('%Y년 %m월 %d일')}")

# 2024년 12월 31일
end_date = datetime(2024, 12, 31)
print(f"목표일: {end_date.strftime('%Y년 %m월 %d일')}")

# 날짜 차이 계산
difference = end_date - today
days_left = difference.days

print(f"남은 일수: D-{days_left}일")

# 추가 예시: 다른 날짜까지 계산
print("\n추가 예시:")
christmas = datetime(2024, 12, 25)
days_to_christmas = (christmas - today).days
print(f"크리스마스까지: D-{days_to_christmas}일")

# 생일 D-day 계산
birthday = datetime(2024, 6, 15)
if birthday > today:
    days_to_birthday = (birthday - today).days
    print(f"생일까지: D-{days_to_birthday}일")
else:
    print("생일이 이미 지났습니다!")
print()


# 실습 1-4: 데이터 변환
print("=== 실습 1-4: 데이터 변환 ===")

# 원본 딕셔너리
student = {"name": "김철수", "age": 25, "grade": "A"}
print(f"원본 딕셔너리: {student}")
print(f"타입: {type(student)}")

# 딕셔너리 → JSON 문자열로 변환
json_string = json.dumps(student, ensure_ascii=False)
print(f"\nJSON 문자열: {json_string}")
print(f"타입: {type(json_string)}")

# JSON 문자열 → 딕셔너리로 변환
student_back = json.loads(json_string)
print(f"\n다시 딕셔너리: {student_back}")
print(f"타입: {type(student_back)}")

# 같은지 확인
print(f"\n원본과 같은가? {student == student_back}")

# 추가 예시: 리스트도 가능
print("\n추가 예시: 리스트 변환")
students_list = [
    {"name": "김철수", "age": 25},
    {"name": "이영희", "age": 23}
]
json_str = json.dumps(students_list, ensure_ascii=False)
print(f"리스트 → JSON: {json_str}")

# 추가 예시: 예쁘게 출력 (indent 사용)
print("\n예쁘게 출력:")
pretty_json = json.dumps(student, ensure_ascii=False, indent=2)
print(pretty_json)
print()


# 실습 1-5: 랜덤 팀 구성
print("=== 실습 1-5: 랜덤 팀 구성 ===")

students = ["김철수", "이영희", "박민수", "최지은", "정수진"]
print(f"전체 학생: {students}")

# 랜덤하게 3명 선택
team = random.sample(students, 3)
print(f"\n선택된 팀원: {team}")

# 여러 번 실행해보기
print("\n3번 더 팀 구성:")
for i in range(3):
    team = random.sample(students, 3)
    print(f"팀 {i+1}: {team}")

# 추가 예시: 전체를 섞기
print("\n추가 예시: 전체 학생 순서 섞기")
shuffled = students.copy()  # 원본 보존
random.shuffle(shuffled)
print(f"섞인 순서: {shuffled}")
print(f"원본 유지: {students}")

# 추가 예시: 2팀으로 나누기
print("\n추가 예시: 2팀으로 나누기")
shuffled = students.copy()
random.shuffle(shuffled)
team_a = shuffled[:3]
team_b = shuffled[3:]
print(f"A팀: {team_a}")
print(f"B팀: {team_b}")
print()