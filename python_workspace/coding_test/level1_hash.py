# def solution(participant, completion):
#     answer = ''
#     for i , v in enumerate(participant) :
#         for index,value in enumerate(completion):
#             if v != value:
                
        
#     return answer
import collections
def solution(participant, completion):
    answer = ''
    participant = list(set(participant))
    completion = list(set(completion))
    for i,v in enumerate(participant):
        tmp = 0
        for index,value in enumerate(completion):
            if v == value:
                tmp +=1
                del participant[i]
                print(participant,completion)
        if tmp == 0 :
            answer = participant[i]
    
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
#"leo", "kiki", "eden"
#"marina", "josipa", "nikola", "vinko", "filipa"
#"marina", "josipa", "nikola", "vinko"
#"eden", "kiki"
#mislav, stanko, mislav, ana
#stanko, ana, mislav]
