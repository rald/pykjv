import xml.etree.ElementTree as ET

tree = ET.parse("bbe.xml")
root = tree.getroot()

for book in root.findall("BIBLEBOOK"):

	print(f"{book.get('bname')} -> {book.get('bsname')}")

	for chap in book.findall("CHAPTER"):
		for vers in chap.findall("VERS"):
			bname=book.get("bname")
			cnum=chap.get("cnumber")
			vnum=vers.get("vnumber")
			text=vers.text

#			print(f"{bname}|{cnum}|{vnum}|{text}")

