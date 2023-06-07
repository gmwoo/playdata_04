g_x = 1  # 전역변수

def myfunc():
    x = 2  # 지역변수, 함수 내에서만 사용 가능
    # g_x = g_x + 1  -> 함수 내에 있으므로 지역변수로 인식하므로 에러
    global g_x   # 전역변수임을 지정
    g_x = g_x + 1
    print("지역변수 ", x)
    print("전역변수 ", g_x)
    
myfunc()  # 함수 호출   2 2
myfunc()  # 함수 호출   2 3
myfunc()  # 함수 호출   2 4
myfunc()  # 함수 호출   2 5
myfunc()  # 함수 호출   2 6

# 반환 값 문제 - 반환이 값이 하나만 됨
def doubleValue(x, y):
    # 함수 내의 매개변수는 함수 외부로부터 읽어만 오며, 보내지 못함
    x = x + 2
    y = y + 2
    return x, y  # 자동으로 tuple로 바뀌면서 하나가 return

a = 5
b = 7
result = doubleValue(a, b)
print(result, type(result))

a , b = doubleValue(a, b)
print("a = ", a)
print("b = ", b)
