class Cite:
    def __init__(self,bname,bsname,scnum,ecnum,svnum,evnum):
        self.bname=bname
        self.bsname=bsname
        self.scnum=scnum
        self.ecnum=ecnum
        self.svnum=svnum
        self.evnum=evnum
    def __repr__(self):
        return f"Cite {{ bname: \"{self.bname}\", bsname: \"{self.bsname}\" scnum: {self.scnum}, ecnum: {self.ecnum}, svnum: {self.svnum}, evnum: {self.evnum} }}"
