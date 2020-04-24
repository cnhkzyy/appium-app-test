from common.base_driver import BaseDriver
import pytest
import allure

driver = None


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default=None, help=None)



@pytest.fixture
def cmdopt(pytestconfig):
    #两种写法
    #return pytestconfig.getoption("--cmdopt")
    return pytestconfig.option.cmdopt




#定义公共的fixture
@pytest.fixture
def common_driver(cmdopt):
    global driver
    base_driver = BaseDriver(eval(cmdopt))
    driver = base_driver.base_driver()
    yield driver
    driver.close_app()
    driver.quit()


#定义含有toast弹框的fixture
@pytest.fixture
def common_toast_driver(cmdopt):
    global driver
    base_driver = BaseDriver(eval(cmdopt))
    driver = base_driver.base_driver(automationName="UIAutomator2")
    yield driver
    driver.close_app()
    driver.quit()




#失败自动截图，展示到html报告中
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    #pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            if file_name:
                with allure.step("添加失败截图"):
                    allure.attach(_capture_screenshot(), "失败截图", allure.attachment_type.PNG)
            #screen_img = _capture_screenshot()
        #     if file_name:
        #         html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
        #                'onclick="window.open(this.src)" align="right"/></div>' % screen_img
        #         extra.append(pytest_html.extras.html(html))
        # report.extra = extra


#截图保存为base_64，展示在html中
def _capture_screenshot():
    return driver.get_screenshot_as_png()
    #return driver.get_screenshot_as_base64()
