### 版本3.0
1. 使用了pytesseract和PIL截取并识别图片中的文字，来做首页的断言
2. 在Images的__init__.py中，初始化了清理图片的操作，在PageObjects的__init__.py中，初始化了清理缓存的操作
3. 添加了pytest.ini配置文件，用来解决PytestUnknownMarkWarning警告


### 缺点
1. 一个测试方法创建一个新的driver，造成资源的浪费，能否用同一个driver替代
2. 分层设计不完善，代码和测试数据未分离
3. 页面的属性和方法和测试方法混杂在一起，代码可读性差，不太直观，维护起来也不容易
