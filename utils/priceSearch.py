from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

class CollectSample():
  
  def setup_method(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def collectDataSample(self,riven):
    self.driver.get("https://warframe.market/auctions")
    self.driver.set_window_size(1296, 696)
    self.driver.find_element(By.CSS_SELECTOR, ".real-input > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".real-input > input").send_keys(riven)
    self.driver.find_element(By.CSS_SELECTOR, ".real-input > input").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".my-auto > .small--_nJ6X:nth-child(2) > span").click()
    self.driver.find_element(By.ID, "auctions-search-sort").click()
    self.driver.find_element(By.ID, "auctions-search-sort").click()
    dropdown = self.driver.find_element(By.ID, "auctions-search-sort")
    dropdown.find_element(By.XPATH, "//option[. = 'Price (ascending)']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".auctions-search__find > div").click()

    WebDriverWait(self.driver, 10).until(
        EC.title_contains(riven)
    )
    
    prices = self.driver.find_elements(By.XPATH, "//b[@class='price']") 
    for price in prices:                                                
      print(price.text)                                                 

    return(prices)
