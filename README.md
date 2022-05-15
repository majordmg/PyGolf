# PyGolf

 _______            ______          __     ___
|_   __ \         .' ___  |        [  |  .' ..]
  | |__) |_   __ / .'   \_|   .--.  | | _| |_
  |  ___/[ \ [  ]| |   ____ / .'`\ \| |'-| |-'
 _| |_    \ '/ / \ `.___]  || \__. || |  | |
|_____| [\_:  /   `._____.'  '.__.'[___][___]
         \__.'

Automatically reserve golfing timeslots through Foreupsoftware. 

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

For example, the configuration below will register a tee time 4-9 AM, system time, at Bethpage State Park. 

config['am-pm'] = 'am'
config['max-hour'] = '4'
config['min-hour'] = '9'
config['site-url'] = 'https://foreupsoftware.com/index.php/booking/19765/2431#teetimes'

////
