from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

YOUR_EMAIL = "your_email"
YOUR_PASSWORD = "your_password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3754591626&geoId=90000084&keywords=software%20engineer&location=San%20Francisco%20Bay%20Area&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
time.sleep(2)

# Click Sign in button
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

# Sign in
email = driver.find_element(By.ID, value="username")
email.send_keys(YOUR_EMAIL)
password = driver.find_element(By.ID, value="password")
password.send_keys(YOUR_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(3)

# Get listings
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    # Try to save
    try:
        save = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
        save.click()
    except NoSuchElementException:
        print("No save button, skipped.")
        continue

time.sleep(5)
driver.quit()
