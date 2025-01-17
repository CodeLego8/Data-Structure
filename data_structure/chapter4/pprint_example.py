from pprint import pprint   

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "hiking", "coding"],
    "education": {
        "high_school": "Springfield High",
        "university": {
            "name": "MIT",
            "degree": "Computer Science"
        }
    }
}

# print(data)
# print()
pprint(data) # pprint의 기본 동작은 딕셔너리의 키를 알파벳 순서로 정렬하여 출력  
print()                 #데이터 구조를 사람이 읽기 쉽도록 줄 바꿈과 들여쓰기를 자동으로 적용
pprint(data, sort_dicts=False)  # 알파벳 순서가 아닌 원래 순서로 출력력