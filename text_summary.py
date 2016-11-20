# coding=utf-8
import textrank4zh


class summary(object):
	def key_sentence(self, text, num=5):
		key_sentence = textrank4zh.TextRank4Sentence()
		key_sentence.analyze(text=text, lower=True, source='all_filters')
		# 新建排序列表
		s_index = []
		# 建立index=>sentence字典
		s_dict = {}
		# 添加索引列表和字典
		for ks in key_sentence.get_key_sentences(num):
			s_index.append(ks.index)
			s_dict[ks.index] = ks.sentence
		# 排序索引列表(按照先后顺序)
		s_index.sort()
		# 按索引列表顺序输出字典里的关键句
		return (s_index, s_dict)
