#*-*coding:utf-8 *-*  
''''' 
Created on 2012-6-14 
 
@author: bitter_tea 
'''  
def gen_file(path,size):  
    #首先以路径path新建一个文件，并设置模式为写  
    file = open(path,'w')  
    #根据文件大小，偏移文件读取位置   
    file.seek(1024*1024*size)#姑且以GB为单位吧  
    #然后在当前位置写入任何内容，必须要写入，不然文件不会那么大哦  
    file.write('\x00')  
    file.close()  
      
      
gen_file('./_100MB.jpg',100)  