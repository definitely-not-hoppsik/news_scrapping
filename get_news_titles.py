from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://www.bbc.com/news/world')
driver.implicitly_wait(5)
accept = driver.find_element_by_class_name('fc-button')
accept.click()

headlines_elements = driver.find_elements_by_class_name(
    'gs-c-promo-heading__title')
headlines_list = []
for element in headlines_elements:
    headlines_list.append(element.get_attribute('textContent'))

url_elements = driver.find_elements_by_class_name('gs-c-promo-heading')
url_list = []
for element in url_elements:
    url_list.append(element.get_attribute('href'))

zipped = set(zip(headlines_list, url_list))

with open('headlines_and_links.txt', 'w') as f:
    for line in zipped:
        f.write(str(line)+'\n')


driver.close()
