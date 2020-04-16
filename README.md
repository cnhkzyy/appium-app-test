### 版本2.0
1. 提取了公共的driver，但实例化时还是会创建多个driver
2. 实例化的driver变量要写在方法内，写在方法外仍然会报错


### 缺点
1. 一个测试方法创建一个新的driver，这样提取公共的方法换汤不换药
2. 分层设计不完善，代码和测试数据未分离
3. 页面的属性和方法和测试方法混杂在一起，代码可读性差，不太直观，维护起来也不容易


### 源码分析
在Common目录下定义base_driver时，有个如下图import的过程
```python
from appium import webdriver
```
经过查看源码，发现webdriver实际上是appium下的一个webdriver的包  
如果你在webdriver上按住Ctrl，会跳转到一个__init__.py的包文件
其源码如下：
__init__.py
```python
#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Appium Python Client: WebDriver module
"""

from .webdriver import WebDriver as Remote
from .webelement import WebElement
```
怎么理解这个```from .webdriver import WebDriver as Remote```呢？
如果查看源码的结构会发现是这样的：
```python
appium
    |__ webdriver
        |__ __init__.py
        |__ webdriver.py-->WebDriver类-->Remote
```
实际上，这个.webdriver就代表当前目录下的webdriver.py模块，从这个模块中导入WebDriver类，然后起了个别名Remote（Remote作为一个变量）
当Python首次导入某个目录时，会自动执行其目录下的__init__.py文件中的所有的程序代码。因此，这类文件自然就是放置在包下所需要的初始化代码的场所。例如，可以使用其初始化文件，来创建所需要的的数据文件，连接数据库等
实际上``from .webdriver import WebDriver as Remote```的作用就相当于：
```python
webdriver = appium/webdriver.py   #from语句在导入时会创建新变量webdriver
Remote = webdriver.WebDriver     #从变量webdriver中，加载模块的一部分WebDriver，并赋值给新变量Remote
```
在导入包后，会返回一个模块对象，此对象的命名空间内包含着webdriver的__init__.py文件所赋值的所有变量名，因此，我们可以使用webdriver.Remote调用WebDriver类
实际上，这个webdriver，就是一个名字为__init__.py的变量，直接指向模块对象





