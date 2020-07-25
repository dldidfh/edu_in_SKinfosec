from pro_service import ProService
from pro_view import MessageBox

class ProController:
    #중복확인
    def duplication_pro_name(self,proName):
        #서비스에 중복 확인 함수 
        if proName == "" or len(proName) == 0:
            return MessageBox(self,"제품명을 입력해 주세요")
        else:
            getProName = ProService().is_exist(proName)
            if getProName != None:
               return MessageBox(self,"이미 등록된 제품입니다")
               
            else: 
               return MessageBox(self,"사용 가능합니다")   
                
    #등록
    def register_controller(self, pro_entity):
            message = ProService().register(pro_entity)
            MessageBox(self,message)
    #리스트로 가져오기
    def get_all_entity_controller(self):
        pro_list = ProService.get_all_entity(self)
        return pro_list
      
    #수정하기
    def update_controller(self,pro_entity):
        if pro_entity.proName == "" or len(pro_entity.proName) ==0 :
            MessageBox(self,"이메일 형식이 잘못됐습니다.")
        else:
           
            message = ProService().entity_update(pro_entity)
            MessageBox(self,message)
    #삭제하기
    def delete_controller(self, proName):
        if proName == "" or len(proName) == 0 :
            MessageBox(self,"이메일 형식이 잘못됐습니다.") 
        else:
            message = ProService().entity_remove(proName)
            MessageBox(self,message)

    def get_entity_controller(self,proName):
        if proName == "" or len(proName) == 0 :
            MessageBox(self,"제품명 형식이 잘못됐습니다.")        
        else:
            pro_entity = ProService().get_pro_entity(proName)
            if pro_entity != None :
                return pro_entity
            else:
                MessageBox(self,"존재하지 않습니다.") 
    
    def close(self):
        ProService.close_DB(self)


