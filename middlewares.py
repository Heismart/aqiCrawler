# -*- coding: utf-8 -*-


from scrapy.http import HtmlResponse
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if "month=" in request.url:
            # driver = webdriver.Chrome(executable_path="F:\work_software\chromedriver\chromedriver.exe")
            opt = webdriver.ChromeOptions()
            opt.set_headless()
            driver = webdriver.Chrome(options=opt, executable_path="F:\work_software\chromedriver\chromedriver.exe")
            driver.get(request.url)
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
                )
                html = driver.page_source
                return HtmlResponse(url=request.url, body=html, encoding='utf-8', request=request)
            except Exception as e:
                print(e)
            finally:
                driver.quit()


