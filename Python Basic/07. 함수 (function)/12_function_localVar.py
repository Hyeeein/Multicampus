# 함수 내에서 정의된 변수 : 지역변수(local variable)
# 함수 내에서만 사용.
# 함수가 호출되면 생성되고, 함수가 종료되면 지역변수는 소명

# def show():
#     a=1       # 함수 내부에서 정의된 지역변수
#     print('show() 함수')
#     print(a)

# print(a)

def show(a):    # a : 매개변수 => 함수 내부에서 지역변수로 사용
    a=a+1
    print('show() 함수')
    print(a)

show(10)
print(a)

# def show():
#     a=1     # a : 지역변수
#     a=a+1
#     print('show() 함수')
#     print(a)
#
# show()

a=1  # 함수 밖에서 정의된 전역변수 a

def show():
    print('show() 함수')
    print(a) # 전역변수 a

def add():
    print('add()함수')
    print(a)
    print(b)
    print('---------')

# 전역변수 a를 변경하려고 할 때
def add2():
    global a
    a = a + 1     # a: 지역변수
    c = a + b
    print('add2()함수')
    print(a)
    print(b)
    print(c)
    print('---------')

b=10

# 전역변수는 함수 내부에서 사용이 가능함
# show()
print(a)
add2()
print(a)
# print(b)

# 전역변수는 어디서든지 사용 가능(함수 내부에서 사용 가능)
# 함수내부의 지역변수나 매개변수는 함수 내에서만 사용가능
# 지역변수가 전역변수 보다 우선순위가 높음
# 함수 내부에서 할당연산자 = 사용하는 식에서 변수는 지역변수로 인식
# 함수 내부에서 전역변수를 변경할 때는 global 키워드를 사용
