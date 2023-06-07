#1. 추가
#2. 수정
#3. 삭제
#4. 주급계산 및 출력
# 함수를 잘 만드는 방법은 [책. 클린코드-자바] => 1. 작게 만들어라  2. 더 작게 만들어라  3. 더더 작게 만들어라
# 함수는 한 가지의 기능에 집중하라
# -> 함수를 여러 개 만들어 '기능1 함수', '기능2 함수', '통합함수'를 만들어서 서로 연결하라

payList = []  # 공유 메모리, 모든 함수에서 사용

def init():
    payList.append({"name": '홍길동', "work_time":40, "per_pay":20000})
    payList.append({"name": '임꺽정', "work_time":30, "per_pay":20000})
    payList.append({"name": '장길산', "work_time":20, "per_pay":30000})

def append():    # 데이터 추가만 담당
    data = dict()
    data["name"] = input("이름: ")
    data["work_time"] = int(input("일 한 시간: "))
    data["per_pay"] = int(input("시간 당 단가: "))
    payList.append(data)

def oputput():    # payList(dict table) 출력
    for item in payList:
        print(f"{item['name']} {item['work_time']} {item['per_pay']}")

def process():    # 주급 계산
    for cal in payList:
        print(f"{cal['name']}의 주급: {cal['work_time']*cal['per_pay']} 원")
    
def menuDisplay():  # 처음 값을 위한 메뉴
    print("1. 추가")
    print("2. 출력")
    print("3. 주급 계산")
    print("4. 검색")
    print("5. 수정")
    print("6. 삭제")
    print("0. 종료")

def start():    # append(), output() 호출
    init()
    while True:
        menuDisplay()
        sel = input("선택: ")
        if sel=="1":
            append()
        elif sel=="2":
            oputput()
        elif sel=="3":
            process()
        elif sel=="4":
            search()
        elif sel=="5":
            modify()
        elif sel=="6":
            delete()
        else:
            return  # 함수 종료, while 종료
        
# 위치를 찾는 함수 - 검색해서 출력, 수정, 삭제 시에도 사용
def find(name):
    for i in range(0, len(payList)):
        if name == payList[i]['name']:
            return i  # 서로 일치하는 데이터가 있으면 위치를 반환하고 함수 종료
        
    return None  # for문에서 끝나도록 못찾은 경우, 없다는 의미(None 반환)
    # 파이썬의 경우 함수에서 목적 달성을 못할 때 주로 None 반환
    
def search():  # 검색
    name = input("찾을 이름: ")
    pos = find(name)
    if pos == None:
        print(name + "을 찾지 못했습니다.")
        return    # 더이상 수행을 하지 않음. 이미 오류이므로 여기서 else를 쓰지 않는 것이 프로그램의 확장성 더 높여줌
    # if error1: return 구조로  기술하면 함수를 보다 깔끔하고 확장성 있게 만들 수 있음
    
    # 에러가 아닐 때 처리
    item = payList[pos]  # 해당 위치 값을 가져와서 출력
    print(f"{item['name']} {item['work_time']} {item['per_pay']}")
    
def modify():  # 수정
    name = input("수정할 이름: ")
    pos = find(name)
    if pos == None:
        print(name + "을 찾지 못했습니다.")
        return    
    data = payList[pos]  # 해당 위치 값 가져와서 다시 입력
    data["name"] = input("이름: ")
    data["work_time"] = int(input("일 한 시간: "))
    data["per_pay"] = int(input("시간 당 단가: "))   
    
def delete():  # 삭제
    name = input("삭제할 이름: ")
    pos = find(name)
    if pos == None:
        print(name + "을 찾지 못했습니다.")
        return    
    del payList[pos]  # 해당 위치 값 가져와 삭제
    
    
start()
        
    