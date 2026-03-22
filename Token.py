from enum import Enum

class TokenType(Enum):
	STRING = 1
	NUMBER = 2
	COLON  = 3
	DASH   = 4
	COMMA  = 5
	EOF    = 6

class Token:
	def __init__(self,type,text):
		self.type=type
		self.text=text
	def __repr__(self):
		return f"Token {{Type: {self.type}, Text: \"{self.text}\"}}"
