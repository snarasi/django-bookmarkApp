#test.py
#!/usr/bin/python
import re

class DisplayObject:

	def __init__(self,link,adddate,title):
		self.link=link
		self.adddate=adddate
		self.title=title




content=''
with open("temp.html", "r") as infile:
	for line in infile:
		content+=line

list = content.split("<DT><A HREF=");

print len(list)

displayList = []

for index in range(len(list)):
	if(index !=0 ):
		sublist = list[index].split('"')
		titlelist = list[index].split('>')
		title=titlelist[1]
		#actualTitle=title[:len(title)-3]
		displayList.append(DisplayObject(sublist[1],sublist[3],title[:len(title)-3]))

for item in displayList:
	print item.link+" --- "+item.adddate+" --- "+item.title


