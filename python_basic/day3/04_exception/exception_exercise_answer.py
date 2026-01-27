##################################################
# 실습 1: try-except 기본
##################################################

# 실습 1-1: 안전한 계산기
def calculate(a: float, b: float, operator: str) -> dict:
    """
    안전한 계산 함수
    
    Args:
        a, b: 피연산자
        operator: 연산자 (+, -, *, /)
    
    Returns:
        {"success": True/False, "result": 결과 또는 "error": 에러메시지}
    """
    try:
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b  # 0으로 나누면 ZeroDivisionError 발생
        else:
            return {
                "success": False,
                "error": f"잘못된 연산자: {operator}"
            }
        
        return {
            "success": True,
            "result": result
        }
    
    except ZeroDivisionError:
        return {
            "success": False,
            "error": "0으로 나눌 수 없습니다"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"계산 오류: {str(e)}"
        }

# 테스트
print("=== 실습 1-1: 안전한 계산기 ===")

# 정상 케이스
result = calculate(10, 5, "+")
print(f"10 + 5 = {result}")  # {"success": True, "result": 15}

result = calculate(10, 3, "/")
print(f"10 / 3 = {result}")  # {"success": True, "result": 3.333...}

# 에러 케이스
result = calculate(10, 0, "/")
print(f"10 / 0 = {result}")  # {"success": False, "error": "0으로 나눌 수 없습니다"}

result = calculate(10, 5, "%")
print(f"10 % 5 = {result}")  # {"success": False, "error": "잘못된 연산자: %"}

# 사용 예시
print("\n계산기 사용:")
operations = [
    (10, 5, "+"),
    (20, 4, "*"),
    (100, 0, "/"),  # 에러!
    (50, 10, "-"),
    (10, 2, "^")    # 에러!
]

for a, b, op in operations:
    result = calculate(a, b, op)
    if result["success"]:
        print(f"  {a} {op} {b} = {result['result']}")
    else:
        print(f"  {a} {op} {b} → 오류: {result['error']}")
print()


# 실습 1-2: 사용자 검색
def find_user(users: list, user_id: int) -> dict:
    """
    사용자 검색 함수
    
    Args:
        users: 사용자 리스트
        user_id: 찾을 사용자 ID
    
    Returns:
        {"found": True/False, "user": {...} 또는 "message": "..."}
    """
    try:
        for user in users:
            if user["id"] == user_id:
                return {
                    "found": True,
                    "user": user
                }
        
        # 찾지 못한 경우
        return {
            "found": False,
            "message": "사용자 없음"
        }
    
    except KeyError:
        return {
            "found": False,
            "message": "잘못된 사용자 데이터 형식"
        }
    except Exception as e:
        return {
            "found": False,
            "message": f"검색 오류: {str(e)}"
        }

# 테스트
print("=== 실습 1-2: 사용자 검색 ===")

users = [
    {"id": 1, "name": "김철수", "age": 25},
    {"id": 2, "name": "이영희", "age": 23},
    {"id": 3, "name": "박민수", "age": 28}
]

# 찾는 경우
result = find_user(users, 2)
print(f"ID 2 검색: {result}")
# {"found": True, "user": {"id": 2, "name": "이영희", "age": 23}}

if result["found"]:
    print(f"  → 찾음: {result['user']['name']}")

# 못 찾는 경우
result = find_user(users, 999)
print(f"\nID 999 검색: {result}")
# {"found": False, "message": "사용자 없음"}

if not result["found"]:
    print(f"  → {result['message']}")

# 여러 ID 검색
print("\n여러 사용자 검색:")
search_ids = [1, 5, 3, 10, 2]
for uid in search_ids:
    result = find_user(users, uid)
    if result["found"]:
        print(f"  ID {uid}: {result['user']['name']}")
    else:
        print(f"  ID {uid}: {result['message']}")
print()


# 실습 1-3: 안전한 리스트 접근
def get_nth_item(items: list, n: int, default="없음") -> any:
    """
    안전한 n번째 항목 접근
    
    Args:
        items: 리스트
        n: 인덱스
        default: 에러 시 반환할 기본값
    
    Returns:
        n번째 항목 또는 default
    """
    try:
        return items[n]
    except IndexError:
        return default
    except TypeError:
        return default
    except Exception as e:
        return default

# 테스트
print("=== 실습 1-3: 안전한 리스트 접근 ===")

fruits = ["사과", "바나나", "오렌지"]

# 정상 접근
print(f"0번째: {get_nth_item(fruits, 0)}")  # 사과
print(f"2번째: {get_nth_item(fruits, 2)}")  # 오렌지

# 범위 초과
print(f"5번째: {get_nth_item(fruits, 5)}")  # 없음

# 커스텀 기본값
print(f"10번째: {get_nth_item(fruits, 10, '과일 없음')}")  # 과일 없음

# 음수 인덱스 (Python에서는 에러 아님!)
print(f"-1번째: {get_nth_item(fruits, -1)}")  # 오렌지

# 다양한 케이스
print("\n여러 인덱스 접근:")
numbers = [10, 20, 30, 40, 50]
indices = [0, 2, 5, 10, -1]

for i in indices:
    value = get_nth_item(numbers, i, "범위초과")
    print(f"  인덱스 {i}: {value}")
print()


# 실습 1-4: 데이터 검증
def validate_age(age_str: str) -> dict:
    """
    나이 검증 함수
    
    Args:
        age_str: 나이 문자열
    
    Returns:
        {"valid": True/False, "age": 숫자 또는 "message": "에러"}
    """
    try:
        # 문자열을 정수로 변환
        age = int(age_str)
        
        # 범위 체크
        if age < 0 or age > 150:
            return {
                "valid": False,
                "message": "나이는 0~150 사이여야 합니다"
            }
        
        return {
            "valid": True,
            "age": age
        }
    
    except ValueError:
        return {
            "valid": False,
            "message": "숫자가 아닙니다"
        }
    except Exception as e:
        return {
            "valid": False,
            "message": f"검증 오류: {str(e)}"
        }

# 테스트
print("=== 실습 1-4: 데이터 검증 ===")

# 정상 케이스
test_ages = ["25", "30", "0", "150"]
print("정상 케이스:")
for age_str in test_ages:
    result = validate_age(age_str)
    print(f"  '{age_str}' → {result}")

# 에러 케이스
print("\n에러 케이스:")
error_ages = ["abc", "-5", "200", "25.5", ""]
for age_str in error_ages:
    result = validate_age(age_str)
    print(f"  '{age_str}' → {result}")

# 실전 사용
print("\n회원가입 시뮬레이션:")
user_inputs = [
    ("김철수", "25"),
    ("이영희", "abc"),
    ("박민수", "200"),
    ("최지은", "30")
]

for name, age_str in user_inputs:
    result = validate_age(age_str)
    if result["valid"]:
        print(f"  {name}({result['age']}세) - 가입 성공!")
    else:
        print(f"  {name} - 가입 실패: {result['message']}")
print()


##################################################
# 실습 2: raise
##################################################

# 실습 2-1: 점수 검증 함수
def validate_score(score: int) -> int:
    """
    점수 검증 함수 (0~100)
    
    Args:
        score: 점수
    
    Returns:
        검증된 점수
    
    Raises:
        ValueError: 점수가 범위를 벗어난 경우
    """
    if score < 0 or score > 100:
        raise ValueError(f"점수는 0~100 사이여야 합니다. 입력값: {score}")
    
    return score

# 테스트
print("=== 실습 2-1: 점수 검증 ===")

# 정상 케이스
try:
    result = validate_score(85)
    print(f"점수 85: 검증 성공 → {result}")
except ValueError as e:
    print(f"점수 85: 검증 실패 → {e}")

# 에러 케이스
try:
    result = validate_score(150)
    print(f"점수 150: 검증 성공 → {result}")
except ValueError as e:
    print(f"점수 150: 검증 실패 → {e}")

try:
    result = validate_score(-10)
    print(f"점수 -10: 검증 성공 → {result}")
except ValueError as e:
    print(f"점수 -10: 검증 실패 → {e}")

# 여러 점수 검증
print("\n여러 점수 검증:")
scores = [85, 90, 150, -5, 100, 0, 101]

for score in scores:
    try:
        validated = validate_score(score)
        print(f"  {score:4d} → ✓ 유효")
    except ValueError as e:
        print(f"  {score:4d} → ✗ {e}")
print()


# 실습 2-2: 비밀번호 검증 함수
def validate_password(password: str) -> str:
    """
    비밀번호 검증 함수 (6자 이상)
    
    Args:
        password: 비밀번호
    
    Returns:
        검증된 비밀번호
    
    Raises:
        ValueError: 비밀번호가 6자 미만인 경우
    """
    if len(password) < 6:
        raise ValueError(f"비밀번호는 6자 이상이어야 합니다. 현재 길이: {len(password)}")
    
    return password

# 테스트
print("=== 실습 2-2: 비밀번호 검증 ===")

# 정상 케이스
try:
    result = validate_password("abc12345")
    print(f"'abc12345': 검증 성공 ✓")
except ValueError as e:
    print(f"'abc12345': 검증 실패 → {e}")

# 에러 케이스
try:
    result = validate_password("abc")
    print(f"'abc': 검증 성공 ✓")
except ValueError as e:
    print(f"'abc': 검증 실패 → {e}")

# 여러 비밀번호 검증
print("\n여러 비밀번호 검증:")
passwords = ["password123", "abc", "test1234", "12", "secure_pw", ""]

for pw in passwords:
    try:
        validated = validate_password(pw)
        print(f"  '{pw:15s}' → ✓ 유효 (길이: {len(pw)})")
    except ValueError as e:
        print(f"  '{pw:15s}' → ✗ 무효")
print()


# 실습 2-3: 사용자 찾기 함수
def find_user_strict(users: dict, user_id: int) -> dict:
    """
    사용자 찾기 함수 (엄격한 버전)
    
    Args:
        users: 사용자 딕셔너리 {id: user_info}
        user_id: 사용자 ID
    
    Returns:
        사용자 정보
    
    Raises:
        KeyError: 사용자를 찾을 수 없는 경우
    """
    if user_id not in users:
        raise KeyError(f"사용자 ID {user_id}를 찾을 수 없습니다")
    
    return users[user_id]

# 테스트
print("=== 실습 2-3: 사용자 찾기 (raise 버전) ===")

users = {
    1: {"name": "김철수", "email": "kim@example.com"},
    2: {"name": "이영희", "email": "lee@example.com"},
    3: {"name": "박민수", "email": "park@example.com"}
}

# 정상 케이스
print("정상 케이스:")
try:
    user = find_user_strict(users, 1)
    print(f"  ID 1 → 찾음: {user}")
except KeyError as e:
    print(f"  ID 1 → 오류: {e}")

# 에러 케이스 (try-except로 처리)
print("\n에러 케이스 (try-except 처리):")
try:
    user = find_user_strict(users, 999)
    print(f"  ID 999 → 찾음: {user}")
except KeyError as e:
    print(f"  ID 999 → 오류: {e}")

# 여러 사용자 검색
print("\n여러 사용자 검색:")
search_ids = [1, 5, 2, 10, 3]

for uid in search_ids:
    try:
        user = find_user_strict(users, uid)
        print(f"  ID {uid}: {user['name']} ({user['email']})")
    except KeyError as e:
        print(f"  ID {uid}: 사용자 없음")
print()