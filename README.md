### 版本14.0
1. 基于pytest-xdist实现分布式APP自动化测试
2. 在Centos7下执行
3. 使用jenkins做持续集成，结合allure生成测试报告
4. 相关文章见：[博客园](https://www.cnblogs.com/my_captain/category/1752378.html)

### 缺点
1. test_invest.py中的登录步骤很重复,能否合并，如果在conftest中提取出一个login_driver，中间又涉及到页面对象中的方法，比较混杂


  