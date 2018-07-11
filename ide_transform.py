from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pre-u.paiming.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/company/SiteIndex.aspx")
        driver.find_element_by_css_selector("#openSite > c").click()
        driver.find_element_by_link_text(u"提交新企业资料").click()
        driver.find_element_by_link_text(u"创建").click()
        driver.find_element_by_id("TB_name").clear()
        driver.find_element_by_id("TB_name").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("TB_short_name").click()
        driver.find_element_by_id("TB_short_name").clear()
        driver.find_element_by_id("TB_short_name").send_keys(u"简体中文基础资料")
        driver.find_element_by_css_selector("body.view").click()
        driver.find_element_by_id("addTrade").click()
        driver.find_element_by_xpath("(//p[@onclick='getCategory(this);'])[4]").click()
        driver.find_element_by_css_selector("li.add_search_tw_con_tj").click()
        driver.find_element_by_link_text(u"确认").click()
        driver.find_element_by_id("TB_main_word_1").clear()
        driver.find_element_by_id("TB_main_word_1").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("TB_main_word_2").clear()
        driver.find_element_by_id("TB_main_word_2").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("Fu_logo").clear()
        driver.find_element_by_id("Fu_logo").send_keys("C:\\Users\\pc\\Desktop\\267f9e2f07082838b5168c32b299a9014c08f1f9.jpg")
        driver.find_element_by_id("Fu_release_img").clear()
        driver.find_element_by_id("Fu_release_img").send_keys("C:\\Users\\pc\\Desktop\\tooopen_sy_188713354445.jpg")
        driver.find_element_by_id("wyzc_nex").click()
        driver.find_element_by_id("TB_corporation").clear()
        driver.find_element_by_id("TB_corporation").send_keys(u"简体中文基础资料")
        driver.find_element_by_link_text(u"请选择").click()
        driver.find_element_by_id("DL_company_type_3").click()
        driver.find_element_by_id("TB_company_address").clear()
        driver.find_element_by_id("TB_company_address").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("TB_company_create_time").click()
        driver.find_element_by_css_selector("td.WotherDayOn").click()
        driver.find_element_by_id("TB_business_licence").clear()
        driver.find_element_by_id("TB_business_licence").send_keys("54648")
        driver.find_element_by_id("TB_tax_registration").clear()
        driver.find_element_by_id("TB_tax_registration").send_keys("4564648")
        driver.find_element_by_id("TB_Business").clear()
        driver.find_element_by_id("TB_Business").send_keys(u"46864848648简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料简体中文基础资料")
        driver.find_element_by_id("TB_annual_survey_time").click()
        driver.find_element_by_id("TB_annual_survey_time").click()
        driver.find_element_by_css_selector("td.WotherDayOn").click()
        driver.find_element_by_id("wyzc_nex").click()
        driver.find_element_by_id("TB_contact").clear()
        driver.find_element_by_id("TB_contact").send_keys(u"简体中文基础资料")
        driver.find_element_by_css_selector("#DL_diplomaList > a.wyzc_select_title_one").click()
        driver.find_element_by_id("DL_diploma_3").click()
        driver.find_element_by_id("TB_email").clear()
        driver.find_element_by_id("TB_email").send_keys("12345648@qq.com")
        driver.find_element_by_link_text(u"大陆").click()
        driver.find_element_by_id("DL_mobile_1").click()
        driver.find_element_by_id("TB_mobile").clear()
        driver.find_element_by_id("TB_mobile").send_keys("61234567")
        driver.find_element_by_id("TB_phone2").clear()
        driver.find_element_by_id("TB_phone2").send_keys("56468")
        driver.find_element_by_id("TB_phone3").clear()
        driver.find_element_by_id("TB_phone3").send_keys("48846464")
        driver.find_element_by_id("TB_phone4").clear()
        driver.find_element_by_id("TB_phone4").send_keys("6488648")
        driver.find_element_by_css_selector("#DL_eara2List > a.wyzc_select_title_one").click()
        driver.find_element_by_id("DL_eara2_4").click()
        driver.find_element_by_css_selector("#DL_eara3List > a.wyzc_select_title_one").click()
        driver.find_element_by_id("DL_eara3_4").click()
        driver.find_element_by_css_selector("#DL_eara4List > a.wyzc_select_title_one").click()
        driver.find_element_by_id("DL_eara4_6").click()
        driver.find_element_by_id("TB_area").clear()
        driver.find_element_by_id("TB_area").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("TB_zip_code").clear()
        driver.find_element_by_id("TB_zip_code").send_keys("456464")
        driver.find_element_by_id("TB_domain").clear()
        driver.find_element_by_id("TB_domain").send_keys("4546.com")
        driver.find_element_by_id("TB_qq").clear()
        driver.find_element_by_id("TB_qq").send_keys("156484")
        driver.find_element_by_id("wyzc_nex").click()
        driver.find_element_by_link_text(u"提交").click()
        driver.find_element_by_id("department_name").clear()
        driver.find_element_by_id("department_name").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("Fhonour_img").clear()
        driver.find_element_by_id("Fhonour_img").send_keys("C:\\Users\\pc\\Desktop\\267f9e2f07082838b5168c32b299a9014c08f1f9.jpg")
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_link_text(u"提交").click()
        driver.find_element_by_id("department_name").clear()
        driver.find_element_by_id("department_name").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("Fhonour_img").clear()
        driver.find_element_by_id("Fhonour_img").send_keys("C:\\Users\\pc\\Desktop\\267f9e2f07082838b5168c32b299a9014c08f1f9.jpg")
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_link_text(u"提交").click()
        driver.find_element_by_id("department_name").clear()
        driver.find_element_by_id("department_name").send_keys(u"简体中文基础资料")
        driver.find_element_by_id("Fhonour_img").clear()
        driver.find_element_by_id("Fhonour_img").send_keys(u"C:\\Users\\pc\\Desktop\\微信图片_20170425104005.jpg")
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_id("_btnOK").click()
        driver.find_element_by_id("btnOK").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
