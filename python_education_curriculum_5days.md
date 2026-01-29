# FastAPI 백엔드 개발 과정

## 🎯 교육 목표

Python 초보자가 FastAPI를 활용한 백엔드 서버를 직접 구축할 수 있는 수준 달성

## 📅 과정 구성

- **기초 과정** (5일, 40시간): FastAPI 사용을 위한 Python 문법
- **응용 과정** (3일, 21시간): 웹 개념과 FastAPI CRUD
- **심화 과정** (3일, 21시간): 인증 및 고급 기능, 실전 프로젝트

※ 각 과정 사이 시간 간격이 있을 수 있음

## ⏰ 일일 시간표 (8교시 체제)

- 1교시: 09:00-09:50 (50분)
- 2교시: 10:00-10:50 (50분)
- 3교시: 11:00-11:50 (50분)
- 4교시: 12:00-12:50 (50분)
- 점심: 12:50-14:00 (70분)
- 5교시: 14:00-14:50 (50분)
- 6교시: 15:00-15:50 (50분)
- 7교시: 16:00-16:50 (50분)
- 8교시: 17:00-17:50 (50분)

---

# 📘 기초 과정 (5일, 40시간)

## FastAPI를 위한 Python 필수 문법

---

## 기초 Day 1: Python 시작 & 기본 자료형

### 1교시 (09:00-09:50): Python과 개발 환경 구축

#### 1-1. Python 소개 (20분)

- Python이란?
- FastAPI와의 관계
- Python의 특징과 장점
- 백엔드 개발에서 Python의 위치

#### 1-2. 개발 환경 구축 (30분)

- Python 설치 및 버전 확인
- VS Code 설치 및 설정
  - Python 확장 설치
  - 테마 설정
- Git 설치 및 버전 확인
- 터미널 기본 사용법
- 👉 Practice: 터미널에서 python 실행
- 👉 Practice: 첫 프로그램 - print("Hello World")
- 👉 Practice: 간단한 계산 출력

### 2교시 (10:00-10:50): 입출력과 변수

#### 2-1. print()와 input() (15분)

- print() 함수 기본
- 👉 Practice: 기본 출력
- 여러 인자 출력 (쉼표 사용)
- 👉 Practice: 여러 값 출력
- input() 함수
- 👉 Practice: 이름 입력받기
- 형변환 (int, float, str)
- 👉 Practice: 숫자 입력받아 계산

#### 2-2. 변수와 타입 (20분)

- 변수란? 변수 할당
- 변수명 작성 규칙 (snake_case)
- 👉 Practice: 변수 만들기
- 👉 Practice: 여러 변수 사용
- type() 함수로 타입 확인
- 👉 Practice: 타입 확인
- 타입 힌트 미리보기
- 👉 Practice: 타입 힌트 써보기

#### 2-3. Exercise (15분)

- ✏️ Exercise: 입출력과 변수 (4문제)

### 3교시 (11:00-11:50): 숫자형

#### 3-1. 숫자형 기본 (15분)

- 정수(int), 실수(float)
- 👉 Practice: 숫자 타입 확인
- 산술 연산자 (+, -, \*, /, //, %, \*\*)
- 👉 Practice: 사칙연산
- 나눗셈 종류 비교
- 👉 Practice: /, //, % 차이

#### 3-2. 복합 연산자 (15분)

- 복합 연산자 (+=, -=, \*=, /=)
- 👉 Practice: 복합 연산자 사용
- 👉 Practice: 카운터 만들기
- 👉 Practice: 계산 누적

#### 3-3. Exercise (20분)

- ✏️ Exercise: 숫자 연산 (5문제)

### 4교시 (12:00-12:50): 문자열 기본

#### 4-1. 문자열 생성 (15분)

- 문자열 생성 ("", '', """ """)
- 👉 Practice: 여러 방법으로 만들기
- 문자열 연산 (+, \*)
- 👉 Practice: 문자열 연결
- 👉 Practice: 문자열 반복
- 문자열 길이 (len)
- 👉 Practice: 문자열 길이 확인

#### 4-2. f-string 포매팅 (20분)

- **f-string만 집중!** (%, format()은 "옛날 방식" 언급만)
- f-string이 필요한 이유
- 👉 Practice: f-string 기본
- 👉 Practice: 변수 포함
- 👉 Practice: 계산식 포함
- 👉 Practice: 자기소개 출력
- 👉 Practice: 영수증 형식

#### 4-3. Exercise (15분)

- ✏️ Exercise: 문자열 기본 (4문제)

### 점심시간 (12:50-14:00)

### 5교시 (14:00-14:50): 문자열 인덱싱과 슬라이싱

#### 5-1. 인덱싱 (20분)

- 인덱스 개념 (0부터 시작)
- 👉 Practice: 문자 하나씩 접근
- 👉 Practice: 첫 글자, 마지막 글자
- 음수 인덱스 (-1부터)
- 👉 Practice: 뒤에서부터 접근
- 👉 Practice: 음수 인덱스 활용

#### 5-2. 슬라이싱 (20분)

- 슬라이싱 [start:end]
- 👉 Practice: 문자열 자르기
- 👉 Practice: 처음부터, 끝까지
- step 사용 [start:end:step]
- 👉 Practice: 2칸씩 건너뛰기
- 👉 Practice: 문자열 거꾸로 ([::-1])

#### 5-3. Exercise (10분)

- ✏️ Exercise: 인덱싱/슬라이싱 (3문제)

### 6교시 (15:00-15:50): 문자열 메서드 1

#### 6-1. 대소문자 변환 (15분)

- upper, lower, capitalize, title
- 👉 Practice: 대소문자 변환
- 👉 Practice: 이름 정규화
- 👉 Practice: 제목 만들기

#### 6-2. 공백 제거 (15분)

- strip, lstrip, rstrip
- 👉 Practice: 입력값 정리
- 👉 Practice: 여러 줄 처리
- 👉 Practice: 사용자 입력 정제

#### 6-3. Exercise (20분)

- ✏️ Exercise: 문자열 메서드 1 (4문제)

### 7교시 (16:00-16:50): 문자열 메서드 2 + Boolean

#### 7-1. split과 join (15분) ⭐

- split으로 나누기
- 👉 Practice: 문자열을 리스트로
- 👉 Practice: CSV 데이터 파싱
- join으로 합치기
- 👉 Practice: 리스트를 문자열로

#### 7-2. 기타 메서드 (10분)

- replace, find, startswith, endswith
- 👉 Practice: 문자열 변경
- 👉 Practice: 이메일 검증 (간단)

#### 7-3. Boolean (12분)

- True/False
- 👉 Practice: Boolean 값 확인
- 비교 연산자 (==, !=, >, <, >=, <=)
- 👉 Practice: 값 비교
- 논리 연산자 (and, or, not)
- 👉 Practice: 조건 조합

#### 7-4. Exercise (13분)

- ✏️ Exercise: 문자열 메서드 2 + Boolean (4문제)

### 8교시 (17:00-17:50): 🎯 Day 1 종합 실습

**주제: 텍스트 처리 프로그램**

**기초 문제 (15분):**

1. 두 숫자를 입력받아 사칙연산 결과 출력
2. 이름과 나이 입력받아 f-string으로 자기소개 출력
3. 주민번호 입력받아 앞자리 추출 (슬라이싱)
4. 문자열 거꾸로 출력하기

**응용 문제 (20분):** 5. 여러 줄 문자열(""")로 영수증 만들기 6. 이메일 주소 유효성 간단 체크 (@ 포함, .com 끝) 7. CSV 형식 문자열 파싱 ("이름,나이,이메일") 8. 입력받은 문장의 단어 개수 세기

**도전 문제 (15분):** 9. 온도 변환기 (섭씨 ↔ 화씨)

- 입력: "25C" → 출력: "77F"
- 입력: "77F" → 출력: "25C"

10. 비밀번호 강도 체크 (길이, 대문자, 숫자 포함 여부)

---

## 기초 Day 2: 자료형 완성 (리스트, 딕셔너리)

### 1교시 (09:00-09:50): Day 1 복습 ⏮️

#### 복습 퀴즈 (20분)

- 변수와 타입 확인
- 문자열 인덱싱/슬라이싱
- f-string 포매팅
- 문자열 메서드
- Boolean과 비교 연산자

#### 복습 Practice (30분)

- 👉 Practice: 어제 배운 내용 재작성
  - 변수 선언과 타입 힌트
  - f-string으로 정보 출력
  - 문자열 슬라이싱
  - 문자열 메서드 조합
  - Boolean 조건
- 👉 Practice: 헷갈렸던 부분 재확인
- 질의응답

### 2교시 (10:00-10:50): 리스트 기본

#### 2-1. 리스트 생성 (20분)

- 리스트란? (FastAPI 응답에서 많이 사용!)
- 생성 방법 []
- 👉 Practice: 빈 리스트, 숫자 리스트
- 👉 Practice: 문자열 리스트, 혼합 리스트
- 리스트 연산 (+, \*)
- 👉 Practice: 리스트 합치기
- 👉 Practice: 리스트 반복

#### 2-2. 리스트 접근 (20분)

- 리스트 인덱싱
- 👉 Practice: 요소 접근
- 👉 Practice: 첫 번째, 마지막 요소
- 리스트 슬라이싱
- 👉 Practice: 리스트 자르기
- 👉 Practice: 부분 리스트 추출
- len 함수
- 👉 Practice: 리스트 크기 확인

#### 2-3. Exercise (10분)

- ✏️ Exercise: 리스트 기본 (3문제)

### 3교시 (11:00-11:50): 리스트 수정

#### 3-1. 요소 추가 (15분)

- append로 끝에 추가
- 👉 Practice: 할 일 추가하기
- insert로 중간에 삽입
- 👉 Practice: 특정 위치에 삽입
- extend로 여러 요소 추가
- 👉 Practice: 리스트 확장

#### 3-2. 요소 삭제 (12분)

- remove로 값으로 삭제
- 👉 Practice: 특정 값 삭제
- pop으로 인덱스로 삭제
- 👉 Practice: 마지막 요소 제거
- del로 삭제
- 👉 Practice: 여러 요소 삭제

#### 3-3. 요소 수정 (8분)

- 인덱스로 수정
- 👉 Practice: 할 일 수정하기
- 슬라이싱으로 여러 요소 수정
- 👉 Practice: 범위 수정

#### 3-4. Exercise (15분)

- ✏️ Exercise: 리스트 수정 (5문제)

### 4교시 (12:00-12:50): 리스트 메서드와 내장함수

#### 4-1. 리스트 메서드 (15분)

- sort로 정렬
- 👉 Practice: 오름차순, 내림차순
- reverse로 뒤집기
- 👉 Practice: 리스트 역순
- count로 개수 세기
- 👉 Practice: 특정 값 개수
- index로 위치 찾기
- 👉 Practice: 값의 위치

#### 4-2. in 연산자 (8분)

- in으로 포함 여부 확인
- 👉 Practice: 값 존재 확인
- 👉 Practice: 회원 여부 체크

#### 4-3. 내장 함수 (12min)

- sum, max, min, len
- 👉 Practice: 통계 구하기
- 👉 Practice: 점수 분석
- 👉 Practice: 문자열에서도 사용 (max, min)

#### 4-4. Exercise (15분)

- ✏️ Exercise: 리스트 메서드/내장함수 (5문제)

### 점심시간 (12:50-14:00)

### 5교시 (14:00-14:50): 튜플, 집합, None + 딕셔너리 시작

#### 5-1. 튜플 (8분)

- 튜플의 특징 (변경 불가)
- 튜플 생성 ()
- 👉 Practice: 좌표 데이터 (x, y)
- 👉 Practice: 튜플 언패킹

#### 5-2. 집합 (5분)

- 집합의 특징 (중복 불가, 순서 없음)
- 집합 생성 {}
- 👉 Practice: 중복 제거하기

#### 5-3. None (2분)

- None의 의미와 용도
- 👉 Practice: None 체크

#### 5-4. 딕셔너리 소개 (25분)

- 딕셔너리란? Key-Value 개념
- **JSON과 딕셔너리의 관계** (FastAPI의 핵심!)
- 왜 딕셔너리가 중요한가?
- 딕셔너리 생성 {}
- 👉 Practice: 첫 딕셔너리 만들기
- 👉 Practice: 사용자 정보 딕셔너리 (name, age, email)
- 👉 Practice: 상품 정보 딕셔너리 (name, price, stock)
- Key로 Value 접근
- 👉 Practice: 정보 가져오기

#### 5-5. Exercise (10분)

- ✏️ Exercise: 튜플/집합/딕셔너리 기본 (3문제)

### 6교시 (15:00-15:50): 딕셔너리 기본

#### 6-1. 딕셔너리 접근 (15분)

- [] 대괄호로 접근
- 👉 Practice: 값 가져오기
- get() 메서드 (안전한 접근)
- 👉 Practice: 없는 키 처리
- 👉 Practice: 기본값 설정
- KeyError 이해
- 👉 Practice: 에러 확인

#### 6-2. 딕셔너리 조작 (20min)

- 값 추가하기
- 👉 Practice: 새 정보 추가
- 👉 Practice: 여러 정보 추가
- 값 수정하기
- 👉 Practice: 정보 업데이트
- 값 삭제하기 (del, pop)
- 👉 Practice: 정보 삭제
- 👉 Practice: pop으로 안전하게 삭제

#### 6-3. Exercise (15분)

- ✏️ Exercise: 딕셔너리 CRUD (5문제)

### 7교시 (16:00-16:50): 딕셔너리 심화 + 언패킹 ⭐⭐⭐

#### 7-1. 딕셔너리 메서드 (15분)

- keys(), values(), items()
- 👉 Practice: 모든 키 확인
- 👉 Practice: 모든 값 확인
- 👉 Practice: Key-Value 쌍으로 출력
- in 연산자 (키 존재 확인)
- 👉 Practice: 키 검색
- 👉 Practice: 안전한 접근 패턴

#### 7-2. 딕셔너리 언패킹 (20분) ⭐⭐⭐

- \*\* 언패킹이란?
- **왜 중요한가?** (FastAPI에서 필수!)
- 👉 Practice: 함수 호출 시 언패킹

  ```python
  user_data = {"name": "철수", "age": 25}

  def create_user(name, age):
      return {"name": name, "age": age}

  user = create_user(**user_data)
  ```

- 👉 Practice: 딕셔너리 병합 (매우 유용!)

  ```python
  default_config = {"role": "user", "active": True}
  user_input = {"name": "철수", "age": 25}

  user = {**default_config, **user_input}
  # {"role": "user", "active": True, "name": "철수", "age": 25}
  ```

- 👉 Practice: 설정 덮어쓰기

  ```python
  config = {"timeout": 30, "retry": 3}
  custom = {"timeout": 60}

  final = {**config, **custom}  # timeout이 60으로 덮어씌워짐
  ```

- 👉 Practice: 여러 딕셔너리 병합

  ```python
  user_basic = {"name": "철수"}
  user_contact = {"email": "test@test.com", "phone": "010-1234-5678"}
  user_role = {"role": "admin", "active": True}

  user = {**user_basic, **user_contact, **user_role}
  ```

#### 7-3. Exercise (15분)

- ✏️ Exercise: 딕셔너리 심화 + 언패킹 (5문제)

### 8교시 (17:00-17:50): 🎯 Day 2 종합 실습

#### 8-1. 리스트 + 딕셔너리 조합 (10분)

- **딕셔너리의 리스트** (FastAPI 응답 형태!)
- 👉 Practice: 사용자 목록 만들기
  ```python
  users = [
      {"name": "철수", "age": 25, "email": "chul@test.com"},
      {"name": "영희", "age": 23, "email": "young@test.com"},
      {"name": "민수", "age": 27, "email": "min@test.com"}
  ]
  ```
- 👉 Practice: 상품 목록 만들기
- 👉 Practice: for문으로 순회 (간단히 맛보기)
  ```python
  for user in users:
      print(user["name"])
  ```

#### 8-2. 종합 실습 (40분)

**주제: 학생 성적 관리 시스템**

**기초 문제 (15분):**

1. 학생 정보 딕셔너리 3개 만들기
   - 이름, 국어, 영어, 수학 점수 포함
2. 학생들을 리스트에 추가하기
3. 모든 학생 정보 출력 (for문 사용)

**응용 문제 (15분):** 4. 특정 학생 찾기 (이름으로 검색) 5. 각 학생의 평균 점수 계산 6. 80점 이상 학생만 필터링 7. 과목별 전체 평균 계산

**도전 문제 (10분):** 8. 딕셔너리 언패킹으로 학생 생성 함수 만들기

```python
def create_student(name, korean, english, math):
    return {"name": name, "korean": korean,
            "english": english, "math": math}

student_data = {"name": "철수", "korean": 85, "english": 90, "math": 88}
student = create_student(**student_data)
```

9. 딕셔너리 병합으로 기본 정보 추가
   ```python
   default_info = {"grade": 1, "class": "A"}
   student_score = {"name": "철수", "score": 85}
   student = {**default_info, **student_score}
   ```
10. 튜플로 (이름, 평균) 쌍 만들기

---

## 기초 Day 3: 흐름 제어 (if, for, while, 컴프리헨션)

### 1교시 (09:00-09:50): Day 2 복습 ⏮️

#### 복습 퀴즈 (20분)

- 리스트 조작 (append, remove, pop)
- 리스트 메서드 (sort, reverse, count)
- 딕셔너리 CRUD
- 딕셔너리 언패킹
- 리스트 + 딕셔너리 조합

#### 복습 Practice (30분)

- 👉 Practice: 리스트 종합 연습
  - 리스트 생성, 수정, 정렬
  - 통계 계산
- 👉 Practice: 딕셔너리 종합 연습
  - CRUD 전체
  - 언패킹 활용
- 👉 Practice: 리스트 + 딕셔너리
  - 사용자 목록 만들기
  - 정보 추가/수정/삭제
- 질의응답

### 2교시 (10:00-10:50): if문 기본

#### 2-1. if문 소개 (18분)

- if문이 필요한 이유
- if문의 구조 (들여쓰기 4칸, 콜론!)
- 👉 Practice: 기본 if문
  ```python
  age = 20
  if age >= 18:
      print("성인입니다")
  ```
- 비교 연산자 복습
- 👉 Practice: 나이 확인
- 👉 Practice: 점수 확인

#### 2-2. if-else (12min)

- if-else 구조
- 👉 Practice: 짝수/홀수 판별
- 👉 Practice: 합격/불합격 판정
- 👉 Practice: 양수/음수 판별

#### 2-3. elif (10min)

- elif로 여러 조건 처리
- 👉 Practice: 성적 등급 계산 (A, B, C, D, F)
- 👉 Practice: 계절 판별 (봄, 여름, 가을, 겨울)

#### 2-4. Exercise (10min)

- ✏️ Exercise: if-else-elif (3문제)

### 3교시 (11:00-11:50): if문 심화

#### 3-1. 복합 조건 (20min)

- and 연산자
- 👉 Practice: 두 조건 모두 만족
  ```python
  age = 25
  has_license = True
  if age >= 18 and has_license:
      print("운전 가능")
  ```
- or 연산자
- 👉 Practice: 하나라도 만족
- not 연산자
- 👉 Practice: 조건 부정
- 복합 조건 조합
- 👉 Practice: 로그인 검증 (아이디 and 비밀번호)
- 👉 Practice: 할인 조건 (회원 or 쿠폰)

#### 3-2. in 연산자 활용 (15분)

- 리스트에서 in 사용
- 👉 Practice: 회원 여부 확인
  ```python
  members = ["철수", "영희", "민수"]
  name = "철수"
  if name in members:
      print("회원입니다")
  ```
- 딕셔너리 키 확인
- 👉 Practice: 키 존재 여부
- 문자열에서 in 사용
- 👉 Practice: 부분 문자열 검색

#### 3-3. Exercise (15분)

- ✏️ Exercise: if문 심화 (5문제)

### 4교시 (12:00-12:50): for문 기본

#### 4-1. for문 소개 (12분)

- 반복문이 필요한 이유
- for문의 구조 (in, 콜론, 들여쓰기)
- 👉 Practice: 리스트 순회
  ```python
  fruits = ["사과", "바나나", "오렌지"]
  for fruit in fruits:
      print(fruit)
  ```
- 👉 Practice: 모든 요소 출력

#### 4-2. 다양한 순회 (12분)

- 문자열 순회
- 👉 Practice: 문자 하나씩 출력
- 👉 Practice: 모음 개수 세기
- 튜플 순회
- 👉 Practice: 좌표 출력

#### 4-3. range 함수 (16분)

- range(n)
- 👉 Practice: 0부터 9까지
- 👉 Practice: 1부터 10까지 (range(1, 11))
- range(start, end)
- 👉 Practice: 특정 범위 출력
- range(start, end, step)
- 👉 Practice: 2씩 증가
- 👉 Practice: 역순 반복 (range(10, 0, -1))

#### 4-4. Exercise (10분)

- ✏️ Exercise: for문 기본 (3문제)

### 점심시간 (12:50-14:00)

### 5교시 (14:00-14:50): for문 심화 1 - 딕셔너리

#### 5-1. 딕셔너리 keys() 순회 (10분)

- keys()로 모든 키 순회
- 👉 Practice: 키만 출력
- 👉 Practice: 키로 값 접근
  ```python
  user = {"name": "철수", "age": 25, "email": "test@test.com"}
  for key in user.keys():
      print(f"{key}: {user[key]}")
  ```

#### 5-2. 딕셔너리 values() 순회 (5분)

- values()로 모든 값 순회
- 👉 Practice: 값만 출력
- 👉 Practice: 점수 합계

#### 5-3. 딕셔너리 items() 순회 (10min) ⭐

- **items()가 가장 유용!**
- 👉 Practice: Key-Value 쌍으로 출력
  ```python
  user = {"name": "철수", "age": 25, "email": "test@test.com"}
  for key, value in user.items():
      print(f"{key}: {value}")
  ```
- 👉 Practice: 딕셔너리 정보 표시

#### 5-4. 딕셔너리 리스트 순회 (15min) ⭐⭐

- **FastAPI 응답 형태!**
- 👉 Practice: 사용자 목록 처리

  ```python
  users = [
      {"name": "철수", "age": 25},
      {"name": "영희", "age": 23},
      {"name": "민수", "age": 27}
  ]

  for user in users:
      print(f"{user['name']}님은 {user['age']}살입니다")
  ```

- 👉 Practice: 상품 목록 출력
- 👉 Practice: 조건에 맞는 항목 찾기

#### 5-5. Exercise (10min)

- ✏️ Exercise: 딕셔너리 순회 (3문제)

### 6교시 (15:00-15:50): for문 심화 2 - enumerate, 중첩, 제어

#### 6-1. enumerate (15분)

- enumerate로 인덱스와 값 동시에
- 👉 Practice: 순서 번호 매기기
  ```python
  fruits = ["사과", "바나나", "오렌지"]
  for index, fruit in enumerate(fruits):
      print(f"{index + 1}. {fruit}")
  ```
- 👉 Practice: 순위 표시
- 시작 번호 지정 (enumerate(list, start=1))
- 👉 Practice: 1부터 시작하는 번호

#### 6-2. 중첩 for문 (20분)

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
          print(num, end=" ")
      print()
  ```

- 👉 Practice: 구구단 전체 출력 (2단~9단)
- 👉 Practice: 좌표 쌍 만들기
  ```python
  for x in range(3):
      for y in range(3):
          print(f"({x}, {y})")
  ```

#### 6-3. break와 continue (10분)

- break로 반복 탈출
- 👉 Practice: 검색 후 중단
- continue로 건너뛰기
- 👉 Practice: 특정 값 제외

#### 6-4. Exercise (5분)

- ✏️ Exercise: enumerate/중첩/제어 (2문제)

### 7교시 (16:00-16:50): while & 리스트 컴프리헨션

#### 7-1. while문 (15분)

- while문 기본
- 👉 Practice: 조건이 True일 동안 반복
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```
- while과 break
- 👉 Practice: 사용자 입력 반복 (종료 조건)
  ```python
  while True:
      answer = input("계속하시겠습니까? (y/n): ")
      if answer == 'n':
          break
  ```
- 무한 루프 주의!

#### 7-2. 리스트 컴프리헨션 (20분)

- 리스트 컴프리헨션이란?
- **왜 사용하나?** (FastAPI에서 유용!)
- 👉 Practice: 기본 형태

  ```python
  # for문 방식
  numbers = []
  for i in range(10):
      numbers.append(i)

  # 컴프리헨션 방식
  numbers = [i for i in range(10)]
  ```

- 조건부 리스트 컴프리헨션
- 👉 Practice: 짝수만 필터링
  ```python
  numbers = [i for i in range(10) if i % 2 == 0]
  ```
- 👉 Practice: 제곱 리스트
  ```python
  squares = [i**2 for i in range(10)]
  ```
- 딕셔너리 리스트 처리
- 👉 Practice: 이름만 추출
  ```python
  users = [{"name": "철수", "age": 25}, {"name": "영희", "age": 23}]
  names = [user["name"] for user in users]
  ```
- 👉 Practice: 조건부 추출
  ```python
  adults = [user["name"] for user in users if user["age"] >= 20]
  ```

#### 7-3. Exercise (15분)

- ✏️ Exercise: while/컴프리헨션 (5문제)

### 8교시 (17:00-17:50): 🎯 Day 3 종합 실습

**주제: 학생 성적 관리 시스템 (제어문 활용)**

**기초 문제 (15분):**

1. 학생 정보 딕셔너리 3개 만들기
2. for문으로 모든 학생 정보 출력
3. 특정 학생 찾기 (이름 검색 + break)
4. if문으로 합격/불합격 표시 (평균 60점 이상)

**응용 문제 (20분):** 5. for + if로 80점 이상 학생만 필터링 6. enumerate로 등수 매기기 7. 과목별 전체 평균 계산

- 중첩 for문 또는 컴프리헨션 사용

8. 리스트 컴프리헨션으로 우등생 목록 만들기 (평균 90점 이상)

**도전 문제 (15분):** 9. while문으로 메뉴 시스템 만들기

```
1. 학생 추가
2. 학생 조회 (이름 입력)
3. 전체 평균 보기
4. 종료
```

10. 성적순 정렬 (+ 동점자 처리)
    - sort 사용
    - 평균이 같으면 이름순
11. 2차원 리스트로 성적표 출력
    ```
    이름    국어  영어  수학  평균
    ============================
    철수    85   90   88   87.7
    영희    92   88   95   91.7
    ```

---

## 기초 Day 4: 함수와 모듈

### 1교시 (09:00-09:50): Day 3 복습 ⏮️

#### 복습 퀴즈 (20분)

- if, for, while
- 리스트 컴프리헨션
- 딕셔너리 순회 (items)
- break, continue
- enumerate

#### 복습 Practice (30분)

- 👉 Practice: 흐름 제어 종합
  - if-elif-else 복잡한 조건
  - for문으로 딕셔너리 리스트 처리
  - 리스트 컴프리헨션으로 필터링
  - 중첩 for문
- 👉 Practice: 헷갈렸던 부분 재확인
- 질의응답

### 2교시 (10:00-10:50): 함수 기본

#### 2-1. 함수 소개 (20분)

- 함수가 필요한 이유
  - 코드 재사용
  - 구조화
  - 유지보수
- 함수의 구조 (def, 매개변수, return)
- 👉 Practice: 첫 함수 만들기

  ```python
  def greet():
      print("안녕하세요!")

  greet()  # 함수 호출
  ```

- 👉 Practice: 인사 함수 (이름 받기)
  ```python
  def greet(name):
      print(f"안녕하세요, {name}님!")
  ```
- 함수 호출과 반환값
- 👉 Practice: 계산 함수

  ```python
  def add(a, b):
      return a + b

  result = add(3, 5)
  print(result)  # 8
  ```

#### 2-2. 여러 함수 만들기 (20분)

- 👉 Practice: 더하기, 빼기, 곱하기, 나누기 함수
- 👉 Practice: 문자열 처리 함수 (대문자 변환, 역순)
- 👉 Practice: 리스트 처리 함수 (합계, 평균)

#### 2-3. Exercise (10분)

- ✏️ Exercise: 함수 기본 (3문제)

### 3교시 (11:00-11:50): 매개변수와 인자

#### 3-1. 위치 인자 (12분)

- 위치 인자란?
- 👉 Practice: 여러 매개변수 함수

  ```python
  def introduce(name, age, city):
      print(f"{name}님은 {age}살이고 {city}에 삽니다")

  introduce("철수", 25, "서울")
  ```

- 순서가 중요!
- 👉 Practice: 순서 바꿔서 호출

#### 3-2. 키워드 인자 (10min)

- 키워드 인자란?
- 👉 Practice: 키워드로 호출
  ```python
  introduce(age=25, name="철수", city="서울")  # 순서 무관
  ```
- 👉 Practice: 위치 + 키워드 혼합

#### 3-3. 기본값 (13분)

- 기본값 설정
- 👉 Practice: 기본값이 있는 함수

  ```python
  def greet(name, greeting="안녕하세요"):
      print(f"{greeting}, {name}님!")

  greet("철수")  # 안녕하세요, 철수님!
  greet("영희", "반갑습니다")  # 반갑습니다, 영희님!
  ```

- 👉 Practice: 선택적 매개변수
  ```python
  def create_user(name, age, email=None):
      user = {"name": name, "age": age}
      if email:
          user["email"] = email
      return user
  ```

#### 3-4. Exercise (15분)

- ✏️ Exercise: 매개변수 활용 (5문제)

### 4교시 (12:00-12:50): 함수의 다양한 형태

#### 4-1. 여러 반환값 (12분)

- 튜플로 여러 값 반환
- 👉 Practice: 몫과 나머지 반환

  ```python
  def divide(a, b):
      quotient = a // b
      remainder = a % b
      return quotient, remainder

  q, r = divide(10, 3)
  print(f"몫: {q}, 나머지: {r}")
  ```

- 👉 Practice: 최대값과 최소값 동시 반환

#### 4-2. 딕셔너리 반환 (18min) ⭐

- **API 응답 형태!**
- 👉 Practice: 사용자 정보 반환

  ```python
  def create_user(name, age, email):
      return {
          "name": name,
          "age": age,
          "email": email,
          "created_at": "2024-01-28"
      }

  user = create_user("철수", 25, "test@test.com")
  ```

- 👉 Practice: 상품 정보 반환
- 👉 Practice: 통계 정보 반환
  ```python
  def calculate_stats(numbers):
      return {
          "count": len(numbers),
          "sum": sum(numbers),
          "avg": sum(numbers) / len(numbers),
          "max": max(numbers),
          "min": min(numbers)
      }
  ```

#### 4-3. 리스트 처리 함수 (10분)

- 👉 Practice: 리스트 필터링 함수
- 👉 Practice: 리스트 변환 함수

#### 4-4. Exercise (10분)

- ✏️ Exercise: 함수 형태 (3문제)

### 점심시간 (12:50-14:00)

### 5교시 (14:00-14:50): 타입 힌트 (기본 + typing 모듈) ⭐⭐⭐

#### 5-1. 기본 타입 힌트 (15분)

- 타입 힌트가 필요한 이유
  - 코드 가독성
  - VS Code 자동완성
  - 버그 예방
- 매개변수 타입 힌트
- 👉 Practice: int, str, float 타입
  ```python
  def add(a: int, b: int):
      return a + b
  ```
- 반환 타입 힌트 (->)
- 👉 Practice: 완전한 타입 힌트
  ```python
  def greet(name: str) -> str:
      return f"안녕하세요, {name}님!"
  ```

#### 5-2. typing 모듈 (20분) ⭐⭐⭐

- **FastAPI에서 필수!**
- typing 모듈 import
- **Optional** - None도 허용
- 👉 Practice: Optional[str]

  ```python
  from typing import Optional

  def greet(name: Optional[str] = None) -> str:
      if name:
          return f"안녕하세요, {name}님!"
      return "안녕하세요!"
  ```

- **List** - 리스트 타입
- 👉 Practice: List[int], List[str]

  ```python
  from typing import List

  def sum_numbers(numbers: List[int]) -> int:
      return sum(numbers)

  def get_names(users: List[str]) -> List[str]:
      return [name.upper() for name in users]
  ```

- **Dict** - 딕셔너리 타입
- 👉 Practice: Dict[str, int], Dict[str, str]

  ```python
  from typing import Dict

  def count_words(text: str) -> Dict[str, int]:
      words = text.split()
      return {"count": len(words)}
  ```

- **복합 타입** (FastAPI 스타일!)
- 👉 Practice: List[Dict[str, str]]

  ```python
  from typing import List, Dict

  def get_users() -> List[Dict[str, str]]:
      return [
          {"name": "철수", "email": "chul@test.com"},
          {"name": "영희", "email": "young@test.com"}
      ]
  ```

- 👉 Practice: Optional과 List 조합

  ```python
  from typing import List, Optional, Dict

  def find_user(
      users: List[Dict[str, str]],
      name: str
  ) -> Optional[Dict[str, str]]:
      for user in users:
          if user["name"] == name:
              return user
      return None
  ```

#### 5-3. Exercise (15분)

- ✏️ Exercise: 타입 힌트 (5문제)

### 6교시 (15:00-15:50): 람다 함수 + 모듈 맛보기

#### 6-1. 람다 함수 (25분) ⭐⭐

- 람다가 필요한 이유
- 👉 Practice: 간단한 람다
  ```python
  add = lambda x, y: x + y
  result = add(3, 5)  # 8
  ```
- **sorted에서 람다** (FastAPI에서 자주!)
- 👉 Practice: 숫자 리스트 정렬
  ```python
  numbers = [5, 2, 8, 1, 9]
  sorted_numbers = sorted(numbers, reverse=True)
  ```
- 👉 Practice: 딕셔너리 리스트 정렬 ⭐⭐⭐

  ```python
  users = [
      {"name": "철수", "age": 25},
      {"name": "영희", "age": 23},
      {"name": "민수", "age": 27}
  ]

  # 나이순 정렬
  sorted_by_age = sorted(users, key=lambda x: x['age'])

  # 이름순 정렬
  sorted_by_name = sorted(users, key=lambda x: x['name'])

  # 나이 역순
  sorted_desc = sorted(users, key=lambda x: x['age'], reverse=True)
  ```

- 👉 Practice: 여러 조건 정렬

  ```python
  # 점수 내림차순, 같으면 이름 오름차순
  students = [
      {"name": "철수", "score": 85},
      {"name": "영희", "score": 90},
      {"name": "민수", "score": 85}
  ]

  sorted_students = sorted(
      students,
      key=lambda x: (-x['score'], x['name'])
  )
  ```

- filter에서 람다
- 👉 Practice: 조건 필터링

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

  adults = list(filter(lambda x: x['age'] >= 20, users))
  ```

#### 6-2. 모듈 맛보기 (15분)

- 모듈이란? (FastAPI도 모듈!)
- import 문
- 👉 Practice: random 모듈 (10분)

  ```python
  import random

  # 랜덤 숫자
  num = random.randint(1, 10)

  # 리스트에서 랜덤 선택
  fruits = ["사과", "바나나", "오렌지"]
  choice = random.choice(fruits)
  ```

- 👉 Practice: datetime 모듈 (5분)

  ```python
  from datetime import datetime

  # 현재 시간
  now = datetime.now()
  print(now)

  # 포매팅
  formatted = now.strftime("%Y-%m-%d %H:%M:%S")
  ```

#### 6-3. Exercise (10분)

- ✏️ Exercise: 람다/모듈 (3문제)

### 7교시 (16:00-16:50): JSON & \*args/\*\*kwargs

#### 7-1. json 모듈 (25분) ⭐⭐⭐

- **FastAPI에서 핵심!**
- JSON이 중요한 이유
- 딕셔너리와 JSON의 관계
- 👉 Practice: 딕셔너리 → JSON 문자열

  ```python
  import json

  user = {"name": "철수", "age": 25, "email": "test@test.com"}
  json_str = json.dumps(user, ensure_ascii=False, indent=2)
  print(json_str)
  ```

- 👉 Practice: JSON 문자열 → 딕셔너리
  ```python
  json_str = '{"name": "철수", "age": 25}'
  user = json.loads(json_str)
  print(user["name"])  # 철수
  ```
- 👉 Practice: 리스트 + 딕셔너리 JSON 변환

  ```python
  users = [
      {"name": "철수", "age": 25},
      {"name": "영희", "age": 23}
  ]

  json_str = json.dumps(users, ensure_ascii=False, indent=2)
  print(json_str)
  ```

- 👉 Practice: JSON 파일 저장
  ```python
  with open("users.json", "w", encoding="utf-8") as f:
      json.dump(users, f, ensure_ascii=False, indent=2)
  ```
- 👉 Practice: JSON 파일 읽기
  ```python
  with open("users.json", "r", encoding="utf-8") as f:
      users = json.load(f)
  ```

#### 7-2. \*args, \*\*kwargs (15분)

- 가변 인자가 필요한 이유
- \*args (위치 인자 여러 개)
- 👉 Practice: \*args 사용

  ```python
  def sum_all(*args):
      return sum(args)

  print(sum_all(1, 2, 3))  # 6
  print(sum_all(1, 2, 3, 4, 5))  # 15
  ```

- \*\*kwargs (키워드 인자 여러 개)
- 👉 Practice: \*\*kwargs 사용

  ```python
  def create_user(name: str, **kwargs) -> dict:
      user = {"name": name}
      user.update(kwargs)
      return user

  user1 = create_user("철수", age=25, email="test@test.com")
  user2 = create_user("영희", age=23, city="서울", phone="010-1234-5678")
  ```

- 👉 Practice: \*args와 \*\*kwargs 조합

  ```python
  def flexible_function(*args, **kwargs):
      print(f"위치 인자: {args}")
      print(f"키워드 인자: {kwargs}")

  flexible_function(1, 2, 3, name="철수", age=25)
  ```

#### 7-3. Exercise (10min)

- ✏️ Exercise: JSON/\*args/\*\*kwargs (3문제)

### 8교시 (17:00-17:50): 🎯 Day 4 종합 실습

**주제: 성적 처리 함수 라이브러리**

**기초 문제 (15분):**

1. 평균 계산 함수 (타입 힌트 포함)
   ```python
   def calculate_average(scores: List[int]) -> float:
       ...
   ```
2. 등급 판정 함수 (90 이상 A, 80 이상 B, ...)
   ```python
   def get_grade(score: int) -> str:
       ...
   ```
3. 학생 정보 생성 함수 (딕셔너리 반환)
   ```python
   def create_student(name: str, korean: int,
                     english: int, math: int) -> Dict[str, any]:
       ...
   ```

**응용 문제 (20분):** 4. 여러 학생 처리 함수 (List[Dict] 타입)

```python
def process_students(
    students: List[Dict[str, any]]
) -> List[Dict[str, any]]:
    # 각 학생에 평균과 등급 추가
    ...
```

5. 통계 함수 (Optional 사용)
   ```python
   def get_stats(
       students: List[Dict[str, any]],
       subject: Optional[str] = None
   ) -> Dict[str, float]:
       # subject가 None이면 전체 평균, 있으면 해당 과목 통계
       ...
   ```
6. 학생 검색 함수
   ```python
   def find_student(
       students: List[Dict[str, any]],
       name: str
   ) -> Optional[Dict[str, any]]:
       ...
   ```
7. 람다로 학생 정렬 함수
   ```python
   def sort_students(
       students: List[Dict[str, any]],
       key: str = "average"
   ) -> List[Dict[str, any]]:
       # key: "average", "name" 등
       ...
   ```

**도전 문제 (15분):** 8. JSON 저장/불러오기

```python
def save_to_json(students: List[Dict], filename: str) -> None:
    ...

def load_from_json(filename: str) -> List[Dict]:
    ...
```

9. \*\*kwargs로 유연한 학생 생성

   ```python
   def create_student_flexible(name: str, **scores) -> Dict[str, any]:
       # scores에 어떤 과목이든 올 수 있음
       ...

   student1 = create_student_flexible("철수", korean=85, english=90)
   student2 = create_student_flexible("영희", math=95, science=88, history=92)
   ```

10. 모든 함수 조합해서 완전한 성적표 시스템
    - JSON 파일에서 학생 데이터 로드
    - 평균과 등급 계산
    - 정렬
    - 통계 출력
    - 다시 JSON으로 저장

---

## 기초 Day 5: 클래스와 예외 처리

### 1교시 (09:00-09:50): Day 4 복습 ⏮️

#### 복습 퀴즈 (20분)

- 함수 정의와 호출
- 매개변수 (위치, 키워드, 기본값)
- 타입 힌트 (기본 + typing 모듈)
- 람다 함수
- json 모듈
- \*args, \*\*kwargs

#### 복습 Practice (30분)

- 👉 Practice: 함수 재작성
  - 타입 힌트가 있는 함수
  - Optional, List, Dict 사용
- 👉 Practice: 람다로 정렬
  - 딕셔너리 리스트 다양하게 정렬
- 👉 Practice: JSON 변환
  - 딕셔너리 ↔ JSON
- 👉 Practice: \*\*kwargs 활용
  - 유연한 함수 만들기
- 질의응답

### 2교시 (10:00-10:50): 클래스 기본

#### 2-1. 클래스 소개 (15분)

- 클래스가 필요한 이유
- 클래스와 객체의 개념
- **클래스 vs 딕셔너리**
- 👉 Practice: 딕셔너리로 표현
  ```python
  # 딕셔너리 방식
  user1 = {"name": "철수", "age": 25}
  user2 = {"name": "영희", "age": 23}
  ```
- 딕셔너리의 한계
  - 구조 강제 불가
  - 메서드 추가 어려움
  - 타입 체크 어려움

#### 2-2. 첫 클래스 (20분)

- 👉 Practice: 첫 클래스 만들기

  ```python
  class User:
      pass

  user1 = User()
  user2 = User()
  ```

- 인스턴스 생성
- 👉 Practice: 여러 인스턴스
- 👉 Practice: 타입 확인
  ```python
  print(type(user1))  # <class '__main__.User'>
  print(isinstance(user1, User))  # True
  ```
- 👉 Practice: 인스턴스 변수 직접 추가 (비추천)
  ```python
  user1.name = "철수"
  user1.age = 25
  ```

#### 2-3. Exercise (15분)

- ✏️ Exercise: 클래스 기본 (4문제)

### 3교시 (11:00-11:50): 클래스 구조

#### 3-1. **init** 생성자 (20분)

- 생성자의 역할
- 👉 Practice: 생성자 추가

  ```python
  class User:
      def __init__(self, name, age):
          self.name = name
          self.age = age

  user = User("철수", 25)
  print(user.name)  # 철수
  ```

- 👉 Practice: 더 많은 속성
  ```python
  class User:
      def __init__(self, name, age, email):
          self.name = name
          self.age = age
          self.email = email
  ```
- 👉 Practice: 기본값 설정
  ```python
  class User:
      def __init__(self, name, age, role="user"):
          self.name = name
          self.age = age
          self.role = role
  ```

#### 3-2. self의 이해 (20분)

- self가 무엇인가?
- 👉 Practice: self 이해하기

  ```python
  class Counter:
      def __init__(self):
          self.count = 0

      def increment(self):
          self.count += 1

      def get_count(self):
          return self.count

  counter = Counter()
  counter.increment()
  counter.increment()
  print(counter.get_count())  # 2
  ```

- 👉 Practice: Product 클래스

  ```python
  class Product:
      def __init__(self, name, price, stock):
          self.name = name
          self.price = price
          self.stock = stock

  product = Product("노트북", 1000000, 10)
  ```

#### 3-3. Exercise (10min)

- ✏️ Exercise: 생성자와 self (3문제)

### 4교시 (12:00-12:50): 메서드와 타입 힌트

#### 4-1. 메서드 (20분)

- 메서드란?
- 👉 Practice: 메서드 추가

  ```python
  class User:
      def __init__(self, name: str, age: int):
          self.name = name
          self.age = age

      def greet(self) -> str:
          return f"안녕하세요, {self.name}입니다"

      def is_adult(self) -> bool:
          return self.age >= 18

  user = User("철수", 25)
  print(user.greet())  # 안녕하세요, 철수입니다
  print(user.is_adult())  # True
  ```

- 👉 Practice: 계산 메서드
  ```python
  class Product:
      def __init__(self, name: str, price: int, stock: int):
          self.name = name
          self.price = price
          self.stock = stock

      def total_value(self) -> int:
          return self.price * self.stock

      def is_available(self) -> bool:
          return self.stock > 0
  ```
- 👉 Practice: 정보 출력 메서드
  ```python
  def display_info(self) -> None:
      print(f"상품: {self.name}")
      print(f"가격: {self.price}원")
      print(f"재고: {self.stock}개")
  ```

#### 4-2. 클래스 타입 힌트 (20분)

- 클래스에 타입 힌트 적용
- 👉 Practice: 완전한 타입 힌트 클래스
  ```python
  class User:
      def __init__(self, name: str, age: int, email: str):
          self.name = name
          self.age = age
          self.email = email

      def to_dict(self) -> dict:
          return {
              "name": self.name,
              "age": self.age,
              "email": self.email
          }
  ```
- 👉 Practice: 타입 힌트가 있는 Product

  ```python
  from typing import Optional

  class Product:
      def __init__(
          self,
          name: str,
          price: int,
          stock: int,
          description: Optional[str] = None
      ):
          self.name = name
          self.price = price
          self.stock = stock
          self.description = description
  ```

#### 4-3. Exercise (10min)

- ✏️ Exercise: 메서드/타입힌트 (3문제)

### 점심시간 (12:50-14:00)

### 5교시 (14:00-14:50): 클래스 활용 (언패킹) + 상속 ⭐

#### 5-1. 딕셔너리 언패킹으로 인스턴스 생성 (15분) ⭐⭐⭐

- **FastAPI에서 필수 패턴!**
- 👉 Practice: 기본 언패킹

  ```python
  class User:
      def __init__(self, name: str, age: int, email: str):
          self.name = name
          self.age = age
          self.email = email

  # 딕셔너리 데이터
  user_data = {
      "name": "철수",
      "age": 25,
      "email": "test@test.com"
  }

  # ** 언패킹으로 인스턴스 생성 (Pydantic 스타일!)
  user = User(**user_data)
  ```

- 👉 Practice: JSON에서 클래스로

  ```python
  import json

  # JSON 문자열
  json_str = '{"name": "철수", "age": 25, "email": "test@test.com"}'

  # JSON → 딕셔너리 → 클래스
  data = json.loads(json_str)
  user = User(**data)
  ```

- 👉 Practice: 여러 인스턴스 생성

  ```python
  users_data = [
      {"name": "철수", "age": 25, "email": "chul@test.com"},
      {"name": "영희", "age": 23, "email": "young@test.com"}
  ]

  users = [User(**data) for data in users_data]
  ```

#### 5-2. 인스턴스 리스트 관리 (15분)

- 👉 Practice: 학생 목록 관리

  ```python
  class Student:
      def __init__(self, name: str, korean: int,
                   english: int, math: int):
          self.name = name
          self.korean = korean
          self.english = english
          self.math = math

      def average(self) -> float:
          return (self.korean + self.english + self.math) / 3

  students = [
      Student("철수", 85, 90, 88),
      Student("영희", 92, 88, 95),
      Student("민수", 78, 82, 80)
  ]

  # for문으로 처리
  for student in students:
      print(f"{student.name}: {student.average():.1f}")

  # 정렬
  sorted_students = sorted(students, key=lambda s: s.average(), reverse=True)
  ```

- 👉 Practice: 메서드로 리스트 반환

  ```python
  def to_dict(self) -> dict:
      return {
          "name": self.name,
          "korean": self.korean,
          "english": self.english,
          "math": self.math,
          "average": self.average()
      }

  # 딕셔너리 리스트로 변환
  students_dict = [s.to_dict() for s in students]
  ```

#### 5-3. 상속 기초 (8분)

- 상속이란?
- 👉 Practice: Animal → Dog

  ```python
  class Animal:
      def __init__(self, name: str):
          self.name = name

      def speak(self) -> str:
          return "소리를 냅니다"

  class Dog(Animal):
      def speak(self) -> str:
          return "멍멍!"

  dog = Dog("뽀삐")
  print(dog.name)  # 뽀삐
  print(dog.speak())  # 멍멍!
  ```

- 👉 Practice: FastAPI 미리보기

  ```python
  # Pydantic BaseModel 스타일
  class BaseModel:
      def to_dict(self) -> dict:
          return self.__dict__

  class User(BaseModel):
      def __init__(self, name: str, age: int):
          self.name = name
          self.age = age

  user = User("철수", 25)
  print(user.to_dict())  # {'name': '철수', 'age': 25}
  ```

#### 5-4. Exercise (12min)

- ✏️ Exercise: 활용/상속 (4문제)

### 6교시 (15:00-15:50): 예외 처리 기본

#### 6-1. 예외란? (10분)

- 에러와 예외의 차이
- 예외 처리가 필요한 이유
- 👉 Practice: 에러 발생시켜보기

  ```python
  # ZeroDivisionError
  result = 10 / 0

  # IndexError
  numbers = [1, 2, 3]
  print(numbers[10])

  # KeyError
  user = {"name": "철수"}
  print(user["age"])
  ```

#### 6-2. try-except 기본 (18분)

- try-except 구조
- 👉 Practice: 기본 예외 처리
  ```python
  try:
      result = 10 / 0
  except:
      print("에러가 발생했습니다!")
  ```
- 👉 Practice: 사용자 입력 검증
  ```python
  try:
      age = int(input("나이를 입력하세요: "))
      print(f"당신의 나이는 {age}살입니다")
  except:
      print("숫자를 입력해주세요!")
  ```
- 👉 Practice: 계산기
  ```python
  try:
      a = int(input("첫 번째 숫자: "))
      b = int(input("두 번째 숫자: "))
      result = a / b
      print(f"결과: {result}")
  except:
      print("계산 중 오류가 발생했습니다")
  ```

#### 6-3. 특정 예외 처리 (12min)

- ValueError, KeyError, IndexError, ZeroDivisionError
- 👉 Practice: 여러 except
  ```python
  try:
      age = int(input("나이: "))
      print(10 / age)
  except ValueError:
      print("숫자를 입력해주세요")
  except ZeroDivisionError:
      print("0으로 나눌 수 없습니다")
  ```
- 👉 Practice: 딕셔너리 접근

  ```python
  user = {"name": "철수", "age": 25}

  try:
      email = user["email"]
  except KeyError:
      print("이메일 정보가 없습니다")
  ```

- 👉 Practice: 에러 메시지 출력
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      print(f"에러 발생: {e}")
  ```

#### 6-4. Exercise (10min)

- ✏️ Exercise: try-except (3문제)

### 7교시 (16:00-16:50): 예외 처리 심화

#### 7-1. raise (18min)

- raise가 필요한 이유
- 👉 Practice: 조건 검증

  ```python
  def set_age(age: int) -> int:
      if age < 0:
          raise ValueError("나이는 0 이상이어야 합니다")
      if age > 150:
          raise ValueError("나이가 너무 많습니다")
      return age

  try:
      age = set_age(-5)
  except ValueError as e:
      print(f"에러: {e}")
  ```

- 👉 Practice: 함수에서 raise
  ```python
  def create_user(name: str, age: int) -> dict:
      if not name:
          raise ValueError("이름은 필수입니다")
      if age < 0:
          raise ValueError("나이는 0 이상이어야 합니다")

      return {"name": name, "age": age}
  ```
- 👉 Practice: 클래스에서 raise
  ```python
  class Product:
      def __init__(self, name: str, price: int, stock: int):
          if price < 0:
              raise ValueError("가격은 0 이상이어야 합니다")
          if stock < 0:
              raise ValueError("재고는 0 이상이어야 합니다")

          self.name = name
          self.price = price
          self.stock = stock

      def sell(self, quantity: int) -> None:
          if quantity > self.stock:
              raise ValueError("재고가 부족합니다")
          self.stock -= quantity
  ```
- 👉 Practice: raise + try-except 조합

  ```python
  try:
      product = Product("노트북", -1000, 10)
  except ValueError as e:
      print(f"상품 생성 실패: {e}")

  try:
      product = Product("노트북", 1000000, 10)
      product.sell(20)
  except ValueError as e:
      print(f"판매 실패: {e}")
  ```

#### 7-2. else와 finally (12min)

- else의 용도 (예외가 없을 때만 실행)
- 👉 Practice: else 활용
  ```python
  try:
      age = int(input("나이: "))
  except ValueError:
      print("숫자를 입력해주세요")
  else:
      print(f"입력한 나이: {age}")
  ```
- 👉 Practice: 딕셔너리 조회

  ```python
  user = {"name": "철수", "age": 25}

  try:
      email = user["email"]
  except KeyError:
      print("이메일 없음")
  else:
      print(f"이메일: {email}")
  ```

- finally의 용도 (항상 실행)
- 👉 Practice: finally 활용

  ```python
  count = 0

  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("에러 발생")
  finally:
      count += 1
      print(f"시도 횟수: {count}")
  ```

#### 7-3. 함수에서 예외 처리 (8min)

- 👉 Practice: 예외를 던지는 함수
  ```python
  def divide(a: int, b: int) -> float:
      if b == 0:
          raise ZeroDivisionError("0으로 나눌 수 없습니다")
      return a / b
  ```
- 👉 Practice: 예외를 처리하는 함수
  ```python
  def safe_divide(a: int, b: int) -> Optional[float]:
      try:
          return a / b
      except ZeroDivisionError:
          print("0으로 나눌 수 없습니다")
          return None
  ```

#### 7-4. Exercise (12min)

- ✏️ Exercise: raise/else/finally (4문제)

### 8교시 (17:00-17:50): 🎯 Day 5 종합 실습 & 기초 과정 마무리

**주제: 상품 관리 프로그램 (CLI 버전)**

**요구사항:**

- Product 클래스 (name, price, stock)
- 함수로 기능 분리
- 타입 힌트 필수
- 예외 처리 필수

**기초 문제 (12분):**

1. Product 클래스 구현 (타입 힌트)
   ```python
   class Product:
       def __init__(self, name: str, price: int, stock: int):
           # 검증 로직 포함
           ...
   ```
2. 상품 추가 함수
   ```python
   def add_product(
       products: List[Product],
       **product_data
   ) -> None:
       product = Product(**product_data)
       products.append(product)
   ```
3. 상품 조회 함수
   ```python
   def get_products(products: List[Product]) -> List[Dict[str, any]]:
       return [p.to_dict() for p in products]
   ```

**응용 문제 (18분):** 4. 상품 검색 함수 (이름으로)

```python
def find_product(
    products: List[Product],
    name: str
) -> Optional[Product]:
    ...
```

5. 상품 수정 함수
6. 상품 삭제 함수
7. 가격 범위 필터링 (람다 사용)
8. 예외 처리 추가
   - 음수 가격
   - 음수 재고
   - 존재하지 않는 상품

**도전 문제 (15분):** 9. 재고 관리 (입고/출고)

```python
class Product:
    def sell(self, quantity: int) -> None:
        if quantity > self.stock:
            raise ValueError("재고 부족")
        self.stock -= quantity

    def restock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("음수 불가")
        self.stock += quantity
```

10. JSON 저장/불러오기 + 언패킹

    ```python
    def save_products(products: List[Product], filename: str) -> None:
        data = [p.to_dict() for p in products]
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_products(filename: str) -> List[Product]:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Product(**item) for item in data]
    ```

11. 람다로 상품 정렬 (가격순, 이름순, 재고순)
12. 전체 시스템 통합
    - while문으로 메뉴
    - 모든 기능 연결
    - 예외 처리로 안정성 확보

**기초 과정 회고 (5분):**

- 5일간 배운 내용 정리
  - Day 1: 기본 문법, 문자열
  - Day 2: 리스트, 딕셔너리
  - Day 3: 제어문 (if, for, while)
  - Day 4: 함수, 타입 힌트, 람다, JSON
  - Day 5: 클래스, 예외 처리
- 응용 과정 예고 (FastAPI!)
- 질의응답

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
  - FastAPI 설치: `pip install fastapi uvicorn`
- **첫 FastAPI 애플리케이션**
  - 👉 Practice: Hello World API
  - uvicorn으로 서버 실행
  - 브라우저로 확인하기
  - 👉 Practice: 간단한 엔드포인트 추가
- **Path Parameter**
  - Path Parameter란?
  - 👉 Practice: 동적 경로 만들기 (item_id)
  - 👉 Practice: 여러 Path Parameter
  - ✏️ Exercise: Path Parameter 활용 (3-4문제)

- **Query Parameter**
  - Query Parameter란?
  - 👉 Practice: 쿼리 파라미터 처리 (q, limit)
  - 선택적 파라미터 (기본값)
  - 👉 Practice: 검색 API 만들기
  - ✏️ Exercise: Query Parameter 활용 (2-3문제)

#### 4-3. 🎯 응용 Day 1 종합 실습 (70분)

**주제: 간단한 정보 조회 API**

기초 문제:

1. 사용자 정보 반환 API (Path Parameter)
2. 상품 목록 조회 API
3. 검색 API (Query Parameter)

응용 문제: 4. 필터링 API (여러 Query Parameter) 5. 페이징 API (page, size 파라미터)

도전 문제: 6. 복합 조건 검색 API 7. Swagger 문서 확인하고 테스트하기

---

## 응용 Day 2: Request Body & Pydantic

### 오전 (09:00-12:30)

#### 5-0. Day 1 복습 (20분)

- HTTP Methods 복습
- Path/Query Parameter 복습
- 👉 Practice: 간단한 GET API

#### 5-1. Pydantic 모델 (120분)

- **Pydantic이란?** (10분)
  - 데이터 검증과 직렬화
  - 왜 Pydantic을 사용하나?

- **Python 클래스 복습 + 딕셔너리 변환** (30분)
  - 기초 Day 5 클래스 빠른 복습
  - 👉 Practice: 일반 Python 클래스 만들기
  - 👉 Practice: 딕셔너리 언패킹으로 클래스 생성 (\*\*)
  - 👉 Practice: 클래스를 딕셔너리로 변환 (**dict**)
  - ✏️ Exercise: 딕셔너리/클래스 변환 (2문제)
- **BaseModel 기본** (30분)
  - 👉 Practice: 첫 Pydantic 모델 (타입 힌트 사용)
  - 👉 Practice: 딕셔너리 → Pydantic (자동 변환)
  - 👉 Practice: Pydantic → 딕셔너리 (model_dump)
  - 타입 힌트의 중요성
  - 👉 Practice: 여러 타입 활용
  - ✏️ Exercise: Pydantic 기본 (3-4문제)
- **선택적 필드** (20분)
  - Optional 사용
  - 기본값 설정
  - 👉 Practice: 선택적 필드가 있는 모델 (Optional, 기본값)
  - ✏️ Exercise: 선택적 필드 (2-3문제)

- **모델 검증** (20분)
  - 자동 타입 변환
  - 유효성 검사
  - 👉 Practice: 잘못된 데이터 처리
  - Field로 상세 검증 (min_length, max_length, ge, le, pattern)
  - 👉 Practice: Field 활용
  - ✏️ Exercise: 데이터 검증 (2-3문제)

#### 5-2. POST 요청 처리 (60분)

- **Request Body**
  - Request Body란?
  - POST 메서드로 데이터 받기
  - 👉 Practice: 사용자 생성 API
  - 👉 Practice: Pydantic 자동 변환 확인
- **데이터 저장** (메모리)
  - 리스트에 데이터 저장
  - 👉 Practice: 메모리에 사용자 저장
  - 전역 변수 활용
  - 👉 Practice: 저장된 데이터 조회
  - 👉 Practice: model_dump()로 응답 반환
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

응용 문제: 3. GET (단건), PUT, DELETE 구현 4. 완료/미완료 필터링 (Query Parameter) 5. 에러 처리 추가

도전 문제: 6. 검색 기능 (제목으로) 7. 정렬 기능 (생성일, 제목)

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
- **테이블 생성**
  - 👉 Practice: users 테이블 생성 (id, name, email)
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

응용 문제: 3. GET (단건), PUT, DELETE 구현 4. 작성자별 조회 5. 페이징 (limit, offset)

도전 문제: 6. 검색 기능 (제목 + 내용) 7. 정렬 기능 (최신순, 오래된 순) 8. 조회수 기능 추가

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
  - 👉 Practice: 비밀번호 해싱 (CryptContext)
  - 👉 Practice: 비밀번호 검증 (verify)
  - ✏️ Exercise: 해싱 활용 (2-3문제)

### 오후 (13:30-17:00)

#### 7-3. JWT 토큰 (120분)

- **JWT란?**
  - JWT 구조 (Header, Payload, Signature)
  - 왜 JWT를 사용하나?
- **python-jose 사용**
  - 설치: `pip install python-jose[cryptography]`
  - 👉 Practice: JWT 토큰 생성 (encode)
  - 👉 Practice: JWT 토큰 검증 (decode)
  - ✏️ Exercise: JWT 기본 (3-4문제)

- **만료 시간 설정**
  - 👉 Practice: 토큰 만료 구현
  - 👉 Practice: 만료 토큰 처리
  - ✏️ Exercise: 만료 처리 (2문제)

#### 7-4. 회원가입과 로그인 (90분)

- **회원가입 API**
  - 👉 Practice: 사용자 등록 (비밀번호 해싱 + DB 저장)
  - 이메일 중복 체크
  - 👉 Practice: 중복 검증
  - ✏️ Exercise: 회원가입 (2-3문제)

- **로그인 API**
  - 👉 Practice: 로그인 구현 (사용자 조회 + 비밀번호 검증 + JWT 발급)
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

응용 문제: 3. 로그인 API 구현 4. 이메일 형식 검증 5. 비밀번호 강도 체크

도전 문제: 6. Refresh Token 개념 이해 7. 토큰 갱신 API 설계

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
  - 👉 Practice: 현재 사용자 가져오기 (get_current_user)
  - 👉 Practice: 보호된 엔드포인트 (/me)
  - ✏️ Exercise: 인증 의존성 (3-4문제)

- **권한 체크**
  - 본인 데이터만 수정
  - 👉 Practice: 권한 검증
  - 👉 Practice: 403 Forbidden 처리
  - ✏️ Exercise: 권한 관리 (2-3문제)

#### 8-2. 파일 업로드 (70분)

- **File Upload**
  - 👉 Practice: 파일 받기 (UploadFile)
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
  - 👉 Practice: CORS 미들웨어 (CORSMiddleware)

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

응용 문제: 3. 조회 API 구현 4. 삭제 API (권한 체크) 5. 내 이미지만 보기 API

도전 문제: 6. 이미지 썸네일 생성 7. 페이징 및 정렬 8. 좋아요 기능

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

- 파트 종료 후 5-15분
- 2-5문제 혼자 풀기
- 막히면 손들기!

### Problem (🎯)

- 하루 마지막 30-90분
- 종합 문제 혼자 풀기
- 기초 → 응용 → 도전 순서

### 복습의 중요성

- 각 과정 첫날은 복습부터!
- 매일 복습 퀴즈
- 이전 내용 활용한 새 예제
