from Token import TokenType,Token
from Cite import Cite

class Parser:

    def __init__(self,tokens):
        self.tokens=tokens
        self.i=0

        self.bname=None
        self.bsname=None
        self.scnum=None
        self.ecnum=None
        self.svnum=None
        self.evnum=None

    def p99(self):
        if self.ecnum==None: self.ecnum=self.scnum
        if self.evnum==None: self.evnum=self.svnum

        if self.ecnum==None:
            if self.scnum==None:
                self.scnum=0
                self.ecnum=0
            else:
                self.ecnum=self.scnum

        if self.evnum==None:
            if self.svnum==None:
                self.svnum=0
                self.evnum=0
            else:
                self.evnum=self.svnum

        return Cite(self.bname,self.bsname,self.scnum,self.ecnum,self.svnum,self.evnum)

    def p7(self):
        if self.tokens[self.i].type==TokenType.NUMBER:
            self.evnum=int(self.tokens[self.i].text)
            self.i+=1
            return self.p99()
        return None

    def p6(self):
        if self.tokens[self.i].type==TokenType.NUMBER:
            self.ecnum=int(self.tokens[self.i].text)
            self.i+=1
            return self.p99()
        return None

    def p5(self):
        if self.tokens[self.i].type==TokenType.DASH:
            self.i+=1
            return self.p7()
        else:
            return self.p99()
        return None

    def p4(self):
        if self.tokens[self.i].type==TokenType.NUMBER:
            self.svnum=int(self.tokens[self.i].text)
            self.evnum=self.svnum
            self.i+=1
            return self.p5()
        return None

    def p3(self):
        if self.tokens[self.i].type==TokenType.COLON:
            self.i+=1
            return self.p4()
        elif self.tokens[self.i].type==TokenType.DASH:
            self.i+=1
            return self.p6()
        else:
            return self.p99()
        return None

    def p2(self):
        if self.tokens[self.i].type==TokenType.NUMBER:
            self.scnum=int(self.tokens[self.i].text)
            self.i+=1
            return self.p3()
        return None

    def p1(self):
        if self.tokens[self.i].type==TokenType.STRING:
            self.bname=self.tokens[self.i].text
            self.bsname=self.tokens[self.i].text
            self.i+=1
            return self.p2()
        elif self.tokens[self.i].type==TokenType.NUMBER:
            self.bname=self.tokens[self.i].text+" "
            self.bsname=self.tokens[self.i].text
            self.i+=1
            if self.tokens[self.i].type==TokenType.STRING:
                self.bname+=self.tokens[self.i].text
                self.bsname+=self.tokens[self.i].text
                self.i+=1
                return self.p2()
        return None

    def parse(self):
        cites=[]
        n=len(self.tokens)

        while self.tokens[self.i].type!=TokenType.EOF:

            cite=self.p1()
            if cite:
                cites.append(cite)

            while self.tokens[self.i].type==TokenType.COMMA:
                self.i+=1
                cite=self.p4()
                if cite:
                    cites.append(cite)

            self.bname=None
            self.bsname=None
            self.scnum=None
            self.ecnum=None
            self.svnum=None
            self.evnum=None

        return cites

