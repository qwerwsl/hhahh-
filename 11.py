# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/7/17

import datetime, os


"""
1. ffmpeg可以用下面的参数来录制Windows 桌面操作的视频。

ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop
-c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "fffffffffffffffff"

其中 fffffffffffffffff 部分 是需要填入 产生的视频文件名。

录制过程中，用户按键盘 q 键，可以退出录制。


2. ffmpeg还可以用来合并视频文件，windows下面的格式如下

ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4

其中concat.txt 是要合并视频的文件列表。格式如下，每行以file 开头 后面是要合并的视频文件名：

file 20170330_110818.mp4
file 20170330_110833.mp4



------------------------------
下载ffmpeg程序 (进入 http://ffmpeg.zeranoe.com/builds/ 点击 Download FFmpeg按钮即可)

要求大家写一个python程序，运行后提示用户是要做什么操作，如下
 '请选择您要做的操作：1：录制视频，2：合并视频：'

 如果用户输入1并回车， 则调用ffmpeg录制视频文件，产生在当前目录下面。
 要求录制的视频文件名 是当前时间（年月日_时分秒.mp4格式），
 比如 '20170330_093612.mp4' （怎么产生这种时间格式的字符串，不知道的请自行网上搜索方法）

 如果用户输入2并回车，则按字母顺序列出当前目录下所有的 mp4为扩展名
 的视频文件(怎么列出，请自行网上搜索方法)，并在前面编上序号。如下所示

 ---------------------------------
    目录中有这些视频文件：
    1 - 20170329_202814.mp4
    2 - 20170330_093251.mp4
    3 - 20170330_093612.mp4

    请选择要合并视频的视频文件序号(格式 1,2,3,4) :
 ---------------------------------

 用户输入视频序号（序号以逗号隔开）后， 程序合并视频文件， 输出的合并后视频文件名 固定为 out.mp4
"""

# 可执行程序的路径
ffmpegPath = """D:\desktop\songqin\python进阶\day2\\ffmpeg-20190219-ff03418-win64-static\\bin"""

# 视频文件的输出路径
out_path = """D:\desktop\songqin\python进阶\day2\\test"""



# 如果用户输入1并回车， 则调用ffmpeg录制视频文件，产生在当前目录下面。
#  要求录制的视频文件名 是当前时间（年月日_时分秒.mp4格式），
#  比如 '20170330_093612.mp4' （怎么产生这种时间格式的字符串，不知道的请自行网上搜索方法）
def recording():
    now_time = datetime.datetime.now()
    video_name = str(now_time.strftime("%Y%m%d_%H%M%S"))+".mp4"


    cmdStr = ffmpegPath+"""\\ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop -c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M %s\%s""" %(out_path, video_name)
    print(cmdStr)
    os.system(cmdStr)

# 2. ffmpeg还可以用来合并视频文件，windows下面的格式如下
#
# ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4
#
# 其中concat.txt 是要合并视频的文件列表。格式如下，每行以file 开头 后面是要合并的视频文件名：
#
# file 20170330_110818.mp4
# file 20170330_110833.mp4
def merging():
    # 切换工作目录到视频文件所在目录
    os.chdir(out_path)


    # 获取目录下的文件列表
    fileSli = os.listdir(out_path)

    # 如果文件列表为空， 则结束运行
    if not fileSli:
        print("文件列表为空")
        return

    # 排序列表
    fileSli.sort()

    # 如果不是 .mp4文件则过滤
    for i in fileSli:
        # 如果不是 .mp4文件则过滤
        if not i.endswith(".mp4"):
            fileSli.remove(i)


    # 列出文件列表
    idx = 0
    for i in fileSli:
        print(idx, i)
        idx += 1


    # 选择需要操作的文件序号
    chooseNum = input("请选择需要合并的视频文件序号（格式： 1,2,3,4）")
    chooseSli = chooseNum.split(",")

    # 操作 concat.txt 文件
    with open("./concat.txt", "w", encoding="utf8") as f:
        for i in chooseSli:

            f.write("file "+fileSli[int(i)]+"\n")

    cmdStr = ffmpegPath+"\\ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4"
    print(cmdStr)
    os.system(cmdStr)


while True:
    chooseOption = input("请选择需要的操作：1、录制视频；2、合并视频")

    if chooseOption == "1":
        recording()
    elif chooseOption == "2":
        merging()
    elif chooseOption == "exit":
        break
    else:
        print("非法输入")
