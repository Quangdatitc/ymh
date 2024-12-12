# 更新履歴
# 1.2 220902 webdriverを用意しなくてもいいように
# 1.2.1 221101 configparser不使用 url指定に 情シス監視モニタ用

import sys
import os
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager # ドライバーの自動更新

# エラー「システムに接続されたデバイスが機能していません。」の回避
#参考：https://miya-mitsu.com/python-0x1ferror/
from msedge.selenium_tools import Edge,EdgeOptions
options = EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True

url='http://10.145.156.49:8787/motionboard/main?mbid=fidpafgjifl3ja6zo3aaaafuklpzu&boardpath=/アクションボード/ＭＥ製造部生産課/製造技術課/端末稼働監視'

# Microsoft Edgeを立ち上げ、urlを開く。
from selenium.webdriver.common.keys import Keys
from time import sleep
try:
    os.environ['WDM_SSL_VERIFY'] = 'false' # これでEdgeChromiumDriverManagerを使える

    driver = webdriver.Edge(EdgeChromiumDriverManager().install()) # options=options)
    driver.implicitly_wait(10) # seconds
    driver.get(url)
    
    # idを入力
    keyword_txb = driver.find_element('name', 'id')
    keyword_txb.send_keys('memes')

    # passを入力
    keyword_txb = driver.find_element('name', 'pw')
    keyword_txb.send_keys('ymc001')
    
    # enterを押下
    keyword_txb.send_keys(Keys.ENTER)
except Exception as e:
    driver.close()
    print(f'エラー：{e}')
    input('エンターキーを押してください。\nプログラムを終了します。\n')
finally:
    sys.exit # コンソールを閉じる
