from tkinter import *
from tkinter.ttk import *
import os
import json


def Read_MAA_Config(path):
    with open(path,"r",encoding='utf-8') as MAA_Config:
    #打开json并传入MAA_data
        MAA_data = json.load(MAA_Config)
        return MAA_data
    
def Save_MAA_Config(path,data):
    #打开json并写入data内数据
    with open(path,"w",encoding='utf-8') as MAA_Config:
        json.dump(data,MAA_Config,indent=4,ensure_ascii=False)

def Get_Values_list(path,key1):
    #获取组件的初始参数
    List = []
    for i in Read_MAA_Config(path)[key1]:
        List.append(i["name"])
    return List

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_Start_Task = self.__tk_button_Start_Task(self)
        self.tk_label_ADB_Part_Label = self.__tk_label_ADB_Part_Label(self)
        self.tk_label_ADB_Address_Label = self.__tk_label_ADB_Address_Label(self)
        self.tk_label_Resource_Type_Label = self.__tk_label_Resource_Type_Label(self)
        self.tk_label_Add_Task_Label = self.__tk_label_Add_Task_Label(self)
        self.tk_label_Add_Task_Label_2 = self.__tk_label_Add_Task_Label_2(self)
        self.tk_input_ADB_Path_Input = self.__tk_input_ADB_Path_Input(self)
        self.tk_input_ADB_Address_Input = self.__tk_input_ADB_Address_Input(self)
        self.tk_select_box_Resource_Type_Select = self.__tk_select_box_Resource_Type_Select(self)
        self.tk_select_box_Add_Task_Select = self.__tk_select_box_Add_Task_Select(self)
        self.tk_button_Add_Task_Button = self.__tk_button_Add_Task_Button(self)
        self.tk_label_Task_List_Label = self.__tk_label_Task_List_Label(self)
        self.tk_list_box_Task_List = self.__tk_list_box_Task_List(self)
        self.tk_button_Move_Up_Button = self.__tk_button_Move_Up_Button(self)
        self.tk_button_Move_Down_Button = self.__tk_button_Move_Down_Button(self)
        self.tk_button_Delete_Button = self.__tk_button_Delete_Button(self)
        self.tk_select_box_Add_Task_Select_1 = self.__tk_select_box_Add_Task_Select_1(self)
        self.tk_select_box_Add_Task_Select_2 = self.__tk_select_box_Add_Task_Select_2(self)
        self.tk_select_box_Add_Task_Select_3 = self.__tk_select_box_Add_Task_Select_3(self)
        self.tk_select_box_Add_Task_Select_4 = self.__tk_select_box_Add_Task_Select_4(self)
        self.tk_label_Add_Task_Label_3 = self.__tk_label_Add_Task_Label_3(self)
        self.tk_label_Add_Task_Label_4 = self.__tk_label_Add_Task_Label_4(self)
        self.tk_label_Add_Task_Label_5 = self.__tk_label_Add_Task_Label_5(self)
        self.tk_label_Add_Task_Label_6 = self.__tk_label_Add_Task_Label_6(self)
    def __win(self):
        self.title("MAA-GUI")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_button_Start_Task(self,parent):
        btn = Button(parent, text="开始任务", takefocus=False,)
        btn.place(x=200, y=460, width=70, height=30)
        return btn
    def __tk_label_ADB_Part_Label(self,parent):
        label = Label(parent,text="ADB路径",anchor="center", )
        label.place(x=0, y=0, width=70, height=30)
        return label
    def __tk_label_ADB_Address_Label(self,parent):
        label = Label(parent,text="ADB端口",anchor="center", )
        label.place(x=0, y=40, width=70, height=30)
        return label
    def __tk_label_Resource_Type_Label(self,parent):
        label = Label(parent,text="客户端类型",anchor="center", )
        label.place(x=0, y=80, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label(self,parent):
        label = Label(parent,text="添加任务",anchor="center", )
        label.place(x=0, y=120, width=340, height=30)
        return label
    def __tk_label_Add_Task_Label_2(self,parent):
        label = Label(parent,text="任务类型",anchor="center", )
        label.place(x=0, y=160, width=70, height=30)
        return label
    def __tk_input_ADB_Path_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=0, width=260, height=30)
        return ipt
    def __tk_input_ADB_Address_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=40, width=260, height=30)
        return ipt
    def __tk_select_box_Resource_Type_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = (Get_Values_list(os.getcwd()+"\MAA_bin\interface.json","resource"))
        cb.place(x=80, y=80, width=140, height=30)
        return cb
    def __tk_select_box_Add_Task_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = (Get_Values_list(os.getcwd()+"\MAA_bin\interface.json","task"))
        cb.place(x=80, y=160, width=260, height=30)
        return cb
    def __tk_button_Add_Task_Button(self,parent):
        btn = Button(parent, text="添加任务", takefocus=False,)
        btn.place(x=80, y=460, width=70, height=30)
        return btn
    def __tk_label_Task_List_Label(self,parent):
        label = Label(parent,text="任务列表",anchor="center", )
        label.place(x=380, y=0, width=180, height=30)
        return label
    def __tk_list_box_Task_List(self,parent):
        lb = Listbox(parent)
        for item in Get_Values_list(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task"):
            lb.insert(END, item)
        lb.place(x=360, y=40, width=220, height=400)
        return lb
    def __tk_button_Move_Up_Button(self,parent):
        btn = Button(parent, text="上移", takefocus=False,)
        btn.place(x=360, y=460, width=50, height=30)
        return btn
    def __tk_button_Move_Down_Button(self,parent):
        btn = Button(parent, text="下移", takefocus=False,)
        btn.place(x=445, y=460, width=50, height=30)
        return btn
    def __tk_button_Delete_Button(self,parent):
        btn = Button(parent, text="删除", takefocus=False,)
        btn.place(x=530, y=460, width=50, height=30)
        return btn
    def __tk_select_box_Add_Task_Select_1(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("1号选项")
        cb.place(x=80, y=200, width=260, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_2(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("2号选项")
        cb.place(x=80, y=240, width=260, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_3(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("3号选项")
        cb.place(x=80, y=280, width=260, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_4(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("4号选项")
        cb.place(x=80, y=320, width=260, height=30)
        return cb
    def __tk_label_Add_Task_Label_3(self,parent):
        label = Label(parent,text="1号标签",anchor="center", )
        label.place(x=0, y=200, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label_4(self,parent):
        label = Label(parent,text="2号标签",anchor="center", )
        label.place(x=0, y=240, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label_5(self,parent):
        label = Label(parent,text="3号标签",anchor="center", )
        label.place(x=0, y=280, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label_6(self,parent):
        label = Label(parent,text="4号标签",anchor="center", )
        label.place(x=0, y=320, width=70, height=30)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_Start_Task.bind('<Button-1>',self.ctl.Start_Task)
        self.tk_input_ADB_Path_Input.bind('<Return>',self.ctl.Save_ADB_Path)
        self.tk_input_ADB_Address_Input.bind('<Return>',self.ctl.Save_ADB_Address)
        self.tk_select_box_Resource_Type_Select.bind('<<ComboboxSelected>>',self.ctl.Save_Resource_Type_Select)
        self.tk_select_box_Add_Task_Select.bind('<<ComboboxSelected>>',self.ctl.Add_Task_Select_More_Select)
        self.tk_button_Add_Task_Button.bind('<Button-1>',self.ctl.Add_Task)
        self.tk_button_Move_Up_Button.bind('<Button-1>',self.ctl.Click_Move_Up_Button)
        self.tk_button_Move_Down_Button.bind('<Button-1>',self.ctl.Click_Move_Down_Button)
        self.tk_button_Delete_Button.bind('<Button-1>',self.ctl.Click_Delete_Button)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()