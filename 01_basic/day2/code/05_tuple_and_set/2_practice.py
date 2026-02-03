# 2_practice.py

"""
Day 2 - 5교시: 튜플 + 집합
Practice (강사와 함께 실습)

학습 목표:
- 튜플 언패킹으로 좌표 처리
- 함수에서 여러 값 리턴받기
- 집합으로 중복 제거 및 검색
"""

# ============================================
# 실습 1: 좌표 처리 (전체 타이핑)
# ============================================

# 2D 좌표를 튜플로 표현
start_point = (0, 0)
end_point = (100, 50)

# 언패킹하여 x, y 좌표 분리
start_x, start_y = start_point
end_x, end_y = end_point

# 거리 계산 (가로 + 세로)
distance_x = end_x - start_x
distance_y = end_y - start_y

print(f"시작점: ({start_x}, {start_y})")  # 출력: 시작점: (0, 0)
print(f"끝점: ({end_x}, {end_y})")  # 출력: 끝점: (100, 50)
print(f"이동 거리: 가로 {distance_x}, 세로 {distance_y}")
# 출력: 이동 거리: 가로 100, 세로 50


# ============================================
# 실습 2: 함수 다중 리턴값 (TODO)
# ============================================

def get_product_info():
    """상품 정보를 여러 값으로 리턴"""
    product_name = "노트북"
    price = 1200000
    stock = 15
    return product_name, price, stock

# TODO: 리턴값을 언패킹하여 세 변수에 저장하세요
# 힌트: name, p, s = get_product_info()
name, p, s = get_product_info()

print(f"상품명: {name}")  # 출력: 상품명: 노트북
print(f"가격: {p}원")  # 출력: 가격: 1200000원
print(f"재고: {s}개")  # 출력: 재고: 15개


# ============================================
# 실습 3: RGB 색상값 (TODO)
# ============================================

# RGB 색상을 튜플로 표현 (빨강, 초록, 파랑)
red_color = (255, 0, 0)
green_color = (0, 255, 0)

# TODO: red_color를 언패킹하여 r, g, b 변수에 저장하세요
r, g, b = red_color

print(f"빨강 색상: R={r}, G={g}, B={b}")
# 출력: 빨강 색상: R=255, G=0, B=0


# ============================================
# 실습 4: 태그 중복 제거 (TODO)
# ============================================

# 블로그 게시글의 태그들 (중복 있음)
post_tags = ["python", "coding", "tutorial", "python", "beginner", "coding"]

# TODO: set()으로 중복을 제거하세요
unique_tags = set(post_tags)

print(f"원래 태그: {post_tags}")
print(f"중복 제거된 태그: {unique_tags}")
# 출력: 중복 제거된 태그: {'python', 'coding', 'tutorial', 'beginner'}


# ============================================
# 실습 5: 허용 사용자 검색 (TODO)
# ============================================

# 관리자 권한을 가진 사용자들
admin_users = set(["alice", "bob", "charlie"])

# 로그인 시도 사용자
login_user = "alice"

# TODO: login_user가 admin_users에 있는지 확인하세요
# 힌트: is_admin = login_user in admin_users
is_admin = login_user in admin_users

print(f"{login_user}는 관리자인가? {is_admin}")  # 출력: alice는 관리자인가? True

# 일반 사용자 확인
guest_user = "guest"
is_guest_admin = guest_user in admin_users
print(f"{guest_user}는 관리자인가? {is_guest_admin}")  # 출력: guest는 관리자인가? False
