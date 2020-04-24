### 版本11.0
1. docker容器多进程并发运行测试用例
2. 由于centos7下tesseract-ocr配置有问题，因此修改test_welcome.py的测试用例
3. 使用dcoker运行appium-server时，要用```docker appium_1```，不能使用```docker logs -f appium_1```打印实时日志，否则窗口不会执行后面的操作


### 缺点
1. test_invest.py中的登录步骤很重复,能否合并，如果在conftest中提取出一个login_driver，中间又涉及到页面对象中的方法，比较混杂
2. 多进程兼容性测试测试报告展示问题
3. 缺少allure更美观的报告


  