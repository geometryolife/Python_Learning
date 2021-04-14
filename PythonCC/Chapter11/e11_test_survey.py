import unittest
from e8_survey import AnonymousSurvey

print("----------方法setUp()----------")
# 前面的test_survey.py中，在每个测试方法中都创建了一个AnonymousSurvey实
# 例，并在每个方法中都创建了答案。

# 更优雅的做法是使用unittest.TestCase类中的方法setUp()，只需创建这些对象
# 一次，并在每个测试方法中使用它们。

# 如果在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以
# test_打头的方法。


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()


# 方法setUp()做了两件事情:
# 创建一个调查对象；
# 创建一个答案列表。
# 存储这两样东西的变量名包含前缀self(即存储在属性中)，因此可在这个类的任
# 何地方使用。让两个测试方法都更简单，因为它们都不用创建调查对象和答案。

# 总结:
# 测试自己编写的类时，方法setUp()让测试方法编写起来更容易:
# 可在setUp()方法中创建一系列实例并设置它们的属性，再在测试方法中
# 直接使用这些实例。

# 运行测试用例时，每完成一个单元测试，Python都打印一个字符:
# 1.测试通过时打印一个句点；
# 2.测试引发错误时打印一个E；
# 3.测试导致断言失败时打印一个F。

# 如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果来
# 获悉有多少个测试通过了。

# 测试是很多初学者都不熟悉的主题。作为初学者，并非必须为你尝试的所有
# 项目编写测试；但参与工作量较大的项目时，你应对自己编写的函数和类的
# 重要行为进行测试。这样你就能够更加确定自己所做的工作不会破坏项目的
# 其他部分，你就能够随心所欲地改进既有代码了。如果不小心破坏了原来的
# 功能，你马上就会知道，从而能够轻松地修复问题。相比等到不满意的用户
# 报告Bug后再采取措施，在测试未通过时采取措施要容易得多。

# ----------测试类----------
# ----------方法setUp()----------
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.012s

# OK
