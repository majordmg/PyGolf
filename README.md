# PyGolf

```
 ____  __ __  ____  ___  _     _____ 
|    \|  |  |/    |/   \| |   |     |
|  o  |  |  |   __|     | |   |   __|
|   _/|  ~  |  |  |  O  | |___|  |_  
|  |  |___, |  |_ |     |     |   _] 
|  |  |     |     |     |     |  |   
|__|  |____/|___,_|\___/|_____|__|   

Automate golf tee time reservations through foreupsoftware.com

```              

Create a config.json and create the following fields:
```
logging.debug('reading config file')
f = open('./config.json', 'r').read()
config = json.loads(f)
driver_path = config['chromedriver'] # "/usr/bin/chromedriver"
username = config['username']
password = config['password']
headless_int = config['headless']
min_hour = config['min-hour']
max_hour = config['max-hour']
site-url = config['site-url']
am_pm = config['am-pm']
```

The time-related fields in the config are the parameters under which the reservation will be made. 

For example, the configuration below will register a tee time 4-9 AM, system time, at Bethpage State Park:

```
config['am-pm'] = 'am'
config['max-hour'] = '4'
config['min-hour'] = '9'
config['site-url'] = 'https://foreupsoftware.com/index.php/booking/19765/2431#teetimes'
```

