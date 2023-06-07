# s1 = "아메리카노, 에스프레소, 카페라떼, 캬라멜마끼아또"
# print(s1[0])
# print(s1[1])
# print(s1[2])
# print(s1[6],s1[7],s1[8],s1[9],s1[10])

# # str, tuple 둘 다 randomly 라 인덱싱을 통한 값 변경 불가
# # s1[0]="어" # TypeError: 'str' object does not support item assignment

# # 슬라이싱 [시작:종료:증감치] - 시작과 종료에는 값을 생각할 경우
# # 처음부터 마지막까지 라는 의미가 있음

# print(s1[::2]) # 0,2,4,6,8
# print(s1[:5]) # 0~4까지 잘라내기
# print(s1[6:11])
# print(s1[::-1]) # 뒤로부터 역순으로 출력

# s2 = s1[6:11]
# print(s2)

# # 토큰분리: spllt 함수는 반환 값이 list 타입, 문자열에서 특정 문자 기준으로 잘라 냄.
# wordList = s1.split(",")
# print(wordList)

# # "연결할 문자열".join(리스트타입)
# s2 = " ".join(wordList)
# print(s2)

# s2 = ",".join(wordList)
# print(s2)

# # 문자열은 한 번 값이 정해지면 자체는 수정 불가
# s1 = "hello, python"
# s1 = "H"+s1[1:] # H, ello,python 문자하고 합친 문자가 다시 s1에 전달
# print(s1)

# s1 = s1[:7] + "P" + s1[8:]
# print(s1)



# 문제 : 각 첫 글자만 대문자로 바꾸어서 출력
colorList = ["red", "white", "green", "cyan", "magenta", "violet", "blue"]
print(colorList[0])
print(colorList[2])
print(colorList[4])
print(colorList[5])

print(colorList[:4])
print(colorList[4::-1])  # 4번부터 역순으로 

### 내 풀이
for x in colorList:
    print(x[0].upper()+x[1:], end=', ')
print()
    
### 선생님 코드
colorList2 = []
for color in colorList:
    temp = color[0].capitalize() + color[1:]
    colorList2.append(temp)
print(colorList2)


# 데이터 추가 수정 삭제
colorList2.append("Black") # 무조건 맨뒤에
colorList2.insert(0, "yellow") # 위치지정이 가능하다
print( colorList2 )

# 수정
colorList2[0] = "Yellow"
print(colorList2)

# 삭제 - 값으로
colorList2.remove("Red")
# 삭제 - 위치 값으로
del colorList2[5]
print(colorList2) 