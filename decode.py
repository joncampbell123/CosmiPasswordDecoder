#!/usr/bin/python3
import sys
if sys.version_info[0] < 3:
    raise Exception("This code is intended for Python 3")
import csv,configparser

def decode(s):
	d=0x80
	out=[]
	for i in range(len(s)):
		v=ord(s[i])^d
		out.append(v)
		d+=1

	return ''.join([chr(x) for x in out][5:])


config = configparser.ConfigParser(strict=False, comment_prefixes= ('#', ';', '//'))
config.read('setup.ini',
            encoding='Windows-1252')
with open('results.csv','w',newline='') as f:
	csvw=csv.writer(f)
	csvw.writerow(['Name','Boxed','Jewelcase'])
	for section in config.sections():
		if section.startswith('!'):
			continue
		parts=[section,'','']
		print('Software:',section)
		for stype,si,opt in (('Boxed',1,'Bpassword'),('Jewelcase',2,'Jpassword')):
			if config.has_option(section,opt):
				res=decode(config.get(section,opt))
				print(stype,'password:',res)
				parts[si]=res
		print()
		csvw.writerow(parts)

		