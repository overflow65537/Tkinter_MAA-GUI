from ui import Win
import subprocess
import os
from tool import *
import requests
from zipfile import ZipFile 
import shutil
from tkinter import messagebox  
import threading


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
        
        #服务器资源 
        self.ui.tk_select_box_Resource_Type_Select['values'] = (Get_Values_list(os.getcwd()+"\MAA_bin\interface.json","resource"))
        self.ui.tk_select_box_Add_Task_Select['values'] = (Get_Values_list(os.getcwd()+"\MAA_bin\interface.json","task"))
        self.ui.tk_select_box_Controller_Type_Select['values'] = (Get_Values_list(os.getcwd()+"\MAA_bin\interface.json","controller"))
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

        #隐藏下载进度条 进度显示 和版本显示
        self.ui.tk_label_Stable_online.place_forget()
        self.ui.tk_progressbar_ProgressBar.place_forget()
        self.ui.tk_button_Update_button.place_forget()

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
        #打开maa_pi_config.json并写入新的控制端
        Controller_Type_Select = self.ui.tk_select_box_Controller_Type_Select.get()
        MAA_Pi_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")
        MAA_Pi_Config["controller"] = Controller_Type_Select
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
        self.ui.tk_list_box_Task_List.delete(0,100)#为什么END用不了?那我直接选第100位,什么时候真有100个任务了我就写1000位
        for item in Get_Values_list_Option(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)

    
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


    
    def Add_Task_Select_More_Select(self, evt):  
        # 清除所有额外显示的下拉框和标签  
        self.clear_extra_widgets()  
    
        # 获取选中的任务  
        select_target = self.ui.tk_select_box_Add_Task_Select.get()  
    
        # 使用after()方法延迟执行  
        def delayed_update():  
            MAA_Pi_Config = Read_MAA_Config(os.getcwd() + "\MAA_bin\interface.json")  
    
            # 查找是否有选中的任务并包含option  
            for task in MAA_Pi_Config["task"]:  
                if task["name"] == select_target and task.get("option") is not None:  
                    option_length = len(task["option"])  
    
                    # 根据option数量动态显示下拉框和标签  
                    for i in range(option_length):  
                        select_box = getattr(self.ui, f'tk_select_box_Add_Task_Select_{i+1}')  
                        label = getattr(self.ui, f'tk_label_Add_Task_Label_{i+3}')  
                        option_name = task["option"][i]
    
                        # 填充下拉框数据  
                        select_box['values'] = tuple(Get_Task_List(option_name))  
                        select_box.place(x=80, y=200 + (i * 40), width=180, height=30)  
    
                        # 显示标签  
                        label["text"] = option_name  
                        label.place(x=0, y=200 + (i * 40), width=70, height=30)  
    
                        # 更新widget  
                        select_box.update()  
                        label.update()  
    
                    break  # 找到匹配的任务后退出循环  
    
        # 使用after()方法延迟200毫秒执行  
        self.ui.after(100, delayed_update)  
    
    def clear_extra_widgets(self):  
        # 隐藏并清除所有额外的下拉框和标签的选项  
        for i in range(1, 5): 
            select_box = getattr(self.ui, f'tk_select_box_Add_Task_Select_{i}')  
            select_box['values'] = ()  # 清除选项  
            select_box.place_forget()  # 隐藏下拉框  
            
            label = getattr(self.ui, f'tk_label_Add_Task_Label_{i+2}')  
            label.place_forget()  # 隐藏标签
    def Check_Update(self, evt):  
        # 使用threading启动一个新线程来执行检查更新操作  
        threading.Thread(target=self._check_update_thread_function, daemon=True).start()
    
    def _check_update_thread_function(self):
        with open(os.getcwd()+"/config.json","r",encoding='utf-8') as GUI_Config:
            url =  json.load(GUI_Config)["url"]
            
        global Cont
        Cont=requests.get(url).json()
        #显示版本
        self.ui.tk_label_Stable_online.place(x=205, y=420, width=130, height=30)
        self.ui.tk_label_Stable_online["text"] = "最新版本"+Cont["tag_name"]
        self.ui.tk_label_Stable_online.update()

        #显示进度条和更新按钮
        self.ui.tk_button_Update_button.place(x=0, y=385, width=50, height=30)

    def Update(self, evt):  
        # 使用threading启动一个新线程来执行更新操作  
        threading.Thread(target=self._update_thread_function, daemon=True).start()

    def _update_thread_function(self):
        #找出win-x86_64版本的下载地址
        browser_download_url = []
        for i in Cont["assets"]:
            if i["name"] == "MSBA-win-x86_64-"+Cont["tag_name"]+".zip":
                browser_download_url.append(i["browser_download_url"])
        zip_url = browser_download_url[0]
                # 读取config.json中的当前tag_name  
        try:  
            with open(os.getcwd()+"/config.json", "r", encoding='utf-8') as config_file:  
                config_data = json.load(config_file)  
                current_tag_name = config_data.get("tag_name", "")  
        except Exception as e:  
            print(f"Error reading config.json: {e}")  
            current_tag_name = ""  
  
        # 获取最新的tag_name  
        new_tag_name = Cont["tag_name"]
  
        # 比较新旧tag_name，并更新UI和config.json（如果需要）  
        if new_tag_name != current_tag_name:  
            # 更新config.json  
            config_data["tag_name"] = new_tag_name  
            with open(os.getcwd()+"/config.json", "w", encoding='utf-8') as config_file:  
                json.dump(config_data, config_file, indent=4, ensure_ascii=False)  

        # 检查MAA-bin文件夹是否存在，如果不存在则创建它  
        maa_bin_dir = os.path.join(os.getcwd(), 'MAA_bin')  
        if not os.path.exists(maa_bin_dir):  
            os.makedirs(maa_bin_dir)  
    
        # 构建保存ZIP文件的路径  
        zip_file_path = os.path.join(os.getcwd(), 'download.zip')  
    
        # 下载ZIP文件  
        try:  
            with requests.get(zip_url, stream=True) as r:  
                r.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常  
                with open(zip_file_path, 'wb') as f:  
                    shutil.copyfileobj(r.raw, f)  
            
            # 解压ZIP文件到MAA-bin文件夹  
            with ZipFile(zip_file_path, 'r') as zip_ref:  
                zip_ref.extractall(maa_bin_dir)  
    
            #删除ZIP文件
            os.remove(zip_file_path)  
            messagebox.showinfo("成功", "文件已下载并解压到MAA-bin文件夹内！")  
        except requests.exceptions.RequestException as e:  
            messagebox.showerror("下载错误", str(e))  
        except Exception as e:  
            messagebox.showerror("错误", str(e))  
    