from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = ""
password = ""
url = "https://blackboard.maltepe.edu.tr/"
analysis_course_url = "https://blackboard.maltepe.edu.tr/ultra/courses/_58063_1/outline"
python_course_url = "https://blackboard.maltepe.edu.tr/ultra/courses/_55516_1/outline"
driver_path = "chromedriver.exe"

def close_policy_popup():
    try:
        driver.find_element_by_class_name("locationPane")
        driver.find_element_by_id("agree_button").click()
    except:
        print("Policy pop-up does not exist")

def login():
    driver.find_element_by_id("user_id").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("entry-login").click()

def open_collaborate(lecture):
    if(lecture == "analysis"):
        url = analysis_course_url
    elif(lecture == "python"):
        url = python_course_url
    else:
        url = "https://google.com/"
    driver.get(url)
    try:
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#sessions-list-dropdown > .blue-link").click()
        driver.find_element(By.CSS_SELECTOR, "#sessions-list span").click()
        driver.switch_to.window(driver.window_handles[-1])
    except:
        print("hata")

def close_permisson_popup():
    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR, ".close:nth-child(5)").click()
        print("close 1")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#announcement-modal-page-wrap > .close").click()
        print("annuacement closed")
    except:
        print("permisson popup does not exist")

def open_students_page():
    try:
        driver.find_element(By.ID, "side-panel-open").click()
        print("Side panel open")
        time.sleep(3)
        driver.find_element(By.ID, "panel-control-participants").click()
        print("student page opens")
    except:
        print("student page couldnt open")        

def raise_your_hand():
    hand_raised_students = driver.find_elements(By.CLASS_NAME, "status-hand-raised")
    count = len(hand_raised_students)
    if (count > 10):
        driver.find_element(By.ID, "raise-hand").click()

with webdriver.Chrome(driver_path) as driver:
    username = input('Username: ')
    password = input('Password: ')
    print('1. Analysis')
    print('2. Python')
    choise = input('choise :')
    lecture = ''
    if (choise == 1):
        lecture = 'analysis'
    elif (choise == 2):
        lecture = 'python'
    else:
    driver.get(url)
    close_policy_popup()
    login()
    open_collaborate("analysis")
    time.sleep(10)
    close_permisson_popup()
    time.sleep(5)
    open_students_page()
    time.sleep(5)
    raise_your_hand()
    input()
    