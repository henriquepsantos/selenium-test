from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://selenium-python.readthedocs.io/")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Getting Started')]")[0]
elemText = elem.text
elem.click()


conj = set(elemText)

if len(elemText) > len(conj):
    print("the sentence has duplicate letters")
else:
    print("the sentence has no duplicate letters") 

driver.close()
