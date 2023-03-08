###주석
# 이것은 한 줄 주석 입니다.
"""
이것은
여러줄
주석입니다.
"""
### print() 함수 : 출력함수
# print("hello, world!")

### type() 함수 : 자료형 타입을 반환
# print(type("hello")) #str :string(문자열)

# print(1+1) #int : integer(정수)
# print(type(3.14159)) #float : 실수(소수점이 있는 숫자)

### 연산자
# print(1+1)
# print(10-2)
# print(10*3)
# print(10/2)  #나눗셈은 자료형이 float(실수)로 바뀐다
# print(10//3)  #나눗셈 몫만 구하는 연산
# print(10%3) #나눗셈 나머지만 구하는 연산
# print(2**3) #제곱근구하는 연산

###변수
# a = 10 # = : 대입연산자
# print(a)

# name = "sehyun"
# age = 14
# height = 156.3

# print(name)
# print(age)
# print(height)


### 변수의 연산 
# age += 1 #복합 대입 연산자
# print(age)

## 비교연산자
# print(a == 14) #같다

# a=10
# b=20

# print(a == b) #false
# print(a != b) #true
# print(a > b) #false
# print(a < b) #true
# print(a>=b) #false
# print(a<=b) #true

###논리 연산자
a=10
b=20

print(a<b and a==10)  #T T -> true
print(a<b and a==20) #T F -> false
print(a>b and a==20) #F F -> false

print(a<b or a==20) #T T -> true
print(a<b or a==20) #T F -> true
print(a>b or a==20) #F F -> false

print(not a<b) #T -> false
print(not a>b) #F -> true
print(not a==10) #T -> false