### 문자열(string)
## 문자열 선언
# text = "hello"
# print(text)

## 문자열 연산
# fruit1 = "watermelon"
# fruit2 = "dragonfruit"
# print(f"{fruit1} + {fruit2} = {fruit1+fruit2}") #병합
# # print(f"{fruit1} - {fruit2} = {fruit1+fruit2}") #오류발생
# print(f"{fruit1}* {3} = {fruit1*3}")   #반복
# # print(f"{fruit1} / {fruit2} = {fruit1/fruit2}")   #오류발생


## index(인덱스)
# big = "mi"
# small = "n"

# name = big[0] + big[1] + small[-1]
# print(name)

##이스케이프 코드
print('엄마가 말씀하셨다. "숙제 다 했니?')
# 엄마가 말했다. "숙제 다 했니?"
print("\t엄마가 말했다.\n \"숙제 다 했니?\"\\")

##문자열함수
hi = "hello, world!"

print(hi.count('o'))  #특정 문자 개수 반환
print("woooooo".count('o'))  

print(hi)
print(hi.lower())  #문자열을 소문자로 반환
print(hi.upper())  #문자열을 대문자로 반환

print(hi.replace('Hello', 'Buy'))  #문자치환(Hello->Buy)

num = "01011112222"
print(num.inisalpha())  #문자가 알파벳으로만 구성 되었는지 확인
print(num.isdight())    #문자가 숫자로만 구성 되었느지 확인

date = "2023/03/15"
dates = date.split('/')
print(date)
print(dates)

print(len(num))
print(len(date))
print(len(dates))