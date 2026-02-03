# 3_exercise_solution.py

"""
Day 2 - 5교시: 튜플 + 집합
Exercise - 이메일 목록 중복 제거 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

email_list = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
    "bob@example.com",
    "david@example.com",
    "alice@example.com",
    "eve@example.com"
]

check_email = "alice@example.com"


# ============================================
# 정답 코드
# ============================================

# 1. set()으로 중복 제거
unique_emails = set(email_list)

# 2. 원래 개수와 중복 제거 후 개수 출력
print(f"원래 이메일 개수: {len(email_list)}개")  # 출력: 원래 이메일 개수: 8개
print(f"중복 제거 후: {len(unique_emails)}개")  # 출력: 중복 제거 후: 5개

# 3. check_email이 unique_emails에 있는지 확인 (True/False)
is_registered = check_email in unique_emails

print(f"{check_email} 등록 여부: {is_registered}")
# 출력: alice@example.com 등록 여부: True
