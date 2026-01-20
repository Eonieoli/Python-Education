class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def to_dict(self):
        """객체 → 딕셔너리"""
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }
        
    @classmethod
    def from_dict(cls, data):
        """딕셔너리 → 객체"""
        return cls(
            name=data["name"],
            age=data["age"],
            email=data["email"]
        )

# 객체 생성
user = User("김철수", 25, "kim@test.com")

# 객체 → 딕셔너리 (API 응답용)
user_dict = user.to_dict()
print(user_dict)

# 딕셔너리 → 객체 (API 요청 처리)
data = {"name": "이영희", "age": 30, "email": "lee@test.com"}
new_user = User.from_dict(data)
print(new_user.name)  # 이영희

# 실용 예제: JSON 데이터 처리
import json

# 객체 → JSON
json_str = json.dumps(user.to_dict(), ensure_ascii=False)
print(json_str)

# JSON → 객체
json_data = '{"name": "박민수", "age": 28, "email": "park@test.com"}'
dict_data = json.loads(json_data)
user_from_json = User.from_dict(dict_data)
print(user_from_json.name)