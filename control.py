from ui import Win
import subprocess
import os
from tool import *
import requests
from zipfile import ZipFile 
import shutil
from tkinter import messagebox  
import threading
import time

#获取初始resource序号
Add_Resource_Type_Select_Values = []
for i in Read_Config(os.getcwd()+"\\MAA_bin\\interface.json")["resource"]:
    Add_Resource_Type_Select_Values.append(i["name"])
Resource_Type = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")["resource"]

Resource_count = 0
for i in Add_Resource_Type_Select_Values:
    if i == Resource_Type:
        break
    else:
        Resource_count+=1

#获取初始Controller序号
Add_Controller_Type_Select_Values = []
for i in Read_Config(os.getcwd()+"\\MAA_bin\\interface.json")["controller"]:
    Add_Controller_Type_Select_Values.append(i["name"])
Controller_Type = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")["controller"] ["name"]

Controller_count = 0
for i in Add_Controller_Type_Select_Values:
    if i == Controller_Type:
        break
    else:
        Controller_count+=1


#初始显示
init_ADB_Path = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")["adb"]["adb_path"]
init_ADB_Address = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")["adb"]["address"]
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
        with open(os.getcwd()+"\\config.json","r",encoding='utf-8') as f :
            config_data = json.load(f)
        if "startapp" not in config_data:  
            config_data["startapp"] = ""  
        if "startapp_p" not in config_data:  
            config_data["startapp_p"] = ""  
        if "startapp_w" not in config_data:  
            config_data["startapp_w"] = "10" 
        
        with open(os.getcwd()+"\\config.json","w",encoding="utf-8") as f:  
            json.dump(config_data, f, indent=4)  
        
        #打开config文件查找StartApp参数,如果没有创建一个新的
        self.ui.tk_input_StartAPP_Address.insert(0,config_data["startapp"])
        self.ui.tk_input_StartAPP_Address_P.insert(0,config_data["startapp_p"])
        self.ui.tk_input_StartAPP_wait.insert(0,config_data["startapp_w"])
        #服务器资源 
        self.ui.tk_select_box_Resource_Type_Select["values"] = (Get_Values_list(os.getcwd()+"\\MAA_bin\\interface.json","resource"))
        self.ui.tk_select_box_Add_Task_Select["values"] = (Get_Values_list(os.getcwd()+"\\MAA_bin\\interface.json","task"))
        self.ui.tk_select_box_Controller_Type_Select["values"] = (Get_Values_list(os.getcwd()+"\\MAA_bin\\interface.json","controller"))
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
        self.ui.tk_label_Add_Task_Label_1.place_forget()
        self.ui.tk_label_Add_Task_Label_2.place_forget()
        self.ui.tk_label_Add_Task_Label_3.place_forget()
        self.ui.tk_label_Add_Task_Label_4.place_forget()

        #隐藏下载进度条 进度显示 和版本显示
        self.ui.tk_label_Stable_online.place_forget()
        self.ui.tk_button_Update_button.place_forget()
    def Start_Task(self,evt):
        # 使用threading启动一个新线程来执行更新操作  
        threading.Thread(target=self._Start_TaskB_thread_function, daemon=True).start()
    def _Start_TaskB_thread_function(self):
        #保存
        self.Save_ADB_Address(self)
        self.Save_ADB_Path(self)

        if self.ui.tk_input_StartAPP_Address.get() != "":
            APP_Path = self.ui.tk_input_StartAPP_Address.get()
            APP_P = self.ui.tk_input_StartAPP_Address_P.get()
            APP_wait = self.ui.tk_input_StartAPP_wait.get()
            subprocess.Popen(str(APP_Path)+str(APP_P))

            seconds = int(APP_wait)
            while seconds > 0:  
                print(f"剩余时间: {seconds}秒")  
                time.sleep(1)  # 等待1秒  
                seconds -= 1  
        #使用-d参数打开MaaPiCli.exe
        subprocess.Popen(os.getcwd()+"\\MAA_bin\\MaaPiCli.exe -d")

    def Save_APP_Setting(self,evt):
        with open(os.getcwd()+"\\config.json","r",encoding='utf-8') as f :
            config_data = json.load(f)
        config_data["startapp"] = self.ui.tk_input_StartAPP_Address.get()
        config_data["startapp_p"] = self.ui.tk_input_StartAPP_Address_P.get()
        config_data["startapp_w"] = self.ui.tk_input_StartAPP_wait.get()
        with open(os.getcwd()+"\\config.json","w",encoding="utf-8") as Config:
            json.dump(config_data,Config,indent=4,ensure_ascii=False)
    def Save_ADB_Path(self,evt):
        #打开maa_pi_config.json并写入新的ADB路径
        ADB_Path = self.ui.tk_input_ADB_Path_Input.get().replace("\\","/")
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        MAA_Pi_Config["adb"]["adb_path"] = ADB_Path
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)

    def Save_ADB_Address(self,evt):
        #打开maa_pi_config.json并写入新的ADB端口
        ADB_Address = self.ui.tk_input_ADB_Address_Input.get()
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        MAA_Pi_Config["adb"]["address"] = ADB_Address
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)

    def Save_Resource_Type_Select(self,evt):
        #打开maa_pi_config.json并写入新的资源
        Resource_Type_Select = self.ui.tk_select_box_Resource_Type_Select.get()
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        MAA_Pi_Config["resource"] = Resource_Type_Select
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)

    def Save_Controller_Type_Select(self,evt):
        #打开maa_pi_config.json并写入新的控制端
        Controller_Type_Select = self.ui.tk_select_box_Controller_Type_Select.get()
        interface_Controller = Read_Config(os.getcwd()+"\\MAA_bin\\interface.json")["controller"]
        
        for i in interface_Controller:
            if i["name"] == Controller_Type_Select:
                Controller_target = i
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        MAA_Pi_Config["controller"] = Controller_target
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)

    def Add_Task(self,evt):
        #添加任务至GUI列表并保存配置文件
        task = self.ui.tk_select_box_Add_Task_Select.get()

        Option = []
        Select_Target = self.ui.tk_select_box_Add_Task_Select.get()
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\interface.json")
        #Option_list存放所有带有option的键值
        Option_list = []
        for i in MAA_Pi_Config["task"]:
            #将所有带有option的键值存进Option_list
            if i.get("option")!= None:
                Option_list.append(i)
        for i in Option_list:
            #检查当前选中任务的是否为option_list中的元素
            if Select_Target == i["name"]:  
                l = len(i["option"])  
                options_dicts = []  
                # 根据option的长度，循环添加选项到列表中  
                for index in range(l):  
                    select_box_name = f"tk_select_box_Add_Task_Select_{index + 1}"  
                    selected_value = getattr(self.ui, select_box_name).get()  
                    options_dicts.append({"name": i["option"][index], "value": selected_value})  
                Option.extend(options_dicts)
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        MAA_Pi_Config["task"].append({"name": task,"option": Option})
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)
        #刷新GUI任务列表
        self.ui.tk_list_box_Task_List.delete(0,100)#为什么END用不了?那我直接选第100位,什么时候真有100个任务了我就写1000位
        for item in Get_Values_list_Option(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)

    
    def Click_Move_Up_Button(self,evt):
        #上移任务
        Select_Target = self.ui.tk_list_box_Task_List.curselection()[0]
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        Select_Task = MAA_Pi_Config["task"].pop(Select_Target)
        MAA_Pi_Config["task"].insert(Select_Target-1, Select_Task)
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)
        #刷新GUI任务列表
        self.ui.tk_list_box_Task_List.delete(0,100)
        for item in Get_Values_list_Option(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)
        self.ui.tk_list_box_Task_List.selection_set(Select_Target-1)


    def Click_Move_Down_Button(self,evt):
        #下移任务
        Select_Target = self.ui.tk_list_box_Task_List.curselection()[0]
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        Select_Task = MAA_Pi_Config["task"].pop(Select_Target)
        MAA_Pi_Config["task"].insert(Select_Target+1, Select_Task)
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)
        #刷新GUI任务列表
        self.ui.tk_list_box_Task_List.delete(0,100)
        for item in Get_Values_list_Option(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json","task"):
            self.ui.tk_list_box_Task_List.insert(100, item)
        self.ui.tk_list_box_Task_List.selection_set(Select_Target+1)


    def Click_Delete_Button(self,evt):
        #删除选定任务
        Select_Target = self.ui.tk_list_box_Task_List.curselection()[0]
        self.ui.tk_list_box_Task_List.delete(Select_Target)
        Task_List = Get_Values_list2(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json","task")
        del Task_List[Select_Target]
        MAA_Pi_Config = Read_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json")
        del MAA_Pi_Config["task"]
        MAA_Pi_Config.update({"task":Task_List})
        Save_Config(os.getcwd()+"\\MAA_bin\\config\\maa_pi_config.json",MAA_Pi_Config)
        self.ui.tk_list_box_Task_List.selection_set(Select_Target-1)


    
    def Add_Task_Select_More_Select(self, evt):  
        # 清除所有额外显示的下拉框和标签  
        self.clear_extra_widgets()  
    
        # 获取选中的任务  
        select_target = self.ui.tk_select_box_Add_Task_Select.get()  
    
        # 使用after()方法延迟执行  
        def delayed_update():  
            MAA_Pi_Config = Read_Config(os.getcwd() + "\\MAA_bin\\interface.json")  
    
            # 查找是否有选中的任务并包含option  
            for task in MAA_Pi_Config["task"]:  
                if task["name"] == select_target and task.get("option") is not None:  
                    option_length = len(task["option"])  
    
                    # 根据option数量动态显示下拉框和标签  
                    for i in range(option_length):  
                        select_box = getattr(self.ui, f"tk_select_box_Add_Task_Select_{i+1}")  
                        label = getattr(self.ui, f"tk_label_Add_Task_Label_{i+1}")  
                        option_name = task["option"][i]
    
                        # 填充下拉框数据  
                        select_box["values"] = tuple(Get_Task_List(option_name))  
                        select_box.place(x=110, y=40 + (i * 40), width=200, height=30)  
    
                        # 显示标签  
                        label["text"] = option_name  
                        label.place(x=0, y=40 + (i * 40), width=100, height=30)  
    
                        # 刷新GUI
                        select_box.update()  
                        label.update()  
    
                    break  # 找到匹配的任务后退出循环  
    
        self.ui.after(100, delayed_update)  
    
    def clear_extra_widgets(self):  
        # 隐藏并清除所有额外的下拉框和标签的选项  
        for i in range(1, 5): 
            select_box = getattr(self.ui, f"tk_select_box_Add_Task_Select_{i}")  
            select_box.set("")  # 清除选项
            select_box.place_forget()  # 隐藏下拉框  
            
            label = getattr(self.ui, f"tk_label_Add_Task_Label_{i}")  
            label.place_forget()  # 隐藏标签
    def Check_Update(self, evt):  
        # 使用threading启动一个新线程来执行检查更新操作  
        threading.Thread(target=self._check_update_thread_function, daemon=True).start()
    
    def _check_update_thread_function(self):
        with open(os.getcwd()+"\\config.json","r",encoding="utf-8") as GUI_Config:
            url =  json.load(GUI_Config)["url"]
            
        global Cont
        Cont=requests.get(url).json()
        #显示版本
        self.ui.tk_label_Stable_online.place(x=200, y=420, width=130, height=30)
        self.ui.tk_label_Stable_online["text"] = "最新版本"+Cont["tag_name"]
        self.ui.tk_label_Stable_online.update()

        #显示进度条和更新按钮
        self.ui.tk_button_Update_button.place(x=0, y=380, width=50, height=30)

    def Update(self, evt):  
        # 使用threading启动一个新线程来执行更新操作  
        threading.Thread(target=self._update_thread_function, daemon=True).start()

    def _update_thread_function(self):
        #找出win-x86_64版本的下载地址
        browser_download_url = []
        for i in Cont["assets"]:
            if "win-x86_64" in i["name"]:
                browser_download_url.append(i["browser_download_url"])
        zip_url = browser_download_url[0]
                # 读取config.json中的当前tag_name  
        try:  
            with open(os.getcwd()+"\\config.json", "r", encoding="utf-8") as config_file:  
                config_data = json.load(config_file)  
                current_tag_name = config_data.get("tag_name", "")  
        except Exception as e:  
            messagebox.showinfo(f"Error reading config.json: {e}")  
            current_tag_name = ""  
  
        # 获取最新的tag_name  
        new_tag_name = Cont["tag_name"]
  
        # 比较新旧tag_name，并更新UI和config.json（如果需要）  
        if new_tag_name != current_tag_name:  
            # 更新config.json  
            config_data["tag_name"] = new_tag_name  
            with open(os.getcwd()+"\\config.json", "w", encoding="utf-8") as config_file:  
                json.dump(config_data, config_file, indent=4, ensure_ascii=False)  

        # 检查MAA-bin文件夹是否存在，如果不存在则创建它  
        maa_bin_dir = os.path.join(os.getcwd(), "MAA_bin")  
        if not os.path.exists(maa_bin_dir):  
            os.makedirs(maa_bin_dir)  
    
        # 构建保存ZIP文件的路径  
        zip_file_path = os.path.join(os.getcwd(), "download.zip")  
    
        # 下载ZIP文件  
        try:  
            print("开始下载")
            with requests.get(zip_url, stream=True) as r:  
                r.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常  
                with open(zip_file_path, "wb") as f:  
                    shutil.copyfileobj(r.raw, f)  
            
            # 解压ZIP文件到MAA-bin文件夹  
            with ZipFile(zip_file_path, "r") as zip_ref:  
                zip_ref.extractall(maa_bin_dir)  
    
            #删除ZIP文件
            os.remove(zip_file_path)  
            messagebox.showinfo("成功", "文件已下载并解压到MAA-bin文件夹内！")  
        except requests.exceptions.RequestException as e:  
            messagebox.showerror("下载错误", str(e))  
        except Exception as e:  
            messagebox.showerror("错误", str(e))  
    def Click_Auto_Detect_ADB(self,evt):
        # 使用threading启动一个新线程来执行更新操作  
        threading.Thread(target=self._Click_Auto_Detect_ADB_thread_function, daemon=True).start()
    def _Click_Auto_Detect_ADB_thread_function(self):
        emulator = [
            {
                "name":"BlueStacks",
                "exe_name":"HD-Player.exe",
                "may_path":["HD-Adb.exe","Engine\\ProgramFiles\\HD-Adb.exe"],
                "port":["127.0.0.1:5555","127.0.0.1:5556","127.0.0.1:5565","127.0.0.1:5575"]
            },
            {
                "name":"MuMuPlayer12",
                "exe_name":"MuMuPlayer.exe",
                "may_path":["vmonitor\\bin\\adb_server.exe","MuMu\\emulator\\nemu\\vmonitor\\bin\\adb_server.exe","adb.exe"],
                "port":["127.0.0.1:16384", "127.0.0.1:16416", "127.0.0.1:16448"]
            },
            {
                "name":"LDPlayer",
                "exe_name":"dnplayer.exe",
                "may_path":["adb.exe"],
                "port":["127.0.0.1:5555","127.0.0.1:5556"]
            },
            {
                "name":"Nox",
                "exe_name":"Nox.exe",
                "may_path":["nox_adb.exe"],
                "port":["127.0.0.1:62001", "127.0.0.1:59865"]
            },
            {
                "name":"MuMuPlayer6",
                "exe_name":"NemuPlayer.exe",
                "may_path":["vmonitor\\bin\\adb_server.exe","MuMu\\emulator\\nemu\\vmonitor\\bin\\adb_server.exe","adb.exe"],
                "port":["127.0.0.1:7555"]
            },
            {
                "name":"MEmuPlayer.exe",
                "exe_name":"MEmu",
                "may_path":["adb.exe"],
                "port":["127.0.0.1:21503"]
            },
            {
                "name":"ADV",
                "exe_name":"qemu-system.exe",
                "may_path":["..\\..\\..\\platform-tools\\adb.exe"],
                "port":["127.0.0.1:5555"]
            }
]       
        
        global emulator_result
        emulator_result = []
        print("开始查找")
        for app in emulator:
            process_path = find_process_by_name(app["exe_name"])
            
            if process_path:
                #判断程序是否正在运行,是进行下一步,否则放弃
                info_dict = {"exe_path":process_path,"may_path":app["may_path"]}
                ADB_path = find_existing_file(info_dict)
                if ADB_path:
                    
                    #判断ADB地址是否存在,是进行下一步,否则放弃
                    port_data = check_port(app["port"])
                    if port_data:
                        #判断端口是否存在,是则组合字典,否则放弃
                        emulator_result.extend([{"name":app["name"],"path":ADB_path,"port": item} for item in port_data])
        
        if emulator_result:
            processed_list = [] 
            messagebox.showinfo("提示","查找完成")
            for i in emulator_result:
                processed_s = f"{i["name"]}"
                processed_list.append(processed_s)
            self.ui.tk_select_box_Auto_Detect_ADB_Select["values"] = processed_list
            self.ui.tk_select_box_Auto_Detect_ADB_Select.update()
        else:
            messagebox.showerror("错误","未找到模拟器")
    def Replace_ADB_data(self,evt):
        print(emulator_result[self.ui.tk_select_box_Auto_Detect_ADB_Select.current()]["port"])
        print(emulator_result[self.ui.tk_select_box_Auto_Detect_ADB_Select.current()]["path"])
        self.ui.tk_input_ADB_Address_Input.delete(0,100)
        self.ui.tk_input_ADB_Path_Input.delete(0,100)
        self.ui.tk_input_ADB_Address_Input.insert(0,emulator_result[self.ui.tk_select_box_Auto_Detect_ADB_Select.current()]["port"])
        self.ui.tk_input_ADB_Path_Input.insert(0,emulator_result[self.ui.tk_select_box_Auto_Detect_ADB_Select.current()]["path"])
        self.Save_ADB_Address(self)
        self.Save_ADB_Path(self)