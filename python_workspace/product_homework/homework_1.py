#명령문 반복문 연습 예제
#----메뉴를 선택하세요----  while 
# 1번 누르면 AI 수강생 등록 
# 2번 누르면 AI 수강생 목록보기
# input 으로 입력값 
# 수강생 정보는 dictionary 로 list 에 등록 
# 파이썬은 매개변수에 타입을 지정하지 않기때문에 출력함수를 만들어 뭐든 출력할 수 있다.




#
#       강의시간에 만든 프로그램에 제가 부족했던 입출력 시 데이터 형태 변환에 대하여 강사님의 코드를 보고 수정하였습니다. 
#






import os
PATH = os.getcwd()
UserInfo = {
}
FileName = "user_list.txt"
UserDB=[]

def ReadData():
    
    fileExist = os.path.isfile(FileName)
    
    if fileExist : 
        print("파일확인")
        with open(FileName,"r") as file:
            print("파일오픈")
            while True:
                print("읽기 시작")
                UserData = file.readline()
                if len(UserData.split("|")) == 2 :
                    print("데이터 정형화ㅣ")
                    UserDict = UserData.split("|")[1].rstrip("\n").split(",")
                    print(UserDict)
                    UserDB.append({"UserName":UserDict[0].strip(),"UserAge":int(UserDict[1].strip()),"UserMajor":UserDict[2].strip()})
                    print(UserDB)
                    return UserDB
                if not UserData :break
            #return UserDB
    
        
#UserDB=[ReadFile]
#UserDB = [ReadFile]                                         # 유저 정보를 저장할 리스트 
#print("11111{}".format(ReadFile))
#print("{}".format(UserDB))
def UserResit(UserInfo):                            # 유저 등록 함수 
    
    i = UserSearch(UserInfo["UserName"])
    #print(i,"111111111111111111")
    if i < 0 :
        print(UserInfo["UserName"])
        print(UserInfo["UserAge"])
        print(UserInfo["UserMajor"])
        UserDB.append(UserInfo)                         #유저에게 입력받은 이름, 나이, 전공을 dictionary로 저장해 UserDB에 추가한다
    else:
        print("이미 있는 사용자 입니다.")

    return print("성공")

def UserList():                                     #유저 정보 보기 함수
    return print("수강생 명단 {}".format(UserDB))   #유저 정보를 print 해준다


def UserSearch(UserName):                           #유저 검색 함수 
    if UserDB is not None:
        for i , dic_a in enumerate(UserDB):             # enumerate로 쪼개 i만큼 돌때 dic_a에 UserDB[i]를 집어넣는다
            if dic_a["UserName"] == UserName:           # 만약 위에서 쪼갠 dic_a의 UserName 과 입력받은 UserName이 같다면 If문을 실행 시킨다
                return i                                # i 는 if 문에서 멈췄을 때 i의 값으로 인덱스라고 생각하면 된다 
    #elif UserDB is None: 
    return -1
def F_UserDel(UserName):                            # 유저 삭제 함수
    dic_Del = UserSearch(UserName)                  # dic_Del 에 유저 검색 함수에서 찾은 인덱스를 저장한다 0~N
    del(UserDB[dic_Del])                            # 입력받은 인덱스 정보로 UserDB의 dic_Del 인덱스 번째 정보를 삭제한다
    return print("성공")

def UserModify(UserName):                               # 유저 수정 함수
    UserModIndex = UserSearch(UserName)                 # 검색 함수에서 인덱스를 받는다
    UserModiAge = input("수정할 나이을 입력해 주세요 ")  
    UserModiMajor = input("수정할 전공을입력해 주세요")
    UserModiInfo =UserDB[UserModIndex]                  # UserDB의 인덱스 번째 정보를 dictionary에 저장한다 ( 리스트의 주소값이 저장된다)
    UserModiInfo["UserAge"] = UserModiAge               # 각각 키와 맞는 정보를 입력받은 값으로 변경한다
    UserModiInfo["UserMajor"] = UserModiMajor           # 위와 같음 
    return print("성공")

def UserNameSearch(UserName):                           # 유저 이름으로 특정 인원 검색
    UserModIndex = UserSearch(UserName)                 # 검색 함수로 인덱스 가져오기
    if UserModIndex is not None :
        SearchDic = UserDB[UserModIndex]                    # 인덱스 번째 UserDB정보를 dictionary에 저장 ( 주소값 저장)
        return print(SearchDic)                             # 프린트해주기
    print("없는 수강생 입니다.")
def CloseData():
    with open(FileName,"w") as file:
        if UserDB == []:
            print()
        else: 
            for i,v in enumerate(UserDB):
                if i == len(UserDB)-1:
                   
                    file.write("{0}번째 | {1},{2},{3}".format(i, v["UserName"],v["UserAge"],v["UserMajor"]))
                else:
                    
                    file.write("{0}번째 | {1},{2},{3}\n".format(i, v["UserName"],v["UserAge"],v["UserMajor"]))


UserDB = ReadData()
while True :
    print("\t----메뉴를 선택하세여----\n\t 1. AI 수강생 등록 하기 \n\t 2. AI 수강생 목록보기 \n\t 3. 수강생 삭제 \n\t 4. 수강생 정보 수정\n\t 0. 종료 ")
    UserInput = input("당신의 선택은")
#    print(UserInput)
    if UserInput == "1" :
        UserName = input("이름을 입력해 주세요")
        UserAge = input("나이를 입력해 주세요")
        UserMajor = input("전공을입력해 주세요")

        UserInfo = {"UserName" : UserName,
                    "UserAge" : UserAge,
                    "UserMajor" : UserMajor
         }
        UserResit(UserInfo)
        # print("성공적으로 입력되었습니다{}".format(UserInfo))
        # UserDB.append(UserInfo)
       
    elif UserInput == "2" :
        #print("수강생 명단 {}".format(UserDB))
        UserList()

    elif UserInput == "3" :
        UserDel = input("삭제할 학생 이름을 입력해주세요")
       #dic_a = list(enumerate(UserDB))
        # for i , dic_a in enumerate(UserDB):
        #    if dic_a["UserName"] == UserDel:
        #        del(UserDB[i])
        F_UserDel(UserDel)
        
    elif UserInput == "4" : 
        UserModi = input("수정할 학생 이름을 입력해주세요")
            # enumerate(UserDB) 는 UserDB의 주소값을 가져온다고 생각하면 된다 
            # 가져온 주소값을 Modi_dic에 넣었고 Modi_dic을 수정하는 것은 UserDB의 주소값을 수정하는 것과 같다 
        # for i, Modi_dic in enumerate(UserDB):
        #     if Modi_dic["UserName"] == UserModi:
        #         UserModiAge = input("수정할 나이을 입력해 주세요 ")
        #         UserModiMajor = input("수정할 전공을입력해 주세요")
                
        #         Modi_dic["UserName"] = UserModi
        #         Modi_dic["UserAge"] = UserModiAge
        #         Modi_dic["UserMajor"] = UserModiMajor
        UserModify(UserModi)
    elif UserInput == "5":
        UserNameInput = input("보고싶은 학생 이름")
        UserNameSearch(UserNameInput)
    elif UserInput == "0":
        CloseData()
        break
    else :
        print("잘못입력하셨습니다")


# i = 0
        # while i > len(UserDB):
        #     #UserDel 이 UserDB에서 나눈 dic 의 UserName과 같으면 그때 i 를 인덱스로 삭제한다
        #     dic_a = UserDB[i]
        #     print(type(dic_a))
        #     print(i)
        #     while UserDel in dic_a:
        #         del(UserDB[i])
