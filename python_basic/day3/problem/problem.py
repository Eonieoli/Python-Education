"""
요구사항:
- Product 클래스 정의
  - 속성: id, name, price, stock
  - 메서드: sell(), restock(), to_dict()
  
- 함수로 기능 분리
  - add_product(): 상품 추가
  - find_product(): 상품 검색
  - list_products(): 전체 목록
  - sell_product(): 판매 처리
  - update_stock(): 재고 업데이트
  
- 예외 처리
  - 잘못된 입력 처리
  - 재고 부족 처리
  - 상품 없음 처리

기초 문제 (20분)
1. Product 클래스 구현
2. 상품 추가 함수 구현

응용 문제 (20분)
3. 상품 목록 조회 및 검색
4. 판매 처리 (재고 감소)
5. 예외 처리 추가

도전 문제 (20분)
6. 재고 관리 기능 (입고/출고)
7. 가격 범위 필터링
8. 전체 재고 가치 계산
"""


# 힌트
##################################################
"""
# Product 클래스
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

# 상품 추가
def add_product(name, price, stock):
    global next_id
    product = Product(next_id, name, price, stock)
    products.append(product)
    next_id += 1
    return product

# 판매 처리
def sell_product(product_id, quantity):
    product = find_product(product_id)
    if not product:
        return {"success": False, "message": "상품 없음"}
    
    if product.sell(quantity):
        return {"success": True, "message": "판매 완료"}
    else:
        return {"success": False, "message": "재고 부족"}
"""
##################################################