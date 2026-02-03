# 3_exercise.py

"""
Day 2 - 5교시: 튜플 + 집합
Exercise - 이메일 목록 중복 제거

문제:
회원 가입 시스템에서 중복된 이메일을 제거하고,
특정 이메일이 등록되어 있는지 확인하는 프로그램을 작성하세요.

요구사항:
1. 이메일 리스트에서 중복을 제거하세요
2. 중복 제거된 이메일 개수를 출력하세요
3. 특정 이메일이 등록되어 있는지 확인하세요 (True/False)

출력 예시:
원래 이메일 개수: 8개
중복 제거 후: 5개
alice@example.com 등록 여부: True
"""

# ============================================
# 주어진 데이터
# ============================================

# 회원 이메일 목록 (중복 있음)
email_list = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",  # 중복
    "charlie@example.com",
    "bob@example.com",  # 중복
    "david@example.com",
    "alice@example.com",  # 중복
    "eve@example.com"
]

# 확인할 이메일
check_email = "alice@example.com"


# ============================================
# TODO: 여기서부터 코드를 작성하세요
# ============================================

# 1. set()으로 중복을 제거하세요
unique_emails =

# 2. 원래 개수와 중복 제거 후 개수 출력
print(f"원래 이메일 개수: {len(email_list)}개")
print(f"중복 제거 후: {len(unique_emails)}개")

# 3. check_email이 unique_emails에 있는지 확인 (True/False 출력)
# 힌트: is_registered = check_email in unique_emails
is_registered =

print(f"{check_email} 등록 여부: {is_registered}")
