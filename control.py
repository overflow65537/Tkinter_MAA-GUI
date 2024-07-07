from ui import Win
import subprocess
import os
import json

def Read_MAA_Config(path):
    with open(path,"r",encoding='utf-8') as MAA_Config:
        # 打开json并传入MAA_data
        MAA_data = json.load(MAA_Config)
        return MAA_data
def Save_MAA_Config(path,data):
        # 打开json并写入data内数据
    with open(path,"w",encoding='utf-8') as MAA_Config:
        json.dump(data,MAA_Config,indent=4,ensure_ascii=False)

#下面两个是ADB端口和ADB地址的初始显示
init_ADB_Path = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")["adb"]["adb_path"]
init_ADB_Address = Read_MAA_Config(os.getcwd()+"\MAA_bin\config\maa_pi_config.json")["adb"]["address"]

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
        self.ui.tk_input_ADB_Address_Input.insert(0,init_ADB_Address)
        self.ui.tk_input_ADB_Path_Input.insert(0,init_ADB_Path)


    def Start_Task(self,evt):
        #使用-d参数打开MaaPiCli.exe
        subprocess.Popen(os.getcwd()+"\MAA_bin\MaaPiCli.exe -d")

    def Save_ADB_Path(self,evt):
        #打开maa_pi_config.json并写入新的ADB路径
        ADB_Path = self.ui.tk_input_ADB_Path_Input.get()
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

    def Add_Task(self,evt):
        #添加任务按钮
        pass
