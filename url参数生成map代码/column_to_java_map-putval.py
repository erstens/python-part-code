#coding=utf-8

f = open('map.txt','r')
fp = open('map_w.txt','w')

fp.write("Map m1 = new HashMap();\n")
v = f.read().split('\n')
for i in v:
	k = i.split("=")[0]
	v = i.split("=")[1]
	fp.write("m1.put(\"%s\",\"%s\");\n" % (k,v))