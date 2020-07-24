from ai_exception import DuplicateException, RecordNotFoundException
from DBstore import AIStore
from domain import AIEntity

class AIService:
    #AIEntuty 정보를 저장하는 클래스 변수
    db = AIStore()
  
    #수강생등록 : email 존재여부 체크
    def register(self,ai_entity):
        result = self.is_exist(ai_entity.email)
        if not bool(result):
            AIService.db.insert(ai_entity)
            return ai_entity.name+"님 등록되었습니다."
        else:
            try:
                raise DuplicateException(ai_entity.name)  
            except DuplicateException as error:
                return str(error)


    #수강생목록
    def get_all_entity(self):
        return AIService.db.select_all()

    #수강생정보 수정
    def entity_update(self,ai_entity):
        result = self.is_exist(ai_entity.email)
        if bool(result) :
            AIService.db.update(ai_entity)
            return ai_entity.name+"님 정보수정 되었습니다."
        else:
            try:
                raise RecordNotFoundException(ai_entity.name)
            except RecordNotFoundException as updateError:
                return str(updateError)
    
    #수강생정보 삭제
    def entity_remove(self,email):
        result = self.is_exist(email)
        if bool(result):
            AIService.db.delete(email)
            return email+" 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeError:
                return str(removeError)
           
    #수강생 상세 정보
    def get_ai_entity(self,email):
        result = self.is_exist(email)
        if bool(result):
            return AIEntity (result["name"],result["age"],result["email"],result["major"])
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as SearchError:
                return str(SearchError)
                
        # for value in enumerate(AIService.ai_list):
        #     if value.email == email:
        #         return value
        # try:
        #     raise RecordNotFoundException(email)
        # except RecordNotFoundException as searchError:
        #     return str(searchError)

    #email 존재여부
    def is_exist(self,email):
        result = AIService.db.select_by_email(email)
        return result

    def close_DB(self):
        AIService.db.close()