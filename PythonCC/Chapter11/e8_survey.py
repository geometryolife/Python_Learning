print("----------测试类----------")
# 如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为

# 断言方法检查你认为应该满足的条件是否确实满足。

# 6种常用的断言方法:
# 核实返回值等于或不等于预期的值、返回的值为True或False、返回的值在
# 列表中或不在列表中。
# assertEqual(a, b)        核实a == b
# assertNotEqual(a, b)     核实a != b
# assertTrue(x)            核实x为True
# assertFalse(x)           核实x为False
# assertIn(item, list)     核实item在list中
# assertNotIn(item, list)  核实item不在list中

# 使用上述方法必须继承类unittest.TestCas。


class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
