# 성적처리: 이름, 국어, 영어, 수학 입력 받아서 총점 및 평균 구하기
# 수우미양가 까지 구하기 (90, 80, 70, 60, 50)

scoreLst = []

def append():
    data = dict()
    data["name"] = input("이름: ")
    data["국어"] = int(input("국어: "))
    data["영어"] = int(input("영어: "))
    data["수학"] = int(input("수학: "))
    scoreLst.append(data)
    
def sum():
    for cal in scoreLst:
        cal["총점"] = cal["국어"] + cal["영어"] + cal["수학"]

def avg():
    for cal in scoreLst:
        cal["평균"] = cal["총점"] / 3

def score():
    for x in scoreLst:
        if x["평균"] >= 90:
            x["등급"] = "수"
        elif x["평균"] >= 80:
            x["등급"] = "우"
        elif x["평균"] >= 70:
            x["등급"] = "미"
        elif x["평균"] >= 60:
            x["등급"] = "양"
        else:
            x["등급"] = "가"            

def out_put():
    print(scoreLst)

def start():
    while True:
        print("1. 추가")
        print("2. 출력")
        print("0. 종료")
        sel = input("선택: ")
        if sel=="1":
            append()
            sum()
            avg()
            score()
        elif sel=="2":
            out_put()
        else:
            return  # 함수 종료, while 종료

start()