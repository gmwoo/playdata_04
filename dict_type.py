mydict = {"red":"빨간색","green":"초록색"}
mydict["blue"] = "파란색"  # 추가 또는 수정, 키 값이 없으면 추가 / 추가 키 값이 있으면 수정으로 판단

# keys() 함수는 키만 반환

if "red" in mydict.keys():
    print('red가 있다')
else:
    print('red가 없다')

print(mydict.keys(), type(mydict.keys()))
print(mydict.values(), type(mydict.values()))

print(mydict['red'])
print(mydict['green'])
print(mydict['blue'])   
# print(mydict['yellow'])  # 키값이 없으면 예외 발생

# 삭제 후
del mydict['red']
print(mydict.keys())