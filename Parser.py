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

    def look(self):
        return self.tokens[self.i]

    def next(self):
        self.i+=1

    def getType(self):
        return self.tokens[self.i].type

    def getText(self):
        return self.tokens[self.i].text

    def match(self,type):
        return self.look().type == type

    def p99(self):
        self.cites.append(Cite(self.bname,self.bsname,self.scnum,self.ecnum,self.svnum,self.evnum))

    def p7(self):
        if self.match(TokenType.COMMA):
            self.next()
            self.p3()

    def p6(self):
        if self.match(TokenType.NUMBER):
            self.ecnum=int(self.getText())
            self.svnum=0
            self.evnum=0
            self.next()
            self.p99()

    def p5(self):
        if self.match(TokenType.NUMBER):
            self.evnum=int(self.getText())
            self.next()
            self.p99()
            self.p7()

    def p4(self):
        if self.match(TokenType.DASH):
            self.next()
            self.p5()
        elif self.match(TokenType.COMMA):
            self.p99()
            self.next()
            self.p3()
        else:
            self.p99()

    def p3(self):
        if self.match(TokenType.NUMBER):
            self.svnum=int(self.getText())
            self.evnum=self.svnum
            self.next()
            self.p4()

    def p2(self):
        if self.match(TokenType.COLON):
            self.next()
            self.p3()
        elif self.match(TokenType.DASH):
            self.next()
            self.p6()
        else:
            self.svnum=0
            self.evnum=0
            self.p99()

    def p1(self):
        if self.match(TokenType.NUMBER):
            self.scnum=int(self.getText())
            self.ecnum=self.scnum
            self.next()
            self.p2()

    def p0(self):
        if self.match(TokenType.STRING):
            self.bname=self.getText()
            self.bsname=self.getText()
            self.next()
            self.p1()
        elif self.match(TokenType.NUMBER):
            self.bname=self.getText()+" "
            self.bsname=self.getText()
            self.next();
            if self.match(TokenType.STRING):
                self.bname+=self.getText()
                self.bsname+=self.getText()
                self.next()
                self.p1()

    def parse(self):
        while not self.match(TokenType.EOF):
            self.p0()
        return self.cites
