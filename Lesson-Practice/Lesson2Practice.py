# 01/20/2024 Lesson 2 Lesson-Practice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

search_dropdown_by_id = driver.find_element(By.ID,'searchDropdownBox')
search_box_by_xpath = driver.find_element(By.XPATH,'//input[@aria-label="Search Amazon"]')
search_box_by_xpath2 = driver.find_element( By.XPATH,"//select[@aria-describedby='searchDropdownDescription' and "
                                            "@data-nav-digest='/Z5mo/vEI3mGCoNJKb6dSkA7k4g=' and "
                                            "@title='Search in']")
