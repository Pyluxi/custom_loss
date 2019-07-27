import pandas as pd
input_file = '../tmp/selected.xls'
output_file = '../tmp/classfication.xls'
data = pd.read_excel(input_file)
data['客户类型'] = None
for i in range(len(data)):
    #第一、二年飞行次数比例小于50%的客户定义为已流失
    if data['飞行次数比例'][i] < 0.5:
        data['客户类型'][i] = 0 #0代表已流失
    #第一、二年飞行次数比例在[0.5,0.9)之间的客户定义为准流失
    if (data['飞行次数比例'][i] >= 0.5) & (data['飞行次数比例'][i] < 0.9) :
        data['客户类型'][i] = 1 #1代表准流失
    #第一、二年飞行次数比例大于等于90%的客户定义为未流失
    if data['飞行次数比例'][i] >= 0.9:
        data['客户类型'][i] = 2 #2代表未流失
#导出
data.to_excel(output_file,index=None)