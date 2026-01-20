# 연습 1: Product 클래스
# 속성: name, price, stock
# 메서드: 
# - get_info(): 상품 정보 딕셔너리 반환
# - sell(quantity): 재고 감소
#   재고 부족하면 "재고 부족" 출력

# 연습 2: Student 클래스
# 속성: name, korean, english, math
# 메서드:
# - get_average(): 평균 점수 반환
# - get_grade(): 등급 반환 (90이상 A, 80이상 B...)
# - print_info(): 이름, 평균, 등급 출력

# 연습 3: BankAccount 클래스
# 속성: owner, balance (초기값 0)
# 메서드:
# - deposit(amount): 입금
# - withdraw(amount): 출금
#   잔액 부족하면 "잔액 부족" 출력
# - get_balance(): 현재 잔액 반환

# 연습 4: Book 클래스
# 속성: title, author, price, is_available (초기값 True)
# 메서드:
# - borrow(): 대출 (is_available = False)
# - return_book(): 반납 (is_available = True)
# - get_info(): 책 정보 딕셔너리 반환


# 연습 1: Comment 클래스
# 속성: id, author, content, created_at
# 메서드:
# - to_dict(): 딕셔너리로 변환
# - from_dict(data): 딕셔너리에서 객체 생성

# 연습 2: Order 클래스
# 속성: order_id, user_name, items (리스트), total_price
# 메서드:
# - add_item(item, price): items에 추가, total_price 업데이트
# - to_dict(): 주문 정보 딕셔너리 반환
# 예: Order(1, "김철수")
#     order.add_item("노트북", 1500000)
#     order.add_item("마우스", 30000)

# 연습 3: TodoItem 클래스
# 속성: id, title, completed (초기값 False), created_at
# 메서드:
# - mark_complete(): completed = True
# - mark_incomplete(): completed = False
# - to_dict(): 딕셔너리 변환
# - from_dict(data): 딕셔너리에서 생성

# 연습 4: 여러 객체 관리
todos = []  # TodoItem 객체 리스트
# 1. 3개의 할 일 객체 생성해서 todos에 추가
# 2. 모든 할 일을 딕셔너리 리스트로 변환
#    힌트: [todo.to_dict() for todo in todos]
# 3. 첫 번째 할 일을 완료 처리