from tool import *
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_Main_Tabs = self.__tk_tabs_Main_Tabs(self)
        self.tk_label_Stable_loca = self.__tk_label_Stable_loca( self.tk_tabs_Main_Tabs_1)
        self.tk_button_Check_Update_Button = self.__tk_button_Check_Update_Button( self.tk_tabs_Main_Tabs_1)
        self.tk_label_Stable_online = self.__tk_label_Stable_online( self.tk_tabs_Main_Tabs_1)
        self.tk_button_Update_button = self.__tk_button_Update_button( self.tk_tabs_Main_Tabs_1)
        self.tk_label_frame_ADB_Setting_Frame = self.__tk_label_frame_ADB_Setting_Frame( self.tk_tabs_Main_Tabs_1)
        self.tk_label_ADB_Part_Label = self.__tk_label_ADB_Part_Label( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_label_ADB_Address_Label = self.__tk_label_ADB_Address_Label( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_button_Auto_Detect_ADB_Button = self.__tk_button_Auto_Detect_ADB_Button( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_input_ADB_Address_Input = self.__tk_input_ADB_Address_Input( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_input_ADB_Path_Input = self.__tk_input_ADB_Path_Input( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_select_box_Auto_Detect_ADB_Select = self.__tk_select_box_Auto_Detect_ADB_Select( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_label_Controller_Type_Label = self.__tk_label_Controller_Type_Label( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_label_Resource_Type_Label = self.__tk_label_Resource_Type_Label( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_select_box_Controller_Type_Select = self.__tk_select_box_Controller_Type_Select( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_select_box_Resource_Type_Select = self.__tk_select_box_Resource_Type_Select( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_label_StartApp = self.__tk_label_StartApp( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_input_StartAPP_Address = self.__tk_input_StartAPP_Address( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_input_StartAPP_Address_P = self.__tk_input_StartAPP_Address_P( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_label_StartAPP_P = self.__tk_label_StartAPP_P( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_label_frame_Task_List_Frame = self.__tk_label_frame_Task_List_Frame( self.tk_tabs_Main_Tabs_0)
        self.tk_list_box_Task_List = self.__tk_list_box_Task_List( self.tk_label_frame_Task_List_Frame) 
        self.tk_label_frame_Select_Task_Frame = self.__tk_label_frame_Select_Task_Frame( self.tk_tabs_Main_Tabs_0)
        self.tk_label_Add_Task_Label_1 = self.__tk_label_Add_Task_Label_1( self.tk_label_frame_Select_Task_Frame) 
        self.tk_label_Add_Task_Label_3 = self.__tk_label_Add_Task_Label_3( self.tk_label_frame_Select_Task_Frame) 
        self.tk_label_Add_Task_Label_2 = self.__tk_label_Add_Task_Label_2( self.tk_label_frame_Select_Task_Frame) 
        self.tk_select_box_Add_Task_Select = self.__tk_select_box_Add_Task_Select( self.tk_label_frame_Select_Task_Frame) 
        self.tk_select_box_Add_Task_Select_2 = self.__tk_select_box_Add_Task_Select_2( self.tk_label_frame_Select_Task_Frame) 
        self.tk_select_box_Add_Task_Select_1 = self.__tk_select_box_Add_Task_Select_1( self.tk_label_frame_Select_Task_Frame) 
        self.tk_select_box_Add_Task_Select_3 = self.__tk_select_box_Add_Task_Select_3( self.tk_label_frame_Select_Task_Frame) 
        self.tk_select_box_Add_Task_Select_4 = self.__tk_select_box_Add_Task_Select_4( self.tk_label_frame_Select_Task_Frame) 
        self.tk_label_Add_Task_Label_4 = self.__tk_label_Add_Task_Label_4( self.tk_label_frame_Select_Task_Frame) 
        self.tk_label_Add_Task_Label = self.__tk_label_Add_Task_Label( self.tk_label_frame_Select_Task_Frame) 
        self.tk_frame_Button_Frame = self.__tk_frame_Button_Frame( self.tk_tabs_Main_Tabs_0)
        self.tk_button_Delete_Button = self.__tk_button_Delete_Button( self.tk_frame_Button_Frame) 
        self.tk_button_Move_Down_Button = self.__tk_button_Move_Down_Button( self.tk_frame_Button_Frame) 
        self.tk_button_Start_Task = self.__tk_button_Start_Task( self.tk_frame_Button_Frame) 
        self.tk_button_Add_Task_Button = self.__tk_button_Add_Task_Button( self.tk_frame_Button_Frame) 
        self.tk_button_Move_Up_Button = self.__tk_button_Move_Up_Button( self.tk_frame_Button_Frame) 
        self.tk_label_Tpis_Setting = self.__tk_label_Tpis_Setting( self.tk_label_frame_ADB_Setting_Frame) 
        self.tk_input_StartAPP_wait = self.__tk_input_StartAPP_wait( self.tk_label_frame_ADB_Setting_Frame) 

    def __win(self):
        self.title("MAA-GUI")
        # 设置窗口大小、居中
        width = 800
        height = 460
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
    def __tk_tabs_Main_Tabs(self,parent):
        Style().configure('TNotebook', tabposition='wn')
        frame = Notebook(parent,style='TNotebook')
        self.tk_tabs_Main_Tabs_0 = self.__tk_frame_Main_Tabs_0(frame)
        frame.add(self.tk_tabs_Main_Tabs_0, text="主页")
        self.tk_tabs_Main_Tabs_1 = self.__tk_frame_Main_Tabs_1(frame)
        frame.add(self.tk_tabs_Main_Tabs_1, text="设置")
        frame.place(x=0, y=0, width=800, height=460)
        return frame
    def __tk_frame_Main_Tabs_0(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=800, height=460)
        return frame
    def __tk_frame_Main_Tabs_1(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=800, height=460)
        return frame
    def __tk_label_Stable_loca(self,parent):
        try:  
            with open(os.getcwd()+"\\config.json", "r", encoding='utf-8') as config_file:  
                config_data = json.load(config_file)  
                current_tag_name = config_data["tag_name"]
        except Exception as e:
            print(e)
            current_tag_name = ""  
        label = Label(parent,text="当前版本:"+current_tag_name,anchor="center", )
        label.place(x=65, y=420, width=130, height=30)
        return label
    def __tk_button_Check_Update_Button(self,parent):
        btn = Button(parent, text="检查", takefocus=False,)
        btn.place(x=0, y=420, width=50, height=30)
        return btn
    def __tk_label_Stable_online(self,parent):
        label = Label(parent,text="在线更新",anchor="center", )
        label.place(x=200, y=400, width=130, height=30)
        return label
    def __tk_button_Update_button(self,parent):
        btn = Button(parent, text="更新", takefocus=False,)
        btn.place(x=0, y=360, width=50, height=30)
        return btn
    def __tk_label_frame_ADB_Setting_Frame(self,parent):
        frame = LabelFrame(parent,text="设置",)
        frame.place(x=0, y=0, width=780, height=140)
        return frame
    def __tk_label_ADB_Part_Label(self,parent):
        label = Label(parent,text="ADB地址",anchor="center", )
        label.place(x=0, y=0, width=70, height=30)
        return label
    def __tk_label_ADB_Address_Label(self,parent):
        label = Label(parent,text="ADB端口",anchor="center", )
        label.place(x=0, y=40, width=70, height=30)
        return label
    def __tk_button_Auto_Detect_ADB_Button(self,parent):
        btn = Button(parent, text="自动检测", takefocus=False,)
        btn.place(x=0, y=80, width=70, height=30)
        return btn
    def __tk_input_ADB_Address_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=0, width=150, height=30)
        return ipt
    def __tk_input_ADB_Path_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=40, width=150, height=30)
        return ipt
    def __tk_select_box_Auto_Detect_ADB_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=80, y=80, width=150, height=30)
        return cb
    def __tk_label_Controller_Type_Label(self,parent):
        label = Label(parent,text="控制端",anchor="center", )
        label.place(x=240, y=0, width=70, height=30)
        return label
    def __tk_label_Resource_Type_Label(self,parent):
        label = Label(parent,text="客户端",anchor="center", )
        label.place(x=420, y=0, width=70, height=30)
        return label
    def __tk_select_box_Controller_Type_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=320, y=0, width=80, height=30)
        return cb
    def __tk_select_box_Resource_Type_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=500, y=0, width=80, height=30)
        return cb
    def __tk_label_StartApp(self,parent):
        label = Label(parent,text="启动地址",anchor="center", )
        label.place(x=240, y=40, width=70, height=30)
        return label
    def __tk_input_StartAPP_Address(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=320, y=40, width=130, height=30)
        return ipt
    def __tk_label_StartAPP_P(self,parent):
        label = Label(parent,text="参数",anchor="center", )
        label.place(x=510, y=40, width=50, height=30)
        return label
    def __tk_input_StartAPP_Address_P(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=460, y=40, width=40, height=30)
        return ipt
    def __tk_label_frame_Task_List_Frame(self,parent):
        frame = LabelFrame(parent,text="任务列表",)
        frame.place(x=460, y=10, width=300, height=425)
        return frame
    def __tk_list_box_Task_List(self,parent):
        lb = Listbox(parent)
        for item in Get_Values_list_Option(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json","task"):
            lb.insert(END, item)
        lb.place(x=10, y=10, width=280, height=390)
        return lb
    def __tk_label_frame_Select_Task_Frame(self,parent):
        frame = LabelFrame(parent,text="选择任务",)
        frame.place(x=0, y=10, width=340, height=425)
        return frame
    def __tk_label_Add_Task_Label_1(self,parent):
        label = Label(parent,text="隐藏标签1",anchor="center", )
        label.place(x=0, y=40, width=100, height=30)
        return label
    def __tk_label_Add_Task_Label_3(self,parent):
        label = Label(parent,text="隐藏标签3",anchor="center", )
        label.place(x=0, y=120, width=100, height=30)
        return label
    def __tk_label_Add_Task_Label_2(self,parent):
        label = Label(parent,text="隐藏标签2",anchor="center", )
        label.place(x=0, y=80, width=100, height=30)
        return label
    def __tk_select_box_Add_Task_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=110, y=0, width=200, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_2(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=110, y=80, width=200, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_1(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=110, y=40, width=200, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_3(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=110, y=120, width=200, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_4(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(x=110, y=160, width=200, height=30)
        return cb
    def __tk_label_Add_Task_Label_4(self,parent):
        label = Label(parent,text="隐藏标签4",anchor="center", )
        label.place(x=0, y=160, width=100, height=30)
        return label
    def __tk_label_Add_Task_Label(self,parent):
        label = Label(parent,text="任务",anchor="center", )
        label.place(x=0, y=0, width=100, height=30)
        return label
    def __tk_frame_Button_Frame(self,parent):
        frame = LabelFrame(parent,text="",)
        frame.place(x=350, y=20, width=100, height=230)
        return frame
    def __tk_button_Delete_Button(self,parent):
        btn = Button(parent, text="删除", takefocus=False,)
        btn.place(x=15, y=120, width=70, height=30)
        return btn
    def __tk_button_Move_Down_Button(self,parent):
        btn = Button(parent, text="下移", takefocus=False,)
        btn.place(x=15, y=80, width=70, height=30)
        return btn
    def __tk_button_Start_Task(self,parent):
        btn = Button(parent, text="开始任务", takefocus=False,)
        btn.place(x=15, y=160, width=70, height=30)
        return btn
    def __tk_button_Add_Task_Button(self,parent):
        btn = Button(parent, text="添加任务", takefocus=False,)
        btn.place(x=15, y=0, width=70, height=30)
        return btn
    def __tk_button_Move_Up_Button(self,parent):
        btn = Button(parent, text="上移", takefocus=False,)
        btn.place(x=15, y=40, width=70, height=30)
        return btn
    def __tk_label_Config_Label(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label
    def __tk_input_StartAPP_wait(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=510, y=40, width=65, height=30)
        return ipt
    def __tk_label_Tpis_Setting(self,parent):
        label = Label(parent,text="启动地址-启动参数-启动延迟",anchor="center", )
        label.place(x=240, y=80, width=340, height=30)
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
        self.tk_select_box_Add_Task_Select.bind('<Enter>',self.ctl.Save_ADB_Address)
        self.tk_button_Add_Task_Button.bind('<Button-1>',self.ctl.Add_Task)
        self.tk_button_Move_Up_Button.bind('<Button-1>',self.ctl.Click_Move_Up_Button)
        self.tk_button_Move_Down_Button.bind('<Button-1>',self.ctl.Click_Move_Down_Button)
        self.tk_button_Delete_Button.bind('<Button-1>',self.ctl.Click_Delete_Button)
        self.tk_select_box_Controller_Type_Select.bind('<<ComboboxSelected>>',self.ctl.Save_Controller_Type_Select)
        self.tk_list_box_Task_List.bind('<Delete>',self.ctl.Click_Delete_Button)
        self.tk_button_Update_button.bind('<Button-1>',self.ctl.Update)
        self.tk_button_Check_Update_Button.bind('<Button-1>',self.ctl.Check_Update)
        self.tk_button_Auto_Detect_ADB_Button.bind('<Button-1>',self.ctl.Click_Auto_Detect_ADB)
        self.tk_select_box_Auto_Detect_ADB_Select.bind('<<ComboboxSelected>>',self.ctl.Replace_ADB_data)
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()