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
import pyperclip
import time
import pyautogui
def put_comment(request):
    c=0
    l=[]
    error="No Errors Founded"
    users=Users.objects.all()
    comment=Comments.objects.get(name="comments")
    op=Operator.objects.get()
    link=comment.link
    i=0
    if op.operator :
        for user in users :
            chrome_options = Options()
            # Open the login page
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument(r"--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data")
            chrome_options.add_argument(r"--profile-directory=Profile 3")
            # chrome_options.add_argument("--disable-gpu")  # Optional for performance
            # chrome_options.add_argument("--headless") 
            driver =webdriver.Chrome(options=chrome_options)
            try:
                time.sleep(4)
                driver.get("https://www.instagram.com/?hl=en")
                time.sleep(1)
                try :
                    switch=driver.find_element(By.XPATH,"//div[@role='button' and text()='Switch accounts']")
                    switch.click()
                    time.sleep(2)
                except :
                    pass
                usr=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
                usr.click()
                usr.send_keys(Keys.CONTROL + "a")
                usr.send_keys(Keys.DELETE)
                usr.send_keys(user.username)
                time.sleep(2)
                password=driver.find_element(By.NAME,"password")
                password.click()
                password.send_keys(Keys.CONTROL + "a")
                password.send_keys(Keys.DELETE)
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
                pyperclip.copy(comment.comment['comments'][0])
                comment_area=driver.find_element(By.XPATH,"//textarea[@placeholder='Add a comment…']")
                comment_area.send_keys(Keys.CONTROL, 'v')
                i+=1
                time.sleep(2)
                comment_area.send_keys(Keys.ENTER)
                print("...............................")
                time.sleep(4)
                settings=driver.find_element(By.XPATH, "//div//*[name()='svg' and @aria-label='Settings']")
                settings.click()
                time.sleep(3)
                log_out=driver.find_element(By.XPATH,"//div[contains(@class, 'x1n2onr6')]/div/div/div/div/span/span[text()='Log out']")
                log_out.click()
                time.sleep(4)
                c+=1
                driver.quit()
            except Exception as e:
                error=str(e)
                l.append(user.username)
                driver.quit()
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
        data=json.loads(request.body)
        link=data["link"]
        comments=list(data['comments'])
        c=Comments.objects.get()
        c.comment['comments']=comments
        c.link=link
        c.save()
        return JsonResponse({"status":"mission has been done"})
    return JsonResponse({"status":"mission failed"})
@csrf_exempt
def add_account(request):
    if request.method=='POST':
        data=json.loads(request.body)
        accounts=data['accounts']
        for d in accounts :
            map=d
            username=map['username']
            password=map['password']
            c=Users.objects.create(username=username,password=password)
        c.save()
        return JsonResponse({"status":"mission has been done"})
    return JsonResponse({"status":"mission failed"})
@csrf_exempt
def modify_account(request):
    if request.method=='POST':
        data=json.loads(request.body)
        username=data['username']
        password=data['password']
        c=Users.objects.get(username=username)
        c.password=password
        c.save()
        return JsonResponse({"status":"mission has been done"})
    return JsonResponse({"status":"mission failed"})
def posts(request) :
    error="No Errors Founded"
    users=Users.objects.all()
    comment=Comments.objects.get(name="comments")
    op=Operator.objects.get()
    post=Post.objects.get()
    image_path=post.image
    caption=post.caption
    link=comment.link
    c=0
    if op.operator== True :
        chrome_options = Options()
        # Open the login page
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument(r"--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data")
        chrome_options.add_argument(r"--profile-directory=Profile 3")
        # chrome_options.add_argument("--disable-gpu")  # Optional for performance
        # chrome_options.add_argument("--headless") 
        driver =webdriver.Chrome(options=chrome_options)
        driver.get("https://www.instagram.com/?hl=en")
        time.sleep(3)
        for user in users :
            if user.username=="nehadfayed22":
                continue
            try :
                settings=driver.find_element(By.XPATH, "//div//*[name()='svg' and @aria-label='Settings']")
                settings.click()
                time.sleep(2)
                log_out=driver.find_element(By.XPATH,"//div[contains(@class, 'x1n2onr6')]/div/div/div/div/span/span[text()='Log out']")
                log_out.click()
                time.sleep(3)
                log_out_confirm=driver.find_element(By.XPATH,"//div[normalize-space()='Log out']")
                log_out_confirm.click()
            except Exception as e :
                print(f"errrrrrrrrrrrrrrrrrrrrror1 {e}")
                try :
                    settings2=driver.find_element(By.XPATH,"//div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Menu' and contains(@class, 'wbloks_1')]")
                    settings2.click()
                    log_out2=driver.find_element(By.XPATH,"//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 xw2csxc x1odjw0f x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']//div[@class='wbloks_1']//div[@class='wbloks_1']//div[@class='wbloks_1']//div[@class='wbloks_1']//div[@role='button']")
                    log_out2.click()
                    log_out_confirm=driver.find_element(By.XPATH,"//div[normalize-space()='Log out']")
                    log_out_confirm.click()
                except Exception as e:
                    print(f"errrrrrrrrrrrrrrrrrrrrror2 {e}")
                    pass
            try:
                time.sleep(3)
                try :
                    switch=driver.find_element(By.XPATH,"//div[@role='button' and text()='Switch accounts']")
                    switch.click()
                    time.sleep(2)
                except :
                    pass
                try :
                    time.sleep(2)
                    usr=driver.find_element(By.NAME, "username")
                    usr.click()
                    usr.send_keys(Keys.CONTROL + "a")
                    usr.send_keys(Keys.DELETE)
                    usr.send_keys(user.username)
                    time.sleep(2)
                    password=driver.find_element(By.NAME,"password")
                    password.click()
                    password.send_keys(Keys.CONTROL + "a")
                    password.send_keys(Keys.DELETE)
                    password.send_keys(f"{user.password}")
                    time.sleep(2)
                    sign_button=driver.find_element(By.XPATH,"//button[@type='submit']")
                    driver.execute_script("arguments[0].click();", sign_button)
                    time.sleep(12)
                    try :
                        dismis_btn=driver.find_element(By.XPATH,"//button[@type='dismiss]")
                        dismis_btn.click()
                    except :
                        pass
                except :
                    pass
                new_post_button = driver.find_element(By.XPATH, "//div//*[name()='svg' and @aria-label='New post']")
                new_post_button.click()
                time.sleep(3)
                # Click "Next" button
                choose_image = driver.find_element(By.XPATH, "//button[normalize-space()='Select from computer']")
                choose_image.click()
                time.sleep(2)
                pyautogui.typewrite(image_path)
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(3)
                next_button = driver.find_element(By.XPATH, "//div[contains(text(),'Next')]")
                next_button.click()
                time.sleep(2)
                next_button2 = driver.find_element(By.XPATH, "//div[contains(text(),'Next')]")
                next_button2.click()
                time.sleep(2)
                caption_area = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r']")
                pyperclip.copy(caption)
                caption_area.send_keys(Keys.CONTROL,"v")
                time.sleep(2)
                share_button = driver.find_element(By.XPATH, "//div[contains(text(),'Share')]")
                share_button.click()
                time.sleep(20)
                try :
                    close_btn=driver.find_element(By.XPATH,"//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']//*[name()='svg']")
                    close_btn.click()
                except :
                    pass
                time.sleep(1)
                settings=driver.find_element(By.XPATH, "//div//*[name()='svg' and @aria-label='Settings']")
                settings.click()
                time.sleep(2)
                log_out=driver.find_element(By.XPATH,"//div[contains(@class, 'x1n2onr6')]/div/div/div/div/span/span[text()='Log out']")
                log_out.click()
                time.sleep(5)
                c+=1
            except Exception as e:
                error=str(e)
    return JsonResponse({"posts done is ":c,"error":error})
def account_problem(request) :
    li=[]
    users=Users.objects.all()
    for u in users :
        if u.account_problem==True :
            mp={
                "username" : u.username,
                "password" :u.password,
            }
            li.append(mp)
    return JsonResponse({
        "result" :li
    })
# //div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']//*[name()='svg']  XPATH
# line[fill='none'][stroke='currentColor'][stroke-linecap='round'][stroke-linejoin='round'][stroke-width='3']  css selector
# Create your views here.
# //div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Menu' and contains(@class, 'wbloks_1')]
# //div[@class='_ap3a _aaco _aacu _aad6']  bacakupcode
