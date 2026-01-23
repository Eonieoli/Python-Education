##################################################
# 실습 1: try-except 기본
##################################################

# 실습 1-1: 안전한 계산기
# calculate(a, b, operator) 함수
# operator: "+", "-", "*", "/"
# try-except로 안전하게 처리
# 0으로 나누기, 잘못된 연산자 처리

# 실습 1-2: 사용자 검색
users = [
    {"id": 1, "name": "김철수"},
    {"id": 2, "name": "이영희"}
]
# find_user(users, user_id) 함수
# user_id로 사용자 찾기
# 못 찾으면 {"found": False, "message": "사용자 없음"}
# 찾으면 {"found": True, "user": {...}}

# 실습 1-3: 안전한 리스트 접근
# get_nth_item(items, n, default="없음") 함수
# n번째 항목 반환
# 인덱스 에러 시 default 반환

# 실습 1-4: 데이터 검증
# validate_age(age_str) 함수
# 문자열을 숫자로 변환
# 0~150 범위 체크
# 성공: {"valid": True, "age": 25}
# 실패: {"valid": False, "message": "잘못된 나이"}


##################################################
# 실습 2: raise
##################################################

# 실습 2-1: 점수 검증 함수
# 0~100 범위를 벗어나면 ValueError 발생
# 함수명: validate_score(score)

# 실습 2-2: 비밀번호 검증 함수
# 6자 미만이면 ValueError 발생
# 함수명: validate_password(password)

# 실습 2-3: 사용자 찾기 함수
users = {
    1: {"name": "김철수"},
    2: {"name": "이영희"}
}
# 없는 user_id면 KeyError 발생
# 함수명: find_user(user_id)
# try-except로 처리까지 구현하기