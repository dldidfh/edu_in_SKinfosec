#View : 입력하는 화면제공, 결과값 출력
try:
    import Tkinter as tk
except:
    import tkinter as tk
    #LabelFrame
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
            "닫기" : ProClose
        }
        key_dict = dict_pro.keys()
        for value in key_dict :
            print(dict_pro[value])
            tk.Button(self, text=value,
                command=lambda: master.switch_frame(dict_pro[value])).pack()
        # tk.Button(self, text="닫기",
        #            command=self.quit).pack()

class ProRegist(tk.Frame):
    def __init__(self, master):
        print("ProRegist")
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="11111111111111", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class ProShowList(tk.Frame):
    def __init__(self, master):
        print("ProShowList")
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="2222222222222", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class ProModify(tk.Frame):
    def __init__(self, master):
        print("ProModify")
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="333333333333", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class ProDelete(tk.Frame):
    def __init__(self, master):
        print(ProDelete)
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class ProSearchAsName(tk.Frame):
    def __init__(self, master):
        print(ProSearchAsName)
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class ProClose(tk.Frame):
    def __init__(self, master):
        print(ProClose)
        self.destroy()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


        