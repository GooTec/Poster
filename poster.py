#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

import xlwings
import requests
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from urllib.error import HTTPError
from urllib.parse import urlencode
import pyperclip
import time

chromedriver_path = './chromedriver.exe'

client_ID = '1iH_V46JZamBwak5lE_j'
client_PWD = 'wWegAXh_B4'
callback_URL = 'http://superlink.co.kr/download/callback.php'
state='RANDOM_STATE'

## 네이버 카페 아이디 및 암호 엑셀에서 읽어오기
naver_id = 'navigado'
naver_pw = 'pass#1247*'
api_url = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={}&redirect_uri={}&state={}".format(client_ID, callback_URL, state)

## 현재 인증 안된 네이버 계정들은 자동 인증 코드 필요함 ㅠㅠ 
## 새로운 네이버 계정 로그인 시 확인 가능

driver = webdriver.Chrome(chromedriver_path)  # driver = webdriver.PhantomJS()
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
time.sleep(1)
input_js = 'document.getElementById("id").value = "{}";document.getElementById("pw").value = "{}";'.format(naver_id,naver_pw)
driver.execute_script(input_js) 
driver.find_element_by_id("log.login").click()


driver.get(api_url)

response = driver.find_element_by_tag_name('body').text
json_response = response.split(' ')[1]

json_response = json.loads(json_response)
access_token = json_response['access_token']
import os
import sys
import requests
import urllib.request

header = "Bearer " + access_token # Bearer 다음에 공백 추가
## 네이버 카페 아이디 엑셀에서 읽어오기
clubid = "12730407" # 카페의 고유 ID값

## 네이버 카페 게시판 아이디 엑셀에서 읽어오기
menuid = "16"  # (상품게시판은 입력 불가)


url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"

##  제목 엑셀에서 읽어오기
subject_content = xlbook
subject = urllib.parse.quote(subject_content)

## 게시물 내용 엑셀에서 읽어오기
body_content = xlbook
content = urllib.parse.quote(body_content)

data = {'subject': subject, 'content': content}

## 이미지 파일 경로 받아오기
img_file = xlbook
if img_file != None :
    files = [
        ('image', ('YOUR_FILE_1', open('', 'rb'), 'image/png', {'Expires': '0'})),
        ]
    ## 이미지 파일과 함께 업로드하는 코드 Naver Developers 참고

else :
    headers = {'Authorization': header }
    response = requests.post(url, headers=headers, data=data)

rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print(rescode)