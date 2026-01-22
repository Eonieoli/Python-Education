##################################################
# 집합으로 만들기
##################################################

# 집합 생성 - 중괄호 {} 사용
fruits = {"apple", "banana", "orange"}
print(fruits)  # {'banana', 'apple', 'orange'}
# 순서가 뒤죽박죽! 순서 없음!

# 빈 집합 생성
empty_set = set()       # empty_set = {} 는 빈 딕셔너리 생성
print(empty_set)

# 중복된 값을 넣어도 자동으로 하나만 남음
colors = {"red", "blue", "red", "green", "blue"}
print(colors)  # {'blue', 'green', 'red'}

# in 연산자 - 매우 빠름!
print("apple" in fruits)  # True
print("grape" in fruits)  # False


##################################################
# 집합으로 중복 제거하기
##################################################

# 중복이 있는 리스트
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(numbers)  # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# set으로 변환하면 중복 제거!
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}

# 다시 리스트로 변환
result = list(unique_numbers)
print(result)  # [1, 2, 3, 4]