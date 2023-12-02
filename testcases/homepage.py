import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_home_page():
    driver.maximize_window()
    driver.get("https://exabyting.com/")
    time.sleep(1)

    try:
        # Banner section Test Execution

        h1_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[1]/div[2]/div/div/section[1]/div/div[1]/div/div[1]/div/h1')))
        if h1_title.is_displayed():
            print(h1_title.text)
        else:
            print("!!!!!!!!!! h1_title not found !!!!!!!!!!")

        banner_copy = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[1]/div[2]/div/div/section[1]/div/div[1]/div/div[2]/div')))
        if banner_copy.is_displayed():
            print(banner_copy.text)
        else:
            print("!!!!!!!!!! banner_copy not found !!!!!!!!!!")

        lets_talk = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[1]/div[2]/div/div/section[1]/div/div[1]/div/div[3]/div/div/a')))
        time.sleep(1)
        print("CTA Text:", lets_talk.text)
        time.sleep(1)
        lets_talk.click()
        time.sleep(3)

        pop_up = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '//*[@id="elementor-popup-modal-1651"]/div/div[2]/div/section')))
        if pop_up.is_displayed():
            print("POP up Displayed")
        else:
            print("!!!!!!!!!! POP up not Displayed !!!!!!!!!!")

        close_pop_up = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '//*[@id="elementor-popup-modal-1651"]/div/a')))
        close_pop_up.click()
        time.sleep(2)

        # Industry Expertise section Test Execution

        scroll_to_industry_section = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[3]')))
        driver.execute_script("arguments[0].scrollIntoView();", scroll_to_industry_section)
        time.sleep(1)

        h5_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[4]/div/div/div/div[1]/div/h5')))
        if h5_title.is_displayed():
            print(h5_title.text)
        else:
            print("!!!!!!!!!! h5_title not found !!!!!!!!!!")

        h2_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[4]/div/div/div/div[2]/div/h2')))
        if h2_title.is_displayed():
            print(h2_title.text)
        else:
            print("!!!!!!!!!! h2_title not found !!!!!!!!!!")

        image_dot_scroll_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-carousel-f36cd4e"]/ul/li[1]')))
        image_dot_scroll_1.click()
        time.sleep(5)
        image_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide20"]/div/section/div/div/div/section/div/div[1]/div/div/div/img')))
        if image_1.is_displayed():
            print("Image found")
        else:
            print("!!!!!!!!!! Image not found !!!!!!!!!!")

        image_1_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ind-slider"]/div/h2')))
        if image_1_title.is_displayed():
            print(image_1_title.text)
        else:
            print("!!!!!!!!!! image_1_title not found !!!!!!!!!!")

        image_1_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide20"]/div/section/div/div/div/section/div/div[2]/div/div[2]/div')))
        if image_1_paragraph.is_displayed():
            print(image_1_paragraph.text)
        else:
            print("!!!!!!!!!! image_1_paragraph not found !!!!!!!!!!")

        click_learn_more = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide20"]/div/section/div/div/div/section/div/div[2]/div/div[3]/div/div/a/span/span[2]')))
        click_learn_more.click()
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(2)

        image_dot_scroll_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-carousel-f36cd4e"]/ul/li[2]')))
        image_dot_scroll_2.click()
        time.sleep(5)
        image_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide21"]/div/section/div/div/div/section/div/div[1]/div/div/div/img')))
        if image_2.is_displayed():
            print("image_2 found")
        else:
            print("!!!!!!!!!! Image not found !!!!!!!!!!")

        image_2_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ind-slider"]/div')))
        if image_2_title.is_displayed():
            print(image_2_title.text)
        else:
            print("!!!!!!!!!! image_2_title not found !!!!!!!!!!")

        image_2_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide21"]/div/section/div/div/div/section/div/div[2]/div/div[2]')))
        if image_2_paragraph.is_displayed():
            print(image_2_paragraph.text)
        else:
            print("!!!!!!!!!! image_2_paragraph not found !!!!!!!!!!")

        click_learn_more_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide21"]/div/section/div/div/div/section/div/div[2]/div/div[3]/div/div/a/span/span[2]')))
        click_learn_more_2.click()
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(2)

        image_dot_scroll_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-carousel-f36cd4e"]/ul/li[3]')))
        image_dot_scroll_3.click()
        time.sleep(5)
        image_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide22"]/div/section/div/div/div/section/div/div[1]/div/div/div/img')))
        if image_3.is_displayed():
            print("image_3 found")
        else:
            print("!!!!!!!!!! Image not found !!!!!!!!!!")

        image_3_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ind-slider"]/div/h2')))
        if image_3_title.is_displayed():
            print(image_3_title.text)
        else:
            print("!!!!!!!!!! image_3_title not found !!!!!!!!!!")

        image_3_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="slick-slide22"]/div/section/div/div/div/section/div/div[2]/div/div[2]')))
        if image_3_paragraph.is_displayed():
            print(image_3_paragraph.text)
        else:
            print("!!!!!!!!!! image_3_paragraph not found !!!!!!!!!!")

        click_learn_more_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide22"]/div/section/div/div/div/section/div/div[2]/div/div[3]/div/div/a/span/span[2]')))
        click_learn_more_3.click()
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(2)

        image_dot_scroll_4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-carousel-f36cd4e"]/ul/li[4]')))
        image_dot_scroll_4.click()
        time.sleep(5)
        image_4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide23"]/div/section/div/div/div/section/div/div[1]/div/div/div/img  ')))
        if image_4.is_displayed():
            print("image_4 found")
        else:
            print("!!!!!!!!!! Image not found !!!!!!!!!!")

        image_4_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ind-slider"]/div/h2')))
        if image_4_title.is_displayed():
            print(image_4_title.text)
        else:
            print("!!!!!!!!!! image_4_title not found !!!!!!!!!!")

        image_4_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide23"]/div/section/div/div/div/section/div/div[2]/div/div[2]/div')))
        if image_4_paragraph.is_displayed():
            print(image_4_paragraph.text)
        else:
            print("!!!!!!!!!! image_4_paragraph not found !!!!!!!!!!")

        click_learn_more_4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slick-slide23"]/div/section/div/div/div/section/div/div[2]/div/div[3]/div/div/a/span/span[2]')))
        click_learn_more_4.click()
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(2)

        # Development practices section test case execution

        scroll_to_industry_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="premium-carousel-f36cd4e"]/ul')))
        driver.execute_script("arguments[0].scrollIntoView();", scroll_to_industry_section)
        time.sleep(1)

        h5_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[5]/div/div/div/div[1]/div/h5')))
        if h5_title.is_displayed():
            print(h5_title.text)
        else:
            print("!!!!!!!!!! h5_title not found !!!!!!!!!!")

        h2_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[5]/div/div/div/div[2]/div/h2')))
        if h2_title.is_displayed():
            print(h2_title.text)
        else:
            print("!!!!!!!!!! h2_title not found !!!!!!!!!!")

        paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[5]/div/div/div/div[3]/div')))
        if paragraph.is_displayed():
            print(paragraph.text)
        else:
            print("!!!!!!!!!! Paragraph not found !!!!!!!!!!")

        click_on_development_learn_more = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[5]/div/div/div/div[4]/div/div/a/span/span[2]')))
        click_on_development_learn_more.click()
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(2)

        development_image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[5]/div/div/div/div[5]/div/img')))
        if development_image.is_displayed():
            print("development_image found")
        else:
            print("!!!!!!!!!! development_image not found !!!!!!!!!!")

        # Our Expertise test case execution

        scroll_to_industry_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]')))
        driver.execute_script("arguments[0].scrollIntoView();", scroll_to_industry_section)
        time.sleep(1)

        h2_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[1]/div/div[1]/div/h5')))
        if h2_title.is_displayed():
            print(h2_title.text)
        else:
            print("!!!!!!!!!! h2_title not found !!!!!!!!!!")

        paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[1]/div/div[2]/div/h2')))
        if paragraph.is_displayed():
            print(paragraph.text)
        else:
            print("!!!!!!!!!! Paragraph not found !!!!!!!!!!")

        click_on_expertise_learn_more = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[1]/div/div[3]/div/div/a')))
        click_on_expertise_learn_more.click()
        current_url = driver.current_url
        title = driver.title
        print("Redirected URL is:", current_url)
        print("Page Title:", title)
        driver.back()
        time.sleep(2)

        expert_image_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[1]/div/div/div/div/figure/img')))
        if expert_image_1.is_displayed():
            print("expert_image_1 found")
        else:
            print("!!!!!!!!!! expert_image_1 not found !!!!!!!!!!")

        expert_image_1_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[1]/div/div/div/div/div/h5')))
        if expert_image_1_title.is_displayed():
            print(expert_image_1_title.text)
        else:
            print("!!!!!!!!!! expert_image_1_title not found !!!!!!!!!!")

        expert_image_1_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[1]/div/div/div/div/div/p')))
        if expert_image_1_paragraph.is_displayed():
            print(expert_image_1_paragraph.text)
        else:
            print("!!!!!!!!!! expert_image_1_paragraph not found !!!!!!!!!!")

        expert_image_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[2]/div/div/div/div/figure/img')))
        if expert_image_2.is_displayed():
            print("expert_image_2 found")
        else:
            print("!!!!!!!!!! expert_image_2 not found !!!!!!!!!!")

        expert_image_2_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[2]/div/div/div/div/div/h5')))
        if expert_image_2_title.is_displayed():
            print(expert_image_2_title.text)
        else:
            print("!!!!!!!!!! expert_image_2_title not found !!!!!!!!!!")

        expert_image_2_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[2]/div/div/div/div/div/p')))
        if expert_image_2_paragraph.is_displayed():
            print(expert_image_2_paragraph.text)
        else:
            print("!!!!!!!!!! expert_image_2_paragraph not found !!!!!!!!!!")

        expert_image_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[3]/div/div/div/div/figure/img')))
        if expert_image_3.is_displayed():
            print("expert_image_3 found")
        else:
            print("!!!!!!!!!! expert_image_3 not found !!!!!!!!!!")

        expert_image_3_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[3]/div/div/div/div/div/h5')))
        if expert_image_3_title.is_displayed():
            print(expert_image_3_title.text)
        else:
            print("!!!!!!!!!! expert_image_3_title not found !!!!!!!!!!")

        expert_image_3_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[1]/div/div[3]/div/div/div/div/div/p')))
        if expert_image_3_paragraph.is_displayed():
            print(expert_image_3_paragraph.text)
        else:
            print("!!!!!!!!!! expert_image_3_paragraph not found !!!!!!!!!!")

        expert_image_4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[2]/div/div[1]/div/div/div/div/figure/img')))
        if expert_image_4.is_displayed():
            print("expert_image_4 found")
        else:
            print("!!!!!!!!!! expert_image_4 not found !!!!!!!!!!")

        expert_image_4_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[2]/div/div[1]/div/div/div/div/div/h5')))
        if expert_image_4_title.is_displayed():
            print(expert_image_4_title.text)
        else:
            print("!!!!!!!!!! expert_image_4_title not found !!!!!!!!!!")

        expert_image_4_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[2]/div/div[1]/div/div/div/div/div/p')))
        if expert_image_4_paragraph.is_displayed():
            print(expert_image_4_paragraph.text)
        else:
            print("!!!!!!!!!! expert_image_4_paragraph not found !!!!!!!!!!")

        expert_image_5 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[2]/div/div[2]/div/div/div/div/figure/img')))
        if expert_image_5.is_displayed():
            print("expert_image_5 found")
        else:
            print("!!!!!!!!!! expert_image_5 not found !!!!!!!!!!")

        expert_image_5_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[2]/div/div[2]/div/div/div/div/div/h5')))
        if expert_image_5_title.is_displayed():
            print(expert_image_5_title.text)
        else:
            print("!!!!!!!!!! expert_image_5_title not found !!!!!!!!!!")

        expert_image_5_paragraph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[6]/div/div/div/section/div/div[2]/div/div/div/div/div/section[1]/div/div/div/section[2]/div/div[2]/div/div/div/div/div/p')))
        if expert_image_5_paragraph.is_displayed():
            print(expert_image_5_paragraph.text)
        else:
            print("!!!!!!!!!! expert_image_5_paragraph not found !!!!!!!!!!")

    finally:
        driver.quit()


verify_home_page()
