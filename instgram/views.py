from django.shortcuts import render
import requests
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
from bs4 import BeautifulSoup
class SocialInstgram :
    chrome_options = Options()
    users=Users.objects.all()
    op=Operator.objects.get()
    post=Post.objects.get()
    comment=Comments.objects.get()
    def __init__(self) -> None:
        self.chrome_options.add_argument(r"--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data")
        self.chrome_options.add_argument(r"--profile-directory=Profile 3")
    def login(self,driver : webdriver.Chrome,user : Users) :
        try :
                        time.sleep(2)
                        usr=driver.find_element(By.NAME, "username")
                        usr.click()
                        try :
                            usr.send_keys(Keys.CONTROL + "a")
                            usr.send_keys(Keys.DELETE)
                        except :
                            pass
                        usr.send_keys(user.username)
                        time.sleep(2)
                        password=driver.find_element(By.NAME,"password")
                        password.click()
                        try :
                            password.send_keys(Keys.CONTROL + "a")
                            password.send_keys(Keys.DELETE)
                        except :
                            pass
                        password.send_keys(f"{user.password}")
                        time.sleep(2)
                        sign_button=driver.find_element(By.XPATH,"//button[@type='submit']")
                        driver.execute_script("arguments[0].click();", sign_button)
                        time.sleep(12)
                        try :
                            dismis_btn=driver.find_element(By.XPATH,"//button[text()='dismiss]")
                            dismis_btn.click()
                        except :
                            pass
                        password.send_keys(f"{user.password}")
                        time.sleep(2)
                        sign_button=driver.find_element(By.XPATH,"//button[@type='submit']")
                        driver.execute_script("arguments[0].click();", sign_button)
                        time.sleep(12)
                        try :
                            dismis_btn=driver.find_element(By.XPATH,"//button[text()='Dismiss]")
                            dismis_btn.click()
                        except :
                            pass
        except :
                        pass
    def logout(self,driver : webdriver.Chrome) :
        try :
                    settings=driver.find_element(By.XPATH, "//div//*[name()='svg' and @aria-label='Settings']")
                    settings.click()
                    # //div[@data-bloks-name='ig.components.Icon']
                    time.sleep(2)
                    log_out=driver.find_element(By.XPATH,"//div[contains(@class, 'x1n2onr6')]/div/div/div/div/span/span[text()='Log out']")
                    log_out.click()
                    time.sleep(3)
                    log_out_confirm=driver.find_element(By.XPATH,"//div[normalize-space()='Log out']")
                    log_out_confirm.click()
        except :
                    try :
                        settings2=driver.find_element(By.XPATH,"//div[@data-bloks-name='ig.components.Icon']")
                        settings2.click()
                        log_out2=driver.find_element(By.CSS_SELECTOR,"div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 xw2csxc x1odjw0f x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'] div[class='wbloks_1'] div[class='wbloks_1'] div[class='wbloks_1'] div[class='wbloks_1'] div[role='button'] span[data-bloks-name='bk.components.Text']")
                        log_out2.click()
                        confirm=driver.find_element(By.XPATH,"//div[text()='Log out']")
                        confirm.click()
                    except :
                        pass
    def put_comment(self):
        c=0
        l=[]
        error="No Errors Founded"
        link=self.comment.link
        i=0
        if self.op.operator :
            for user in self.users :
                driver =webdriver.Chrome(options=self.chrome_options)
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
                    pyperclip.copy(self.comment.comment['comments'][0])
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
    def test_func(self,request) :
        return HttpResponse("your app is correctly operated")
    def delete(self,request):
        Comments.objects.all().delete()
        return HttpResponse("deleted")
    @csrf_exempt
    def add_comment(self,request):
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
    def add_account(self,request):
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
    def modify_account(self,request):
        if request.method=='POST':
            data=json.loads(request.body)
            username=data['username']
            password=data['password']
            c=Users.objects.get(username=username)
            c.password=password
            c.save()
            return JsonResponse({"status":"mission has been done"})
        return JsonResponse({"status":"mission failed"})
    def react(self) :
        pass
    def posts(self,request) :
        error="No Errors Founded"
        image_path=self.post.image
        caption=self.post.caption
        c=0
        if self.op.operator== True :
            time.sleep(3)
            driver =webdriver.Chrome(options=self.chrome_options)
            driver.get("https://www.instagram.com/?hl=en")
            time.sleep(3)
            for user in self.users :
                self.logout(driver=driver)
                try:
                    time.sleep(3)
                    try :
                        switch=driver.find_element(By.XPATH,"//div[@role='button' and text()='Switch accounts']")
                        switch.click()
                        time.sleep(2)
                    except : 
                        pass
                    self.login(driver=driver,user=user)
                    new_post_button = driver.find_element(By.XPATH, "//div//*[name()='svg' and @aria-label='New post']")
                    new_post_button.click()
                    time.sleep(1)
                    time.sleep(2)
                    # Click "Next" 
                    # Select From Computer
                    try :
                        choose_image = driver.find_element(By.XPATH, "//button[text()='Select From Computer']")
                        choose_image.click()
                    except :
                        pyautogui.click(clicks=1,x=590,y=633)
                    time.sleep(3)
                    try :
                        pyautogui.typewrite(image_path)
                        time.sleep(1)
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
                    except :
                        pass
                    try :
                        close_btn=driver.find_element(By.XPATH,"//div[@class='x160vmok x10l6tqk x1eu8d0j x1vjfegm']//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']//*[name()='svg']")
                        # //div[@class='x160vmok x10l6tqk  x1vjfegm']//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']//*[name()='svg']
                        close_btn.click()
                    except :
                        pyautogui.click()
                    time.sleep(1)
                    self.logout(driver=driver)
                    time.sleep(5)
                    c+=1
                except:
                    user.account_problem=True
                    user.save()
                    pass
        return JsonResponse({"posts done is ":c,"error":error})
    def account_problem(self,request) :
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
    def comment_only(self,request) :
        self.put_comment()
    def react_only(self,request):
        self.react()
    def comment_and_react(self,request) :
        driver =webdriver.Chrome(options=self.chrome_options)
        driver.get("https://www.instagram.com/?hl=en")
        users= Users.objects.all()
        for user in users :
            self.login(driver=driver,user=user)
            self.put_comment()
            self.react()
    def test_soup(self,request) :
        page=requests.get("https://www.instagram.com/")
        cont=page.content
        soup=BeautifulSoup(cont,"lxml")
        print(soup)
        return HttpResponse(soup)
    # //div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']//*[name()='svg']  XPATH
    # line[fill='none'][stroke='currentColor'][stroke-linecap='round'][stroke-linejoin='round'][stroke-width='3']  css selector
    # Create your views here.
    # //div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Menu' and contains(@class, 'wbloks_1')]
    # //div[@class='_ap3a _aaco _aacu _aad6']  bacakupcode
    # //button[@type='button']
