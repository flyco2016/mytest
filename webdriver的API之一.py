from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()  # 打开浏览器，生产一个浏览器实例
driver.get("https://www.python.org")    # 打开网页
driver.maximize_window()

print(driver.title)    # 标题属性
print("baidu" in driver.title)
print(driver.current_url)

elem1 = driver.find_element_by_id("id-search-field") # by id
print(elem1)
elem1.send_keys("selenium")

sleep(5)
elem1.clear()
                                  
elem2 = driver.find_element_by_name("q")    # by name 与上面一样定位到同一元素，                                            # 地址是一样的
print(elem2)
elem2.send_keys("numpy")

button_elem = driver.find_element_by_class_name("search-button")
button_elem.click()
driver.back()
driver.forward()
#driver.close()

elem3 = driver.find_element_by_tag_name("meta")
print(elem3.id, elem3.size)    # 相同的标签名字时，返回第一个标签的内容



    






                                  
