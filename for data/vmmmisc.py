class AddressTranslationError(Exception):
	def __init__(self, pid, addr):
		self.pid = pid
		self.addr = addr

	def __str__(self):
		return repr("Address Tranlation Failed. pid: " + str(self.pid) + ", addr: " + self.addr)

class FrameNotFoundError(Exception):
	def __init__(self, pid, page):
		self.pid = pid
		self.page = page

	def __str__(self):
		return repr("Frame Not Found. pid: " + str(self.pid) + ", page: " + str(self.page))

class SignalUser1():
	def __init__(self):
		self.pid = -1
		self.page = -1
		
	def set(self, pid, page):
		self.pid = pid
		self.page = page
		
	def send(self, handler): 
		handler(self.pid, self.page)
