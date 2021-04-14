from e8_survey import AnonymousSurvey

print("----------一个要测试的类----------")
# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What Language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()


# ----------测试类----------
# ----------一个要测试的类----------
# What Language did you first learn to speak?
# Enter 'q' at any time to quit.

# Language: English
# Language: Spanish
# Language: English
# Language: Mandarin
# Language: q

# Thank you to everyone who participated in the survey!
# Survey results:
# - English
# - Spanish
# - English
# - Mandarin
