from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.python.org/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_name(name="q").send_keys("bla bla")
driver.find_element_by_id(id_="submit").click()
print(driver.find_element("xpath",'//*[@id="content"]/div/section/form/ul/p').text)
print (driver.title)
print (driver. current_url)
time.sleep(5)
driver.close()





driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.python.org/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_name(name="q").send_keys("bla bla")
driver.find_element_by_id(id_="submit").click()
print(driver.find_element("xpath",'//*[@id="content"]/div/section/form/ul/p').text)
print (driver.title)
print (driver. current_url)
time.sleep(5)
driver.close()



