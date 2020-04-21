from .base_page import BasePage
#import pytesseract
#from PIL import Image
from common.conf_dir import images_dir
#import images
import time


class WelcomePage(BasePage):

    #配置tessdata目录路径
    #tessdata_dir_config = '--tessdata-dir "D:/program/Tesseract-OCR/tessdata"'

    #元素定位
    experience_now_id = "com.xxzb.fenwoo:id/btn_start"

    #滑屏
    def swipe_screen(self):
        time.sleep(1.5)
        size = self.driver.get_window_size()
        for i in range(3):
            self.swipe(0.9, 0.5, 0.1, 0.5, size)


    #截取特定区域的图片
    # def get_spe_screenshot(self, x1=180/720, y1=1176/1280, x2=539/720, y2=1235/1280, name_1=1, name_2=2):
    #     #截取整张图并保存
    #     self.driver.get_screenshot_as_file(f"{images_dir}/{name_1}.png")
    #     image = Image.open(f"{images_dir}/{name_1}.png")
    #
    #     #截取部分图片并保存
    #     size = self.driver.get_window_size()
    #     region = (x1 * size["width"], y1 * size["height"], x2 * size["width"], y2 * size["height"])
    #     area = image.crop(region)
    #     area.save(f"{images_dir}/{name_2}.png")
    #     time.sleep(3)


    #识别图片
    # def identify_screenshot(self, name=2):
    #     image = Image.open(f"{images_dir}/{name}.png")
    #     image_text = pytesseract.image_to_string(image, lang="chi_sim", config=self.tessdata_dir_config)
    #     return image_text


    #点击立即体验
    def click_experience_now(self):
        self.get_element(self.experience_now_id).click()




