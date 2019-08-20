#这个程序相当于对app进行使用


from Survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = " What language did you first learn to speak? "
my_servey = AnonymousSurvey(question)

#显示问题并且存储答案
my_servey.show_question()
print("Enter 'q' at any time to quit \n")
while True:
    response = input("language:")
    if response == 'q':
        break
    my_servey.store_response(response)

#显示调查结果
print("Thank you")
my_servey.show_results()
