import os.path
#ai 수강생 관리 시스템
ai_list=[]

#수강생등록 : 동명이인이 있는지 체크하고 message 리턴
def register(ai_dic):
    index = is_exist(ai_dic["name"])
    if index < 0 :
       ai_list.append(ai_dic)
       return ai_dic["name"]+"님 등록되었습니다."
    else:
        return ai_dic["name"]+"님은 이미 등록되었습니다."

#수강생목록 : 리스트의 수강생 목록 리턴
def ais():
    return ai_list

#수강생수정 : 이름검색 나이, 전공 수정하고 message 리턴
def ai_update(ai_dic):
    index = is_exist(ai_dic["name"])
    if index > -1 : 
        ai =ai_list[index]
        ai["age"] = ai_dic["age"]
        ai["major"] = ai_dic["major"]
        return ai_dic["name"]+"이 수정되었습니다."
    else:
        return ai_dic["name"]+"정보는 존재하지 않습니다."

#수강생삭제 : 이름검색 리스트에서 삭제하고 message 리턴
def ai_remove(name):
    index = is_exist(name)
    if index > -1 :
        ai_list.pop(index)  #ai_list.remove(ai_list[index])
        return name+"이 삭제되었습니다."
    else:
        return name+"정보는 존재하지 않습니다."


#수강생검색 : 이름으로 검색해서 dictionary 리턴
def ai_search(name):
    for index, value in enumerate(ai_list):
        if value["name"] == name:
            return value
        else:
            return name+"정보는 존재하지 않습니다."

#이름존재여부검색 : 이름으로 검색해서 리스트의 index 값 리턴
def is_exist(name):
    for index, value in enumerate(ai_list):
        if value["name"] == name:
            return index
    return -1

def menu_display():
    print("====  AI 수강생 관리 프로그램 =====")
    print("1. 수강생 등록")
    print("2. 수강생 목록")
    print("3. 수강생 수정")
    print("4. 수강생 삭제")
    print("5. 수강생 검색")
    print("0. 종료")

def message_display(message):
    print(message)

#ai_list ai_list.dat 파일저장
def save_list():
    save_file = open("ai_list.dat", "w")
    for index, value in enumerate(ai_list):
        save_file.write("{0}번째 | {1},{2},{3}\n".format(index, value["name"],value["age"],value["major"]))
    save_file.close()

#ai_list.dat 파일 내용 ai_list에 append
def read_data():
    fileExist = os.path.isfile("ai_list.dat")
    if fileExist:
        read_file = open("ai_list.dat","r")
        while True:
            ai_data = read_file.readline()
            if len(ai_data.split("|")) == 2 :
                ai = ai_data.split("|")[1].rstrip("\n").split(",")
                ai_list.append({"name":ai[0].strip(),"age":int(ai[1].strip()),"major":ai[2].strip()})
            if not ai_data: break
        read_file.close()
def init():
    read_data()

while True:
    init()
    menu_display()

    menu = input("메뉴를 선택하세요 ")
    if menu == '1':
        name = input("name : ")
        while True:
            try:
                age = int(input("age : "))
                break
            except:
                age = int(input("나이는 숫자로 입력해 주세여."))
        
        major = input("major : ")
        message = register({"name":name,"age":age,"major":major})
        message_display(message)
    elif menu == '2':
        message_display("==== AI 수강생 목록 ===")
        message_display(ais())
    elif menu == '3':
        name = input("수정할 수강생 이름을 입력하세요 ")

        while True:
            try:
                age = int(input("age : "))
                break
            except:
                age = int(input("나이는 숫자로 입력해 주세여."))

        major = input("major : ")
        message = ai_update({"name":name, "age":age, "major":major})
        message_display(message)
    elif menu == '4':
        name = input("삭제할 수강생 이름을 입력하세요 ")
        message = ai_remove(name)
        message_display(message)
    elif menu == '5':
        name = input("검색할 수강생 이름을 입력하세요 ")
        ai = ai_search(name)  
        message_display(ai)
               
    elif menu =='0':
        save_list()
        break
    else:
        message_display("메뉴는 1,2,3,4,5 중 하나를 선택하시고 종료를 원하시면 0번을 선택하세요")
    continue