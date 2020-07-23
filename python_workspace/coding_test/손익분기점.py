# def calc(A,B,C):
#     i = 0
    
#     while True:
#         if B>C:
#             return -1
#         i+=1
#         if A<(C-B)*i:
#             break
#     return i
#print(calc(1000,70,70))

    
A, B, C = map(int, input().split())

if B>=C :
    print(-1)
else:
    i = int(A/(C-B)) + 1
    print(i)

    