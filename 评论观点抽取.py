from AipNlp import client

text = "三星电脑电池不给力"

""" 如果有可选参数 """
options = {}
options["type"] = 13

""" 带参数调用评论观点抽取 """
result = client.commentTag(text, options)

print(result)
# print('情感',result['sentiment'])
# print(result['type'])