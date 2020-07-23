

# asd = input("정수입력 : ")
# try:
#     #정상흐름 실행문
#     print("입력받은 데이터 : {}".format(int(asd)))
# except :
#     #비정상흐름 시 실행하는 실행문
#     print("잘못 입력하신거 같은데예?>")
# else:
#     #정상흐름 실행문 
#     print("else")
# finally:
#     #예외 발생 여부 상관없이 항상 실행
#     #보통 자원반납 db연결종료 같은 실행 
#     print("Finally")
# print("트라이문 밖")
# #multi exception 하나의 try문에 
# try:
# except Exception as errorExcept:
# except ValueError as errorValue:
# #자식type 의 Exception 부터 처리
# Except e
list1 = [10,20,30,40,50]
try :
    InputInt = int(input("정수형 데이터"))                          #ValueError
    list1.append(InputInt)
    for i in range(len(list1)):
        div = list1[i] + list1[i]/i                                 #ZeroDivisionError
        print("{}번째 데이터는 {} 입니다.".format(i,list1[i]))       #IndexError
except ValueError as ErrorValue:
    print("정수를 입력해 주세여")
except IndexError as ErrorIndex:
    print("for문이 작동중에 리스트값을 넘었습니다")
except ZeroDivisionError as ErrorZeroDiv:
    print("0은 0으로 나눌 수 없습니다.")
except Exception as ErrorExcep:
    print("예기치 못한 에러 발생")
#뭉뜽그려서 광범위하게 Exception 으로 처리하면 나중에 오류에서 오류난 부분을 찾기 힘드니 최대한 자세하게 오류처리를 하자





