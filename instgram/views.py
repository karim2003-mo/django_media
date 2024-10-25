from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
def put_comment(request,path):
    browser=None
    if path=='remote' :
        browser="/usr/bin/chromedriver"
    c=0
    l=["esraa_kamel84","aya_abdelrhman789"]
    for user in l :
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("prefs", {
                "profile.default_content_setting_values.notifications": 2
            })
            # Open the login page
            chrome_options = Options()
            chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
            chrome_options.add_argument("--headless")  # Run in headless mode
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_service=Service(browser)
            driver =webdriver.Chrome(options=chrome_options,service=chrome_service)
            driver.get("https://www.instagram.com/?hl=en")
            time.sleep(2)
            usr=driver.find_element(By.NAME,"username")
            usr.send_keys(user)
            time.sleep(2)
            password=driver.find_element(By.NAME,"password")
            password.send_keys("0504800757")
            time.sleep(2)
            sign_button=driver.find_element(By.XPATH,"//button[@type='submit']")
            sign_button.click()
            time.sleep(17)
            driver.get("https://www.instagram.com/p/DBYRDw9o9uL/")
            time.sleep(2)
            comment_button=driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']")
            time.sleep(2)
            comment_button.click()
            time.sleep(2)
            comment_area=driver.find_element(By.XPATH,"//textarea[@placeholder='Add a comment…']")
            comment_area.send_keys("elegant")
            time.sleep(2)
            comment_area.send_keys(Keys.ENTER)
            print("...............................")
            time.sleep(20)
            c+=1
            driver.quit()
        except Exception as e:
            error=str(e)
            return JsonResponse({"error" : error})
    return JsonResponse({"comments done is ":c})
def test_func(request) :
    return HttpResponse("your app is correctly operated")
# Create your views here.
