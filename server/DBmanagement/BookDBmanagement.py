import os
import sys

from server.data.DBcontext import DBcontext


class BookDBManagement:
	def __init__(self):
		pass

	def getSellerID(self, bookid):
		with DBcontext() as context:
			context.get_cursor().execute("" , )

	def getSearchBook(self, keyWord):


	def getBookInfo(self, bookid):


	def collectBook(self, userid, bookid):


	def changeBookState(self, userid, bookid, newState):


	if __name__ == '__main__':
		pass
