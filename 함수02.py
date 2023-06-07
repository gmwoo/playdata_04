# 객체지향 언어의 특징이 오버로딩(함수의 이름은 같지만 형태가 다른 함수 만들 수 있음)
# C언어 str->int ==> int("1234")   atoi(문자열을 정수), atof(문자열을 실수)
# atoi(4), atoi(4.5)  ==> 함수 두 개를 만들어, 하나는 매개변수가 정수, 하나는 매개변수가 실수

#파이썬은 문법을 버림(만들지 않음)

print(1)
print(3.4)
print("test")

# 매개변수에 기본값을 부여해서 호출 시에 새로운 값을 부여하는 방식에 따라 오버로딩과 유사한 효과를 가짐
def myadd(x,y,z):
    return x+y+z
print(myadd(10, 20, 30))

# 기본값: 매개변수를 선언하면서 값을 줄 수 있으며 이를 기본값이라고 함
# 함수호출 시 매개변수에 값을 전달하지 않으면 기본값이 사용
def myadd2(x=1,y=2,z=3):
    return x+y+z
print(myadd2())
print(myadd2(10))
print(myadd2(10, 20))
print(myadd2(10, 20, 30))

# 매개변수 값을 따로 지정 가능
print(myadd2(x=100))
print(myadd2(z=50))
print(myadd2(y=100))
