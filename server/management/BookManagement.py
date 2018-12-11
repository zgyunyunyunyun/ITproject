import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from server.DBmanagement.BookDBManagement import BookDBManagement

class BookManagement:
	odbm = 0

	def __init__(self):
		self.odbm = BookDBManagement()

	def searchBook(self, keyWord):
		bookInfoList = self.odbm.getSearchBook(keyWord)
		return bookInfoList

	def viewBook(self, bookid):
		bookInfo = self.odbm.getBookInfo(bookid)
		return bookInfo

	def collectBook(self, userid, bookid):
		boolean = self.odbm.collectBook(userid, bookid)
		return boolean
