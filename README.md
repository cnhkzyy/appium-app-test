### 版本4.0
1. 采用PageObject模式，将页面属性方法和测试方法分离，降低了代码的耦合性，提高了可读性，易于理解和维护
2. 使用BasePage类抽离出了公共的driver和方法，其他页面对象通过继承BasePage类来继承其driver和方法
3. 在PageObjects包的__init__.py中导入所有模块下面的方法，这样只需在测试类中，导入PageObjects包下的所有属性和方法(```from PageObjects import *```)，就可以直接使用各个页面对象类，节约了代码量



### 缺点
目前是页面对象类继承BasePage类，而BasePage类中初始化的公共driver存在一定的问题：比如A页面继承BasePage类，B也继承BasePage类，初始化的driver只有一份，当A对应的测试类执行完，此时driver的状态已不是初始状态，所以B对应的测试类的执行会出现问题。
为了保证driver的"干净"，最好一个用例开始前初始化一份，然后用例结束后释放driver。所以之前提到的一直都是要同一个drivert的方法不可取



### 源码分析
在编写BasePage中的方法时，看见了这么一句```WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((by, locator)))```
查看源码类```visibility_of_element_located```如下：
```python
    class visibility_of_element_located(object):
         def __init__(self, locator):
            self.locator = locator

         def __call__(self, driver):
            try:
                return _element_if_visible(_find_element(driver, self.locator))
            except StaleElementReferenceException:
                return False
```
```__call__```的作用是，让实例对象也像函数一样作为可调用对象来用
visibility_of_element_located()
具体分析内容：https://www.cnblogs.com/my_captain/p/12706472.html