import xml.etree.ElementTree as ET

class Passage:

    def __init__(self,bname,cnum,vnum,text):
        self.bname=bname
        self.cnum=cnum
        self.vnum=vnum
        self.text=text

    def __repr__(self):
        return f"{self.bname} {self.cnum}:{self.vnum} -> {self.text}"

    @staticmethod
    def find(cite):

        passages=[]

        tree = ET.parse("kjv.xml")
        root = tree.getroot()

        for book in root.findall("BIBLEBOOK"):
        	for chap in book.findall("CHAPTER"):
        		for vers in chap.findall("VERS"):
        			bname=book.get("bname")
        			bsname=book.get("bsname")
        			cnum=int(chap.get("cnumber"))
        			vnum=int(vers.get("vnumber"))
        			text=vers.text

        			if (bname.lower() == cite.bname.lower() or bsname.lower() == cite.bsname.lower()) and cnum>=cite.scnum and cnum<=cite.ecnum and ((vnum>=cite.svnum and vnum<=cite.evnum) or (cite.svnum==0 and cite.evnum==0)):
        			    passages.append(Passage(bname,cnum,vnum,text))

        return passages
