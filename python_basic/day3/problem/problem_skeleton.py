# Product 클래스 정의
class Product:
    def __init__(self, id, name, price, stock):
        # 여기에 속성 초기화
        pass
        
    def sell(self, quantity):
        # 판매 처리 (재고 감소)
        # 재고 부족하면 False 반환
        pass
        
    def restock(self, quantity):
        # 재고 추가
        pass
        
    def to_dict(self):
        # 딕셔너리로 변환
        pass

# 전역 변수
products = []  # Product 객체 리스트
next_id = 1    # 다음 상품 ID

# 기초 문제
def add_product(name, price, stock):
    """새 상품 추가"""
    global next_id
    # Product 객체 생성
    # products 리스트에 추가
    # next_id 증가
    pass

def find_product(product_id):
    """ID로 상품 찾기"""
    # for문으로 검색
    # 찾으면 Product 객체 반환
    # 못 찾으면 None 반환
    pass

# 응용 문제
def list_products():
    """전체 상품 목록"""
    # 모든 상품을 딕셔너리 리스트로 반환
    pass

def sell_product(product_id, quantity):
    """상품 판매"""
    # 상품 찾기
    # sell 메서드 호출
    # 예외 처리
    pass

# 도전 문제
def filter_by_price(min_price, max_price):
    """가격 범위 필터링"""
    pass

def calculate_total_value():
    """전체 재고 가치 (가격 * 재고)"""
    pass