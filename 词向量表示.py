from AipNlp import client

word = "张飞"

""" 调用词向量表示 """
result = client.wordEmbedding(word)

print(result)