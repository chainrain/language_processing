from AipNlp import client

word1 = "北京"

word2 = "上海"

""" 调用词义相似度 """
result = client.wordSimEmbedding(word1, word2)

""" 如果有可选参数 """
options = {}
options["mode"] = 0

""" 带参数调用词义相似度 """
client.wordSimEmbedding(word1, word2, options)

print(result['score'])