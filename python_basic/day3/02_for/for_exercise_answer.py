##################################################
# 실습 1: for 문 기본
##################################################

# 실습 1-1: 이름 출력
students = ["김철수", "이영희", "박민수"]
# 모든 학생 이름을 "학생: 김철수" 형식으로 출력
for student in students:
    print(f"학생: {student}")
print()

# 실습 1-2: 점수 합계
scores = [85, 90, 78, 92, 88]
# 모든 점수의 합계를 구하세요
total = 0
for score in scores:
    total = total + score  # 또는 total += score

print(f"점수 합계: {total}")
print(f"평균: {total / len(scores)}")
print()

# 실습 1-3: 양수만 출력
numbers = [-5, 3, -2, 8, -1, 6]
# 양수만 출력하세요 (if문 활용)
print("양수만 출력:")
for number in numbers:
    if number > 0:
        print(number)
print()

# 실습 1-4: 문자열 대문자 변환
words = ["hello", "world", "python"]
# 각 단어를 대문자로 변환해서 출력
for word in words:
    print(word.upper())
print()


##################################################
# 실습 2: 딕셔너리 순회
##################################################

# 실습 2-1: 상품 정보 출력
product = {"name": "노트북", "price": 1500000, "stock": 10}
# items()를 사용해서 "속성: 값" 형식으로 모두 출력
for key, value in product.items():
    print(f"{key}: {value}")
print()

# 실습 2-2: 총 재고 수량
inventory = {
    "노트북": 10,
    "마우스": 50,
    "키보드": 25,
    "모니터": 15
}
# 모든 재고 수량의 합계 구하기
total_stock = 0
for product, stock in inventory.items():
    total_stock += stock

print(f"총 재고 수량: {total_stock}개")
print()

# 실습 2-3: 학생 목록 처리
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78}
]
# 각 학생의 이름과 점수를 "김철수: 85점" 형식으로 출력
# 평균 점수도 계산해서 출력
total_score = 0
for student in students:
    print(f"{student['name']}: {student['score']}점")
    total_score += student["score"]

average = total_score / len(students)
print(f"평균 점수: {average:.2f}점")
print()

# 실습 2-4: 메뉴 필터링
menu = [
    {"name": "아메리카노", "price": 4000},
    {"name": "라떼", "price": 4500},
    {"name": "케이크", "price": 5500}
]
# 가격이 5000원 미만인 메뉴만 출력
print("5000원 미만 메뉴:")
for item in menu:
    if item["price"] < 5000:
        print(f"{item['name']}: {item['price']}원")
print()


##################################################
# 실습 3: range 활용
##################################################

# 실습 3-1: 1부터 100까지 합
# range(1, 101)을 사용해서 1+2+3+...+100 계산
total = 0
for i in range(1, 101):
    total += i

print(f"1부터 100까지의 합: {total}")
print()

# 실습 3-2: 5의 배수 출력
# 1부터 50까지 중에서 5의 배수만 출력
print("5의 배수:")
for i in range(5, 51, 5):
    print(i, end=" ")
print()
print()

# 실습 3-3: 구구단 (7단)
print("=== 7단 ===")
for i in range(1, 10):
    result = 7 * i
    print(f"7 x {i} = {result}")
print()

# 실습 3-4: 번호 매기기
students = ["김철수", "이영희", "박민수", "최지은"]
# enumerate를 사용해서 "1. 김철수" 형식으로 출력
for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")
print()

# 실습 3-5: 역순 출력
numbers = [10, 20, 30, 40, 50]
# 리스트를 거꾸로 출력
print("역순 출력:")
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])
print()


##################################################
# 실습 4: 중첩 for 문
##################################################

# 실습 4-1: 숫자 표 만들기
# 1부터 9까지의 3×3 표를 출력하세요
print("3x3 숫자 표:")
num = 1
for row in range(3):
    for col in range(3):
        print(num, end=" ")
        num += 1
    print()  # 줄바꿈
print()

# 실습 4-2: 모든 두 자리 숫자 조합
# 1~3과 1~3의 모든 조합을 만들어 리스트에 저장
combinations = []
for i in range(1, 4):
    for j in range(1, 4):
        combinations.append((i, j))

print("모든 조합:", combinations)
print()


##################################################
# 실습 5: 반복 제어
##################################################

# 실습 5-1: 첫 번째 양수 찾기
numbers = [-5, -2, 0, 3, -1, 8]
# 첫 번째 양수를 찾으면 출력하고 반복 종료 (break 사용)
for number in numbers:
    if number > 0:
        print(f"첫 번째 양수: {number}")
        break
print()

# 실습 5-2: 음수 제외하고 출력
numbers = [5, -2, 8, -1, 3, -7, 10]
# 음수는 건너뛰고 양수만 출력 (continue 사용)
print("양수만 출력:")
for number in numbers:
    if number < 0:
        continue
    print(number, end=" ")
print()
print()

# 실습 5-3: 특정 상품 찾기
products = [
    {"name": "노트북", "price": 1500000},
    {"name": "마우스", "price": 30000},
    {"name": "키보드", "price": 80000}
]
# "마우스"를 찾아서 가격 출력하고 종료
# 못 찾으면 "상품 없음" 출력 (for-else 사용)
for product in products:
    if product["name"] == "마우스":
        print(f"마우스 가격: {product['price']}원")
        break
else:
    print("상품 없음")
print()

# 실습 5-4: 조건부 합계
scores = [85, 45, 92, 30, 78, 95]
# 60점 이상인 점수만 합계 구하기
# 60점 미만은 continue로 건너뛰기
total = 0
count = 0
for score in scores:
    if score < 60:
        continue
    total += score
    count += 1

print(f"60점 이상 점수 합계: {total}")
print(f"60점 이상 개수: {count}")
if count > 0:
    print(f"평균: {total / count:.2f}점")