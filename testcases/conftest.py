from Common.base_driver import BaseDriver
import pytest



#定义公共的fixture
@pytest.fixture
def common_driver():
    driver = BaseDriver().base_driver()
    yield driver
    driver.close_app()
    driver.quit()


#定义含有toast弹框的fixture
@pytest.fixture
def common_toast_driver():
    driver = BaseDriver().base_driver(automationName="UIAutomator2")
    yield driver
    driver.close_app()
    driver.quit()
