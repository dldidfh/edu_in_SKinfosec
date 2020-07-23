from ai_exception import DuplicateException, RecordNotFoundException
from filestore import save_data, read_data

class AIService:
    #AIEntuty 정보를 저장하는 클래스 변수
    ai_list =[]
  
    #수강생등록 : email 존재여부 체크
    def register(self,ai_entity):
        index = self.is_exist(ai_entity.email)
        if index < 0:
            AIService.ai_list.append(ai_entity)
            return ai_entity.name+"님 등록되었습니다."
        else:
            try:
                raise DuplicateException(ai_entity.name)  
            except DuplicateException as error:
                return str(error)


    #수강생목록
    def get_all_entity(self):
        return AIService.ai_list

    #수강생정보 수정
    def entity_update(self,ai_entity):
        index = self.is_exist(ai_entity.email)
        if index > -1 :
            ai = AIService.ai_list[index]
            ai.name=ai_entity.name
            ai.age=ai_entity.age
            ai.major=ai_entity.major
            return ai_entity.name+"님 정보수정 되었습니다."
        else:
            try:
                raise RecordNotFoundException(ai_entity.name)
            except RecordNotFoundException as updateError:
                return str(updateError)
    
    #수강생정보 삭제
    def entity_remove(self,email):
        index = self.is_exist(email)
        if index > -1:
            AIService.ai_list.pop(index)
            return email+" 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeError:
                return str(removeError)
           
    #수강생 상세 정보
    def get_ai_entity(self,email):
        index = self.is_exist(email)
        if index > -1:
            return AIService.ai_list[index]
        else:
            return None
                
        # for value in enumerate(AIService.ai_list):
        #     if value.email == email:
        #         return value
        # try:
        #     raise RecordNotFoundException(email)
        # except RecordNotFoundException as searchError:
        #     return str(searchError)

    #email 존재여부
    def is_exist(self,email):
        for index, entity in enumerate(AIService.ai_list):
            if entity.email == email:
                return index
        return -1

    #file store 저장
    def save_list(self):
        save_data(AIService.ai_list)
    
    #file store read
    def read_list(self):
        AIService.ai_list = read_data()

