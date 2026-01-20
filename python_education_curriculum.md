# FastAPI 백엔드 개발 과정

## 🎯 교육 목표
Python 초보자가 FastAPI를 활용한 백엔드 서버를 직접 구축할 수 있는 수준 달성

## 📅 과정 구성
- **기초 과정** (3일, 21시간): FastAPI 사용을 위한 Python 문법x
- **응용 과정** (3일, 21시간): 웹 개념과 FastAPI CRUD
- **심화 과정** (3일, 21시간): 인증 및 고급 기능, 실전 프로젝트

※ 각 과정 사이 시간 간격이 있을 수 있음

## ⏰ 일일 시간표
- 09:00-12:30 (오전 3.5시간, 휴식 포함)
- 12:30-13:30 (점심)
- 13:30-17:00 (오후 3.5시간, 휴식 포함)

---

# 📘 기초 과정 (3일, 21시간)
## FastAPI를 위한 Python 필수 문법

## 기초 Day 1: Python 시작 & 기본 자료형

### 오전 (09:00-12:30)

#### 1-1. Python과 개발 환경 (40분)
- Python이란? FastAPI와의 관계
- 개발 환경 구축
  - Python 설치 및 버전 확인
  - VS Code 설치 및 설정
  - Git 설치 및 버전 확인
  - 터미널 기본 사용법
- 첫 프로그램
  - 👉 Practice: print("Hello World")
  - 👉 Practice: 간단한 계산 출력
  - 주석 사용법 (#, """ """)

#### 1-2. 변수와 숫자형 (70분)
- **변수**
  - 변수란? 변수 할당 규칙
  - 변수명 작성 규칙 (snake_case)
  - 👉 Practice: 변수 만들고 출력하기
  - 변수 타입 확인 (type 함수)
  - 👉 Practice: 여러 타입의 변수
  
- **숫자형**
  - 정수(int), 실수(float)
  - 산술 연산자 (+, -, *, /, //, %, **)
  - 👉 Practice: 사칙연산 계산기
  - 👉 Practice: 나눗셈 종류 (/, //, %)
  - ✏️ Exercise: 숫자 연산 (3-4문제)

#### 1-3. 문자열 (90분)
- **문자열 기본**
  - 문자열 생성 ("", '', """ """)
  - 문자열 연산 (+, *)
  - 문자열 길이 (len)
  - 👉 Practice: 자기소개 문자열 만들기
  - ✏️ Exercise: 문자열 기본 (2문제)
  
- **문자열 인덱싱과 슬라이싱**
  - 인덱스 개념 (0부터 시작)
  - 음수 인덱스 (-1부터)
  - 👉 Practice: 문자 하나씩 접근
  - 슬라이싱 [start:end]
  - 👉 Practice: 문자열 자르기
  - ✏️ Exercise: 인덱싱/슬라이싱 (3문제)
  
- **문자열 포매팅과 메서드**
  - f-string 포매팅 (FastAPI에서 자주 사용!)
  - 👉 Practice: f-string으로 정보 출력
  - 주요 메서드 (upper, lower, strip, split, replace, join)
  - 👉 Practice: 문자열 가공하기
  - ✏️ Exercise: 문자열 처리 (3-4문제)

### 오후 (13:30-17:00)

#### 1-4. 불(Boolean)과 비교 연산자 (30분)
- **불(Boolean)**
  - True/False
  - 비교 연산자 (==, !=, >, <, >=, <=)
  - 👉 Practice: 값 비교하기
  - and, or, not (간단히)
  - 👉 Practice: 조건 조합

#### 1-5. 리스트 (120분)
- **리스트 기본** (FastAPI 응답에서 많이 사용!)
  - 리스트란? 생성 방법 []
  - 👉 Practice: 다양한 리스트 만들기
  - 리스트 인덱싱과 슬라이싱
  - 👉 Practice: 리스트 요소 접근
  - 리스트 길이 (len)
  - ✏️ Exercise: 리스트 기본 (2-3문제)
  
- **리스트 수정**
  - 요소 추가 (append, insert)
  - 👉 Practice: 할 일 추가하기
  - 요소 삭제 (remove, pop, del)
  - 👉 Practice: 할 일 삭제하기
  - 요소 수정 (인덱스로 접근)
  - 👉 Practice: 할 일 수정하기
  - ✏️ Exercise: 리스트 수정 (3-4문제)
  
- **리스트 메서드와 연산**
  - sort, reverse, count, index
  - 👉 Practice: 리스트 정렬하기
  - 리스트 연산 (+, *)
  - 👉 Practice: 리스트 합치기
  - in 연산자 (포함 여부)
  - 👉 Practice: 검색 기능
  - ✏️ Exercise: 리스트 메서드 (3-4문제)

#### 1-6. 튜플, 집합, None (30분)
- **튜플**
  - 튜플의 특징 (변경 불가)
  - 튜플 생성 ()
  - 👉 Practice: 좌표 데이터 (x, y)

- **집합(set)**
  - 집합의 특징 (중복 불가, 순서 없음)
  - 집합 생성 {}
  - 👉 Practice: 중복 제거하기
    ```python
    numbers = [1, 2, 2, 3, 3, 3]
    unique = list(set(numbers))
    print(unique)  # [1, 2, 3]
    ```
  - ※ 간단한 소개만! 집합 연산은 생략
  
- **None**
  - None의 의미와 용도
  - 👉 Practice: None 체크하기

#### 1-7. 🎯 기초 Day 1 종합 실습 (40분)
**주제: 학생 성적 관리 (리스트 버전)**

기초 문제:
1. 학생 이름 리스트 만들기
2. 학생 점수 리스트 만들기
3. 특정 학생 점수 찾기 (인덱스 활용)

응용 문제:
4. 새 학생 추가하기
5. 평균 점수 계산하기
6. 최고 점수 찾기

도전 문제:
7. 60점 이상 학생만 필터링 (for문 없이!)
8. f-string으로 성적표 출력

※ Day 1 시간이 남으면 Day 2의 딕셔너리를 미리 시작!

---

## 기초 Day 2: 딕셔너리와 제어문

### 오전 (09:00-12:30)

#### 2-0. Day 1 복습 (20분)
- 복습 퀴즈 (5문제)
  - 변수, 문자열, 리스트

#### 2-1. 딕셔너리 (100분) - FastAPI의 핵심!
- **딕셔너리 기본**
  - 딕셔너리란? Key-Value 개념
  - JSON과 딕셔너리의 관계 (FastAPI의 핵심!)
  - 딕셔너리 생성 {}
  - 👉 Practice: 사용자 정보 딕셔너리
    ```python
    user = {
        "name": "김철수",
        "age": 25,
        "email": "kim@example.com"
    }
    ```
  - 👉 Practice: 상품 정보 딕셔너리
  - ✏️ Exercise: 딕셔너리 생성 (2-3문제)

- **딕셔너리 조작**
  - Key로 Value 접근하기
  - 👉 Practice: 정보 가져오기
  - 값 추가하기
  - 👉 Practice: 새 정보 추가
  - 값 수정하기
  - 👉 Practice: 정보 업데이트
  - 값 삭제하기 (del, pop)
  - 👉 Practice: 정보 삭제
  - ✏️ Exercise: 딕셔너리 CRUD (3-4문제)

- **딕셔너리 메서드**
  - keys(), values(), items()
  - 👉 Practice: 모든 키/값 확인
  - get() 메서드 (안전한 접근)
  - 👉 Practice: 없는 키 처리
  - in 연산자 (키 존재 확인)
  - 👉 Practice: 키 검색
  - ✏️ Exercise: 딕셔너리 메서드 (3-4문제)

- **리스트 + 딕셔너리 조합** (FastAPI 응답 형태!)
  - 딕셔너리의 리스트
  - 👉 Practice: 사용자 목록 만들기
    ```python
    users = [
        {"name": "김철수", "age": 25},
        {"name": "이영희", "age": 30}
    ]
    ```
  - 👉 Practice: 상품 목록 관리
  - ✏️ Exercise: 복합 자료구조 (2-3문제)

#### 2-2. if 문 - 조건 분기 (70분)
- **if 문 기본**
  - if 문이 필요한 이유
  - if 문의 구조 (들여쓰기, 콜론!)
  - 👉 Practice: 기본 if 문
  - 비교 연산자 복습
  - 👉 Practice: 나이 확인하기
  - ✏️ Exercise: if 기본 (2-3문제)

- **if-else와 elif**
  - if-else 구조
  - 👉 Practice: 짝수/홀수 판별
  - elif로 여러 조건
  - 👉 Practice: 성적 등급 계산
  - 논리 연산자 (and, or, not)
  - 👉 Practice: 복합 조건
  - in 연산자와 if문
  - 👉 Practice: 리스트/딕셔너리에서 검색
  - ✏️ Exercise: 조건 분기 (3-4문제)

### 오후 (13:30-17:00)

#### 2-3. for 문 - 반복 처리 (110분)
- **for 문 기본**
  - 반복문이 필요한 이유
  - for 문의 구조
  - 👉 Practice: 리스트 순회
    ```python
    fruits = ['apple', 'banana', 'orange']
    for fruit in fruits:
        print(fruit)
    ```
  - 문자열 순회
  - 👉 Practice: 문자 하나씩 처리
  - ✏️ Exercise: for 문 기본 (2-3문제)

- **딕셔너리와 for 문** (FastAPI에서 중요!)
  - 딕셔너리 keys 순회
  - 👉 Practice: 모든 키 출력
  - 딕셔너리 values 순회
  - 👉 Practice: 모든 값 출력
  - 딕셔너리 items 순회 ⭐
  - 👉 Practice: Key-Value 쌍 출력
    ```python
    user = {"name": "김철수", "age": 25}
    for key, value in user.items():
        print(f"{key}: {value}")
    ```
  - 딕셔너리 리스트 순회
  - 👉 Practice: 사용자 목록 처리
  - ✏️ Exercise: 딕셔너리 순회 (3-4문제)

- **range 함수**
  - range(n), range(start, end), range(start, end, step)
  - 👉 Practice: 숫자 범위 반복
  - 👉 Practice: 역순 반복
  - enumerate로 인덱스와 값
  - 👉 Practice: 번호 매기기
  - ✏️ Exercise: range 활용 (2-3문제)

- **중첩 for 문** (20분)
  - 중첩 for문이란?
  - 👉 Practice: 2차원 리스트 출력
    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        for num in row:
            print(num, end=' ')
        print()  # 줄바꿈
    ```
  - 👉 Practice: 구구단 한 단 출력
    ```python
    dan = 2
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    ```
  - 👉 Practice: 구구단 전체 출력 (2단~9단)
    ```python
    for dan in range(2, 10):
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan * i}")
        print()  # 단 사이 공백
    ```
  - ✏️ Exercise: 중첩 for문 (2-3문제)
    - 별 사각형 출력
    - 좌표 쌍 만들기 [(1,1), (1,2), ...]

- **for 문 제어**
  - for + if 조합
  - 👉 Practice: 조건부 출력
  - break로 탈출
  - 👉 Practice: 검색 후 중단
  - continue로 건너뛰기
  - 👉 Practice: 특정 값 제외
  - ✏️ Exercise: 반복 제어 (3-4문제)

#### 2-4. while 문 (30분)
- while 문 기본
- 👉 Practice: 조건 반복
- while과 break
- 👉 Practice: 입력 받기 반복
- ✏️ Exercise: while 활용 (2문제)

#### 2-5. 리스트 컴프리헨션 (40분)
- 리스트 컴프리헨션이란? (FastAPI에서 유용!)
- 👉 Practice: 기본 형태
  ```python
  # 일반 for문
  squares = []
  for i in range(5):
      squares.append(i ** 2)
  
  # 리스트 컴프리헨션
  squares = [i ** 2 for i in range(5)]
  ```
- 조건부 리스트 컴프리헨션
- 👉 Practice: 짝수만 필터링
- 👉 Practice: 딕셔너리 리스트에서 추출
- ✏️ Exercise: 리스트 컴프리헨션 (3-4문제)

#### 2-6. 🎯 기초 Day 2 종합 실습 (60분)
**주제: 학생 성적 관리 시스템 (딕셔너리 버전)**

요구사항:
- 학생 정보를 딕셔너리로 저장 (이름, 국어, 영어, 수학)
- 여러 학생을 리스트에 저장

기초 문제:
1. 학생 정보 딕셔너리 3개 만들기
2. 학생 리스트에 추가하기
3. 모든 학생 정보 출력 (for 사용)

응용 문제:
4. 특정 학생 찾기 (이름으로 검색)
5. 각 학생의 평균 점수 계산
6. 80점 이상 학생만 필터링

도전 문제:
7. 딕셔너리 리스트를 점수순 정렬
8. 리스트 컴프리헨션으로 우등생 목록 만들기
   (평균 90점 이상)
9. 과목별 전체 평균 계산

---

## 기초 Day 3: 함수와 클래스 기초

### 오전 (09:00-12:30)

#### 3-0. Day 2 복습 (20분)
- 복습 퀴즈 (5문제)
  - if, for, 리스트 컴프리헨션

#### 3-1. 함수 - 코드 재사용 (120분)
- **함수 기본**
  - 함수가 필요한 이유
  - 함수의 구조 (def, 매개변수, return)
  - 👉 Practice: 간단한 함수 만들기
  - 함수 호출과 반환값
  - 👉 Practice: 계산 함수
  - ✏️ Exercise: 함수 기본 (2-3문제)

- **매개변수와 인자**
  - 위치 인자
  - 👉 Practice: 여러 매개변수 함수
  - 키워드 인자
  - 👉 Practice: 키워드로 호출하기
  - 기본값 설정
  - 👉 Practice: 기본값이 있는 함수
  - ✏️ Exercise: 매개변수 활용 (3-4문제)

- **함수의 다양한 형태** (FastAPI에서 자주 사용!)
  - 리턴값이 있는 함수
  - 리턴값이 없는 함수 (None 반환)
  - 여러 값 반환 (튜플 활용)
  - 👉 Practice: 다양한 형태의 함수
  - 함수에서 딕셔너리 반환 (API 응답 형태!)
  - 👉 Practice: 딕셔너리 반환 함수
  - ✏️ Exercise: 함수 응용 (3-4문제)

#### 3-2. 모듈과 import (40분)
- **모듈 사용**
  - 모듈이란? (FastAPI도 모듈!)
  - import 문
  - 👉 Practice: random 모듈 사용
  - from ... import ...
  - 👉 Practice: datetime 모듈 사용
  - 👉 Practice: json 모듈로 데이터 변환
  - ✏️ Exercise: 모듈 활용 (2-3문제)

### 오후 (13:30-17:00)

#### 3-3. 클래스 기초 (100분)
- **클래스와 객체** (FastAPI의 Pydantic 모델 이해를 위해!)
  - 클래스가 필요한 이유
  - 클래스와 객체의 개념
  - 👉 Practice: 첫 번째 클래스 만들기
  
- **클래스 구조**
  - __init__ 생성자
  - 👉 Practice: 생성자로 초기화
  - 인스턴스 변수 (속성)
  - 👉 Practice: User 클래스 만들기
  - 메서드
  - 👉 Practice: 메서드 추가
  - self의 의미
  - 👉 Practice: self 이해하기
  - ✏️ Exercise: 클래스 기본 (3-4문제)

- **클래스 활용** (FastAPI Pydantic 모델과 유사!)
  - 클래스로 데이터 모델 만들기
  - 👉 Practice: Product 클래스
  - 👉 Practice: 인스턴스 생성과 활용
  - 딕셔너리 ↔ 클래스 변환 개념
  - 👉 Practice: 클래스를 딕셔너리로
  - ✏️ Exercise: 데이터 모델링 (2-3문제)

#### 3-4. 예외 처리 기초 (60분)

- **예외란 무엇인가?** (5분)
  - 에러와 예외
  - 예외 처리가 필요한 이유

- **try-except로 에러 잡기** (25분)
  - try-except 기본 구조
  - 👉 Practice: 기본 예외 처리
```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
```
  - 특정 예외 처리 (ValueError, KeyError, IndexError)
  - 👉 Practice: 여러 except 사용
  - 👉 Practice: 사용자 입력 검증
  - ✏️ Exercise: try-except (3문제)

- **raise로 에러 던지기** (25분) 🆕 추가!
  - raise가 필요한 이유
  - 👉 Practice: 기본 raise
```python
    def validate_age(age):
        if age < 0:
            raise ValueError("나이는 0 이상이어야 합니다")
        return age
    
    try:
        validate_age(-5)
    except ValueError as e:
        print(e)
```
  - 👉 Practice: 함수에서 조건 검증 + raise
  - raise + try-except 조합 (전체 흐름!)
  - 👉 Practice: 상품 검증 함수
```python
    def get_product(product_id):
        if product_id not in products:
            raise KeyError(f"상품 {product_id}가 없습니다")
        return products[product_id]
    
    try:
        product = get_product(999)
    except KeyError as e:
        print(f"에러: {e}")
```
  - ✏️ Exercise: raise 활용 (3문제)

- **else - 예외가 없을 때** (10분)
  - else가 필요한 이유
  - try vs else 차이
  - 👉 Practice: 파일 처리 with else
  - 👉 Practice: DB 조회 with else

- **finally** (5분)
  - finally의 용도 (항상 실행)
  - 👉 Practice: 파일 열고 닫기

#### 3-5. 🎯 기초 Day 3 종합 실습 (60분)
**주제: 간단한 상품 관리 프로그램 (CLI 버전)**

요구사항:
- Product 클래스 정의 (이름, 가격, 재고)
- 함수로 기능 분리
  - 상품 추가 함수
  - 상품 조회 함수 (전체/검색)
  - 상품 수정 함수
  - 상품 삭제 함수
- 예외 처리 (잘못된 입력 등)
- 리스트로 상품 목록 관리

기초 문제:
1. Product 클래스 구현
2. 상품 추가 함수 구현

응용 문제:
3. 상품 목록 조회 및 검색
4. 가격 범위로 필터링
5. 예외 처리 추가

도전 문제:
6. 재고 관리 기능 (입고/출고)
7. json으로 저장/불러오기 (선택)

---

# 📗 응용 과정 (3일, 21시간)
## 웹 개념과 FastAPI CRUD

※ 기초 과정 이후 시간이 경과했을 수 있으므로 복습부터 시작

---

## 응용 Day 1: 기초 복습 & 웹/FastAPI 시작

### 오전 (09:00-12:30)

#### 4-0. 기초 과정 복습 (90분)
**핵심 개념 빠른 복습**

- **자료형 복습** (20분)
  - 리스트, 딕셔너리 재점검
  - 👉 Practice: 딕셔너리 CRUD
  
- **제어문 복습** (20분)
  - if문, for문 재점검
  - 👉 Practice: 리스트 필터링
  
- **함수 복습** (20분)
  - 함수 정의와 호출
  - 👉 Practice: 데이터 처리 함수
  
- **클래스 복습** (20분)
  - 클래스 기본 구조
  - 👉 Practice: 간단한 모델 클래스
  
- **종합 복습 문제** (10분)
  - ✏️ Exercise: 기초 종합 (3-4문제)

#### 4-1. 웹 개발 기초 (100분)
- **웹의 동작 원리**
  - 클라이언트와 서버
  - HTTP 프로토콜이란?
  - Request & Response 개념
  
- **REST API 개념**
  - API란 무엇인가?
  - REST API의 특징
  - HTTP Methods
    - GET: 데이터 조회
    - POST: 데이터 생성
    - PUT: 데이터 수정
    - DELETE: 데이터 삭제
  - 👉 Practice: HTTP Method 이해하기
  
- **JSON 데이터 형식**
  - JSON이란?
  - Python 딕셔너리와 JSON의 관계
  - 👉 Practice: 딕셔너리 ↔ JSON 변환
  - ✏️ Exercise: JSON 다루기 (2-3문제)

### 오후 (13:30-17:00)

#### 4-2. FastAPI 시작 (120분)
- **FastAPI 소개**
  - FastAPI란? 왜 FastAPI인가?
  - FastAPI 설치
    ```bash
    pip install fastapi uvicorn
    ```
  
- **첫 FastAPI 애플리케이션**
  - 👉 Practice: Hello World API
    ```python
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"message": "Hello World"}
    ```
  - uvicorn으로 서버 실행
  - 브라우저로 확인하기
  - 👉 Practice: 간단한 엔드포인트 추가
  
- **Path Parameter**
  - Path Parameter란?
  - 👉 Practice: 동적 경로 만들기
    ```python
    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        return {"item_id": item_id}
    ```
  - 👉 Practice: 여러 Path Parameter
  - ✏️ Exercise: Path Parameter 활용 (3-4문제)

- **Query Parameter**
  - Query Parameter란?
  - 👉 Practice: 쿼리 파라미터 처리
    ```python
    @app.get("/search")
    def search(q: str, limit: int = 10):
        return {"query": q, "limit": limit}
    ```
  - 선택적 파라미터 (기본값)
  - 👉 Practice: 검색 API 만들기
  - ✏️ Exercise: Query Parameter 활용 (2-3문제)

#### 4-3. 🎯 응용 Day 1 종합 실습 (70분)
**주제: 간단한 정보 조회 API**

기초 문제:
1. 사용자 정보 반환 API (Path Parameter)
2. 상품 목록 조회 API
3. 검색 API (Query Parameter)

응용 문제:
4. 필터링 API (여러 Query Parameter)
5. 페이징 API (page, size 파라미터)

도전 문제:
6. 복합 조건 검색 API
7. Swagger 문서 확인하고 테스트하기

---

## 응용 Day 2: Request Body & Pydantic

### 오전 (09:00-12:30)

#### 5-0. Day 1 복습 (20분)
- HTTP Methods 복습
- Path/Query Parameter 복습
- 👉 Practice: 간단한 GET API

#### 5-1. Pydantic 모델 (100분)
- **Pydantic이란?**
  - 데이터 검증과 직렬화
  - 왜 Pydantic을 사용하나?
  
- **BaseModel 기본**
  - 👉 Practice: 첫 Pydantic 모델
    ```python
    from pydantic import BaseModel
    
    class User(Base Model):
        name: str
        age: int
        email: str
    ```
  - 타입 힌트의 중요성
  - 👉 Practice: 여러 타입 활용
  
- **선택적 필드**
  - Optional 사용
  - 기본값 설정
  - 👉 Practice: 선택적 필드가 있는 모델
  - ✏️ Exercise: Pydantic 모델 (3-4문제)

- **모델 검증**
  - 자동 타입 변환
  - 유효성 검사
  - 👉 Practice: 잘못된 데이터 처리
  - Field로 상세 검증
  - 👉 Practice: Field 활용
  - ✏️ Exercise: 데이터 검증 (2-3문제)

#### 5-2. POST 요청 처리 (80분)
- **Request Body**
  - Request Body란?
  - POST 메서드로 데이터 받기
  - 👉 Practice: 사용자 생성 API
    ```python
    @app.post("/users")
    def create_user(user: User):
        return {"message": "User created", "user": user}
    ```
  
- **데이터 저장** (메모리)
  - 리스트에 데이터 저장
  - 👉 Practice: 메모리에 사용자 저장
  - 전역 변수 활용
  - 👉 Practice: 저장된 데이터 조회
  - ✏️ Exercise: CREATE & READ 구현 (3-4문제)

### 오후 (13:30-17:00)

#### 5-3. CRUD 구현 (120분)
- **Read (조회)**
  - 전체 조회 GET
  - 👉 Practice: 전체 목록 API
  - 단건 조회 GET
  - 👉 Practice: ID로 조회 API
  - 404 에러 처리
  - 👉 Practice: HTTPException 사용
  - ✏️ Exercise: Read 구현 (2-3문제)

- **Update (수정)**
  - PUT 메서드
  - 👉 Practice: 데이터 수정 API
  - 부분 수정 vs 전체 수정
  - 👉 Practice: PATCH 구현
  - ✏️ Exercise: Update 구현 (2-3문제)

- **Delete (삭제)**
  - DELETE 메서드
  - 👉 Practice: 데이터 삭제 API
  - 삭제 후 응답 처리
  - ✏️ Exercise: Delete 구현 (2-3문제)

#### 5-4. 🎯 응용 Day 2 종합 실습 (70분)
**주제: Todo API (메모리 기반)**

요구사항:
- Todo 모델 (Pydantic)
  - id, title, description, completed
- CRUD API 구현
  - POST /todos - Todo 생성
  - GET /todos - 전체 조회
  - GET /todos/{id} - 단건 조회
  - PUT /todos/{id} - 수정
  - DELETE /todos/{id} - 삭제

기초 문제:
1. Todo 모델 정의
2. POST, GET (전체) 구현

응용 문제:
3. GET (단건), PUT, DELETE 구현
4. 완료/미완료 필터링 (Query Parameter)
5. 에러 처리 추가

도전 문제:
6. 검색 기능 (제목으로)
7. 정렬 기능 (생성일, 제목)

---

## 응용 Day 3: 데이터베이스 연동

### 오전 (09:00-12:30)

#### 6-0. Day 2 복습 (20분)
- Pydantic 모델 복습
- CRUD 개념 복습
- 👉 Practice: 간단한 CRUD API

#### 6-1. 데이터베이스 기초 (60분)
- **데이터베이스란?**
  - 왜 데이터베이스가 필요한가?
  - SQL vs NoSQL
  - SQLite 소개
  
- **SQL 기본**
  - CREATE TABLE
  - 👉 Practice: 테이블 생성
  - INSERT
  - 👉 Practice: 데이터 삽입
  - SELECT
  - 👉 Practice: 데이터 조회
  - UPDATE
  - 👉 Practice: 데이터 수정
  - DELETE
  - 👉 Practice: 데이터 삭제
  - ✏️ Exercise: SQL 기본 (5-6문제)

#### 6-2. Python에서 SQLite 사용 (110분)
- **sqlite3 모듈**
  - 데이터베이스 연결
  - 👉 Practice: DB 파일 생성
    ```python
    import sqlite3
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    ```
  
- **테이블 생성**
  - 👉 Practice: users 테이블 생성
    ```python
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    ```
  
- **데이터 삽입**
  - 👉 Practice: INSERT 실행
  - 👉 Practice: 여러 행 삽입
  - ✏️ Exercise: 데이터 삽입 (2-3문제)
  
- **데이터 조회**
  - fetchone, fetchall
  - 👉 Practice: SELECT 실행
  - 👉 Practice: WHERE 조건
  - ✏️ Exercise: 데이터 조회 (3-4문제)

### 오후 (13:30-17:00)

#### 6-3. FastAPI + SQLite 통합 (100분)
- **데이터베이스 헬퍼 함수**
  - 연결 관리
  - 👉 Practice: DB 연결 함수
  - 👉 Practice: DB 종료 함수
  
- **CRUD with DB**
  - CREATE - POST로 DB 저장
  - 👉 Practice: 사용자 생성 (DB 저장)
  - READ - GET으로 DB 조회
  - 👉 Practice: 전체/단건 조회 (DB)
  - UPDATE - PUT으로 DB 수정
  - 👉 Practice: 사용자 수정 (DB)
  - DELETE - DELETE로 DB 삭제
  - 👉 Practice: 사용자 삭제 (DB)
  - ✏️ Exercise: DB CRUD (4-5문제)

- **에러 처리**
  - 중복 데이터 처리
  - 존재하지 않는 데이터 처리
  - 👉 Practice: 에러 응답 구현
  - ✏️ Exercise: 에러 처리 (2-3문제)

#### 6-4. 🎯 응용 Day 3 종합 실습 (90분)
**주제: 블로그 포스트 API (SQLite 기반)**

요구사항:
- Post 테이블
  - id, title, content, author, created_at
- CRUD API 구현 (SQLite 연동)
  - POST /posts - 포스트 생성
  - GET /posts - 전체 조회 (페이징)
  - GET /posts/{id} - 단건 조회
  - PUT /posts/{id} - 수정
  - DELETE /posts/{id} - 삭제
- Pydantic 모델
  - PostCreate (생성용)
  - PostResponse (응답용)

기초 문제:
1. 테이블 생성
2. POST, GET (전체) 구현

응용 문제:
3. GET (단건), PUT, DELETE 구현
4. 작성자별 조회
5. 페이징 (limit, offset)

도전 문제:
6. 검색 기능 (제목 + 내용)
7. 정렬 기능 (최신순, 오래된 순)
8. 조회수 기능 추가

---

# 📙 심화 과정 (3일, 21시간)
## 인증/고급 기능 & 실전 프로젝트

※ 응용 과정 이후 시간이 경과했을 수 있으므로 복습부터 시작

---

## 심화 Day 1: 응용 복습 & 인증 시스템

### 오전 (09:00-12:30)

#### 7-0. 응용 과정 복습 (90분)
**핵심 개념 빠른 복습**

- **FastAPI 기본 복습** (20분)
  - HTTP Methods, Path/Query Parameter
  - 👉 Practice: 간단한 API 재작성
  
- **Pydantic 복습** (20분)
  - 모델 정의와 검증
  - 👉 Practice: 모델 재작성
  
- **CRUD 복습** (20분)
  - 메모리 기반 CRUD
  - 👉 Practice: 간단한 CRUD
  
- **SQLite 복습** (20분)
  - SQL 기본과 Python 연동
  - 👉 Practice: DB CRUD 재작성
  
- **종합 복습 문제** (10분)
  - ✏️ Exercise: 응용 종합 (3-4문제)

#### 7-1. 인증의 필요성 (20분)
- 왜 인증이 필요한가?
- 인증 vs 인가
- 세션 vs 토큰 기반 인증

#### 7-2. 비밀번호 해싱 (70분)
- **해싱이란?**
  - 평문 비밀번호의 위험성
  - bcrypt 소개
  
- **passlib 사용**
  - 설치: `pip install passlib[bcrypt]`
  - 👉 Practice: 비밀번호 해싱
    ```python
    from passlib.context import CryptContext
    
    pwd_context = CryptContext(schemes=["bcrypt"])
    hashed = pwd_context.hash("mypassword")
    ```
  - 👉 Practice: 비밀번호 검증
    ```python
    pwd_context.verify("mypassword", hashed)
    ```
  - ✏️ Exercise: 해싱 활용 (2-3문제)

### 오후 (13:30-17:00)

#### 7-3. JWT 토큰 (120분)
- **JWT란?**
  - JWT 구조 (Header, Payload, Signature)
  - 왜 JWT를 사용하나?
  
- **python-jose 사용**
  - 설치: `pip install python-jose[cryptography]`
  - 👉 Practice: JWT 토큰 생성
    ```python
    from jose import jwt
    
    SECRET_KEY = "your-secret-key"
    ALGORITHM = "HS256"
    
    token = jwt.encode({"sub": "user_id"}, SECRET_KEY, algorithm=ALGORITHM)
    ```
  - 👉 Practice: JWT 토큰 검증
    ```python
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    ```
  - ✏️ Exercise: JWT 기본 (3-4문제)

- **만료 시간 설정**
  - 👉 Practice: 토큰 만료 구현
  - 👉 Practice: 만료 토큰 처리
  - ✏️ Exercise: 만료 처리 (2문제)

#### 7-4. 회원가입과 로그인 (90분)
- **회원가입 API**
  - 👉 Practice: 사용자 등록
    ```python
    @app.post("/register")
    def register(user: UserCreate):
        hashed_password = pwd_context.hash(user.password)
        # DB에 저장
        return {"message": "User registered"}
    ```
  - 이메일 중복 체크
  - 👉 Practice: 중복 검증
  - ✏️ Exercise: 회원가입 (2-3문제)

- **로그인 API**
  - 👉 Practice: 로그인 구현
    ```python
    @app.post("/login")
    def login(credentials: LoginRequest):
        # DB에서 사용자 조회
        # 비밀번호 검증
        # JWT 토큰 발급
        return {"access_token": token}
    ```
  - 로그인 실패 처리
  - 👉 Practice: 401 에러 처리
  - ✏️ Exercise: 로그인 (2-3문제)

#### 7-5. 🎯 심화 Day 1 종합 실습 (60분)
**주제: 인증 시스템 구축**

요구사항:
- 사용자 테이블 (id, email, hashed_password, created_at)
- 회원가입 API
  - 이메일 중복 체크
  - 비밀번호 해싱
- 로그인 API
  - 비밀번호 검증
  - JWT 발급

기초 문제:
1. 사용자 테이블 생성
2. 회원가입 API 구현

응용 문제:
3. 로그인 API 구현
4. 이메일 형식 검증
5. 비밀번호 강도 체크

도전 문제:
6. Refresh Token 개념 이해
7. 토큰 갱신 API 설계

---

## 심화 Day 2: 인증 보호 & 고급 기능

### 오전 (09:00-12:30)

#### 8-0. Day 1 복습 (20분)
- 비밀번호 해싱 복습
- JWT 토큰 복습
- 👉 Practice: 로그인 재작성

#### 8-1. 인증이 필요한 엔드포인트 (110분)
- **Depends를 활용한 인증**
  - FastAPI Depends 개념
  - 👉 Practice: 현재 사용자 가져오기
    ```python
    from fastapi import Depends, HTTPException, status
    from fastapi.security import HTTPBearer
    
    security = HTTPBearer()
    
    def get_current_user(token: str = Depends(security)):
        try:
            payload = jwt.decode(token.credentials, SECRET_KEY)
            return payload["sub"]
        except:
            raise HTTPException(status_code=401)
    ```
  - 👉 Practice: 보호된 엔드포인트
    ```python
    @app.get("/me")
    def get_me(current_user = Depends(get_current_user)):
        return {"user_id": current_user}
    ```
  - ✏️ Exercise: 인증 의존성 (3-4문제)

- **권한 체크**
  - 본인 데이터만 수정
  - 👉 Practice: 권한 검증
  - 👉 Practice: 403 Forbidden 처리
  - ✏️ Exercise: 권한 관리 (2-3문제)

#### 8-2. 파일 업로드 (70분)
- **File Upload**
  - 👉 Practice: 파일 받기
    ```python
    from fastapi import File, UploadFile
    
    @app.post("/upload")
    async def upload_file(file: UploadFile = File(...)):
        contents = await file.read()
        # 파일 저장
        return {"filename": file.filename}
    ```
  - 👉 Practice: 이미지 저장
  - 파일 크기 제한
  - 파일 타입 검증
  - ✏️ Exercise: 파일 처리 (3-4문제)

### 오후 (13:30-17:00)

#### 8-3. 에러 처리와 미들웨어 (80분)
- **HTTPException**
  - 다양한 Status Code
  - 👉 Practice: 커스텀 에러 메시지
  - 에러 응답 포맷 통일
  - ✏️ Exercise: 에러 처리 (3-4문제)

- **CORS 설정**
  - CORS란?
  - 👉 Practice: CORS 미들웨어
    ```python
    from fastapi.middleware.cors import CORSMiddleware
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
    )
    ```

- **로깅**
  - 요청 로깅
  - 👉 Practice: 로깅 미들웨어
  - ✏️ Exercise: 미들웨어 (2문제)

#### 8-4. API 문서화 (40분)
- **Swagger UI 활용**
  - 자동 생성 문서 확인
  - 👉 Practice: 태그 추가
  - 👉 Practice: 설명 추가
  - Response Model 정의
  - ✏️ Exercise: 문서 작성 (2문제)

#### 8-5. 🎯 심화 Day 2 종합 실습 (90분)
**주제: 이미지 갤러리 API**

요구사항:
- Image 테이블 (id, title, filename, user_id, created_at)
- 인증 필수 API
  - POST /images - 이미지 업로드 (로그인 필요)
  - GET /images - 전체 조회
  - GET /images/{id} - 단건 조회
  - DELETE /images/{id} - 삭제 (본인만)
- CORS 설정
- 에러 처리

기초 문제:
1. 테이블 생성
2. 파일 업로드 API

응용 문제:
3. 조회 API 구현
4. 삭제 API (권한 체크)
5. 내 이미지만 보기 API

도전 문제:
6. 이미지 썸네일 생성
7. 페이징 및 정렬
8. 좋아요 기능

---

## 심화 Day 3: 최종 프로젝트

### 전체 (09:00-17:00)

#### 9-0. 프로젝트 소개 (30분)
- 프로젝트 요구사항 설명
- 데이터베이스 설계
- API 엔드포인트 설계

#### 9-1. 🎯 최종 프로젝트: 미니 블로그 API (6시간)

**기능 요구사항:**

1. **사용자 관리**
   - 회원가입 (이메일, 비밀번호)
   - 로그인 (JWT 발급)
   - 내 정보 조회

2. **게시글 CRUD**
   - 게시글 작성 (로그인 필요)
   - 게시글 목록 조회 (페이징)
   - 게시글 상세 조회
   - 게시글 수정 (본인만)
   - 게시글 삭제 (본인만)

3. **댓글 기능**
   - 댓글 작성 (로그인 필요)
   - 댓글 조회
   - 댓글 삭제 (본인만)

4. **추가 기능 (선택)**
   - 검색 (제목, 내용)
   - 태그 기능
   - 좋아요 기능
   - 프로필 이미지 업로드

**기술 요구사항:**
- FastAPI
- SQLite
- JWT 인증
- Pydantic 모델
- 에러 처리
- CORS 설정
- API 문서화

**진행 방식:**
- 09:30-12:30: 개발 (3시간)
- 13:30-16:00: 개발 (2.5시간)
- 16:00-17:00: 발표 및 피드백 (1시간)

#### 9-2. 프로젝트 발표 (60분)
- 각자 10분 발표
  - 구현한 기능 시연
  - 어려웠던 점
  - 배운 점
- 피드백 및 질의응답

#### 9-3. 과정 회고 (30분)
- 전체 과정 회고
- 향후 학습 방향
  - 배포 (Docker, AWS)
  - 프론트엔드 연동
  - 더 공부할 주제
- 수료

---

## 📚 참고 자료

### 공식 문서
- Python 공식 문서: https://docs.python.org/
- FastAPI 공식 문서: https://fastapi.tiangolo.com/
- Pydantic 공식 문서: https://docs.pydantic.dev/

### 추천 학습 자료
- 점프 투 파이썬 (온라인 무료)
- FastAPI 튜토리얼
- Real Python

### 도구
- Postman (API 테스트)
- DB Browser for SQLite (DB 확인)

---

## 🎓 학습 가이드

### Practice (👉)
- 강사와 함께 1-3분
- 코드를 직접 타이핑하며 따라하기

### Exercise (✏️)
- 파트 종료 후 5-10분
- 2-4문제 혼자 풀기
- 막히면 손들기!

### Problem (🎯)
- 하루 마지막 30-90분
- 종합 문제 혼자 풀기
- 기초 → 응용 → 도전 순서

### 복습의 중요성
- 각 과정 첫날은 복습부터!
- 매일 복습 퀴즈
- 이전 내용 활용한 새 예제
