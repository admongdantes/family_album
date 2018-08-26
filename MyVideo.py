import os,time, datetime

class MyVideo:
	absPath = ''
	displayDate = ''
	fileName = ''
	fileNameUrl = ''
	mtime = ''

	def __init__(self, absPath):
		self.absPath = absPath
		self.fileName = os.path.split(absPath)[1]
		self.fileNameUrl = os.path.join('/static/media1', self.fileName)
		self.mtime = os.path.getmtime(self.absPath)
		#self.displayDate = time.ctime(self.mtime)
		self.displayDate = datetime.date.fromtimestamp(self.mtime)

	def info(self):
		print(self.absPath)
		print(self.fileName)
		print(self.fileNameUrl)


