### 版本6.0
1. 完善了test_login.py和test_invest.py中的其他用例
2. 新建了一个test_datas用来储存数据，实现了数据和代码的分离


### 缺点
1. driver的初始化数据准备desired_caps没有实现配置化
2. test_invest.py中的登录步骤很重复，能否合并，如果在conftest中提取出一个login_driver，中间又涉及到页面对象中的方法，比较混杂
