#명령문 반복문 연습 예제
#----메뉴를 선택하세요----  while 
# 1번 누르면 AI 수강생 등록 
# 2번 누르면 AI 수강생 목록보기
# input 으로 입력값 
# 수강생 정보는 dictionary 로 list 에 등록 

# 파이썬은 매개변수에 타입을 지정하지 않기때문에 출력함수를 만들어 뭐든 출력할 수 있다.


print("\t----메뉴를 선택하세여----\n\t 1. AI 수강생 등록 하기 \n\t 2. AI 수강생 목록보기 \n\t 3. 수강생 삭제 \n\t 4. 수강생 정보 수정 ")
UserInfo = {
}
FileName = "AIInfoDB.txt"
UserDB=[]

def ReadData():
    with open(FileName,"r") as file:
        if file.readlines == 0:
            UserDB=[]
            print("파일에 텍스트가 없습니다")
        else:
            ReadFile = file.read()
            UserDB=[ReadFile]
        return UserDB
        
#UserDB=[ReadFile]
#UserDB = [ReadFile]                                         # 유저 정보를 저장할 리스트 
#print("11111{}".format(ReadFile))
#print("{}".format(UserDB))
def UserResit(UserInfo):                            # 유저 등록 함수 
    UserDB.append(UserInfo)                         #유저에게 입력받은 이름, 나이, 전공을 dictionary로 저장해 UserDB에 추가한다
    return print("성공")

def UserList():                                     #유저 정보 보기 함수
    return print("수강생 명단 {}".format(UserDB))   #유저 정보를 print 해준다


def UserSearch(UserName):                           #유저 검색 함수 
    for i , dic_a in enumerate(UserDB):             # enumerate로 쪼개 i만큼 돌때 dic_a에 UserDB[i]를 집어넣는다
        if dic_a["UserName"] == UserName:           # 만약 위에서 쪼갠 dic_a의 UserName 과 입력받은 UserName이 같다면 If문을 실행 시킨다
            return i                                # i 는 if 문에서 멈췄을 때 i의 값으로 인덱스라고 생각하면 된다 
        return None
def F_UserDel(UserName):                            # 유저 삭제 함수
    #UserDelInfo = UserSearch(UserName)
    #print(UserDelInfo)
    #del(UserDelInfo)
    dic_Del = UserSearch(UserName)                  # dic_Del 에 유저 검색 함수에서 찾은 인덱스를 저장한다 0~N
    del(UserDB[dic_Del])                            # 입력받은 인덱스 정보로 UserDB의 dic_Del 인덱스 번째 정보를 삭제한다
    # UserDB.pop(인덱스) 또는 UserDB.remove(UserDB[인덱스])

    return print("성공")

def UserModify(UserName):                               # 유저 수정 함수
    UserModIndex = UserSearch(UserName)                 # 검색 함수에서 인덱스를 받는다
    UserModiAge = input("수정할 나이을 입력해 주세요 ")  
    UserModiMajor = input("수정할 전공을입력해 주세요")
    UserModiInfo =UserDB[UserModIndex]                  # UserDB의 인덱스 번째 정보를 dictionary에 저장한다 ( 리스트의 주소값이 저장된다)
    UserModiInfo["UserAge"] = UserModiAge               # 각각 키와 맞는 정보를 입력받은 값으로 변경한다
    UserModiInfo["UserMajor"] = UserModiMajor           # 위와 같음
    #return UserModiInfo    
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
                print(UserDB[i]["UserName"])
                FileUserName = str(UserDB[i]["UserName"])
                FileUserAge = str(UserDB[i]["UserAge"])
                FileUserMajor = str(UserDB[i]["UserMajor"])
                if i == len(UserDB)-1:
                    file.write("{},{},{}".format(FileUserName,FileUserAge,FileUserMajor))
                else:
                    file.write("{},{},{}\n".format(FileUserName,FileUserAge,FileUserMajor))


UserDB = ReadData()
while True :
    
    UserInput = input("당신의 선택은")
    print(UserInput)
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
