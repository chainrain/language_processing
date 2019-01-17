from AipNlp import client

text = "百度是一家高科技公司"

""" 调用词法分析 """
result = client.lexer(text)

print(result['text'])
print(result['items'])

