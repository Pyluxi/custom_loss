import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import joblib
#读取数据
input_file = '../tmp/std.xls'
output_file = '../tmp/loss.pkl'
data = pd.read_excel(input_file)
#划分训练集、测试集
X = data.loc[:,:'单位里程积分'].values
y = data.loc[:,'客户类型'].values
X_train,X_test,y_train,y_test =  train_test_split(X,y,train_size = 0.8)
#采用网格搜索法来寻找SVC的最优参数
svc = SVC(kernel='rbf',C=1.0,gamma=0.01)
# params = {'gamma':[0.1,1.0,10.0],
#           'C':[1.0,10.0,100.0]}
# grid_search = GridSearchCV(svc,params,cv=5)
# grid_search.fit(X_train,y_train)
# print('模型最高分 {:.2f}'.format(grid_search.score(X_test,y_test)))
# print('最优参数为: {}'.format(grid_search.best_params_))
svc.fit(X_train,y_train)
print('模型最高分为：{:.2f}'.format(svc.score(X_test,y_test)))
joblib.dump(svc,output_file)

