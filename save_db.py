# coding=utf-8
import pymysql


class save_db(object):
	# 构造方法，连接数据库，获取指针
	def __init__(self):
		self.db_conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='spider')
		self.db_conn.set_charset("utf8")
		self.cur = self.db_conn.cursor()
		self.cur.execute("use spider")
		self.cur.execute('SET NAMES utf8;')
		self.cur.execute('SET CHARACTER SET utf8;')
		self.cur.execute('SET character_set_connection=utf8;')
	
	# 析构方法，关闭数据库指针和数据库连接
	def __del__(self):
		self.cur.close()
		self.db_conn.close()
	
	# 接收一个字典，包含url,title，info，html_content,text_content,text_summary,date
	def save(self, dir):
		try:
			sql = "update hpu_news set title=\"%s\",info=\"%s\",html_content=\"%s\",text_content=\"%s\",text_summary=\"%s\",date=\"%s\" where url=\"%s\";" % (dir['title'], dir['info'], dir['html_content'], dir['text_content'], dir['text_summary'], dir['date'], dir['url'])
			self.cur.execute(sql)
			self.cur.connection.commit()
		except:
			sql = "update hpu_news set title=\"获取内容失败，请打开url进行浏览\" where url=\"%s\";" % dir['url']
			self.cur.execute(sql)
			self.cur.connection.commit()
		finally:
			pass
