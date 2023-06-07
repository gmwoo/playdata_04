def display():
    print("--------------------")

# 함수 호출
display()
display()
display()
display()

def display2(line):
    for i in range(0, line):
        print("**************")

# 이 함수는 매개변수가 있음
display2(3)
display2(5)

def display3(mark, line, cnt):
    for i in range(0, line):
        for j in range(0,cnt):
            print(mark, end=' ')
        print()
        
display3('^', 3, 5)
display3('$', 4, 10)
display3('@', 5, 30)


# 함수가 일을 처리하고 값을 반환하는 경우를 작성하자
def add(x, y):
    return x+y  # return 구문이 함수를 종료하는 기능, 값을 반환하는 기능이 있다
                # 값은 하나만 반환할 수 있다
# 함수 호출시 매개변수에 값을 전달해야만한다
# 매개변수 - 함수 외부와 함수 내부를 연결하는 역할, 외부에서 값 전달목적으로 사용하는 변수
# def add(x, y): 이때 x와 y가 매개변수이다.
# 매개체가 되는 변수(파라미터, 아규먼트) 라고도 부른다
print(add(4,5))
print (display()) #파이썬은 return 이 없다면 None 이 반환된다

# 1~N 까지의 합계를 구해서 반환하는 함수 만들기
def sigma(limit):
    result = 0
    for i in range(1, limit+1):
        result += i   # result = result + i 일 때, 좌변에 동일한 변수일 때 사용 가능
    
    return result

print(sigma(10))
print(sigma(100))
print(sigma(1000))