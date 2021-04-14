import unittest
from e8_survey import AnonymousSurvey


print("----------测试AnonymousSurvey类----------")
# 验证:
# 如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。
# 使用assertIn()方法核实其确实存储在答案列表中。


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        # 要测试类的行为，需要创建其实例
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()


# ----------测试类----------
# ----------测试AnonymousSurvey类----------
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.012s

# OK


# ----------测试类----------
# ----------测试AnonymousSurvey类----------
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
