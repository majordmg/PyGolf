import logging
import json 
import time
import sys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from collections import Counter 

ts = int(time.time())
logname = "{}.log".format(ts)
logging.basicConfig(handlers=[logging.FileHandler(filename=logname,
                                                 encoding='utf-8', mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)

logging.debug('reading config file')
f = open('./config.json', 'r').read()
config = json.loads(f)
driver_path = config['chromedriver'] # "/usr/bin/chromedriver"
username = config['username']
password = config['password']
headless_int = config['headless']
min_hour = config['min-hour']
max_hour = config['max-hour']
am_pm = config['am-pm']


# generate target hours 
poss_hours = list([str(h)+":" for h in range(int(min_hour), int(max_hour)+1)])
print("search for: ", poss_hours)

chrome_options = Options()
if bool(int(headless_int)):
    chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
driver.get("https://foreupsoftware.com/index.php/booking/20330/4502#/teetimes")

login_btn = driver.find_elements_by_class_name("login")[0]
login_btn.click()

email_field = driver.find_element_by_name("email")
email_field.send_keys(username)
pass_field = driver.find_element_by_name("password")
pass_field.send_keys(password)


driver.find_element_by_xpath("//button[text()='Log In']").click()


#driver.find_element_by_xpath("//a[text()='Reserve a time now.']").click()
#profile-main > div > ul > li > a

time.sleep(1)
al = driver.find_elements_by_xpath("//a[contains(text(), '')]")[-1]
logging.info('found {}'.format(al.text))
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
    """ Returns time elements.
    """
    times = driver.find_elements_by_class_name("start")
    return times 

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

recorded_days = {}
ctr_dict = {}

while True:
    tmrw_btn.click()
    try:
        latest_day = get_latest_day()
        times = get_all_times()
        logging.info('opening all times')
        lt = [(t.text, t) for t in times]
        ltt = [k[0] for k in lt]
    except Exception as e:
        logging.error(e)
        logging.info('presumed stale element - continuing')
        continue 
    if not latest_day.text in recorded_days:
        # record new day 
        recorded_days[latest_day.text] = []
        logging.info("Got new day: {}".format(latest_day.text))
        recorded_days[latest_day.text].extend(ltt)
        logging.info(str(recorded_days))
        # find target hour 
        for time_tuple in lt:
            time_str, time_elem = time_tuple 
            if not str(am_pm) in time_str:
                logging.info('skipping {}'.format(time_str))
            for poss_h in poss_hours:
                if poss_h in time_str:
                    logging.info('time found - {} in {}'.format(poss_h, time_str))
                    time_elem.click()
                    logging.info('clicked {} and breaking'.format(time_str))
                    sys.exit() 
        
    time.sleep(1)
