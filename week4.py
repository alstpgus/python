# month = input("오늘은 몇 월 인가요?")
# day = input("오늘을 몇 일 인가요?")

# print(f"오늘은 {month}월 {day}일 입니다.")

# text1 = input("문자열 입력:")
# text2 = input("두 번째 문자열 입력: ")
    
# print(f"{text1}{text2}")
# print(text1+text2)

# text = input("문자입력: ")
# num = int(input("숫자입력: "))

# print(text * num)


### 리스트
# l = [1, 2, 3, 4, 5]
# print(l, type(l))

# friend = ["민정", "세현", "태연", "동건"]
# print(friend)

# print(l[0], friend[0])
# print(l[1], friend[2])
# print(l[2], friend[1])

##리스트 값 수정
# friend[1] = "대연"
# print(friend)

### 김밥 만들기
# item1 = "동건이의 정성"
# item2 = "동건이의 손맛"
# item3 = "승기의 잔소리"
# item4 = "세현이의 드립"
# item5 = "최준혁 선생님의 응원"

# print(item1, item2, item3, item4, item5)

# items = ["동건이의 정성", "동건이의 손맛", "승기의 잔소리", "세현이의 드립", "최준혁 선생님의 응원"]
# print(items)

# print(len(items))
# items.append("민정이의 지식")     #리스트 맨 뒤에 추가
# print(items)
# items.insert(3, '도운이의 시선')   #입력한 인덱스 자리에 추가
# print(items)

###리스트 삭제
# items.pop()     #리스트 맨 마지막 값 삭제
# print(items)
# items.remove('도운이의 시선')   #특정 값을 삭제
# print(items)

###정보
# print(items.index('동건이의 손맛'))
# items.remove('동건이의 손맛')
# print(items)
# print(items.count('승기의 잔소리'))

score = [90, 100, 80, 50, 100]

print(max(score))
print(min(score))
print(sum(score))
print(f"평균 점수: {sum(score)/5}")