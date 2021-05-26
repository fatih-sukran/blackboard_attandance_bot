
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOed():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_oed(self):
    self.driver.get("https://blackboard.maltepe.edu.tr/ultra/stream")
    self.driver.set_window_size(1920, 1040)
    self.driver.find_element(By.LINK_TEXT, "Dersler").click()
    element = self.driver.find_element(By.LINK_TEXT, "Organizasyonlar")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.ID, "course-link-_58039_1")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, "#course-link-_55516_1 > .js-course-title-element").click()
    self.driver.find_element(By.CSS_SELECTOR, "#sessions-list-dropdown > .blue-link").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#sessions-list span").click()
    self.vars["win6908"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win6908"])
    self.driver.find_element(By.CSS_SELECTOR, ".launch-failure").click()
    self.driver.find_element(By.CSS_SELECTOR, ".launch-failure").click()
    self.driver.switch_to.window(self.vars["root"])
  
