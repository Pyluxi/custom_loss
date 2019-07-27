import joblib
from model import X_test,y_test
#导入模型
model = joblib.load('../tmp/loss.pkl')
#预测分类
y_predict = model.predict([X_test[0]])
print(y_predict)
print(y_test[0])

