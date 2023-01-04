# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_openongv =' "chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\chromedata" '
# opt = Options()
# opt.add_experimental_option('debuggerAddress', 'localhost:8989')
# driver = webdriver.Chrome(executable_path='chromedriver.exe')

# driver.implicitly_wait(5)
# # driver.maximize_window()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-popup-blocking")

# #current window
# first_tab = driver.window_handles[0]
# #create new tab
# driver.execute_script("window.open()")
# #move to new tab
# new_tab = driver.window_handles[1]
# driver.switch_to.window(new_tab)
# driver.get('https://classroom.btu.edu.ge/ge/student/resume/personal')
# from selenium.webdriver.common.action_chains import ActionChains

# # button = driver.find_element_by_class_name('user-change-photo')
# # driver.implicitly_wait(10)
# # ActionChains(driver).move_to_element(button).click(button).perform()

# driver.find_element_by_name('photo_title').send_keys('a')
# driver.find_element_by_name('home_phone_number').send_keys('a')
# sub = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
# driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(sub).click(sub).perform()

# # sub.click()
# # driver.find_element_by_link_text('რეზიუმე').click()
# # driver.find_element_by_class_name('btn-primary').click()
# # driver.find_element_by_class_name('btn-primary').click()
# # driver.find_element_by_class_name('photo').click() 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
   
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "/home/nika/Documents/my_projects/install/geckodriver"
driver = webdriver.Firefox(chrome_driver, chrome_options=chrome_options)
print(driver.title)