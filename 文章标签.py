from AipNlp import client

title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"

content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"

""" 调用文章标签 """
result = client.keyword(title, content)

print(result)