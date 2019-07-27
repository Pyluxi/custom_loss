import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
input_file = '../tmp/std.xls'
data = pd.read_excel(input_file)
#划分X，y
X = data.loc[:,:'单位里程积分'].values
y = data.loc[:,'客户类型'].values
#模型选择使用交叉验证法来评估模型
model1 = DecisionTreeClassifier()
model2 = SVC(kernel='rbf')
score1 = cross_val_score(model1,X,y,cv=5)
score2 = cross_val_score(model2,X,y,cv=5)
print('决策树模型得分：{:.2f}'.format(score1.mean()))
print('SVM模型得分：{:.2f}'.format(score2.mean()))




