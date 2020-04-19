### 版本10.0
1. 新增失败截图
2. 修改test_html_reports目录名字为html_reports


### 缺点
1. test_invest.py中的登录步骤很重复,能否合并，如果在conftest中提取出一个login_driver，中间又涉及到页面对象中的方法，比较混杂
2. 缺少命令行启动appium-server的方法操作
3. 缺少兼容性测试方法操作
4. 缺少allure更美观的报告


  