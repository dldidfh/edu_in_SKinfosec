




# tuple_data = 10,20,30
# tuple_data2 = 30,20,10
# print(type(tuple_data), type(tuple_data2))
# print(tuple_data)
# #tuple_data[1] = 100  튜플은 변경 불가 
# tuple_data = tuple_data2
# print(tuple_data2)

# def incl(v,o):
#     return o+v

# ori_list = [10,20,30,40,50]
# print(ori_list)
# for i,Value in enumerate(ori_list):
#     ori_list[i] = incl(5,Value)
# print(ori_list)
# def inc(v):
#     return v + 10
# def dec(v):
#     return v - 10

# def call_changedata(func,orig):
#     new_list=[]
#     for i, value in enumerate(orig):
#         new_list.append(func(value))

#     return new_list

original = [10,20,30,40,50]
char_filter = ["가","나","다","라","마"]
# print(original)
# print(list(map(inc,original)))
# print(list(map(dec,original)))
# print(list(map(lambda v: v+10,original)))
# 수강생 수정 을 (Lambda UserDB : UserDB.remove(), UserSearch(Name))
# print(list(map(lambda v: v-10,original)))
# print(list(filter(lambda v: v>20,original)))
print(list(filter(lambda v: v<"마",char_filter)))
# print(call_changedata(inc,original))
# print(call_changedata(dec,original))
# print(original)

