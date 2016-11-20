# coding=utf-8
# 该模块主要功能:
# 维护两种Url
# 已经爬取的Url和未爬取的Url

import pymysql


class UrlManager(object):
	# 初始化Url管理器
	def __init__(self):
		self.db_conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='spider')
		self.cur = self.db_conn.cursor()
		self.cur.execute("use spider")
	
	# 析构方法
	def __del__(self):
		self.cur.close()
		self.db_conn.close()
	
	# 处理列表的总控制器
	def add_new_urls(self, urls):
		# 判断如果传入的Url为空，则取消执行
		if urls is None or len(urls) == 0:
			return
		# 否则把url添加到未爬取的new_urls库中
		else:
			for url in urls:
				# 把href属性传过去
				if self.is_new_url(url):
					self.add_new_url(url)
	
	# 对数据库添加新的链接
	def add_new_url(self, url):
		url = url.strip()
		# 如果Url为空，则退出
		if url is None:
			return
		else:
			# 插入到数据库
			sql = "insert into hpu_news (url) values (\"%s\")" % url
			self.cur.execute(sql)
			self.cur.connection.commit()
			print("执行%s" % sql)
	
	# 判断链接是否存在于数据库
	def is_new_url(self, url):
		sql = "select * from hpu_news where url=\"%s\";" % url
		check = self.cur.execute(sql)
		if check == 1:
			return False
		return True
	
	# 判断链接是否已结爬取
	def is_craw(self, url):
		sql = "select url,title from hpu_news where url=\"%s\" and title is null;" % url
		print(sql)
		check = self.cur.execute(sql)
		if check == 1:
			return True
		return False
	
	# 从数据库获取一条没有爬取过的链接
	def get_one_url(self):
		sql = "SELECT url,title FROM hpu_news WHERE title IS NULL;"
		get=self.cur.execute(sql)
		if get:
			one_url = self.cur.fetchone()
			return one_url[0]
		else:
			return False