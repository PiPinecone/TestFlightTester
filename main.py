import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Definitions
Bclosed = "This beta is full."

# Yaml config loading
with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


# Configuring webdriver
opt = Options()
opt.add_argument('--headless')
driver = webdriver.Chrome(executable_path=data['DriverPath'], options=opt)


# Determining whether the beta is open or closed
driver.get(data['BetaURL'])
stat = driver.find_element(By.XPATH, "//div[@class='beta-status']").text

if stat == Bclosed:
    print("Beta full")
    # Add more code to execute
else:
    print("Beta open")
    # Add more code to execute
driver.close()
