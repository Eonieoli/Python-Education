##################################################
# 초기 설정
##################################################

print("=== 상품 관리 프로그램 (CLI 버전) ===")
print()


##################################################
# 기초 1: Product 클래스 구현
##################################################
print("=== 기초 1: Product 클래스 구현 ===")
# 속성: name (str), price (int), stock (int)
# 메서드:
#   - __init__(self, name: str, price: int, stock: int)
#   - get_info(self) -> str : 상품 정보를 문자열로 반환

class Product:
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
    
    def get_info(self) -> str:
        return f"상품명: {self.name}, 가격: {self.price:,}원, 재고: {self.stock}개"
    
    def add_stock(self, amount: int) -> None:
        """재고 추가"""
        self.stock += amount
        print(f"재고 {amount}개 추가됨. 현재 재고: {self.stock}개")
    
    def reduce_stock(self, amount: int) -> None:
        """재고 감소"""
        if amount > self.stock:
            raise ValueError(f"재고 부족! 현재: {self.stock}개")
        self.stock -= amount
        print(f"재고 {amount}개 감소됨. 현재 재고: {self.stock}개")

# 테스트
product1 = Product("노트북", 1500000, 5)
product2 = Product("마우스", 30000, 10)
print(product1.get_info())
print(product2.get_info())

# 출력:
# 상품명: 노트북, 가격: 1,500,000원, 재고: 5개
# 상품명: 마우스, 가격: 30,000원, 재고: 10개
print()


##################################################
# 기초 2: 상품 추가 함수 구현
##################################################
print("=== 기초 2: 상품 추가 구현 ===")
# add_product(products) 함수를 만드세요
# - 사용자에게 상품명, 가격, 재고를 input()으로 입력받기
# - int()로 가격과 재고를 숫자로 변환
# - Product 객체를 생성하고 products 리스트에 추가
# - "'{상품명}' 상품이 추가되었습니다" 출력

def add_product(products: list) -> None:
    """
    사용자에게 상품명, 가격, 재고를 입력받아
    Product 객체를 생성하고 products 리스트에 추가
    """
    name = input("상품명: ")
    price = int(input("가격: "))
    stock = int(input("재고: "))
    
    new_product = Product(name, price, stock)
    products.append(new_product)
    print(f"✓ '{name}' 상품이 추가되었습니다")

# 테스트 (실제로는 input()이 필요하므로 직접 추가)
test_products = []
test_products.append(Product("키보드", 80000, 7))
print(f"✓ '키보드' 상품이 추가되었습니다")
print(f"현재 상품 수: {len(test_products)}개")

# 출력:
# ✓ '키보드' 상품이 추가되었습니다
# 현재 상품 수: 1개
print()


##################################################
# 기초 3: 전체 상품 조회 함수 구현
##################################################
print("=== 기초 3: 전체 상품 조회 함수 구현 ===")
# - products 리스트가 비어있으면 "등록된 상품이 없습니다" 출력
# - 그렇지 않으면 모든 상품의 정보를 출력
# - 형식: "1. 상품명: 노트북, 가격: 1500000원, 재고: 5개"

def show_all_products(products: list) -> None:
    """
    products 리스트의 모든 상품 정보를 출력
    상품이 없으면 "등록된 상품이 없습니다" 출력
    """
    if not products:
        print("등록된 상품이 없습니다")
        return
    
    print(f"총 {len(products)}개의 상품:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product.get_info()}")

# 테스트
test_products.append(Product("노트북", 1500000, 5))
test_products.append(Product("마우스", 30000, 10))
show_all_products(test_products)

# 출력:
# 총 3개의 상품:
# 1. 상품명: 키보드, 가격: 80,000원, 재고: 7개
# 2. 상품명: 노트북, 가격: 1,500,000원, 재고: 5개
# 3. 상품명: 마우스, 가격: 30,000원, 재고: 10개
print()


##################################################
# 응용 1: 상품 검색 함수 구현
##################################################
print("=== 응용 1: 상품 검색 함수 구현 ===")
# search_product(products, name) 함수를 만드세요
# - 이름으로 상품을 검색해서 찾으면 Product 객체 반환
# - 못 찾으면 None 반환

def search_product(products: list, name: str) -> Product | None:
    """
    이름으로 상품을 검색해서 찾으면 Product 객체 반환
    없으면 None 반환
    힌트: for문 + if문, 찾으면 return
    """
    for product in products:
        if product.name == name:
            return product
    return None

# 테스트
found = search_product(test_products, "노트북")
if found:
    print(f"✓ 찾음: {found.get_info()}")
else:
    print("✗ 상품을 찾을 수 없습니다")

not_found = search_product(test_products, "모니터")
if not_found:
    print(f"✓ 찾음: {not_found.get_info()}")
else:
    print("✗ '모니터'를 찾을 수 없습니다")

# 출력:
# ✓ 찾음: 상품명: 노트북, 가격: 1,500,000원, 재고: 5개
# ✗ '모니터'를 찾을 수 없습니다
print()


##################################################
# 응용 2: 상품 삭제 함수 구현
##################################################
print("=== 응용 2: 상품 삭제 함수 구현 ===")
# delete_product(products, name) 함수를 만드세요
# - search_product() 함수를 사용해서 상품을 찾기
# - 찾았으면 products.remove()로 삭제하고 "상품이 삭제되었습니다" 출력
# - 못 찾았으면 "해당 상품이 없습니다" 출력

def delete_product(products: list, name: str) -> None:
    """
    이름으로 상품을 찾아서 삭제
    없으면 "해당 상품이 없습니다" 메시지 출력
    힌트: search_product 함수 재사용, remove 메서드
    """
    product = search_product(products, name)
    
    if product:
        products.remove(product)
        print(f"✓ '{name}' 상품이 삭제되었습니다")
    else:
        print(f"✗ '{name}' 상품을 찾을 수 없습니다")

# 테스트
print(f"삭제 전 상품 수: {len(test_products)}개")
delete_product(test_products, "마우스")
print(f"삭제 후 상품 수: {len(test_products)}개")
delete_product(test_products, "모니터")  # 없는 상품

# 출력:
# 삭제 전 상품 수: 3개
# ✓ '마우스' 상품이 삭제되었습니다
# 삭제 후 상품 수: 2개
# ✗ '모니터' 상품을 찾을 수 없습니다
print()


##################################################
# 응용 3: 가격 입력 검증 함수 구현
##################################################
print("=== 응용 3: 가격 입력 검증 함수 구현 ===")
# get_valid_price() 함수를 만드세요
# - 사용자에게 가격을 입력받되, 숫자가 아니면 다시 입력받기 (ValueError 처리)
# - 0 이하면 raise ValueError("가격은 0보다 커야 합니다")
# - 정상이면 int로 반환
# 힌트: while + try-except + raise

def get_valid_price() -> int:
    """
    유효한 가격 입력받기 (예외 처리 포함)
    
    Returns:
        유효한 가격 (양수)
    
    Raises:
        ValueError: 0 이하의 가격인 경우
    """
    while True:
        try:
            price_str = input("가격: ")
            price = int(price_str)
            
            if price <= 0:
                raise ValueError("가격은 0보다 커야 합니다")
            
            return price
        
        except ValueError as e:
            if "invalid literal" in str(e):
                print("✗ 숫자를 입력해주세요")
            else:
                print(f"✗ {e}")

# 테스트 (주석 처리 - 실제 입력 필요)
# print("유효한 가격 입력 테스트:")
# price = get_valid_price()
# print(f"입력된 가격: {price:,}원")

print("(실제 입력이 필요한 함수이므로 테스트 생략)")

# 예상 출력:
# 가격: abc
# ✗ 숫자를 입력해주세요
# 가격: -100
# ✗ 가격은 0보다 커야 합니다
# 가격: 50000
# 입력된 가격: 50,000원
print()


##################################################
# 도전 1: 재고 관리 기능 추가
##################################################
print("=== 도전 1: 재고 관리 기능 추가 ===")
# Product 클래스에 다음 메서드를 추가하세요
# 
# 1. add_stock(self, amount: int) -> None
#    - 재고를 amount만큼 증가
#    - "재고 {amount}개 추가됨. 현재 재고: {self.stock}개" 출력
#
# 2. reduce_stock(self, amount: int) -> None
#    - 재고를 amount만큼 감소
#    - 재고가 부족하면 raise ValueError("재고 부족! 현재: {self.stock}개")
#    - 성공하면 "재고 {amount}개 감소됨. 현재 재고: {self.stock}개" 출력

# 힌트: Product 클래스로 돌아가서 메서드 추가
#
# def add_stock(self, amount: int) -> None:
#     # 여기에 코드 작성
#
# def reduce_stock(self, amount: int) -> None:
#     # 여기에 코드 작성

# 테스트 (이미 클래스에 추가되어 있음)
laptop = Product("노트북", 1500000, 5)
print(f"초기 재고: {laptop.get_info()}")

# 입고
laptop.add_stock(3)

# 출고
laptop.reduce_stock(2)

# 재고 부족 시도
try:
    laptop.reduce_stock(10)
except ValueError as e:
    print(f"✗ {e}")

print(f"최종 재고: {laptop.get_info()}")

# 출력:
# 초기 재고: 상품명: 노트북, 가격: 1,500,000원, 재고: 5개
# 재고 3개 추가됨. 현재 재고: 8개
# 재고 2개 감소됨. 현재 재고: 6개
# ✗ 재고 부족! 현재: 6개
# 최종 재고: 상품명: 노트북, 가격: 1,500,000원, 재고: 6개
print()


##################################################
# 도전 2: 메인 프로그램 완성하기
##################################################
print("=== 도전 2: 메인 프로그램 완성하기 ===")
# main() 함수를 만들어서 아래 메뉴를 구현하세요
#
# === 상품 관리 프로그램 ===
# 1. 상품 추가
# 2. 전체 조회
# 3. 상품 검색
# 4. 상품 삭제
# 5. 종료
# 선택: 
#
# 힌트: 
# products = []로 시작
# while True:
#     메뉴 출력
#     choice = input("선택: ")
#     if choice == "1": add_product(products)
#     elif choice == "2": show_all_products(products)
#     elif choice == "3": 
#         name = input("검색할 상품명: ")
#         product = search_product(products, name)
#         if product: print(product.get_info())
#         else: print("상품을 찾을 수 없습니다")
#     elif choice == "4":
#         name = input("삭제할 상품명: ")
#         delete_product(products, name)
#     elif choice == "5": 
#         print("프로그램을 종료합니다")
#         break

def main():
    """메인 프로그램"""
    products = []
    
    # 초기 샘플 데이터 (선택사항)
    products.append(Product("노트북", 1500000, 5))
    products.append(Product("마우스", 30000, 10))
    products.append(Product("키보드", 80000, 7))
    
    while True:
        print("\n" + "="*40)
        print("=== 상품 관리 프로그램 ===")
        print("="*40)
        print("1. 상품 추가")
        print("2. 전체 조회")
        print("3. 상품 검색")
        print("4. 상품 삭제")
        print("5. 종료")
        print("="*40)
        
        choice = input("선택: ")
        
        if choice == "1":
            add_product(products)
        
        elif choice == "2":
            show_all_products(products)
        
        elif choice == "3":
            name = input("\n검색할 상품명: ")
            product = search_product(products, name)
            
            if product:
                print(f"✓ {product.get_info()}")
            else:
                print(f"✗ '{name}' 상품을 찾을 수 없습니다")
        
        elif choice == "4":
            name = input("\n삭제할 상품명: ")
            delete_product(products, name)
        
        elif choice == "5":
            print("\n프로그램을 종료합니다")
            break
        
        else:
            print("\n✗ 잘못된 선택입니다. 1-5 사이의 숫자를 입력하세요")


# 프로그램 실행
if __name__ == "__main__":
    # main() 함수 호출하여 프로그램 시작
    print("메인 프로그램을 실행하려면 아래 주석을 해제하세요:")
    print("# main()")
    
    # 실행하려면 아래 주석 해제
    # main()