import requests
import shutil
import time
import os
import urllib 

def pull_newest_image(url):
  response = requests.get(url)
  urllib.urlretrieve(url, "images/" + str(int(time.time())) + ".jpg")  

def get_newest_image():
  x = os.listdir("images/")
  x.sort()
  return "images/" + x[-1]

