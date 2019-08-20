# 这部分为测试代码
# 可见测试代码需要包含的部分有：
# 导入测试库，相关函数
# 创建一个类，用于测试用例
# 在这个类下定义了2个测试方法，分别用于测试应用中可能出现的不同情况
# 定义一个新的变量，将应用的函数及属性赋给新变量（相当于应用的结果给新的变量）
# 用测试函数self.ass...来验证结果，即在括号中写上（应用结果（新变量），测试取的值）
# 最后就是运行测试函数，这部分的形式是固定的


import unittest
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能否处理Andy Walker这样的姓名"""
        format_name = get_formated_name('Andy','Walker')
        self.assertEqual(format_name,'Andy Walker')

    def test_first_middle_last_name(self):
        """能否处理Andy Justin Walker"""
        format_name = get_formated_name('Andy','Walker','Justin')
        self.assertEqual(format_name,'Andy Justin Walker')

unittest.main()


