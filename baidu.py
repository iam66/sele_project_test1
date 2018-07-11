from selenium import webdriver
driver=webdriver.Ie()#浏览器一定要装在C盘
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
driver.quit()
E:\python_practice\baidu.py