# coding=utf-8
import time
import html_download
import html_parser
import url_manager
from save_db import save_db


class SpiderMain(object):
	# 初始化
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_download.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
	
	# 爬取新闻链接
	def get_links(self, url):
		# 使用下载器下载列表页面内容
		html_content = self.downloader.download(url)
		# 获取到所有超链接
		lists_a = self.parser.parser_link(html_content)
		# 进行判断并向数据库添加
		self.urls.add_new_urls(lists_a)
	
	# 爬取网页内容
	def craw_main(self, url):
		# 下载器下载新闻页面内容
		html_content = self.downloader.download(url)
		# 解析处理完成之后，返回一个字典
		content_dir = self.parser.parser_content(url, html_content)
		return content_dir


if __name__ == "__main__":
	# 开始获取新链接
	obj_spider = SpiderMain()
	queryUrl = 'http://news.hpu.edu.cn/SiteFiles/Inner/dynamic/output.aspx?publishmentSystemID=543&'
	queryString = 'publishmentSystemID=543&pageNodeID=694&pageContentID=0&pageTemplateType=ChannelTemplate&isPageRefresh=False&pageUrl=98CL0evdPiTY1bMSnVtpnv1ehO4X1GqCF40add0d3Me0add0cadG7XZCv0slash0OIO9Zi2DwtJdLW&ajaxDivID=ajaxElement_2&templateContent=5h27Jd1Xe0slash0q4uWDOaLlj7476vGbIBdgj4B3RtCTmck6ODrN0add0wGn0slash05qol0slash0b1eo2sXSUD0slash0cq60slash0B4xUpRRC5qFhogEaEh3M0add0eVgXv4yw0iI3kLW4aomo1Fwsf0slash0cxWejcOFyA474fOGa2KyQkBeDi2dMJhskvtPW2VnuyMgTKHJW6gzo8BLcsWVBeWYmDuOh0add0PiZYLPAM0add0yphuSNrar2zNiLZrza54amFZ2PWFRGfzAeF3UA3WGWJf3K6USZCQZJlXSdQ5vAmixNNLXLL3X0DISUq0slash0h54o6j56VTcqvqjNtPNeIz0add0aJmxCjRiu3hW33LOlR8VCqfnwqV5ArShlvM1bFZL0add03HRs2pNSJDqgyx7gHdDXam0slash0Qeb5sLNg3LqD0slash030slash006Ds4EFQzvpmPx7dNGGpeqhkQuCikujcBgOm71I0slash0muHYCqQEemkYbIpSXEMkJaVd1XZBzySTK13RWKGIlZD4Vg1ImEcvUFQA0DBpPNzNQ6zcURvw0rlPp3LdRTlzrqSXTYbw9eLdIyvZXr4flYkuTTpW4jshH8m4VBGAIxYVmtPsaeZpL1DADa2UBmasckInhmYWrsMMnTZV85l9eN1mx2CPGtUzk0slash0O2GjpzBPNK2qV6568w0slash0OZC5Lxv22pg2x0add0edMAmwf8XqT714PtoqKV4ngLewAv5DPqoZNL72Ig4xnaes6ghUnAjBm0qCehALeD0add09S6OqEbz0slash0VK0slash04MzDimaFiJr0slash0bu0slash0HZC1lKX80QRiiw2G475lp7SHPLlf03ouU2WKF4FSo6ZOrtf5eW9IypkTn5S8830HEeYVT4D9Q7QdHGlvw1YL8xQN0add0NxKwfZZhQlYrshrRIXNaGPF3g0add0tkKE76Nu4sve92YMUfd0add0AINcVTDVbrVd0u8fw4uEe0slash0MoBe9iCrH4kjHESgp5e7sY0slash08jUo6tTgWuIb1vZ4LfrXPVk0slash08lvW70IHlna6VYWjgLybEjM5kGKJ9L0rIqMyxKqF3eOHAlcyvMZcb8zFpC9Ndj0QxTB2ZBMUWH3irEiyHex5ripNrbI0slash0TJMalxHTg4VLLgsPoahdQZpmhn61VW16cWtKgOyFJkN0VAXemUQ1qe4BhQq4hEUVFHL1mGuG5u0slash09RS9XRWzKFMBMv4GczVRq2TXtUGL53oO5OWEgi2KmUR3LrDHWS0add0Ei0add0haKJO00e5peSZDk0C4n0add0H4svgehiEd2aNnPCQYKx0add0FC3iCFramxOlQkJI8FbxMrEmERLjoySNdiY2myPaT8681bu6i8vmezCVsaclBoC0u0lbIqQhqsz4LHZXSm8z30add05a4HkKa0add0YgW0slash0wKFS1ZgBmLkVepB7gXS7iM82JmkuFa0slash0Oe0slash0keLb4kvW1i1Ka1roGSRpfesBzOGEwXdC5y26F6wwUW7Hd6c3MmYvaY54Q4rmhPMuv0slash0DT5h2vJwL8UMUmopkD0dNIxclfcITxlT5owUdK1mm616UTtM8LUxaDUdLEV9W1rCfvMFRYnvbopkh4XLsOkgoa4S72xQxs5C2t0slash0vXxIk13QhvrhULWfQkSotd8zBF74Ph7qVddYpXLM4CopKRKeW5LPVXwPVUi8x9zDjevQ2HDOnO7C6R0slash0922hcWyTfNovM0add0G0slash0blOJVMIhSu7Hd5lb0slash0HlGA2yvY6INV67iVTiSSbvRwBg3GlS5bs2Whrm44NDtieITVSyRhgwHRAyxcIM8glNVIQb0slash0ctNr4UBn1J62A2UhmiuXkEyDkUE0DTfirkE15tnMKXXl0slash0arFpDXsg1heMaDLe9230slash0uTQ7rwFol10CoTyZG0add0ds1bvwo11zOGiHluCrfCuTkJCLpVwYhspFtIcMjmLm4jtDRn3Y0onoWAhWypaLr2ZO4BDuID3DVYc0slash0Xj6fa5m1g2GHa2eqrPLjHkOXKtgZFU5J4XGvoDqW0add0Jpv7DGBza275m4Y2eCvyjo08sF0add0XBTdQJBikvgel3vnl47QxHTeRO0add0afD0slash05It52qkHRU5SzeEkjh8iIYlH3ItHHjhYk7EniEVDIf5UdA1qbQY0slash0DDqDW3zkPzn0nnAr5HF1FNkMNFtcR3EZho86Xgn3nv3AMT9QGWJdSV4S7iQlxwAUG1s2QQWRzftGtD3YO9ytBn3IRXSvIPwpb7QY40X8maHBsgoU0add0ESlP0oWPhVZLL0add0pyVzDqtuyQ6ptjqmI410slash0zgEWhbEqSsUiMSqnFF20add0GIfOKmLYnojRGkdEMf33MXurAldFrC0add00add0TmvwfDNPpUBi4vglcZ2H0add0swBJBN2pMwWBFyfbwsFhlRrAR7OLJ0add0ui2BLQm57SsOhSossL0add08XKQBY2QKI1wd9ctU4KgDxuNqV5Cg0slash0I1NyGDAtK0iqnlZ6N38SabJ0add0qiVEgaQEpSkT70add0zUf4KlNuj8oAQrwdmx9f4S1rtZrW0add00add0D7hdeR4dzRQJLv0yulIKJbW6QAb9S8QVNJrZBzjfYI0slash0A0slash0rBogdRT2JfZYCh0Gnd3gyS3kETZnF0add0gByMSnbyCYT3oqS5VMPsp8J15ezDOmgcUvlLsbEMOWXqtQEp0RXWg4Esbrf2LZ9IyP66pBxLOQ1sQg0pCOTwqEz0slash0JX7pE4DWX0tu2bDnNnbHqcleMHs2Gu3M3i3y0add0LThu340add0AiNWU40slash0IFi82oXs0add0qvFvuxTErg2CSd37cQioYuP1Yyg4m0add0aaMpyZJnqIo9nyNHuuQ9ROvBfPy7PPg7tN2Gn5QsHQa2Xt70slash0yfiXNOHj0add0kHDvjHCfa7PXaP0slash0KJia7vUCcOcpIt6xxeSK77Zo3Eh130TO7JZAdjqY7iv54eWh3Ge4Ct0slash0vXUeI6w4lib7jLzrfBmkDwtPTVFtOT9TZ66fytT8UpjAfkpwvhZ7jxXkC9ruolfv0slash0bngsMQy3lywWqvc6D6r4smPYUNE7Df36EnXQ0nASOr995a0slash01GsPFgMsLhxg3VP1Fjmxx00add0YT1I5hvP4U1VB0slash0Ed5bEBU1tEU800slash0vX4S5CMY2ZAoTPUWZEpkibFpJUBE0slash0ojkFbvgs0slash0WR4NNczLWV0DXuNp0add0ePBKBXBh170add0zllS0add06cVgtBmv20slash0qLhg8xR0add0eBAAEPQhsht7ddTt9SJtEZizkdDoMZ1ZIgx0slash00s0slash0jmsrLR1YkBo3txmIWzldGz03Z27Dofn8oJVebuAPG5wk6SinQIL0add0f8CpCXqU9LZCnVuVtppfv0lHX1ykt5JZsv0slash0u6SM0slash0xm2NfcjAgBV2xRkMsNJ34o2ihODXGxigwBrUi9wMOJnH00add0m90wCTw2pUwAGnAm4iAGMhjNN6DOaVCQWTGKt7YFikNuhGaXLucXF6do0add0rh0aDlpGk43LnelM8F75roCZyKxOC80add0Wp2IqlIozMJcg0slash0EDoEdDn0slash0cOgNnonK4B10add0mHplfCFGNOy4VrgnRwylL24wvz8ZI9J7X4wGnceDtx5kGEXQf8h6hW4SIyq6PsrtKr78E1BntdvstekK8zRMR6VwxjELWfHUGEICiGShVN0slash0SPpPG0add0in0H0slash0nEacuN0slash0b3YVfcwFdEqiwmfSXY17eFow40slash0pQGnPE0add0ZmGVQ0equals00equals0&pageNum='
	page_num = 1
	print("正在检查是否有最新新闻...")
	while page_num <= 250:
		list_url = queryUrl + queryString + "%d" % page_num
		obj_spider.get_links(list_url)
		page_num += 1
	print("检查完毕！")
	print("开始获取新闻...")
	# 成功获取所有链接
	# 实例化数据库存储对象
	dbObj = save_db()
	new_url = obj_spider.urls.get_one_url()
	while new_url:
		content_dir = obj_spider.craw_main(new_url)
		# 如果不是false
		if content_dir:
			dbObj.save(content_dir)
			print("爬取%s结束" % content_dir['url'])
		new_url = obj_spider.urls.get_one_url()
