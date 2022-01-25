import os,sys
def get_data():
  BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path是一个列表，包括有所有查找包的目录，直接启动python使用
  sys.path.append(BASE_DIR)
  Data_DIR = os.path.join(BASE_DIR,"Appium_Demo_weixin","paylink.txt")
  print('读取文件路径dir:',Data_DIR )
  file= open(Data_DIR ,'r',encoding='UTF-8')
  lines = file.readlines()
  data=[]
  for line in lines:
     #print(line)
     curline=line.strip('\n')
     data.append(curline)
     #print('data:',data)
  file.close()
  return data

def wirtein(writedatas):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path是一个列表，包括有所有查找包的目录，直接启动python使用
    sys.path.append(BASE_DIR)
    Data_DIR = os.path.join(BASE_DIR,"Appium_Demo_weixin","result.txt")
    with open(Data_DIR,"w") as f:
            f.truncate(0)
            f.writelines(writedatas)
    print('写入路径dir：',Data_DIR)
    print('写入文件成功！')
    f.close()