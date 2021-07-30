import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


opt = Options()
opt.add_argument('--headless')
driver = webdriver.Chrome(executable_path=data['DriverPath'], options=opt)

driver.get(data['BetaURL'])
elem = driver.find_element(By.XPATH, "//div[@class='beta-status']")
print(elem.text)
driver.close()
