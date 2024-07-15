import os
import json

def Read_MAA_Config(path):
    if not os.path.exists(os.getcwd()+"\MAA_bin\config\maa_pi_config.json"):
        os.makedirs(os.getcwd()+"\MAA_bin\config\\")
        date = {"adb": {"adb_path":"请在此处填写ADB路径,回车确定","address":"请在此处填写ADB端口,回车确定","config": {}},"controller": {"name": "安卓端","type": "Adb"},"resource":"官服","task":[]}
        with open(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","w",encoding='utf-8') as MAA_Config:
            json.dump(date,MAA_Config,indent=4,ensure_ascii=False)
    with open(path,"r",encoding='utf-8') as MAA_Config:
        # 打开json并传入MAA_data
        MAA_data = json.load(MAA_Config)
        return MAA_data
    
def Save_MAA_Config(path,date):
        # 打开json并写入data内数据
    with open(path,"w",encoding='utf-8') as MAA_Config:
        json.dump(date,MAA_Config,indent=4,ensure_ascii=False)

def Get_Values_list2(path,key1):
    List = []
    for i in Read_MAA_Config(path)[key1]:
        List.append(i)
    return List

def Get_Values_list(path,key1):
    #获取组件的初始参数
    List = []
    for i in Read_MAA_Config(path)[key1]:
        List.append(i["name"])
    return List
        
def Get_Values_list_Option(path,key1):
    #获取组件的初始参数
    List = []
    for i in Read_MAA_Config(path)[key1]:
        if i["option"]!=[]:
            Option_text = str(i["name"])+" "
            Option_Lens = len(i["option"])
            for t in range(0,Option_Lens,1):
                Option_text+=str(i["option"][t]["value"])+" "
            List.append(Option_text)
        else:
            List.append(i["name"])
    return List

def Get_Task_List(target):
    #输入option名称来输出一个包含所有该option中所有cases的name列表
    #具体逻辑为 interface.json文件/option键/选项名称/cases键/键为空,所以通过len计算长度来选择最后一个/name键
    lists = []
    Task_Config = Read_MAA_Config(os.getcwd()+"\MAA_bin\interface.json")["option"][target]["cases"]
    Lens = len(Task_Config)-1
    for i in range(Lens,-1,-1):
        lists.append(Task_Config[i]["name"])
    return lists