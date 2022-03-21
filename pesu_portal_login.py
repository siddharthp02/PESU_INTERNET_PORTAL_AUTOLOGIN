from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://192.168.254.1:8090/httpclient.html") #change the link to link you see on login if it doesn't work
SRN = "" #Enter SRN
username = browser.find_element_by_css_selector("#username")
username.send_keys(SRN)
password = browser.find_element_by_css_selector("#password")
password.send_keys(SRN)
sub = browser.find_element_by_css_selector("#loginbutton")
sub.click()
browser.quit()