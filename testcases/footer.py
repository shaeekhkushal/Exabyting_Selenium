import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_footer():
    driver.maximize_window()
    driver.get("https://exabyting.com/")
    time.sleep(2)

    try:

        # Footer Fin tech Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_fin_tech = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[1]/div/div[2]/div/ul/li[1]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_fin_tech.text)
        time.sleep(1)
        click_on_footer_fin_tech.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer health tech Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_health_tech = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[1]/div/div[2]/div/ul/li[2]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_health_tech.text)
        time.sleep(1)
        click_on_footer_health_tech.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer ad tech Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_ad_tech = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[1]/div/div[2]/div/ul/li[3]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_ad_tech.text)
        time.sleep(1)
        click_on_footer_ad_tech.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer Process Automation Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_process_automation = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[1]/div/div[2]/div/ul/li[4]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_process_automation.text)
        time.sleep(1)
        click_on_process_automation.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer About Us Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_about_us = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[2]/div/div[2]/div/ul/li[1]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_about_us.text)
        time.sleep(1)
        click_on_footer_about_us.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer Join Us Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_joinn_us = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[2]/div/div[2]/div/ul/li[2]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_joinn_us.text)
        time.sleep(1)
        click_on_footer_joinn_us.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer Contact Us Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_contact_us = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[2]/div/div[2]/div/ul/li[3]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_contact_us.text)
        time.sleep(1)
        click_on_footer_contact_us.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer Our Expertise Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_our_expertise = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[3]/div/div[2]/div/ul/li[1]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_our_expertise.text)
        time.sleep(1)
        click_on_footer_our_expertise.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Footer Development Practises Menu Test Execution

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click_on_footer_development_practise = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/footer/div/div/div/section[1]/div/div[3]/div/div[2]/div/ul/li[2]/a/span')))
        time.sleep(1)
        print("Footer Navigation Text:", click_on_footer_development_practise.text)
        time.sleep(1)
        click_on_footer_development_practise.click()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

    finally:
        driver.quit()


verify_footer()
