from Common.base_driver import BaseDriver
import time
import pytesseract
from PIL import Image
import Images


class WelcomePage:

    #初始化Driver
    driver = BaseDriver().base_driver()

    #元素定位
    experience_now_id = "com.xxzb.fenwoo:id/btn_start"

    tessdata_dir_config = '--tessdata-dir "D:/program/Tesseract-OCR/tessdata"'

    #滑屏
    def swipe_screen(self):
        #等待2s
        time.sleep(2)
        #获取屏幕尺寸
        size = self.driver.get_window_size()
        for i in range(3):
            #向左滑动
            #swipe还有一个参数duration，单位是ms，防止操作过快
            self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.1)
            time.sleep(0.5)


    #截取特定区域的图片
    def get_spe_screenshot(self, x1=180/720, y1=1176/1280, x2=539/720, y2=1235/1280, name_1=1, name_2=2):
        #截取整张图并保存
        self.driver.get_screenshot_as_file("E:/virtual_workshop/APP_AutoTest/Images/{0}.png".format(name_1))
        image = Image.open("E:/virtual_workshop/APP_AutoTest/Images/{0}.png".format(name_1))

        #截取部分图片并保存
        size = self.driver.get_window_size()
        region = (x1 * size["width"], y1 * size["height"], x2 * size["width"], y2 * size["height"])
        area = image.crop(region)
        area.save("E:/virtual_workshop/APP_AutoTest/Images/{0}.png".format(name_2))
        time.sleep(3)


    #识别图片
    def identify_screenshot(self, name=2):
        image = Image.open("E:/virtual_workshop/APP_AutoTest/Images/{0}.png".format(name))
        image_text = pytesseract.image_to_string(image, lang="chi_sim", config=self.tessdata_dir_config)
        return image_text


    #点击立即体验
    def click_experience_now(self):
        self.driver.find_element_by_id(self.experience_now_id).click()




