from AipNlp import client

text = "今天天气怎么样"

""" 调用依存句法分析 """
result = client.depParser(text)

""" 如果有可选参数 """
options = {}
options["mode"] = 1

""" 带参数调用依存句法分析 """
client.depParser(text, options)

print(result['items'])