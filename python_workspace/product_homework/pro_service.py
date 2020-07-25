from pro_db import ProStore
from domain import ProEntity
class ProService:
    db = ProStore()
    def get_pro_name(self,proName):
        result = ProService.db.select_by_proName(proName)
        return result
    def register(self,pro_entity):
        result = self.is_exist(pro_entity.name)
        if not bool(result):
            ProService.db.insert(pro_entity)
            return pro_entity.proName+"이 등록되었습니다."

    #수강생목록
    def get_all_entity(self):
        return ProService.db.select_all()

    #수강생정보 수정
    def entity_update(self,pro_entity):
        result = self.is_exist(pro_entity.name)
        if bool(result) :
            ProService.db.update(pro_entity)
            return pro_entity.proName+"의 정보가 수정 되었습니다."

    #수강생정보 삭제
    def entity_remove(self,name):
        result = self.is_exist(name)
        if bool(result):
            ProService.db.delete(name)
            return name+"이 삭제 되었습니다."

    #수강생 상세 정보
    def get_pro_entity(self,name):
        result = self.is_exist(name)
        if bool(result):
            return ProEntity(result["proName"],result["proPrice"],result["proWeight"],result["proSize"])

    def is_exist(self,name):
        result = ProService.db.select_by_proName(name)
        return result
    def close_DB(self):
        ProService.db.close()