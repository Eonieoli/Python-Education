##################################################
# 연습 1: random 모듈 활용
##################################################

import random

# randint: 정수 난수
dice = random.randint(1, 6)
print(f"주사위: {dice}")

# choice: 리스트에서 랜덤 선택
menu = ["김치찌개", "된장찌개", "순두부"]
today_menu = random.choice(menu)
print(f"오늘의 메뉴: {today_menu}")

# sample: 여러 개 선택 (중복 없이)
numbers = list(range(1, 46))  # 1~45
lotto = random.sample(numbers, 6)
lotto.sort()
print(f"로또 번호: {lotto}")

# shuffle: 리스트 섞기
cards = ["◆A", "◆2", "♥A", "♥2", "♣A", "♣2", "♠A", "♠2"]
random.shuffle(cards)
print(f"섞인 카드: {cards}")

# random: 0.0~1.0 실수 난수
probability = random.random()
print(f"확률: {probability:.2f}")

if probability > 0.5:
    print("성공!")
else:
    print("실패!")


##################################################
# 연습 2: datetime 모듈 활용
##################################################

from datetime import datetime, timedelta

# 현재 시간
now = datetime.now()
print(f"현재: {now}")
print(f"포맷: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 날짜 부분만
print(f"년: {now.year}")
print(f"월: {now.month}")
print(f"일: {now.day}")
print(f"시: {now.hour}")

# 날짜 계산
tomorrow = now + timedelta(days=1)
print(f"내일: {tomorrow.strftime('%Y-%m-%d')}")

next_week = now + timedelta(weeks=1)
print(f"다음주: {next_week.strftime('%Y-%m-%d')}")

# 시간 차이
christmas = datetime(2026, 12, 25)
diff = christmas - now
print(f"크리스마스까지: {diff.days}일")

# 특정 날짜 생성
meeting = datetime(2026, 1, 20, 14, 30)
print(f"회의: {meeting.strftime('%Y년 %m월 %d일 %H시 %M분')}")


##################################################
# 연습 3: json 모듈 활용
##################################################

import json

# Python 딕셔너리 → JSON 문자열
user = {
    "name": "김철수",
    "age": 25,
    "email": "kim@test.com"
}

json_str = json.dumps(user, ensure_ascii=False)
print(json_str)
# {"name": "김철수", "age": 25, "email": "kim@test.com"}
print(type(json_str))  # <class 'str'>

# JSON 문자열 → Python 딕셔너리
json_data = '{"name": "이영희", "age": 30}'
user_dict = json.loads(json_data)
print(user_dict)
print(type(user_dict))  # <class 'dict'>
print(user_dict["name"])  # 이영희

# 리스트도 가능
users = [
    {"name": "김철수", "age": 25},
    {"name": "이영희", "age": 30}
]

json_str = json.dumps(users, ensure_ascii=False, indent=2)
print(json_str)

# 파일 저장/읽기 (개념만)
# with open('data.json', 'w') as f:
#     json.dump(user, f)