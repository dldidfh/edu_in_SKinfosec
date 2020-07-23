#import class_prac
# import student
# import Teacher
# import Employ
from class_prac import Student, Teacher, Employ, Person
#from 2020_07_13.


# S_ai01 = class_prac.Student("S_ai01", "이양로", "정보통신")
# S_ai01.info()

# T_ai01 = class_prac.Teacher("T_ai01","권구엽","정보통신교과목가르친다")
# T_ai01.info()

# E_ai01 = class_prac.Teacher("E_ai01","나윤호","어떤직무를 맏고있다")
# E_ai01.info()

# ai_list = [ class_prac.Student("S_ai01", "이양로", "정보통신"), 
#             class_prac.Teacher("T_ai01","권구엽","정보통신교과목가르친다"),
#             class_prac.Employ("E_ai01","나윤호","어떤직무를 맏고있다")
#             ]
ai_list = [ Student("S_ai01", "이양로", "정보통신"), 
            Student("S_ai01", "배소현", "산공"),    
            Teacher("T_ai01","권구엽","정보통신교과목가르친다"),
            Employ("E_ai01","나윤호","어떤직무를 맏고있다")
            ]
if Person.__eq__():
    print("존재하는 데이터")
else:
    print("쌉가능한 데이터")
for ai in ai_list :
    # if(isinstance(ai,class_prac.Student)):
    #     ai.info()
    # elif isinstance(ai,class_prac.Teacher):
    #     ai.info()
    # elif isinstance(ai, class_prac.Employ):
    #     ai.info()
    ai.info()

