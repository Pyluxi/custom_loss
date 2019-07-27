import pandas as pd
#读数据
input_file = '../data/cleaned.xls'
output_file = '../tmp/selected.xls'
data = pd.read_excel(input_file)
#选取特征
data['单位里程票价'] = (data['SUM_YR_1'] + data['SUM_YR_2'])/data['SEG_KM_SUM']
data['单位里程积分'] = (data['P1Y_BP_SUM'] + data['L1Y_BP_SUM'])/data['SEG_KM_SUM']
data['飞行次数比例'] = data['L1Y_Flight_Count'] / data['P1Y_Flight_Count'] #第二年飞行次数与第一年飞行次数的比例
#筛选出老客户(飞行次数大于6次的为老客户)
data = data[data['FLIGHT_COUNT'] > 6]
#选择特征
data = data[['FFP_TIER','飞行次数比例','AVG_INTERVAL',
             'avg_discount','EXCHANGE_COUNT','Eli_Add_Point_Sum','单位里程票价','单位里程积分']]
#导出
data.to_excel(output_file,index=None)