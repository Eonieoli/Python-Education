##################################################
# 실습 1: 리스트 기본
##################################################

# 실습 1-1: 쇼핑 목록
shopping_list = ["우유", "계란", "빵", "과일", "고기"]

# 첫 번째와 마지막 물건
first_item = shopping_list[0]
last_item = shopping_list[-1]
print(f"첫 번째 물건: {first_item}")
print(f"마지막 물건: {last_item}")

# 총 개수
total_items = len(shopping_list)
print(f"총 {total_items}가지 물건")

# 출력:
# 첫 번째 물건: 우유
# 마지막 물건: 고기
# 총 5가지 물건


# 실습 1-2: 순위
ranks = ["금메달", "은메달", "동메달", "4위", "5위"]

# 메달권 (상위 3개)
medal_ranks = ranks[0:3]  # 또는 ranks[:3]
print(f"메달권: {medal_ranks}")

# 출력: 메달권: ['금메달', '은메달', '동메달']


# 실습 1-3: 과목 점수
scores = [85, 90, 78, 92, 88]

# 첫 번째와 마지막 과목 점수
first_score = scores[0]
last_score = scores[-1]
print(f"첫 번째 과목: {first_score}점")
print(f"마지막 과목: {last_score}점")

# 중간 3개 과목 (인덱스 1, 2, 3)
middle_scores = scores[1:4]
print(f"중간 3개 과목: {middle_scores}")

# 출력:
# 첫 번째 과목: 85점
# 마지막 과목: 88점
# 중간 3개 과목: [90, 78, 92]


##################################################
# 실습 2: 리스트 수정
##################################################

# 실습 2-1: 성적 수정
scores = [85, 90, 75, 88, 92]

# 3번째 과목(index 2) 점수를 80으로 수정
scores[2] = 80
print(f"3번째 수정 후: {scores}")

# 마지막 과목 점수를 95로 수정
scores[-1] = 95  # 또는 scores[4] = 95
print(f"마지막 수정 후: {scores}")

# 출력:
# 3번째 수정 후: [85, 90, 80, 88, 92]
# 마지막 수정 후: [85, 90, 80, 88, 95]


# 실습 2-2: 메뉴 관리
menu = ["김치찌개", "된장찌개", "순두부찌개"]

# "된장찌개"의 위치 찾기
index = menu.index("된장찌개")
print(f"된장찌개 위치: {index}")

# "청국장"으로 변경
menu[index] = "청국장"
print(f"변경 후: {menu}")

# 한 줄로 표현 (추천!)
menu = ["김치찌개", "된장찌개", "순두부찌개"]
menu[menu.index("된장찌개")] = "청국장"
print(f"변경 후: {menu}")

# 출력:
# 된장찌개 위치: 1
# 변경 후: ['김치찌개', '청국장', '순두부찌개']


# 실습 2-3: 연락처 업데이트
contacts = ["010-1111-1111", "010-2222-2222", "010-3333-3333"]

# 두 번째 연락처 변경
contacts[1] = "010-9999-9999"
print(f"두 번째 변경: {contacts}")

# 마지막 연락처 변경
contacts[-1] = "010-8888-8888"
print(f"마지막 변경: {contacts}")

# 출력:
# 두 번째 변경: ['010-1111-1111', '010-9999-9999', '010-3333-3333']
# 마지막 변경: ['010-1111-1111', '010-9999-9999', '010-8888-8888']


##################################################
# 실습 3: 리스트 메서드
##################################################

# 실습 3-1: 성적 통계
scores = [85, 90, 85, 78, 92, 85, 88]

# 85점이 몇 개인지
count_85 = scores.count(85)
print(f"85점 개수: {count_85}개")

# 가장 높은 점수와 낮은 점수
highest = max(scores)
lowest = min(scores)
print(f"최고점: {highest}점")
print(f"최저점: {lowest}점")

# 출력:
# 85점 개수: 3개
# 최고점: 92점
# 최저점: 78점


# 실습 3-2: 과일 가게
fruits = ["사과", "바나나", "오렌지", "사과", "포도"]

# 사과 개수
apple_count = fruits.count("사과")
print(f"사과 개수: {apple_count}개")

# 바나나 위치
banana_index = fruits.index("바나나")
print(f"바나나 위치: {banana_index}")

# 수박 확인
has_watermelon = "수박" in fruits
print(f"수박 있음: {has_watermelon}")

# 출력:
# 사과 개수: 2개
# 바나나 위치: 1
# 수박 있음: False


# 실습 3-3: 순위 정하기
scores = [78, 92, 85, 95, 88]

# 내림차순 정렬 (방법 1: sort)
scores.sort(reverse=True)
print(f"정렬 후: {scores}")

# 1등과 꼴찌
first_place = scores[0]
last_place = scores[-1]
print(f"1등: {first_place}점")
print(f"꼴찌: {last_place}점")

# 방법 2: sorted 사용 (원본 유지)
scores = [78, 92, 85, 95, 88]
sorted_scores = sorted(scores, reverse=True)
print(f"원본: {scores}")
print(f"정렬: {sorted_scores}")

# 출력:
# 정렬 후: [95, 92, 88, 85, 78]
# 1등: 95점
# 꼴찌: 78점


# 실습 3-4: 중복 제거
numbers = [1, 2, 3, 2, 4, 3, 5, 1]

# 각 숫자가 몇 번 나오는지
print("숫자별 개수:")
for num in numbers:
    count = numbers.count(num)
    print(f"{num}: {count}번")

# 출력:
# 숫자별 개수:
# 1: 2번
# 2: 2번
# 3: 2번
# 2: 2번
# 4: 1번
# 3: 2번
# 5: 1번
# 1: 2번

# 더 나은 방법: 중복 제거 후 카운트
numbers = [1, 2, 3, 2, 4, 3, 5, 1]
unique_numbers = list(set(numbers))  # 중복 제거
unique_numbers.sort()  # 정렬

print("\n숫자별 개수 (중복 제거):")
for num in unique_numbers:
    count = numbers.count(num)
    print(f"{num}: {count}번")

# 출력:
# 숫자별 개수 (중복 제거):
# 1: 2번
# 2: 2번
# 3: 2번
# 4: 1번
# 5: 1번


##################################################
# 실습 4: 내장 함수
##################################################

# 실습 4-1: 리스트의 평균, 최고점, 최저점 구하기
scores = [75, 88, 92, 65, 81, 95, 70]

# 평균
total = sum(scores)
count = len(scores)
average = total / count
print(f"총점: {total}점")
print(f"평균: {average}점")

# 최고점과 최저점
highest = max(scores)
lowest = min(scores)
print(f"최고점: {highest}점")
print(f"최저점: {lowest}점")

# 한 번에 출력
print(f"\n=== 성적 통계 ===")
print(f"총점: {sum(scores)}점")
print(f"평균: {sum(scores) / len(scores):.2f}점")
print(f"최고점: {max(scores)}점")
print(f"최저점: {min(scores)}점")

# 출력:
# 총점: 566점
# 평균: 80.85714285714286점
# 최고점: 95점
# 최저점: 65점
#
# === 성적 통계 ===
# 총점: 566점
# 평균: 80.86점
# 최고점: 95점
# 최저점: 65점


# 실습 4-2: 최댓값과 최솟값 차이 구하기
prices = [15000, 8900, 32000, 12500, 45000]

# 최댓값과 최솟값
max_price = max(prices)
min_price = min(prices)
difference = max_price - min_price

print(f"가장 비싼 상품: {max_price:,}원")
print(f"가장 싼 상품: {min_price:,}원")
print(f"가격 차이: {difference:,}원")

# 한 줄로
print(f"\n가격 차이: {max(prices) - min(prices):,}원")

# 출력:
# 가장 비싼 상품: 45,000원
# 가장 싼 상품: 8,900원
# 가격 차이: 36,100원