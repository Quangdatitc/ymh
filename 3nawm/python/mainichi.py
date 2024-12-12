#!/usr/bin/env python
# coding: utf-8

# In[11]:


from selenium import webdriver
import sys
import os
import configparser
# ドライバーをexe化した時に相対パスで使用できるようにする
# 参考：https://www.zacoding.com/post/python-selenium-to-exe/
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# エラー回避
#参考：https://miya-mitsu.com/python-0x1ferror/
from msedge.selenium_tools import Edge,EdgeOptions
options = EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True


# ここに追加してください。

url = "http://10.145.156.119:8787/motionboard/main?mbid=fidm2lbeqdxina67nr6aaaf74whwu&boardpath=/アクションボード/ＭＥ製造部生産課/製造技術課/端末稼働監視/アプリケーション動作確認結果"


path=r".\msedgedriver.exe"


# In[24]:



# In[12]:


# Microsoft Edgeを立ち上げ、urlを開く。
from selenium.webdriver.common.keys import Keys
from time import sleep
try:
    driver = Edge('./msedgedriver.exe', options=options)
    driver.get(url)
    sleep(3)
    
    # idを入力
    keyword_txb = driver.find_element('name', 'id')
    keyword_txb.send_keys('memes')
    driver.implicitly_wait(1) # seconds

    # passを入力
    keyword_txb = driver.find_element('name', 'pw')
    keyword_txb.send_keys('ymc001')
    driver.implicitly_wait(1) # seconds
    
    # enterを押下
    keyword_txb.send_keys(Keys.ENTER)
except Exception as e:
    driver.quit()
    driver.close()
    print(f'エラー：{e}')
    input('エンターキーを押してください。\nプログラムを終了します。\n')
finally:
    sys.exit
    




# In[ ]:




