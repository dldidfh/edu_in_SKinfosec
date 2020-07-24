import os.path

# #ai_list ai_list.dat 파일저장
# def save_data(ai_list):
#     save_file = open("ai_list.dat", "w")
#     for index, entity in enumerate(ai_list):
#         save_file.write("{0}번째 | {1},{2},{3},{4}\n".format(index,entity.name,entity.age,entity.email,entity.major))
#     save_file.close()

# #ai_list.dat 파일 내용 ai_list에 append
# def read_data():
#     ai_list=[]
#     fileExist = os.path.isfile("ai_list.dat")
#     if fileExist:
#         read_file = open("ai_list.dat","r")
#         while True:
#             ai_data = read_file.readline()
#             if len(ai_data.split("|")) == 2 :
#                 ai = ai_data.split("|")[1].rstrip("\n").split(",")
#                 ai_list.append(AIEntity(ai[0].strip(),int(ai[1].strip()),ai[2].strip(),ai[3].strip()))
#             if not ai_data:
#                 break
#         read_file.close()
#     return ai_list

