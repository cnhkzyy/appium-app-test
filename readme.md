### 版本5.0
1. 新增conftest.py，编写了公共的fixture，实例化driver对象并返回，以供测试方法在运行时使用
2. 新增了test_login.py模块中的异常用例
3. 完善了获取toast的公共方法和fixture


### 缺点
数据和方法对象未分离，直接写死在测试方法中


### 编写思路
如果这样写，又会出现driver对象覆盖的问题：
```test_welcome.py```
```python
...

driver = BaseDriver().base_driver()
welcome_page = WelcomePage(driver)


#测试首页滑屏
@pytest.mark.welcome
def test_welcome():
    welcome_page.swipe_screen()
    welcome_page.get_spe_screenshot()
    image_text = welcome_page.identify_screenshot()
    assert image_text == "立即体验"
...
```
```test_login.py```
```python
...

driver = BaseDriver().base_driver()
welcome_page = WelcomePage(driver)
login_page = LoginPage(driver)
index_page = IndexPage(driver)
user_info_page = UserInfoPage(driver)


@pytest.mark.login
def test_login_success():
    welcome_page.swipe_screen()
    welcome_page.click_experience_now()
    login_page.click_register_login()
    login_page.input_phone("18684720553")
    login_page.input_pwd("python")
    index_page.click_later()
    index_page.click_me()
    nickName = user_info_page.get_nickName()
    user_info_page.quit()
    assert nickName == "华华"
...
```