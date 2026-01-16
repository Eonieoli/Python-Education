# 기초 문제
students = ["김철수", "이영희", "박민수"]
scores = [85, 90, 78]

# 특정 학생 점수
search_name = "김철수"
index = students.index(search_name)
print(f"{search_name}의 점수: {scores[index]}점")

# 응용 문제
# 새 학생 추가
students.append("최지은")
scores.append(88)

# 평균
average = sum(scores) / len(scores)
print(f"평균 점수: {average:.1f}점")

# 최고 점수
max_score = max(scores)
max_index = scores.index(max_score)
print(f"최고 점수: {students[max_index]} ({max_score}점)")

# 도전 문제 - 성적표
print("\n===== 성적표 =====")
for i in range(len(students)):
    status = "합격" if scores[i] >= 60 else "불합격"
    print(f"{students[i]}: {scores[i]}점 ({status})")