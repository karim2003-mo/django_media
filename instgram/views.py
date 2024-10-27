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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
def put_comment(request):
    c=0
    l=[]
    error="No Errors Founded"
    users=Users.objects.all()
    comment=Comments.objects.get(name="comments")
    op=Operator.objects.get()
    link=comment.link
    if op.operator :
        for user in users :
            try:
                chrome_options = Options()
                chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
                chrome_options.add_argument("--disable-blink-features=AutomationControlled")
                chrome_options.add_experimental_option("prefs", {
                    "profile.default_content_setting_values.notifications": 2
                })
                # Open the login page
                chrome_options = Options()
                chrome_options.add_argument("--incognito")  # Enable Incognito mode
                chrome_options.add_argument("--window-size=1920,1080")  # Set window size
                chrome_options.add_argument("--disable-gpu")  # Optional for performance
                chrome_options.add_argument("--headless") 
                driver =webdriver.Chrome(options=chrome_options)
                driver.get("https://www.instagram.com/?hl=en")
                time.sleep(2)
                usr=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
                usr.send_keys(user.username)
                time.sleep(2)
                password=driver.find_element(By.NAME,"password")
                password.send_keys(f"{user.password}")
                time.sleep(2)
                sign_button=driver.find_element(By.XPATH,"//button[@type='submit']")
                driver.execute_script("arguments[0].click();", sign_button)
                time.sleep(14)
                driver.get(f"{link}")
                time.sleep(2)
                comment_button=driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']")
                time.sleep(2)
                comment_button.click()
                time.sleep(2)
                comment_area=driver.find_element(By.XPATH,"//textarea[@placeholder='Add a comment…']")
                comment_area.send_keys(f"{comment["comments"][list(users).index(user)]}")
                time.sleep(2)
                comment_area.send_keys(Keys.ENTER)
                print("...............................")
                time.sleep(8)
                c+=1
                driver.quit()
            except Exception as e:
                error=str(e)
                l.append(user.username)
    else :
        return JsonResponse({"sta":"this service is disabled"})
    return JsonResponse({"comments done is ":c,"error":error})
def test_func(request) :
    return HttpResponse("your app is correctly operated")
def delete(request):
    Comments.objects.all().delete()
    return HttpResponse("deleted")
@csrf_exempt
def add_comment(request):
    if request.method=='POST':
        data=json.load(request.body)
        link=data["link"]
        comments=list(data['comments'])
        c=Comments.objects.get()
        c.comment['comments']=comments
        c.link=link
        c.save()
@csrf_exempt
def add_account(request):
    if request.method=='POST':
        data=json.load(request.body)
        accounts=data['accounts']
        for d in accounts :
            map=d
            username=map['username']
            password=map['password']
            c=Users.objects.create(username=username,password=password)
        c.save()
@csrf_exempt
def modify_account(request):
    if request.method=='POST':
        data=json.load(request.body)
        username=data['username']
        password=data['password']
        c=Users.objects.get(username=username)
        c.password=password
        c.save()
# Create your views here.
