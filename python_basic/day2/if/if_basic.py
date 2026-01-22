##################################################
# 기본 if 문
##################################################

# 기본 if 문
age = 20

if age >= 18:
    print("성인입니다")
    print("입장 가능합니다")

print("프로그램 종료")

# 출력:
# 성인입니다
# 입장 가능합니다
# 프로그램 종료

# 조건이 False인 경우
age = 15

if age >= 18:
    print("성인입니다")  # 실행 안 됨!
    
print("프로그램 종료")  # 이건 실행됨

# 출력:
# 프로그램 종료


##################################################
# if-else 구조
##################################################

# if-else: 조건이 True일 때와 False일 때 다르게 처리
age = 15

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")

# 출력: 미성년자입니다

# 짝수/홀수 판별
number = 7

if number % 2 == 0:
    print(f"{number}은(는) 짝수입니다")
else:
    print(f"{number}은(는) 홀수입니다")

# 출력: 7은(는) 홀수입니다

# 로그인 상태
is_logged_in = False

if is_logged_in:
    print("마이페이지로 이동")
else:
    print("로그인 페이지로 이동")

# 출력: 로그인 페이지로 이동


##################################################
# 
##################################################

# elif: 여러 조건 처리
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수: {score}, 등급: {grade}")
# 출력: 점수: 85, 등급: B

# 나이대별 분류
age = 25

if age < 13:
    category = "어린이"
elif age < 20:
    category = "청소년"
elif age < 65:
    category = "성인"
else:
    category = "노인"

print(f"{age}세 - {category}")


##################################################
# 
##################################################

# and: 모두 True여야 True
age = 25
has_license = True

if age >= 18 and has_license:
    print("운전 가능")
else:
    print("운전 불가")

# or: 하나라도 True면 True
is_student = False
is_senior = True

if is_student or is_senior:
    print("할인 대상입니다")
else:
    print("정상 가격입니다")

# not: 반대로
is_raining = False

if not is_raining:
    print("우산 필요 없음")
else:
    print("우산 필요")

# 복합 조건
age = 17
has_parent_permission = True

if (age >= 18) or (age >= 15 and has_parent_permission):
    print("영화 관람 가능")
else:
    print("관람 불가")


##################################################
# 
##################################################

# 리스트에서 검색
fruits = ["apple", "banana", "orange"]
search = "banana"

if search in fruits:
    print(f"{search}를 찾았습니다!")
else:
    print(f"{search}를 찾을 수 없습니다")

# 딕셔너리에서 Key 확인
user = {"name": "김철수", "age": 25}

if "email" in user:
    print(f"이메일: {user['email']}")
else:
    print("이메일 정보가 없습니다")

# 권한 확인
user_roles = ["user", "editor"]

if "admin" in user_roles:
    print("관리자 기능 사용 가능")
elif "editor" in user_roles:
    print("편집 기능 사용 가능")
else:
    print("읽기 전용")

# 문자열 포함 확인
email = "user@example.com"

if "@" in email and "." in email:
    print("유효한 이메일 형식")
else:
    print("잘못된 이메일 형식")