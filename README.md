### 版本7.0
1. 新增了caps目录，使用其中的caps.yml实现desired_caps和server信息的配置化
2. 新增了测试报告和入口模块main.py
3. 新增了common目录下的conf_dir.py，实现了路径的参数化。同时由于在main.py方法中运行时，page_objects目录下的__init__.py中使用相对路径会报错，通过参数化绝对路径的形式解决了这一问题
4. 安装失败重试插件pytest-rerunfailures，尝试以三种方式运行失败重试
5. 在pageObjects下的__init__.py中新增清理测试报告的操作


### 缺点
1. test_invest.py中的登录步骤很重复，能否合并，如果在conftest中提取出一个login_driver，中间又涉及到页面对象中的方法，比较混杂
2. 缺少设置手势密码的方法操作
3. 缺少失败截图
4. 缺少命令行启动appium-server的方法操作
5. 缺少兼容性测试方法和操作
6. 缺少allure更美观的报告

  