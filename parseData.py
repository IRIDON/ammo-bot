from __init__ import *
from lxml import html
import requests
import statistics
import sys

def getKey(item):
	return item["price"]

class IbisParseData(object):
	def __init__(self):
		self.categories = CALIBERS

	def setCategoryId(self, categoryId):
		self.categoryId = categoryId
		self.getAll()

	def getPage(self):
		page = requests.get(self.url)
		tree = html.fromstring(page.content)

		self.tree = tree

		return True

	def getPrices(self):
		price = self.tree.xpath('//div[@class="pb_price "]')
		result = []

		for item in price:
			pr = item.xpath('./text()')

			if pr:
				result.append(float(pr[0]))
			else:
				pn = item.xpath('*/text()')

				result.append(float(pn[0] + pn[1]))

		return result

	def getStructure(self, price):
		title = self.tree.xpath('//a[@class="pb_product_name"]/text()')
		stock = self.tree.xpath('//div[@class="pb_stock"]')
		result = []

		for index, item in enumerate(price):
			dic = {}
			dic["title"] = title[index]
			dic["price"] = price[index]

			if not stock[index].xpath('*/text()'):
				result.append(dic)
			else:
				break

		return sorted(result, key=getKey)

	def getAll(self):
		category = self.categories[self.categoryId]

		self.url = URL_TMP % (AMMM_TYPE[category[1]], category[0])
		self.getPage()
		price = self.getPrices()
		self.data = self.getStructure(price)
		self.price = price

	def getDiscount(self, price, discount):
		factor = (100 - float(discount)) / 100

		return format(price * factor, '.2f')

	def getMedian(self):
		return statistics.median(self.price)

	def topPrices(self, num=3, discount=0):
		result = []
		dataLen = len(self.data)

		if dataLen < num:
			num = dataLen

		for index in range(0,num):
			title = self.data[index]["title"]
			price = self.data[index]["price"]

			if discount == 0:
				result.append("*%s %s* - %s" % (price, CURRENCY, title))
			else:
				result.append( "*%s %s* _(%s)_ - %s" % (self.getDiscount(price, discount), CURRENCY, price, title))
		
		result.append("\n[Visit to site](%s)" % (self.url))

		return "\n".join(result)

