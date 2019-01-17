from AipNlp import client

title = "欧洲冠军杯"

content = "欧洲冠军联赛是欧洲足球协会联盟主办的年度足球比赛，代表欧洲俱乐部足球最高荣誉和水平，被认为是全世界最高素质、最具影响力以及最高水平的俱乐部赛事，亦是世界上奖金最高的足球赛事和体育赛事之一。"

""" 调用文章分类 """
result = client.topic(title, content)

# 分类
print(result['item']['lv1_tag_list'])

# 更细的分类
fenlei = result['item']['lv2_tag_list'][0]
print(fenlei)