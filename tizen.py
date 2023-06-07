from appium import webdriver
from time import sleep

API_KEY = 'your api key here'

_PAO_SERVER = f'https://dev-us-pao-7.headspin.io:7303/v0/{API_KEY}/wd/hub'
_PAO_UDID = '087K3CTN7004332'

_SERVER = _PAO_SERVER
_UDID = _PAO_UDID

caps = {
  "appium:udid": _UDID,
  "appium:deviceName": _UDID,
  "platformName": "tizentv",
  "appium:appPackage": "org.tizen.globoplayapp",
  "appium:rcOnly": True,
  "appium:newCommandTimeout": 120,
  "appium:automationName": "tizentv"
}

driver = webdriver.Remote(
  command_executor=_SERVER,
  desired_capabilities=caps
)

print('driver started')

# From the 'Inicio' page steps to navigate to log in
print('LEFT')
driver.execute_script("tizen: pressKey", {"key": "KEY_LEFT"})
sleep(1)

print('DOWN')
driver.execute_script("tizen: pressKey", {"key": "KEY_DOWN"})
sleep(1)

print('DOWN')
driver.execute_script("tizen: pressKey", {"key": "KEY_DOWN"})
sleep(1)

print('DOWN')
driver.execute_script("tizen: pressKey", {"key": "KEY_DOWN"})
sleep(1)

print('DOWN')
driver.execute_script("tizen: pressKey", {"key": "KEY_DOWN"})
sleep(1)

print('ENTER')
driver.execute_script("tizen: pressKey", {"key": "KEY_ENTER"})
sleep(1)

print('RIGHT')
driver.execute_script("tizen: pressKey", {"key": "KEY_RIGHT"})
sleep(1)

print('ENTER')
driver.execute_script("tizen: pressKey", {"key": "KEY_ENTER"})
sleep(1)

driver.get_screenshot_as_file('Login.png')

sleep(5)
# From login navigate back to 'Inicio'

print('LEFT')
driver.execute_script("tizen: pressKey", {"key": "KEY_LEFT"})
sleep(1)

print('ENTER')
driver.execute_script("tizen: pressKey", {"key": "KEY_ENTER"})
sleep(1)

print('LEFT')
driver.execute_script("tizen: pressKey", {"key": "KEY_LEFT"})
sleep(1)

print('LEFT')
driver.execute_script("tizen: pressKey", {"key": "KEY_LEFT"})
sleep(1)

print('UP')
driver.execute_script("tizen: pressKey", {"key": "KEY_UP"})
sleep(1)

print('UP')
driver.execute_script("tizen: pressKey", {"key": "KEY_UP"})
sleep(1)

print('UP')
driver.execute_script("tizen: pressKey", {"key": "KEY_UP"})
sleep(1)

print('UP')
driver.execute_script("tizen: pressKey", {"key": "KEY_UP"})
sleep(1)

print('ENTER')
driver.execute_script("tizen: pressKey", {"key": "KEY_ENTER"})
sleep(1)

sleep(5)
driver.quit()
print('driver quit')
