

# NOTE_-----> READ THE FILE (README.md) AND THEN SCRAP THIS SITE



from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
 
options = ChromeOptions()
options.add_argument("--start-maximized")
 
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.linkedin.com")
driver.maximize_window()
 
user_name = driver.find_element(By.ID, 'session_key')
user_name.send_keys('YOUR NAME')
 
password = driver.find_element(By.ID, 'session_password')
password.send_keys('YOUR PASSWORD')
 
sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]').click()
 
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3789548015&keywords=python&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")
 
time.sleep(60)
 
jobs = driver.find_elements(By.CLASS_NAME, "disabled.ember-view.job-card-container__link.job-card-list__title")
 
role = []
 
for job in jobs:
    role.append(job.text)

 
print(role)
print()
print(len(role))

location =driver.find_element(By.CLASS_NAME,"")#fill out the class name by clicking inspect option

loc = []
 
for job in jobs:
    loc.append(job.text)

 
print(loc)
print()
print(len(loc))

location =driver.find_element(By.CLASS_NAME,"")#fill out the class name by clicking inspect option

com= []
 
for job in jobs:
    com.append(job.text)

 
print(com)
print()
print(len(com))




 

 
driver.quit()