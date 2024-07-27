# MAA_Tkinter
一个基于Tkinter的MAAFW-GUI项目
![image](/示例图片/maa主界面A.png)
![image](/示例图片/maa主界面B.png)
# 使用方式
- 下载[最新版本](https://github.com/overflow65537/Tkinter_MAA-GUI/releases) 并解压
- 下载需要启动的maapicli程序
- 将程序放入MAA_bin文件夹
- 完成后MAA_bin文件夹应该和图片一样
- ![image](/示例图片/MAA_bin图片.png)
- 返回MAA-GUI文件夹
- 启动MAA-GUI.exe
- 输入ADB端口和ADB地址并回车保存(无法输入小数点可以复制进去)
- 输入任务
- 开始运行
  
# config.json设置
- ```url```:填写项目的更新地址,填写后才可使用自动更新.例如```{"url":"https://api.github.com/repos/作者名/项目名/releases/latest"}``` ***必填***
- ```tag_name```:填写本地项目的版本号,例如```"tag_name": "v1.8.4"``` 更新后会自动生成
- ```startapp```:填写启动app,使用后会自动生成
- ```startapp_p```填写启动app参数,使用后会自动生成
- ```"startapp_w```填写启动app等待时间,使用后会自动生成
# 视频教程
- https://bilibili.com/video/BV1ZBbJeSEHF
# 任务进度
- [x] ADB路径和端口的编辑和保存
- [x] 客户端类型的初始显示,列表中内容的显示以及编辑和保存
- [x] 任务类型选项卡的初始显示,列表中内容的显示,根据任务需求显示更多选项以及正常选择
- [x] 添加任务,开始任务,上移,下移,删除按钮的正常使用
- [x] 任务列表的动态更新
- [x] 任务列表会根据任务的要求显示更多选项
- [x] 检测到第一次使用时自动创建MAA配置文件
- [x] 添加自动更新
- [x] 添加自动寻找adb设备并自动填写adb信息
- [x] 添加启动模拟器功能
- [ ] 为每个游戏添加独立的配置文件
- [ ] 开始任务后会在GUI界面实时显示maapicli的输出内容(黑框应该也不影响使用)
