##################################################
# 실습 1: 문자열 기본
##################################################

# 실습 1-1: 명함 만들기
company = "테크컴퍼니"
name = "김철수"
position = "개발자"

# 방법 1: + 연산자 사용
line = "=" * 18
print(line)
print(company)
print(name + " " + position)
print(line)

# 방법 2: f-string 사용 (추천!)
print("=" * 18)
print(f"{company}")
print(f"{name} {position}")
print("=" * 18)

# 출력:
# ==================
# 테크컴퍼니
# 김철수 개발자
# ==================


# 실습 1-2: 영수증 상단
store_name = "파이썬마트"
star_line = "*" * 20

print(star_line)
print(store_name)
print(star_line)

# 출력:
# ********************
# 파이썬마트
# ********************


##################################################
# 실습 2: 문자열 인덱싱/슬라이싱
##################################################

# 실습 2-1: 주민등록번호 나누기
jumin = "901015-1234567"

# 방법 1: 슬라이싱으로 직접 추출
birth_date = jumin[0:6]      # 또는 jumin[:6]
back_number = jumin[7:14]     # 또는 jumin[7:]
print(f"생년월일: {birth_date}")
print(f"뒷자리: {back_number}")

# 방법 2: split 메서드 사용 (더 간편!)
parts = jumin.split("-")
print(f"생년월일: {parts[0]}")
print(f"뒷자리: {parts[1]}")

# 출력:
# 생년월일: 901015
# 뒷자리: 1234567


# 실습 2-2: 파일명과 확장자 분리
filename = "document.pdf"

# 방법 1: 슬라이싱 (점의 위치가 6)
name_part = filename[0:8]     # 또는 filename[:8]
extension = filename[9:12]     # 또는 filename[9:]
print(f"파일명: {name_part}")
print(f"확장자: {extension}")

# 방법 2: split 메서드 사용 (추천!)
parts = filename.split(".")
print(f"파일명: {parts[0]}")
print(f"확장자: {parts[1]}")

# 출력:
# 파일명: document
# 확장자: pdf


# 실습 2-3: 전화번호 포맷팅
phone = "01012345678"

# 슬라이싱으로 나누기
part1 = phone[0:3]      # "010"
part2 = phone[3:7]      # "1234"
part3 = phone[7:11]     # "5678"

# - 로 연결
formatted = part1 + "-" + part2 + "-" + part3
print(formatted)

# f-string으로 더 깔끔하게
formatted = f"{phone[0:3]}-{phone[3:7]}-{phone[7:11]}"
print(formatted)

# 출력: 010-1234-5678


# 실습 2-4: 이름 첫 글자
name = "김철수"

# 슬라이싱
last_name = name[0]       # 또는 name[0:1]
first_name = name[1:3]    # 또는 name[1:]

print(f"성: {last_name}")
print(f"이름: {first_name}")

# 출력:
# 성: 김
# 이름: 철수


##################################################
# 실습 3: 문자열 처리
##################################################

# 실습 3-1: 이메일 정제
email = "  USER@EXAMPLE.COM  "

# 단계별 처리
cleaned = email.strip()        # 공백 제거
cleaned = cleaned.lower()      # 소문자 변환
print(cleaned)

# 한 줄로 (메서드 체이닝)
cleaned = email.strip().lower()
print(cleaned)

# 출력: user@example.com


# 실습 3-2: CSV 데이터 파싱
data = "김철수,25,서울,개발자"

# split으로 분리
items = data.split(",")

# 각 항목 출력
print(f"이름: {items[0]}")
print(f"나이: {items[1]}")
print(f"지역: {items[2]}")
print(f"직업: {items[3]}")

# 출력:
# 이름: 김철수
# 나이: 25
# 지역: 서울
# 직업: 개발자


# 실습 3-3: 비밀번호 검증
password = "mypassword123"

# 길이 확인
length_ok = len(password) >= 8
print(f"길이 8자 이상: {length_ok}")

# 숫자 포함 확인 (여러 방법)
has_number = "123" in password
print(f"숫자 포함: {has_number}")

# 더 정확한 방법 (어떤 숫자든 포함하는지)
has_digit = any(char.isdigit() for char in password)
print(f"숫자 포함 (정확): {has_digit}")

# 출력:
# 길이 8자 이상: True
# 숫자 포함: True


# 실습 3-4: URL 슬러그 생성
title = "Python Programming Tutorial"

# 단계별 처리
slug = title.lower()              # 소문자로
slug = slug.replace(" ", "-")     # 공백을 -로
print(slug)

# 한 줄로
slug = title.lower().replace(" ", "-")
print(slug)

# 출력: python-programming-tutorial