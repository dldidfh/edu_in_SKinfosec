
# array=[1,2,3,4,5]
# for data in array:
#     print(data, end="\t")

diction_a = { 
    "name" : "이야올",
    'age' : "27" , 
    "addr" : "sdfsdf"
}
diction_b = {
    "name" : "권구엽",
    'age' : 26,
    "addr" : "asdaf"
}
diction_c = {
    1 : "asd",
    2 : "asdd",
    3 : "qwe"
}
# del diction_c[3]
# print(diction_c)
# list1 = [diction_a,diction_b]
# print("나의 이름은 {0} 나이는 {1}  주소는 {2}".format(diction_a["name"],diction_a["age"],diction_a["addr"]))
# # print(diction_a["name"])    

# for data in list1:
#     print(data["name"], data["age"], data["addr"])

#모든 dictionary에 한 키값을 모두 삭제하기
#list1 = [diction_a,diction_b,diction_c]
# asd = input("삭제할 키값을 설정해 주시죠")
# #포문 리스트 = 딕셔너리 반환 , 딕셔너리 포문 = 키값 반환
# print(asd)
# for data in list1 :
#     if asd in data :
#         del data[asd]
#     else:
#         print("{}에는 없는값입니다.".format(data))
# print(" 삭제한 키값은 {0} 이고 남은 리스트는 {1}입니다".format(asd,list1))  

# zxc = len(list1)
# #range

# for i in reversed(range(0,zxc)) : 
#     print(list1[i])
#     print(i)
# for i in range(0,4,1):
#     print(i)
# # for i in range(4,-1,-1):
# #     print(i)

# print(i)

# i = 0
# while i <10:
#     print("{}번쨰 반복한 i는 {}".format(i+1,i))
#     i+=1

# for i in range(0,11,2):
#     if i == 0 :
#         continue
#     else:
#         print(i)
# for i in range(0,11):
#     if i == 0 :
#         continue
#     elif i % 2 == 0:
#         print(i)
# i = 0
# while i <11 :
#     if i != 0 and i % 2 == 0 :
#         print(i)

i = 1
x = 1
z = 1
list1= [1,2,3,4,5,6,7,8,9]
list2= [1,2,3,4,5,6,7,8,9]
# for i in range(1,10):
#     for x in list1:
#         print("{0} * {1} = {2}  ".format(x,i,i*x),end="\t")        
#     print("")

# for i in list1:
#     print("{0}*{1} = {2}  ".format(list1[i-1],list2[i-1],list1[i-1]*list2[i-1]))

#print(list(enumerate(list2)))
# list_diction = [diction_b,diction_c,diction_a]
# print(diction_a.items())
# print(list(enumerate(list_diction)))


array_list = [data+data for data in list1 if data != 2]
print(array_list)

