from AipNlp import client

text = "百度是一家人工只能公司"

""" 调用文本纠错 """
result = client.ecnet(text)['item']

print('纠错后的文本',result['correct_query'])