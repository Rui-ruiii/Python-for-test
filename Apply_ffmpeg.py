"""基于ffmpeg的多功能应用"""
import time
import sys
import os
import subprocess
import re

ffmpeg_path= input("Please enter the path of ffmpeg.exe :")

def Exit():
    """退出应用"""
    print("即将退出")
    time.sleep(3)
    sys.exit(0)

def Finish():
    """考虑除去这一部分"""
    print("Over close the app")
    time.sleep(2)
    sys.exit(0)

def DisPlay():
    """显示页面"""
    """考虑加入是否需要打印结果的选项（先打印，如不需要再删除）"""
    os.chdir("D:")
    if not os.path.exists("D:\\Ffmpeg_Process_Result"):
        os.mkdir("D:\\Ffmpeg_Process_Result")
    print("*" * 20,"Welcome","*" * 20)
    print("Please choose the number of the server you need:")
    print("[*]1.Single File")
    print("[*]2.Multiple Files")
    print("[*]3.exit")
    print("*" * 49)
    try:
        CountOfFile = int(input("Enter the number here:"))
        if CountOfFile == 1:
            SingleFile()
        if CountOfFile == 2:
            MultipleFile()
        if CountOfFile == 3:
            Exit()
        else:
            print("\n")
            print("[*]  请输入列表中的数字")
            print("\n")
            DisPlay()
    except ValueError as VE:
        print("出现（传入无效参数）异常，描述为：")
        print(VE)


def SingleFile():
    """处理单个文件"""
    print("*" * 19,"Operation","*" * 19)
    print("Please select the specific operation to be performed")
    print("[*]1.Get Video/Audio Info")
    print("[*]2.Extract Audio")
    print("[*]3.Extract Video")
    print("[*]4.Clip Length")
    print("[*]5.Conversion Encoding Format")
    print("[*]6.Conversion Package Format")
    print("[*]7.Back to last Operation")
    print("[*]8.Exit")
    print("*" * 49)

    try:
        Operation = int(input("Enter the number here:"))
        if Operation == 1:
            GetInfo()
        if Operation == 2:
            Extract_Audio()
        if Operation == 3:
            Extract_Video()
        if Operation == 4:
            Clip_Length()
        if Operation == 5:
            Conversion_Encoding_Format()
        if Operation == 6:
            Conversion_Package_Format()
        if Operation == 7:
            DisPlay()
        if Operation == 8:
            Exit()
        else:
            print("\n")
            print("[*]  请输入列表中的数字")
            print("\n")
            SingleFile()
    except ValueError as VE:
        print("出现（传入无效参数）异常，描述为：")
        print(VE)


def MultipleFile():
    """处理多个文件"""
    os.chdir(ffmpeg_path)
    print("多个文件")

def GetInfo():
    """获取音视频相关信息"""
    os.chdir('D:\\Ffmpeg_Process_Result')
    ItemFile = input("Please enter the whole path of file: ")
    os.system('cd %s &&ffmpeg -i "%s" >>info.txt 2>&1' %(ffmpeg_path,ItemFile))

def Extract_Audio():
    """抽取音频"""
    os.chdir(ffmpeg_path)
    ItemFile = input("Please enter the whole path of file: ")
    NewName = input("Please enter the name of output file: ")
    suffix = os.path.splitext(ItemFile)[1]
    Order = "ffmpeg -i" + ' "' + ItemFile + '"'+ " -map " + "0:1 " + '-c copy ' + '"' + NewName + suffix + '"'
    run_order = subprocess.run(Order, shell=True)
    print(run_order)

def Extract_Video():
    """抽取视频"""
    os.chdir(ffmpeg_path)
    ItemFile = input("Please enter the whole path of file: ")
    NewName = input("Please enter the name of output file: ")
    suffix = os.path.splitext(ItemFile)[1]
    Order = "ffmpeg -i" + ' "' + ItemFile + '"' + " -map " + "0:0 " + '-c copy ' + '"' + NewName + suffix + '"'
    run_order = subprocess.run(Order, shell=True)
    print(run_order)

def Clip_Length():
    """截取片段"""
    os.chdir(ffmpeg_path)
    ItemFile = input("Please enter the whole path of file: ")
    NewName = input("Please enter the name of output file: ")
    StartTime = input("Please enter the start time (00:00:xx) : ")
    EndTime = input("Please enter the end time (00:00:xx) : ")
    suffix = os.path.splitext(ItemFile)[1]
    Order = "ffmpeg -ss " + StartTime + " -t " + EndTime + " -i" + ' "' + ItemFile + '"' + " -vcodec copy -acodec copy " + '"' + NewName + suffix + '"'
    run_order = subprocess.run(Order, shell=True)
    print(run_order)

def Conversion_Encoding_Format():
    """转换编解码格式"""
    """Todo:用指令ffmpeg -codecs打印一张编解码表，询问转换的是音频编解码还是视频编解码，给出所有可转换的格式列表，再根据选择转换"""
    VideoDecode = []
    VideoEncode = []
    AudioDecode = []
    AudioEncode = []
    os.system('cd %s &&ffmpeg -codecs >>Codecs_info.txt 2>&1' % ffmpeg_path)
    with open(os.path.join(ffmpeg_path,"Codecs_info.txt"),'r',encoding='ISO-8859-1') as CodecsList:
        for line in CodecsList:
            VideoDecodeList1 = re.findall('D.V',line)
            if len(VideoDecodeList1):
                VideoDecodeList2 = re.findall(' \S+ ',VideoDecodeList1[0])
                VideoDecode.append(str(VideoDecodeList2))
        for line in CodecsList:
            VideoEncodeList1 = re.findall('[\S]EV',line)
            if len(VideoEncodeList1):
                VideoEncodeList2 = re.findall(' \S+ ',VideoEncodeList1[0])
                VideoEncode.append(str(VideoEncodeList2))
        for line in CodecsList:
            AudioDecodeList1 = re.findall('D.A',line)
            if len(AudioDecodeList1):
                AudioDecodeList2 = re.findall(' \S+ ',AudioDecodeList1[0])
                AudioDecode.append(str(AudioDecodeList2))
        for line in CodecsList:
            AudioEncodeList1 = re.findall('[\S]EA',line)
            if len(AudioEncodeList1):
                AudioEncodeList2 = re.findall(' \S+ ',AudioEncodeList1[0])
                AudioEncode.append(str(AudioEncodeList2))
    ItemFile = input("Please enter the whole path of file: ")
    suffix = os.path.splitext(ItemFile)[1]
    suffix_name = re.findall('[^.]\S+', suffix)
    print("VideoDecode = ", VideoDecode)
    print("VideoEncode = ", VideoEncode)
    print("AudioDecode = ", AudioDecode)
    print("AudioEncode = ", AudioEncode)
    if suffix_name in VideoDecode or AudioDecode:
        Type = input("Please enter the type of codec (If you need see the list of available codecs,please enter 'y'): ")
        if Type.lower() == "y":
            print("VideoDecode = ",VideoDecode)
            print("VideoEncode = ",VideoEncode)
            print("AudioDecode = ",AudioDecode)
            print("AudioEncode = ",AudioEncode)
            Conversion_Encoding_Format()
        if Type in VideoEncode or AudioEncode:
            NewName = input("Please enter the name of output file: ")
            os.system('cd %s &&ffmpeg -i "%s" -vcodec %s "%s" >>info.txt 2>&1' %(ffmpeg_path,ItemFile,Type,NewName))
    else:
        print("[*] please check the codecs(if input correct&can be decode)")

def Conversion_Package_Format():
    """转换封装格式"""
    """Todo:用指令ffmpeg -formats打印一张封装格式表，询问转换的是音频编解码还是视频编解码，给出所有可转换的格式列表，再根据选择转换"""
    os.system('cd %s &&ffmpeg -formats >>Formats_info.txt 2>&1' % ffmpeg_path)


DisPlay()