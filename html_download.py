# coding=utf-8


# 实现传入Url之后，返回网页内容或None
import urllib2


class HtmlDownloader(object):
	def download(self, url):
		# 如果Url为空，返回None
		if url is None:
			return None
		# 否则执行网页抓取
		else:
			response = urllib2.urlopen(url)
			# 如果连接status不是200（说明访问失败），就返回None
			if response.getcode() != 200:
				print(response.getcode())
				return None
			# 否则，读取内容，return
			else:
				return response.read()
