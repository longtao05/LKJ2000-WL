# -*- encoding=utf-8 -*-

from binascii import *
import json

#准备活动性检测帧应答数据
def openJson():
	with open("./protocols/test.json",'r',encoding='utf-8') as load_f:
	    load_dict = json.load(load_f)
	    #print(load_dict)

	#load_dict['desc'] = "xxxxx"
	#print(load_dict)

	'''with open("../config/record.json","w") as dump_f:
	    json.dump(load_dict,dump_f)'''

	return load_dict

	#return load_dict['fields'][0]['value']+load_dict['fields'][1]['value']
def testx():
	list1=[]
	load_dict = openJson()
	fields_len=len(load_dict['fields'])
	i=0
	while i< fields_len-1:
		print(load_dict['fields'][i]['field'])
		#print(type(load_dict['fields'][i]['value']))
		if ""==load_dict['fields'][i]['value']:
			j=0
			while j< load_dict['fields'][i]['size']:
				list1.append('00')
				j+=1
		else:
			list1.append(load_dict['fields'][i]['value'])
			pass
		i+=1



	return list1

def listtohex(listdata):
	print(listdata)
	str = ''.join(listdata)
	return str

def test():
	return listtohex(testx())

if __name__ == '__main__':
    print("-*-*-*-*-*-*-*-*-start-*-*-*-*-*-*-*-*-")
    print(listtohex(testx()))
    print("-*-*-*-*-*-*-*-*-end-*-*-*-*-*-*-*-*-")
