from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://uta.pw/sakusibbs/post.php?mml_id= 35'
driver.get(url)

e = driver.find_element_by_class_name('posttitle')
print(e.text)

driver.close()