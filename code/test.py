import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
input_file = '../tmp/classfication.xls'

data = pd.read_excel(input_file)

X = data.loc[:,:'单位里程积分'].values
y = data.loc[:,'客户类型'].values

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8)

svc = SVC(kernel='rbf',gamma=0.01,C=1.0)

svc.fit(X_train,y_train)

print('模型得分为：{:.2f}'.format(svc.score(X_test,y_test)))