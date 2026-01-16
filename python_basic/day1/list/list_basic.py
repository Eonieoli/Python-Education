# append: 맨 뒤에 추가
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# insert: 특정 위치에 추가
fruits.insert(1, "grape")  # 1번 위치에
print(fruits)  # ['apple', 'grape', 'banana', 'orange']

# 리스트 합치기 (+)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# extend: 여러 개 추가
fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])
print(fruits)  # ['apple', 'banana', 'orange', 'grape']


# remove: 값으로 삭제 (첫 번째 것만)
fruits = ["apple", "banana", "orange", "banana"]
fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'banana']

# pop: 인덱스로 삭제 (삭제된 값 반환)
fruits = ["apple", "banana", "orange"]
removed = fruits.pop(1)  # 1번 인덱스 삭제
print(removed)  # banana
print(fruits)   # ['apple', 'orange']

# pop(): 마지막 요소 삭제
last = fruits.pop()
print(last)    # orange
print(fruits)  # ['apple']

# del: 인덱스로 삭제
fruits = ["apple", "banana", "orange"]
del fruits[0]
print(fruits)  # ['banana', 'orange']

# clear: 전체 삭제
fruits.clear()
print(fruits)  # []


# 인덱스로 직접 수정
fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits)  # ['apple', 'grape', 'orange']

# 여러 개 동시 수정 (슬라이싱)
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]
print(numbers)  # [1, 20, 30, 4, 5]

# 실용 예제: 할 일 수정
todo_list = ["Python 공부", "운동", "저녁 약속"]
todo_list[2] = "친구 만나기"  # 저녁 약속 변경
print(todo_list)  # ['Python 공부', '운동', '친구 만나기']


# sort: 정렬 (원본 변경)
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]

# 내림차순 정렬
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 2, 1]

# 문자열 정렬
names = ["철수", "영희", "가영", "민수"]
names.sort()
print(names)  # ['가영', '민수', '영희', '철수']

# reverse: 뒤집기
fruits = ["apple", "banana", "orange"]
fruits.reverse()
print(fruits)  # ['orange', 'banana', 'apple']

# sorted: 새 리스트 반환 (원본 유지)
numbers = [5, 2, 8]
sorted_numbers = sorted(numbers)
print(numbers)         # [5, 2, 8] (원본 유지)
print(sorted_numbers)  # [2, 5, 8] (정렬된 새 리스트)


# count: 개수 세기
numbers = [1, 2, 3, 2, 4, 2, 5]
count_2 = numbers.count(2)
print(count_2)  # 3

# index: 위치 찾기
fruits = ["apple", "banana", "orange"]
position = fruits.index("banana")
print(position)  # 1

# in 연산자: 포함 여부 확인
print("banana" in fruits)  # True
print("grape" in fruits)   # False

# 실용 예제: 검색 기능
students = ["김철수", "이영희", "박민수"]
search_name = "이영희"

if search_name in students:
    print(f"{search_name}을(를) 찾았습니다!")
    index = students.index(search_name)
    print(f"위치: {index + 1}번째")
else:
    print("찾을 수 없습니다.")