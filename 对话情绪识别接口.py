from AipNlp import client

text = "今天高高兴兴"

""" 调用对话情绪识别接口 """
client.emotion(text)

""" 如果有可选参数 """
options = {}
options["scene"] = "talk"  # default（默认项-不区分场景），talk（闲聊对话-如度秘聊天等），task（任务型对话-如导航对话等），customer_service（客服对话-如电信/银行客服等

""" 带参数调用对话情绪识别接口 """
result = client.emotion(text, options)

print(result['items'])
print(result['items'][0])