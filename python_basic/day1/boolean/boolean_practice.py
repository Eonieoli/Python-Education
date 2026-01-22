##################################################
# 연습 1: 불리언 값 비교하기
##################################################

# Boolean 변수 사용
is_student = True
is_adult = False

print(is_student)  # True
print(is_adult)    # False

# 비교 결과를 변수에 저장
age = 25
is_adult = age >= 18
print(is_adult)  # True

# 나이 비교
my_age = 17
friend_age = 20
print(my_age == friend_age)  # False
print(my_age < friend_age)   # True


##################################################
# 연습 2: 조건 조합 연습
##################################################

# 입장 가능 여부 판단
age = 20
has_ticket = True

# 18세 이상이고 티켓이 있어야 입장 가능
can_enter = age >= 18 and has_ticket
print("입장 가능:", can_enter)  # True

# 학생이거나 65세 이상이면 할인
is_student = False
age = 70
gets_discount = is_student or age >= 65
print("할인 대상:", gets_discount)  # True

# 로그인 안 한 상태
is_logged_in = False
print("로그인 필요:", not is_logged_in)  # True