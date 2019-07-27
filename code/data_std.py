import pandas as pd
#读数
input_file = '../tmp/classfication.xls'
output_file = '../tmp/std.xls'
data = pd.read_excel(input_file)
#去掉飞行次数比例
data = data[['FFP_TIER','AVG_INTERVAL','avg_discount','EXCHANGE_COUNT',
             'Eli_Add_Point_Sum','单位里程票价','单位里程积分','客户类型']]
#标准化
data.loc[:,:'单位里程积分'] = (data.loc[:,:'单位里程积分'] - data.loc[:,:'单位里程积分'].mean(axis = 0)) \
       / (data.loc[:,:'单位里程积分'].std(axis = 0))
#导出
data.to_excel(output_file,index=None)