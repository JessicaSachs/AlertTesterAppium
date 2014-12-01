from appium import webdriver
import time

# Need to set the path to app in server argument or in caps
# Assumes you have not set autoAcceptAlerts to true

caps = {
	'deviceName': 'iPhone Simulator',
	'platformName': 'iOS',
	'platformVersion': '8.1'
}

wd = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)

button = wd.find_element_by_accessibility_id('Tap me!')
button.click()

time.sleep(1)

print wd.page_source

alertButton = wd.find_element_by_accessibility_id('Thanks')
alertButton.click()

print 'Seems to have worked!'

wd.quit()