from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
import time

URL = "https://www.facebook.com/"

def main():
	chromedriver_autoinstaller.install()
	chrome_options = Options()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs",prefs)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(URL)
	time.sleep(2)

	driver.find_element(By.ID, "email").send_keys('01615124300') 
	time.sleep(2)
	driver.find_element(By.ID, "pass").send_keys('01876644aA@')
	time.sleep(2)

	login=driver.find_element(By.NAME, "login").click()

	time.sleep(60)
	driver.get('https://www.facebook.com/profile.php?id=100006187035221') 
	time.sleep(4)
	profile_btn = WebDriverWait(driver, 20).until(
		EC.element_to_be_clickable((
			By.XPATH,
			"//div[@role='button' and @aria-label='Profile settings see more options']"
			))
		)
	profile_btn.click()

	report_item = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((
					By.XPATH,
					"//div[@role='menuitem' and .//div[normalize-space()='Report profile']]"
			))
	)

	ActionChains(driver)\
			.move_to_element(report_item)\
			.pause(0.3)\
			.click()\
			.perform()

	print("🟢 Click action sent to Report profile")

	something_about_profile =WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((
					By.XPATH,
					"//div[@role='dialog']//div[@role='button' and .//div[normalize-space()='Something about this profile']]"
			))
	)

	ActionChains(driver)\
			.move_to_element(something_about_profile)\
			.pause(0.3)\
			.click()\
			.perform()

	print("🟢 Clicked: Something about this profile")

	under_18_btn = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((
					By.XPATH,
					"//div[@role='dialog']//div[@role='button' and "
					".//div[normalize-space()='Problem involving someone under 18']]"
			))
	)

	ActionChains(driver)\
			.move_to_element(under_18_btn)\
			.pause(0.3)\
			.click()\
			.perform()

	print("🟢 Clicked: Problem involving someone under 18")

	nude_images = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((
					By.XPATH,
					"//div[normalize-space()='Seems like sexual exploitation']/ancestor::div[@role='button']"
			))
	)
	print("🟢 Clicked: Sharing someone’s nude images")

	ActionChains(driver)\
			.move_to_element(nude_images)\
			.pause(0.3)\
			.click()\
			.perform()

	print("🟢 Clicked: Problem involving someone under 18")
	submit_report = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((
					By.XPATH,
					 "//div[@role='dialog']//div[@role='button' and @aria-label='Submit']"
			))
	)
	print("🟢 Clicked: submit_report")

	ActionChains(driver)\
			.move_to_element(submit_report)\
			.pause(0.3)\
			.click()\
			.perform()

	print("🟢 Clicked: submit button")

if __name__ == "__main__":
    main()

class ActionChains(webdriver.ActionChains):
		def pause(self, seconds):
				self._actions.append(lambda: time.sleep(seconds))
				return self
