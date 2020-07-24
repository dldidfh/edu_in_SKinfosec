class AIEntity:
    #생성자정의 : member variable - name, age, email, major 초기화
    def __init__(self, name, age, email, major):
        self.name=name
        self.age=age
        self.email = email
        self.major=major

    #email정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if(self.email == email):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} ".format(self.name, self.email, self.major)


    #toJson   : Entity -> json 변환 
    #fromJson : jons -> Entity 변환

