from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By


username_input = input("Student ID: ")
password_input = input("Password: ")
ch_options = webdriver.ChromeOptions()
ch_options.add_argument("--headless")
ch_options.add_argument("window-size=1920x3000");
ch_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15")
browser = webdriver.Chrome(options=ch_options)

browser.get('https://sydneystudent.sydney.edu.au/sitsvision/wrd/siw_lgn')

ID = browser.find_element(by=By.ID, value='MUA_CODE.DUMMY.MENSYS')
password = browser.find_element(by=By.ID, value='PASSWORD.DUMMY.MENSYS')
ID.send_keys(username_input)
password.send_keys(password_input)
buttom = browser.find_element(by=By.NAME, value='BP101.DUMMY_B.MENSYS')
buttom.click()

results = browser.find_element(by=By.XPATH, value='//*[@id="RESULTS"]')

results.click()

tree = etree.HTML(browser.page_source)
mark = tree.xpath('//table[@class="sv-table sv-table-striped"]/tbody/tr/td[4]/text()')
credit = tree.xpath('//table[@class="sv-table sv-table-striped"]/tbody/tr/td[6]/text()')
for i in range(len(mark)):
    mark[i] = float(mark[i].strip())
    credit[i] = float(credit[i].strip())

tmp = 0
for i in range(len(mark)):
    tmp += mark[i] * credit[i]

total = float(tree.xpath('/html/body/div/div[3]/div/div/div[4]/div/div/div[2]/table/tbody/tr[11]/td[2]/text()')[0].strip())

print('WAM: ' + str(tmp / total))

browser.quit()