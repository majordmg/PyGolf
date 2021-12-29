from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

driver.get("https://foreupsoftware.com/index.php/booking/20330/4502#/teetimes")

login_btn = driver.find_elements_by_class_name("login")[0]
login_btn.click()

username = "danjaaron@gmail.com"
password = "JUQ_cbp@wtj3tvb-bwf"

email_field = driver.find_element_by_name("email")
email_field.send_keys(username)
pass_field = driver.find_element_by_name("password")
pass_field.send_keys(password)


driver.find_element_by_xpath("//button[text()='Log In']").click()


#driver.find_element_by_xpath("//a[text()='Reserve a time now.']").click()
#profile-main > div > ul > li > a

import time
time.sleep(1)
al = driver.find_elements_by_xpath("//a[contains(text(), '')]")[-1]
print(al.text)
al.click()

driver.find_element_by_xpath("//button[text()='Los Verdes Public Times']").click()

def get_tmrw_btn():
    btns = driver.find_elements_by_xpath("//button")
    tmrw_btn = [b for b in btns if b.text == ">"][0]
    return tmrw_btn

def get_latest_day():
    latest = driver.find_elements_by_xpath("//option")[-1]
    return latest 

def get_all_times():
    times = driver.find_elements_by_class_name("start")
    return [t.text for t in times]

# get next day button
no_button = True
while no_button:
    try:
        tmrw_btn = get_tmrw_btn()
    except:
        time.sleep(1)
        continue
    no_button = False

# get to the latest day
for i in range(14):
    tmrw_btn.click()
time.sleep(2)

from collections import Counter 
recorded_days = {}
ctr_dict = {}

while True:
    tmrw_btn.click()
    latest_day = get_latest_day()
    lt = get_all_times()
    if not latest_day.text in recorded_days:
        recorded_days[latest_day.text] = []
        print("\nGot new day: ", latest_day.text)
        print("\n")
        recorded_days[latest_day.text].extend(lt)
        print(recorded_days)
        print("\n")
        ctr_dict[latest_day.text] = Counter()
    time.sleep(1)
