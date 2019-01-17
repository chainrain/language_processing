from AipNlp import client

text = "床前明月光"

""" 调用DNN语言模型 """
result = client.dnnlm(text)

# print(result)
print(result['items'])


"""
log_id	uint64	请求唯一标识码
word	string	句子的切词结果
prob	float	该词在句子中的概率值,取值范围[0,1]
ppl	float	描述句子通顺的值：数值越低，句子越通顺
"""