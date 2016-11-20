# coding=utf-8
import io
from text_summary import summary
from bs4 import BeautifulSoup
from urllib import quote


# 这里是html解析器
# 获取所需要的数据
# 这个爬虫用来获取百度百科的标题和首部信息

class HtmlParser(object):
	# 解析器总控制器
	def parser_link(self, html_cont):
		bsObj = BeautifulSoup(html_cont, 'html.parser')
		lists = bsObj.find_all("a", {"target": "_blank"})
		list_href = []
		for li in lists:
			if li['href'] is not None:
				list_href.append(li['href'])
		return list_href
	
	# 解析正文内容，整理字典返回
	def parser_content(self, url, html_cont):
		# 解析bs对象
		bsObj = BeautifulSoup(html_cont, 'html.parser')
		# 获取标题
		title = bsObj.find("div", {"id": "NewsTitle"}).get_text().strip()
		if title is None:
			return False
		# 反复处理info信息
		info = bsObj.find("span", {"id": "ajaxElement_1"}).parent.get_text()
		info_f = io.StringIO(info)
		info2 = info_f.readline().split("点击数")[0].split("发布时间：")
		# 得到info和date数据
		info = info2[0]
		# 日期
		if len(info2) > 1:
			date = info2[1]
		else:
			date = ''
		# 下面搜集正文
		html_content = bsObj.find("div", {"id": "NewsContent"})
		# 去空行
		text_content = html_content.get_text().replace("\n\n", "\n")
		# 摘要
		sumObj = summary()
		summ = sumObj.key_sentence(text_content, 5)
		# 合并摘要
		text_summary = ''
		for i in summ[0]:
			text_summary += summ[1][i] + '\n'
		# 整理字典
		result_dict = {
			"url"         : url,
			"title"       : title.encode("utf-8"),
			"info"        : info.encode("utf-8"),
			"html_content": quote("%s" % html_content),
			"text_content": text_content.encode("utf-8"),
			"text_summary": text_summary.encode("utf-8"),
			"date"        : date.encode("utf-8")
		}
		# debug打印变量类型
		# for kk in result_dict:
		# 	print(kk,type(result_dict[kk]))
		# exit()
		return result_dict
