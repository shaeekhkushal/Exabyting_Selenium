import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_header():
    driver.maximize_window()
    driver.get("https://exabyting.com/")
    time.sleep(5)

    try:
        # Print title and the URL

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "title")))
        title = driver.title
        current_url = driver.current_url
        print("Current Title is:", title)
        print("Current URL is:", current_url)

        # Click on the LOGO

        logo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[1]/div/div[1]/div/div/div/a/img")))
        logo.click()
        time.sleep(3)
        if driver.current_url == "https://exabyting.com/":
            print("Logo redirection test passed - redirected to correct page")
        else:
            print("Logo redirection test failed - redirection to incorrect page")

        # Service menu Test execute

        hover_on_services = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-20"]/a')))
        action = ActionChains(driver)
        print("hover_on_services is:", hover_on_services.text)
        action.move_to_element(hover_on_services).perform()
        time.sleep(1)

        click_on_our_expertise = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-mega-content-20"]/div/section[1]/div/div/div/section/div/div[2]/div/div[1]/div/div/a/span/span')))
        time.sleep(1)
        print("First Navigation Text:", click_on_our_expertise.text)
        time.sleep(1)
        action.click(click_on_our_expertise).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        hover_on_services = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-20"]/a')))
        action = ActionChains(driver)
        print("hover_on_services is:", hover_on_services.text)
        action.move_to_element(hover_on_services).perform()
        time.sleep(1)

        click_on_devlopment_practice = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-mega-content-20"]/div/section[2]/div/div/div/section/div/div[2]/div/div[1]/div/div/a/span/span')))
        time.sleep(1)
        print("Second Navigation Text:", click_on_devlopment_practice.text)
        time.sleep(1)
        action.click(click_on_devlopment_practice).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Industries menu test execute

        hover_on_industry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-21"]/a')))
        action = ActionChains(driver)
        print("hover_on_industry is:", hover_on_industry.text)
        action.move_to_element(hover_on_industry).perform()
        time.sleep(1)

        click_on_fin_tech = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-mega-content-21"]/div/section[1]/div/div/div/section/div/div[2]/div/div[1]/div/div/a/span/span')))
        time.sleep(1)
        print("First Navigation Text:", click_on_fin_tech.text)
        time.sleep(1)
        action.click(click_on_fin_tech).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        hover_on_industry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-21"]/a')))
        action = ActionChains(driver)
        print("hover_on_industry is:", hover_on_industry.text)
        action.move_to_element(hover_on_industry).perform()
        time.sleep(1)

        click_on_health_tech = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-mega-content-21"]/div/section[2]/div/div/div/section/div/div[2]/div/div[1]/div/div/a/span/span')))
        time.sleep(1)
        print("Second Navigation Text:", click_on_health_tech.text)
        time.sleep(1)
        action.click(click_on_health_tech).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        hover_on_industry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-21"]/a')))
        action = ActionChains(driver)
        print("hover_on_industry is:", hover_on_industry.text)
        action.move_to_element(hover_on_industry).perform()
        time.sleep(1)

        click_on_ad_tech = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-mega-content-21"]/div/section[3]/div/div/div/section/div/div[2]/div/div[1]/div/div/a/span/span')))
        time.sleep(1)
        print("Third Navigation Text:", click_on_ad_tech.text)
        time.sleep(1)
        action.click(click_on_ad_tech).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        hover_on_industry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-21"]/a')))
        action = ActionChains(driver)
        print("hover_on_industry is:", hover_on_industry.text)
        action.move_to_element(hover_on_industry).perform()
        time.sleep(1)

        click_on_process_automation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-mega-content-21"]/div/section[4]/div/div/div/section/div/div[2]/div/div[1]/div/div/a/span/span')))
        time.sleep(1)
        print("Fourth Navigation Text:", click_on_process_automation.text)
        time.sleep(1)
        action.click(click_on_process_automation).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Join Us menu test execute

        click_on_join_us = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-2613"]/a')))
        time.sleep(1)
        print("Fourth Navigation Text:", click_on_join_us.text)
        time.sleep(1)
        action.click(click_on_join_us).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # About Us menu test execute

        click_on_about_us = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-nav-menu-item-2612"]/a')))
        time.sleep(1)
        print("Fourth Navigation Text:", click_on_about_us.text)
        time.sleep(1)
        action.click(click_on_about_us).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

        # Contact US CTA test execute

        hover_on_contact_us = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section[1]/div/div[3]/div/div[1]/div/div/a')))
        action.move_to_element(hover_on_contact_us).perform()
        time.sleep(1)

        click_on_contact_us = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section[1]/div/div[3]/div/div[1]/div/div/a')))
        time.sleep(1)
        print("Fourth Navigation Text:", click_on_contact_us.text)
        time.sleep(1)
        action.click(click_on_contact_us).perform()
        time.sleep(1)
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(1)

    finally:
        driver.quit()


verify_header()
