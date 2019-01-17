from AipNlp import client

text1 = "万达集团"

text2 = "王健林"

""" 调用短文本相似度 """
result = client.simnet(text1, text2)

""" 如果有可选参数 """
options = {}
options["model"] = "CNN"

""" 带参数调用短文本相似度 """
client.simnet(text1, text2, options)

print(result['score'])