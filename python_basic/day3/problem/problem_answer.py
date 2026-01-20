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
        
    def restock(self, quantity):
        self.stock += quantity
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

products = []
next_id = 1

def add_product(name, price, stock):
    global next_id
    product = Product(next_id, name, price, stock)
    products.append(product)
    next_id += 1
    return product.to_dict()

def find_product(product_id):
    for product in products:
        if product.id == product_id:
            return product
    return None

def list_products():
    return [p.to_dict() for p in products]

def sell_product(product_id, quantity):
    try:
        product = find_product(product_id)
        if not product:
            return {"success": False, "message": "상품을 찾을 수 없습니다"}
        
        if product.sell(quantity):
            return {
                "success": True,
                "message": "판매 완료",
                "product": product.to_dict()
            }
        else:
            return {
                "success": False,
                "message": f"재고 부족 (현재 재고: {product.stock})"
            }
    except Exception as e:
        return {"success": False, "message": f"에러: {str(e)}"}

def filter_by_price(min_price, max_price):
    return [
        p.to_dict() 
        for p in products 
        if min_price <= p.price <= max_price
    ]

def calculate_total_value():
    return sum(p.price * p.stock for p in products)

# 테스트
add_product("노트북", 1500000, 10)
add_product("마우스", 30000, 50)

print("전체 상품:", list_products())
print("판매 결과:", sell_product(1, 2))
print("가격 필터:", filter_by_price(0, 100000))
print("총 재고 가치:", calculate_total_value())