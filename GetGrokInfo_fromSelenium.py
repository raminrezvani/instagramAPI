
from selenium import webdriver
import undetected_chromedriver as uc


from selenium.webdriver.common.by import By

driver=uc.Chrome()

driver.get('https://grok.com/')
#-- First Login
input('First loggin...')

import time
#--- send image
def send_image(driver,image_path):
    try:
        # image_path = "c:/2.jpg"
        '/html/body/div/div/main/div[2]/div[2]/div[2]/div/form/div/div/div[3]/button'
        driver.find_element(By.XPATH, '//button[@type="button" and @tabindex="0"]').click()
        time.sleep(3)
        # driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div[2]/div[2]/div/form/div/div/div[2]/button').click()
        try:
            driver.find_element(By.XPATH,'//button[text()="Select files"]/../..//input').send_keys(image_path)
        except:
            driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div[2]/div/div/form/div/input').send_keys(image_path)
    except:
        print(f'Send image Error')


# send_image(driver,'c:/template1.json')
# send_image(driver,'c:/2.jpg')

#----
def send_prompt(driver):
    prompt=f'Fill this template for file template.json for above image . '.replace('\n','   ')

    try:
        driver.find_element(By.XPATH,'/html/body/div/div/main/div[2]/div[2]/div/form/div/div/div[2]/textarea').send_keys(prompt)
    except:
        driver.find_element(By.XPATH,'/html/body/div/div/main/div[2]/div[2]/div/div/form/div/div/div[2]/textarea').send_keys(
            prompt)

    #-- submit
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(5)


#_-- read result
def get_result(driver):
    import json
    res=driver.find_element(By.XPATH,'//code').text
    res_json=json.loads(res)
    return res_json

import pymongo
import json
def send_toDB(res_json,image_path):
    myclient2 = pymongo.MongoClient('mongodb://45.149.76.168:13667')
    mydb2 = myclient2["Mohaddes_Project"]
    mycol_write_posts = mydb2["Post_Hashtags"]
    id=image_path.split('\\')[-1].replace('.jpg','')
    post=list(mycol_write_posts.find({'id':id}))[0]

    mycol_write_posts.update_one({'id':id},{'$set':{'Image_Analysis':res_json}})



#-------------- for each post from database get info
send_image(driver, 'c:/template1.json')
from pathlib import Path

folderPath = 'ImageDownloaded'
folder = Path(folderPath)

for file in folder.iterdir():
    if file.is_file():  # فقط فایل‌ها
        absolute_path = file.absolute()  # مسیر مطلق
        image_path=str(absolute_path)
        send_image(driver, image_path)
        send_prompt(driver)
        res_json=get_result(driver)
        send_toDB(res_json,image_path)