# 기초 1: Product 클래스 구현 (타입 힌트 필수!)
# 속성: name (str), price (int), stock (int)
# 메서드:
#   - __init__(self, name: str, price: int, stock: int)
#   - get_info(self) -> str : 상품 정보를 문자열로 반환

# 기초 2: 상품 추가 함수 구현
def add_product(products: list) -> None:
    """
    사용자에게 상품명, 가격, 재고를 입력받아
    Product 객체를 생성하고 products 리스트에 추가
    """
    # 여기에 코드 작성

# 기초 3: 전체 상품 조회 함수 구현  
def show_all_products(products: list) -> None:
    """
    products 리스트의 모든 상품 정보를 출력
    상품이 없으면 "등록된 상품이 없습니다" 출력
    """
    # 여기에 코드 작성


# 응용 1: 상품 검색 함수 구현
def search_product(products: list, name: str) -> Product | None:
    """
    이름으로 상품을 검색해서 찾으면 Product 객체 반환
    없으면 None 반환
    힌트: for문 + if문, 찾으면 return
    """
    # 여기에 코드 작성

# 응용 2: 상품 삭제 함수 구현 (예외 처리 포함)
def delete_product(products: list, name: str) -> None:
    """
    이름으로 상품을 찾아서 삭제
    없으면 "해당 상품이 없습니다" 메시지 출력
    힌트: search_product 함수 재사용, remove 메서드
    """
    # 여기에 코드 작성

# 응용 3: 가격 입력 검증 함수 구현
def get_valid_price() -> int:
    """
    사용자에게 가격을 입력받되, 
    - 숫자가 아니면 다시 입력받기 (ValueError 처리)
    - 0 이하면 raise ValueError("가격은 0보다 커야 합니다")
    - 정상이면 int로 반환
    힌트: while + try-except + raise
    """
    # 여기에 코드 작성


# 도전 1: 메인 프로그램 완성하기
# while문으로 메뉴를 반복해서 보여주고
# 사용자 선택에 따라 함수를 호출하세요

"""
=== 상품 관리 프로그램 ===
1. 상품 추가
2. 전체 조회
3. 상품 검색
4. 상품 삭제
5. 종료
선택: 
"""

# 힌트: 
# products = []로 시작
# while True:
#     메뉴 출력
#     choice = input()
#     if choice == "1": ...
#     elif choice == "5": break

# 도전 2: 재고 관리 기능 추가 (선택)
# Product 클래스에 메서드 추가:
#   - add_stock(self, amount: int) -> None
#   - reduce_stock(self, amount: int) -> None
# reduce_stock에서는 재고가 부족하면 raise 사용