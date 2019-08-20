#这个程序相当于对使用的结果进行测试，看app的使用结果是否正确

import unittest
from Survey import AnonymousSurvey

class Anstestcase(unittest.TestCase):
    """测试答案是否包含在答案列表中"""

    def test_survey(self):
        """指定一个问题，写出要测试的对象（my_servey）"""
        """先预存一个答案English，再验证一个词（English）是否被包含其中"""
        question = " What language did you first learn to speak? "
        my_servey = AnonymousSurvey(question)
        my_servey.store_response('English')
        self.assertIn('English',my_servey.responses)
        
    def test_more_answer_servey(self):
        """预存多个答案时，匹配答案"""
        question = " What language did you first learn to speak? "
        my_servey = AnonymousSurvey(question)
        my_servey.responses = ['Chinese','English','Franch']
        for response in my_servey.responses:
        self.assertIn('Franch',my_servey.responses)

#测试程序的必要部分
if __name__ == '__main__':
    unittest.main()



