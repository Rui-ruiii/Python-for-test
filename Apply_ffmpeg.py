"""基于ffmpeg的多功能应用"""

def DisPlay():
    """显示页面"""
    """To Do:输入值为非数字时的异常抛出"""
    print("*" * 20,"Welcome","*" * 20)
    print("Please choose the number of the server you need:")
    print("[*]1.Single File")
    print("[*]2.Multiple Files")
    print("*" * 49)
    try:
        CountOfFile = int(input("Enter the number here:"))
        if CountOfFile == 1:
            SingleFile()
        if CountOfFile == 2:
            MultipleFile()
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
    print("*" * 20,"Operation","*" * 20)
    print("Please select the specific operation to be performed")
    print("[*]1.Extract Audio")
    print("[*]2.Extract Video")
    print("[*]3.Clip Length")
    print("[*]4.Conversion Encoding Format")
    print("[*]5.Conversion Package Format")
    try:
        Operation = int(input("Enter the number here:"))
        if Operation == 1:
            Extract_Audio()
        if Operation == 2:
            Extract_Video()
        if Operation == 3:
            Clip_Length()
        if Operation == 4:
            Conversion_Encoding_Format()
        if Operation == 5:
            Conversion_Package_Format()
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
    print("多个文件")

def Extract_Audio():
    """抽取音频"""
    print("抽取音频")

def Extract_Video():
    """抽取视频"""
    print("抽取视频")

def Clip_Length():
    """截取片段"""
    print("截取片段")

def Conversion_Encoding_Format():
    """转换编解码格式"""
    print("转换编解码格式")

def Conversion_Package_Format():
    """转换封装格式"""
    print("转换封装格式")


DisPlay()