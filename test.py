from selenium import webdriver as wb
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = {
    'LoginInPage': 'https://login.taobao.com/member/login.jhtml',
    # 要秒杀的宝贝页面地址，根据需要进行替换
    'test': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.41.2e2f6941HuLj38&id=604693559175&ns=1&abbucket=6'
}

options = wb.ChromeOptions()
prefs = {
    "profile.managed_default_content_settings.images": 2,  # 无图模式
    'permissions.default.stylesheet': 2
}
options.add_experimental_option('prefs', prefs)  # 无图模式，如果启用后不加载二维码，请将此句注释掉
IE = wb.Chrome()
IE.maximize_window()
IE.get(url['LoginInPage'])  # 扫码登陆
time.sleep(10)
IE.get(url['test'])  # 访问你要秒杀的宝贝页面


def wait(method, xpath):  # 等待开抢标志出现
    while True:
        try:
            a = WebDriverWait(IE, 100, 0.01).until(
                EC.presence_of_element_located((method, xpath))).click()
            print('目标已找到')
            return a
        except TimeoutException or NoSuchElementException:
            print('你要的页面找不到了，刷新一下重试')


wait(By.ID, 'J_LinkBuy')
wait(By.CLASS_NAME, 'go-btn')