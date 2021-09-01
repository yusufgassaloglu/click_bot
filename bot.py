from selenium import webdriver
from selenium.webdriver.common import proxy
from selenium.webdriver.common.proxy import Proxy,ProxyType
import time
import json

with open("proxies.json") as file: # You can use different proxy list.
     prxy = json.load(file)

ip_num = 0
proxy_num = 0
count = 0

while count < 1075: # There are 1075 data in proxies.json. 
     ip = prxy["proxies"][ip_num]["ip"] # ATTENTION -- If you have changed the JSON file you have to change this code otherwise the code will not work.
     port = prxy["proxies"][proxy_num]["port"] # ATTENTION -- If you have changed the JSON file you have to change this code otherwise the code will not work.
     print(ip+":"+port)
     print(count + 1)
     ip_num += 1
     proxy_num += 1
     count += 1

     try:
          proxy_ip_port = ip+":"+port 

          proxy = Proxy()
          proxy.proxy_type = ProxyType.MANUAL
          proxy.http_proxy = proxy_ip_port
          proxy.ssl_proxy = proxy_ip_port

          capabilities = webdriver.DesiredCapabilities.CHROME # I am using CHROME
          proxy.add_to_capabilities(capabilities)

          driver = webdriver.Chrome("\webdrivers/chromedriver", desired_capabilities=capabilities) #You need to download and install webdriver. I am using CHROME.
          driver.get("")# Fill in the blank with the URL of the website you want to be clicked.
     except:
          print("error")
     
     time.sleep(10) # Code waits 10 seconds before changing proxy. You can change the waiting time.
     driver.quit()

# Fake clicks are not real viewiers, visitors, etc. 
# You can do better without fake click.

# © yusufgssl 2021 -- https://github.com/yusufgssl -- https://yusufgssl.github.io/
     



