from tkinter import Button, Frame, Tk
import subprocess
import os
import json


class Application(Frame):
    # GUI程序类
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建开始按钮
        self.btn_start = Button(self, text="Start", command=self.StartMission)
        self.btn_start.pack()
        # 创建添加任务按钮
        self.btn_add = Button(self, text="Add", command=self.AddMission)
        self.btn_add.pack()

    def ReadJson(self):
        # 读取maa_pi_config.json
        with open(GetConfigPath, "r", encoding='utf-8') as MAA_Config:
            # 打开maa_pi_config.json并传入MAA_data
            MAA_data = json.load(MAA_Config)
            return MAA_data

    def AddMission(self):
        # 添加任务

        pass

    def StartMission(self):
        # 开始任务
        subprocess.Popen(GetPath)
        print(GetPath)


GetPath = os.getcwd()+"\MAA_bin\MaaPiCli.exe -d"  # 拼接MaaPicli当前路径
GetConfigPath = os.getcwd()+"\MAA_bin\config\maa_pi_config.json"  # 拼接config路径
Getinterface = os.getcwd()+"\MAA_bin\interface.json"


with open(GetConfigPath, "r", encoding='utf-8') as MAA_Config:
    # 打开maa_pi_config.json并传入MAA_data
    MAA_data = json.load(MAA_Config)


root = Tk()
root.title("MAA-GUI MSBA")
root.geometry("800x600+1000+500")
app = Application(master=root)

root.mainloop()
