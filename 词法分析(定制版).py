from AipNlp import client

text = "百度是一家高科技公司"

""" 调用词法分析（定制版） """
result = client.lexerCustom(text)

print(result)