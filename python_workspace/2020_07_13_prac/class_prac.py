class Person:
    #여기에 변수 쓰면 static 변수로 딱 한 번 초기화됨  전역변수 같은 느낌 
    #
    # 클래스변수 클래스가 호출될 때 정의가 되서 메모리상 하나의 메모리주소값을 가진다
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __eq__(self, id):
        if(self.id == id):
            return True
        else : return False
    def __str__(self):
        print("ID : {} \t NAME : {} \t ".format(self.id,self.name))


class Student(Person) :
    def __init__(self,id, name, major):
        super().__init__(id,name)
        #super.id = id
        #super.name = name
        self.major = major
    def info(self):
        super().__str__()
        print("전공 {}".format(self.major))

class Teacher(Person) :
    def __init__(self,id,name,subject):
        super().__init__(id,name)
        self.subject = subject
    def info(self):
        super().__str__()
        print("담당과목 {}".format(self.subject))

class Employ(Person) :
    def __init__(self,id,name,department):
        super().__init__(id,name)
        self.department = department
        print()
    def info(self):
        super().__str__()
        print("담당과목 {}".format(self.department))


