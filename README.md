### 版本10.0
1. 新增多进程兼容性测试操作方法
2. 利用pytestconfig传递设备信息，通过命令行启动appium-server


### 缺点
1. test_invest.py中的登录步骤很重复,能否合并，如果在conftest中提取出一个login_driver，中间又涉及到页面对象中的方法，比较混杂
2. 多进程兼容性测试的时候不能截图，且测试报告展示问题
3. 缺少allure更美观的报告


  