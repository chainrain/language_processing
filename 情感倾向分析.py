from AipNlp import client

text = "苹果是一家伟大的公司"

""" 调用情感倾向分析 """
result = client.sentimentClassify(text)

print(result)