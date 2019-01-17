from AipNlp import client

content = "麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，创造了一种..."

maxSummaryLen = 300

""" 调用新闻摘要接口 """
result = client.newsSummary(content, maxSummaryLen)

""" 如果有可选参数 """
options = {}
options["title"] = "标题"

""" 带参数调用新闻摘要接口 """
client.newsSummary(content, maxSummaryLen, options)
print(result)

"""
无访问权限,用不了~
{'error_msg': 'No permission to access data', 'error_code': 6}
"""