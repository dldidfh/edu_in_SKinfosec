#View : 입력하는 화면제공, 결과값 출력
try:
    import Tkinter as tk
except:
    import tkinter as tk

from pro_cont import ProController
from domain import ProEntity
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

def close_program(self):
    ProController.close(self)
    self.close

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("제품 관리 프로그램")
        master.geometry("640x400")

        dict_pro = {
            "제품 등록" : ProRegist,
            "제품 리스트" : ProShowList,
            "제품 수정" : ProModify,
            "제품 삭제" : ProDelete,
            "제품 이름 검색" : ProSearchAsName,      
        }       
        key_dict = dict_pro.keys()
        for value in key_dict :
            tk.Button(self, text=value,
                command=lambda v= dict_pro[value] : master.switch_frame(v), width=30,pady=10).pack()
        tk.Button(self, text="닫기",
                command=close_program(self) , width=30,pady=10).pack()        

class ProRegist(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="제품 등록", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        frame1 = tk.Frame(self)
        frame1.pack(fill="x")
        tk.Label(frame1, text="제품명", width=10).pack(side="left", padx=10, pady=10)
        proName = tk.Entry(frame1)
        proName.pack(fill="x", padx=10, expand=True)
        inputName = proName.get()
        btnDupl =  tk.Button(frame1, text="중복확인",width=10, command=self.duplication(inputName))
        btnDupl.pack(side="left", padx=10, pady=10)

        frame2 = tk.Frame(self)
        frame2.pack(fill="x")
        tk.Label(frame2, text="가격", width=10).pack(side="left", padx=10, pady=10)
        proPrice = tk.Entry(frame2)
        proPrice.pack(fill="x", padx=10, expand=True)
        inputPrice = proPrice.get()

        frame3 = tk.Frame(self)
        frame3.pack(fill="x")
        tk.Label(frame3, text="무게", width=10).pack(side="left", padx=10, pady=10)
        proWeight = tk.Entry(frame3)
        proWeight.pack(fill="x", padx=10,expand=True)
        inputWeight = proWeight.get()
        
        frame4 = tk.Frame(self)
        frame4.pack(fill="x")
        tk.Label(frame4, text="크키", width=10).pack(side="left", padx=10, pady=10)
        proSize = tk.Entry(frame4)
        proSize.pack(fill="x", padx=10,expand=True)
        inputSize = proSize.get()

        # 저장
        ProEntity(inputName,inputPrice,inputWeight,inputSize)
        frame5 = tk.Frame(self)
        frame5.pack(fill="x")
        btnSave = tk.Button(frame5, text="저장",width=10, command=self.regist_product(ProEntity))
        btnSave.pack(side="left", padx=10, pady=10)
        tk.Button(frame5, text="첫화면으로",
                  command=lambda: master.switch_frame(StartPage),width=10).pack(padx=10, pady=10)
    def duplication(self,proName):
        ProController.duplication_pro_name(self,proName)

    def regist_product(self,proEntity):
        ProController.register_controller(self,ProEntity)

class ProShowList(tk.Frame):
    def __init__(self, master):

        product_list = ProController.get_all_entity_controller(self)
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="제품 리스트", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        listbox = tk.Listbox(self, selectmode='extended', height=0)
        for i, value in product_list:
            listbox.insert(i,value)
        tk.Button(self, text="첫화면으로",
                  command=lambda: master.switch_frame(StartPage)).pack()

class ProModify(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="제품 정보 수정", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        frame1 = tk.Frame(self)
        frame1.pack(fill="x")
        tk.Label(frame1, text="제품명", width=10).pack(side="left", padx=10, pady=10)
        proName = tk.Entry(frame1)
        proName.pack(fill="x", padx=10, expand=True)
        inputName = proName.get()
        btnDupl =  tk.Button(frame1, text="제품명 확인",width=10, command=self.duplication(inputName))
        btnDupl.pack(side="left", padx=10, pady=10)

        frame2 = tk.Frame(self)
        frame2.pack(fill="x")
        tk.Label(frame2, text="가격", width=10).pack(side="left", padx=10, pady=10)
        proPrice = tk.Entry(frame2)
        proPrice.pack(fill="x", padx=10, expand=True)
        inputPrice = proPrice.get()

        frame3 = tk.Frame(self)
        frame3.pack(fill="x")
        tk.Label(frame3, text="무게", width=10).pack(side="left", padx=10, pady=10)
        proWeight = tk.Entry(frame3)
        proWeight.pack(fill="x", padx=10,expand=True)
        inputWeight = proWeight.get()
        
        frame4 = tk.Frame(self)
        frame4.pack(fill="x")
        tk.Label(frame4, text="크키", width=10).pack(side="left", padx=10, pady=10)
        proSize = tk.Entry(frame4)
        proSize.pack(fill="x", padx=10,expand=True)
        inputSize = proSize.get()

        # 저장
        ProEntity(inputName,inputPrice,inputWeight,inputSize)
        frame5 = tk.Frame(self)
        frame5.pack(fill="x")
        btnSave = tk.Button(frame5, text="저장",width=10, command=self.product_update(ProEntity))
        btnSave.pack(side="left", padx=10, pady=10)
        tk.Button(frame5, text="첫화면으로",
                  command=lambda: master.switch_frame(StartPage),width=10).pack(padx=10, pady=10)
    def duplication(self,proName):
        ProController.duplication_pro_name(self,proName)

    def product_update(self,ProEntity):
        ProController.update_controller(self,ProEntity)

class ProDelete(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="제품 정보 삭제", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        frame1 = tk.Frame(self)
        frame1.pack(fill="x")
        tk.Label(frame1, text="제품명", width=10).pack(side="left", padx=10, pady=10)
        proName = tk.Entry(frame1)
        proName.pack(fill="x", padx=10, expand=True)
        btnDupl =  tk.Button(frame1, text="삭제",width=10, command=self.product_delete(self,proName))
        btnDupl.pack(side="left", padx=10, pady=10)

        tk.Button(self, text="첫화면으로",
                  command=lambda: master.switch_frame(StartPage)).pack()
    def product_delete(self,proName):
        ProController.delete_controller(self,proName)

class ProSearchAsName(tk.Frame):
    def __init__(self, master):
        print(ProSearchAsName)
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="제품명 정보 검색", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        frame1 = tk.Frame(self)
        frame1.pack(fill="x")
        tk.Label(frame1, text="제품명", width=10).pack(side="left", padx=10, pady=10)
        proName = tk.Entry(frame1)
        proName.pack(fill="x", padx=10, expand=True)
        btnDupl =  tk.Button(frame1, text="결과 확인",width=10, command=self.product_search_as_name(proName))
        btnDupl.pack(side="left", padx=10, pady=10)

        
        tk.Button(self, text="첫화면으로",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def product_search_as_name(self,proName):
        ProController.get_entity_controller(self,proName)

def MessageBox(self,message):
    tk.messagebox.showinfo("결과",message=message)
    

# class ProClose(tk.Frame):
#     def __init__(self, master):
#         print("종료")
#         sys.exit()
       