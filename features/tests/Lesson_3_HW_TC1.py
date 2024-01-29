# Lesson 2 Homework
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.amazon.com/ap/register?showRememberMe=true"
               "&openid.pape.max_auth_age=900&openid.return_to=https%3"
               "A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3"
               "D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedi"
               "rectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_Acc"
               "ountFlyout_signout&prevRID=2YJK1VCJHGEK4JFMZB30&openid"
               ".assoc_handle=usflex&openid.mode=checkid_setup&prepopu"
               "latedLoginId=&failedSignInCount=0&pageId=usflex&openid"
               ".ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    # Attempting to use CSS Selectors whenever possible as that's what was in the lesson
    print(driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']"))
    print(driver.find_element(By.CSS_SELECTOR, "div > div > h1.a-spacing-small")) # Not sure how else to select this element as it contained no real identifying attribute value
    print(driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name"))
    print(driver.find_element(By.CSS_SELECTOR, "input#ap_email"))
    print(driver.find_element(By.CSS_SELECTOR, "input#ap_password"))
    print(driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must be')]")) # Could not for the life of me figure out how to select this one using CSS Selectors
    print(driver.find_element(By.CSS_SELECTOR, "input#ap_password_check"))
    print(driver.find_element(By.CSS_SELECTOR, "input#continue.a-button-input")) # My Create Account page says to "Continue" here instead of "Create"
    print(driver.find_element(By.CSS_SELECTOR, "div#legalTextRow > a[href*='condition_of_use']"))
    print(driver.find_element(By.CSS_SELECTOR, "div#legalTextRow > a[href*='privacy_notice']"))
    print(driver.find_element(By.CSS_SELECTOR, "a[href*='signin']"))

    driver.quit()

main()