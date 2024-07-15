from ui import Win
import subprocess
import os
from tool import *


#获取初始resource序号
Add_Resource_Type_Select_Values = []
for i in Read_MAA_Config(os.getcwd()+"\MAA_bin\interface.json")["resource"]:
    Add_Resource_Type_Select_Values.append(i["name"])
Resource_Type = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")["resource"]

Resource_count = 0
for i in Add_Resource_Type_Select_Values:
    if i == Resource_Type:
        break
    else:
        Resource_count+=1

#获取初始Controller序号
Add_Controller_Type_Select_Values = []
for i in Read_MAA_Config(os.getcwd()+"\MAA_bin\interface.json")["controller"]:
    Add_Controller_Type_Select_Values.append(i["name"])
Controller_Type = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")["controller"]["name"]

Controller_count = 0
for i in Add_Controller_Type_Select_Values:
    if i == Controller_Type:
        break
    else:
        Controller_count+=1


#初始显示
init_ADB_Path = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")["adb"]["adb_path"]
init_ADB_Address = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")["adb"]["address"]
init_Resource_Type = Resource_count
init_Controller_Type = Controller_count

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):
        pass

    def init(self,ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
        
        #ADB地址和端口输入框
        self.ui.tk_input_ADB_Address_Input.insert(0,init_ADB_Address)
        self.ui.tk_input_ADB_Path_Input.insert(0,init_ADB_Path)
        #服务器和任务下拉框和控制端下拉框
        self.ui.tk_select_box_Controller_Type_Select.current(init_Controller_Type)
        self.ui.tk_select_box_Resource_Type_Select.current(init_Resource_Type)
        self.ui.tk_select_box_Add_Task_Select.current(0)

        #隐藏4个给option准备的下拉框
        self.ui.tk_select_box_Add_Task_Select_1.place_forget()
        self.ui.tk_select_box_Add_Task_Select_2.place_forget()
        self.ui.tk_select_box_Add_Task_Select_3.place_forget()
        self.ui.tk_select_box_Add_Task_Select_4.place_forget()
        self.ui.tk_label_Add_Task_Label_3.place_forget()
        self.ui.tk_label_Add_Task_Label_4.place_forget()
        self.ui.tk_label_Add_Task_Label_5.place_forget()
        self.ui.tk_label_Add_Task_Label_6.place_forget()

    def Start_Task(self,evt):
        #使用-d参数打开MaaPiCli.exe
        subprocess.Popen(os.getcwd()+"\MAA_bin\MaaPiCli.exe -d")

    def Save_ADB_Path(self,evt):
        #打开maa_pi_config.json并写入新的ADB路径
        ADB_Path = self.ui.tk_input_ADB_Path_Input.get().replace("\\","/")
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        MAA_Pi_Config["adb"]["adb_path"] = ADB_Path
        Save_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)

    def Save_ADB_Address(self,evt):
        #打开maa_pi_config.json并写入新的ADB端口
        ADB_Address = self.ui.tk_input_ADB_Address_Input.get()
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        MAA_Pi_Config["adb"]["address"] = ADB_Address
        Save_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)

    def Save_Resource_Type_Select(self,evt):
        #打开maa_pi_config.json并写入新的资源
        Resource_Type_Select = self.ui.tk_select_box_Resource_Type_Select.get()
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        MAA_Pi_Config["resource"] = Resource_Type_Select
        Save_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)

    def Save_Controller_Type_Select(self,evt):
        #打开maa_pi_config.json并写入新的资源
        Resource_Type_Select = self.ui.tk_select_box_Resource_Type_Select.get()
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        MAA_Pi_Config["controller"] = Resource_Type_Select
        Save_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)

    def Add_Task(self,evt):
        #添加任务至GUI列表并保存配置文件
        task = self.ui.tk_select_box_Add_Task_Select.get()

        Option = []
        Select_Target = self.ui.tk_select_box_Add_Task_Select.get()
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\interface.json")
        #Option_list存放所有带有option的键值
        Option_list = []
        for i in MAA_Pi_Config["task"]:
            #将所有带有option的键值存进Option_list
            if i.get("option")!= None:
                Option_list.append(i)
        for i in Option_list:
            #检查当前选中任务的是否为Option_list中的元素
            if Select_Target == i["name"]:
                #是的话通过检查interface.json中该任务任务中option列表的长度
                l = len(i["option"])
                if l == 1:
                    Option.append({"name":i["option"][0],"value":self.ui.tk_select_box_Add_Task_Select_1.get()})
                elif l == 2:
                    Option.append({"name":i["option"][0],"value":self.ui.tk_select_box_Add_Task_Select_1.get()})
                    Option.append({"name":i["option"][1],"value":self.ui.tk_select_box_Add_Task_Select_2.get()})
                elif l == 3:
                    Option.append({"name":i["option"][0],"value":self.ui.tk_select_box_Add_Task_Select_1.get()})
                    Option.append({"name":i["option"][1],"value":self.ui.tk_select_box_Add_Task_Select_2.get()})
                    Option.append({"name":i["option"][2],"value":self.ui.tk_select_box_Add_Task_Select_3.get()})
                elif l == 4:
                    Option.append({"name":i["option"][0],"value":self.ui.tk_select_box_Add_Task_Select_1.get()})
                    Option.append({"name":i["option"][1],"value":self.ui.tk_select_box_Add_Task_Select_2.get()})
                    Option.append({"name":i["option"][2],"value":self.ui.tk_select_box_Add_Task_Select_3.get()})
                    Option.append({"name":i["option"][3],"value":self.ui.tk_select_box_Add_Task_Select_4.get()})
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        MAA_Pi_Config["task"].append({"name": task,"option": Option})
        Save_MAA_Config(os.getcwd()+"/\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)
        #刷新GUI任务列表
        self.ui.tk_list_box_Task_List.delete(0,100)
        for item in Get_Values_list_Option(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)
        self.ui.tk_list_box_Task_List.update()
    
    def Click_Move_Up_Button(self,evt):
        #上移任务
        Select_Target = self.ui.tk_list_box_Task_List.curselection()[0]
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        Select_Task = MAA_Pi_Config["task"].pop(Select_Target)
        MAA_Pi_Config["task"].insert(Select_Target-1, Select_Task)
        Save_MAA_Config(os.getcwd()+"/\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)
        #刷新GUI任务列表
        self.ui.tk_list_box_Task_List.delete(0,100)
        for item in Get_Values_list_Option(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)
        self.ui.tk_list_box_Task_List.selection_set(Select_Target-1)
        self.ui.tk_list_box_Task_List.update()

    def Click_Move_Down_Button(self,evt):
        #下移任务
        Select_Target = self.ui.tk_list_box_Task_List.curselection()[0]
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        Select_Task = MAA_Pi_Config["task"].pop(Select_Target)
        MAA_Pi_Config["task"].insert(Select_Target+1, Select_Task)
        Save_MAA_Config(os.getcwd()+"/\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)
        #刷新GUI任务列表
        self.ui.tk_list_box_Task_List.delete(0,100)
        for item in Get_Values_list_Option(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)
        self.ui.tk_list_box_Task_List.selection_set(Select_Target+1)
        self.ui.tk_list_box_Task_List.update()

    def Click_Delete_Button(self,evt):
        #删除选定任务
        Select_Target = self.ui.tk_list_box_Task_List.curselection()[0]
        self.ui.tk_list_box_Task_List.delete(Select_Target)
        Task_List = Get_Values_list2(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task")
        del Task_List[Select_Target]
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        del MAA_Pi_Config["task"]
        MAA_Pi_Config.update({"task":Task_List})
        Save_MAA_Config(os.getcwd()+"/\MAA_bin\config\maa_pi_config.json",MAA_Pi_Config)
        self.ui.tk_list_box_Task_List.selection_set(Select_Target-1)
        self.ui.tk_list_box_Task_List.update()

    
    def Add_Task_Select_More_Select(self,evt):
        #不用了之后隐藏控件
        self.ui.tk_select_box_Add_Task_Select_1.place_forget()
        self.ui.tk_select_box_Add_Task_Select_2.place_forget()
        self.ui.tk_select_box_Add_Task_Select_3.place_forget()
        self.ui.tk_select_box_Add_Task_Select_4.place_forget()
        self.ui.tk_label_Add_Task_Label_3.place_forget()
        self.ui.tk_label_Add_Task_Label_4.place_forget()
        self.ui.tk_label_Add_Task_Label_5.place_forget()
        self.ui.tk_label_Add_Task_Label_6.place_forget()
        Select_Target = self.ui.tk_select_box_Add_Task_Select.get()
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\interface.json")
        #Option_list存放所有带有option的键值
        Option_list = []
        for i in MAA_Pi_Config["task"]:
            #将所有带有option的键值存进Option_list
            if i.get("option")!= None:
                Option_list.append(i)
        for i in Option_list:
            #检查当前选中任务的是否为Option_list中的元素
            if Select_Target == i["name"]:
                #是的话通过检查interface.json中该任务任务中option列表的长度
                l = len(i["option"])
                
                #根据list长度选择改显示几个任务option选项
                if l == 1:
                    #i["option"][0]为通过interface中task键下的option第0号键值,因为if判断这个option只有一个选项,所以不担心有别的内容不显示
                    #任务数多于4个的话在ui.py添加控件,然后在此文件上方init隐藏,在通过这里来重新调用
                    self.ui.tk_select_box_Add_Task_Select_1['values'] = tuple(Get_Task_List(i["option"][0]))
                    self.ui.tk_select_box_Add_Task_Select_1.place(x=80, y=200, width=260, height=30)
                    self.ui.tk_label_Add_Task_Label_3["text"] = i["option"][0]
                    self.ui.tk_label_Add_Task_Label_3.place(x=0, y=200, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_3.update()
                    self.ui.tk_select_box_Add_Task_Select_1.update() 
                elif l == 2:
                    self.ui.tk_select_box_Add_Task_Select_1['values'] = tuple(Get_Task_List(i["option"][0]))
                    self.ui.tk_select_box_Add_Task_Select_2['values'] = tuple(Get_Task_List(i["option"][1]))
                    self.ui.tk_select_box_Add_Task_Select_1.place(x=80, y=200, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_2.place(x=80, y=240, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_1.update()
                    self.ui.tk_select_box_Add_Task_Select_2.update()
                    self.ui.tk_label_Add_Task_Label_3["text"] = i["option"][0]
                    self.ui.tk_label_Add_Task_Label_4["text"] = i["option"][1]
                    self.ui.tk_label_Add_Task_Label_3.place(x=0, y=200, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_4.place(x=0, y=240, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_3.update()
                    self.ui.tk_label_Add_Task_Label_4.update()
                elif l == 3:
                    self.ui.tk_select_box_Add_Task_Select_1['values'] = tuple(Get_Task_List(i["option"][0]))
                    self.ui.tk_select_box_Add_Task_Select_2['values'] = tuple(Get_Task_List(i["option"][1]))
                    self.ui.tk_select_box_Add_Task_Select_3['values'] = tuple(Get_Task_List(i["option"][2]))
                    self.ui.tk_select_box_Add_Task_Select_1.place(x=80, y=200, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_2.place(x=80, y=240, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_3.place(x=80, y=280, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_1.update()
                    self.ui.tk_select_box_Add_Task_Select_2.update()
                    self.ui.tk_select_box_Add_Task_Select_3.update()
                    self.ui.tk_label_Add_Task_Label_3["text"] = i["option"][0]
                    self.ui.tk_label_Add_Task_Label_4["text"] = i["option"][1]
                    self.ui.tk_label_Add_Task_Label_5["text"] = i["option"][2]
                    self.ui.tk_label_Add_Task_Label_3.place(x=0, y=200, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_4.place(x=0, y=240, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_5.place(x=0, y=280, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_3.update()
                    self.ui.tk_label_Add_Task_Label_4.update()
                    self.ui.tk_label_Add_Task_Label_5.update()
                elif l == 4:
                    self.ui.tk_select_box_Add_Task_Select_1['values'] = tuple(Get_Task_List(i["option"][0]))
                    self.ui.tk_select_box_Add_Task_Select_2['values'] = tuple(Get_Task_List(i["option"][1]))
                    self.ui.tk_select_box_Add_Task_Select_3['values'] = tuple(Get_Task_List(i["option"][2]))
                    self.ui.tk_select_box_Add_Task_Select_4['values'] = tuple(Get_Task_List(i["option"][3]))
                    self.ui.tk_select_box_Add_Task_Select_1.place(x=80, y=200, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_2.place(x=80, y=240, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_3.place(x=80, y=280, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_4.place(x=80, y=320, width=260, height=30)
                    self.ui.tk_select_box_Add_Task_Select_1.update()
                    self.ui.tk_select_box_Add_Task_Select_2.update()
                    self.ui.tk_select_box_Add_Task_Select_3.update()
                    self.ui.tk_select_box_Add_Task_Select_4.update()
                    self.ui.tk_label_Add_Task_Label_3["text"] = i["option"][0]
                    self.ui.tk_label_Add_Task_Label_4["text"] = i["option"][1]
                    self.ui.tk_label_Add_Task_Label_5["text"] = i["option"][2]
                    self.ui.tk_label_Add_Task_Label_6["text"] = i["option"][3]
                    self.ui.tk_label_Add_Task_Label_3.place(x=0, y=200, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_4.place(x=0, y=240, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_5.place(x=0, y=280, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_6.place(x=0, y=320, width=70, height=30)
                    self.ui.tk_label_Add_Task_Label_3.update()
                    self.ui.tk_label_Add_Task_Label_4.update()
                    self.ui.tk_label_Add_Task_Label_5.update()
                    self.ui.tk_label_Add_Task_Label_6.update()
