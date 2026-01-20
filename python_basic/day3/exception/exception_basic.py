# 예외 예시 1: ZeroDivisionError
result = 10 / 0
# ZeroDivisionError: division by zero
# 프로그램 종료!

# 예외 예시 2: ValueError
number = int("abc")
# ValueError: invalid literal for int()
# 프로그램 종료!

# 예외 예시 3: KeyError
user = {"name": "김철수"}
age = user["age"]
# KeyError: 'age'
# 프로그램 종료!

# 예외가 발생하면 그 줄에서 멈추고 에러 메시지 출력!


# 예외 처리 없이 (프로그램 종료)
result = 10 / 0  # ❌ 여기서 프로그램 멈춤
print("이 줄은 실행 안 됨")

# try-except 사용 (프로그램 계속 실행)
try:
    result = 10 / 0
    print("나눗셈 성공")  # 이 줄은 실행 안 됨
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")  # 이 줄 실행!

print("프로그램 계속 실행됨")  # ✅ 이 줄도 실행됨!

# 출력:
# 0으로 나눌 수 없습니다
# 프로그램 계속 실행됨


# 여러 종류의 예외 처리
user_input = input("숫자를 입력하세요: ")

try:
    number = int(user_input)  # ValueError 가능
    result = 100 / number      # ZeroDivisionError 가능
    print(f"결과: {result}")
    
except ValueError:
    print("숫자를 입력해주세요!")
    
except ZeroDivisionError:
    print("0이 아닌 숫자를 입력해주세요!")

# 입력: "abc" → "숫자를 입력해주세요!"
# 입력: "0"   → "0이 아닌 숫자를 입력해주세요!"
# 입력: "5"   → "결과: 20.0"


# as 키워드로 예외 객체 받기
data = {"name": "김철수", "age": 25}

try:
    email = data["email"]  # KeyError 발생
    
except KeyError as e:
    print(f"에러 발생: {e}")
    print(f"'{e}' 키가 존재하지 않습니다")

# 출력:
# 에러 발생: 'email'
# 'email' 키가 존재하지 않습니다

# 다른 예시
try:
    number = int("hello")
except ValueError as e:
    print(f"변환 실패: {e}")


# raise로 예외 발생시키기
def validate_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다")
    if age > 150:
        raise ValueError("나이가 너무 많습니다")
    return age

# 정상 케이스
result = validate_age(25)
print(f"검증 성공: {result}세")  # 검증 성공: 25세

# 예외 발생 케이스
result = validate_age(-5)  # ❌ ValueError 발생!
# ValueError: 나이는 0 이상이어야 합니다
print("이 줄은 실행 안 됨")


# 방법 1: try 블록에 모두 넣기
try:
    result = 10 / 2
    print("계산 성공!")  # 예외 없으면 실행
    print(f"결과: {result}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")

# 방법 2: else 블록 활용 (더 명확!)
try:
    result = 10 / 2  # 시도하는 부분만!
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
else:
    # 성공했을 때만 실행
    print("계산 성공!")
    print(f"결과: {result}")

# 왜 else가 좋은가?
# 1. 의도가 명확함 (시도 vs 성공 후 처리)
# 2. try 블록은 짧게! (에러 발생 가능한 부분만)
# 3. else 블록에서 추가 에러 발생 시 catch 안 됨


# finally 사용 예시
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        print(content)
        return content
        
    except FileNotFoundError:
        print(f"파일 {filename}을 찾을 수 없습니다")
        
    finally:
        if file:
            file.close()
            print("파일을 닫았습니다")

# 파일이 있는 경우
read_file("test.txt")
# 출력:
# (파일 내용)
# 파일을 닫았습니다

# 파일이 없는 경우
read_file("없는파일.txt")
# 출력:
# 파일 없는파일.txt을 찾을 수 없습니다
# 파일을 닫았습니다  ← finally는 실행됨!


# 완전한 예외 처리 구조
def divide_safely(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        return None
    except TypeError:
        print("숫자만 입력 가능합니다!")
        return None
    else:
        # 예외가 없을 때만 실행
        print("계산 성공!")
        return result
    finally:
        # 항상 실행 (에러 여부 무관)
        print("함수 종료")

print(divide_safely(10, 2))
# 계산 성공!
# 함수 종료
# 5.0

print(divide_safely(10, 0))
# 0으로 나눌 수 없습니다!
# 함수 종료
# None