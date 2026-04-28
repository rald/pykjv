from Token import TokenType,Token
from Cite import Cite

class Parser:

    def __init__(self,tokens):
        self.tokens=tokens
        self.i=0
        self.cites=[]

        self.bname=None
        self.bsname=None
        self.scnum=None
        self.ecnum=None
        self.svnum=None
        self.evnum=None

    def look(self, offset = 0):
        return self.tokens[self.i + offset]

    def next(self,offset=1):
        self.i+=offset

    def getType(self,offset=0):
        return self.tokens[self.i+offset].type

    def getText(self,offset=0):
        return self.tokens[self.i+offset].text

    def match(self, type, offset = 0):
        return self.look(offset).type == type

    def add(self):
        self.cites.append(Cite(self.bname,self.bsname,self.scnum,self.ecnum,self.svnum,self.evnum))

    def parse(self):

        if self.match(TokenType.NUMBER,0) and \
            self.match(TokenType.STRING,1) and \
            self.match(TokenType.NUMBER,2) and \
            self.match(TokenType.COLON,3) and \
            self.match(TokenType.NUMBER,4) and \
            self.match(TokenType.DASH,5) and \
            self.match(TokenType.NUMBER,6):
            self.bname=self.getText(0)+" "+self.getText(1)
            self.bsname=self.getText(0)+self.getText(1)
            self.scnum=int(self.getText(2))
            self.ecnum=self.scnum;
            self.svnum=int(self.getText(4))
            self.evnum=int(self.getText(6))
            self.add()
        elif self.match(TokenType.STRING,0) and \
            self.match(TokenType.NUMBER,1) and \
            self.match(TokenType.COLON,2) and \
            self.match(TokenType.NUMBER,3) and \
            self.match(TokenType.DASH,4) and \
            self.match(TokenType.NUMBER,5):
            self.bname=self.getText(0)
            self.bsname=self.getText(0)
            self.scnum=int(self.getText(1))
            self.ecnum=self.scnum;
            self.svnum=int(self.getText(3))
            self.evnum=int(self.getText(5))
            self.add()
        elif self.match(TokenType.NUMBER,0) and \
            self.match(TokenType.STRING,1) and \
            self.match(TokenType.NUMBER,2) and \
            self.match(TokenType.COLON,3) and \
            self.match(TokenType.NUMBER,4):
            self.bname=self.getText(0)+" "+self.getText(1)
            self.bsname=self.getText(0)+self.getText(1);
            self.scnum=int(self.getText(2))
            self.ecnum=self.scnum;
            self.svnum=int(self.getText(4))
            self.evnum=self.svnum
            self.add()
        elif self.match(TokenType.STRING,0) and \
            self.match(TokenType.NUMBER,1) and \
            self.match(TokenType.COLON,2) and \
            self.match(TokenType.NUMBER,3):
            self.bname=self.getText(0)
            self.bsname=self.getText(0)
            self.scnum=int(self.getText(1))
            self.ecnum=self.scnum;
            self.svnum=int(self.getText(3))
            self.evnum=self.svnum
            self.add()


        return self.cites
