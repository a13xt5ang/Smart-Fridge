import requests
import shutil
import time
import os
url = 'http://10.189.1.36:8080/shot.jpg' #needs to be set before demo
def pull_newest_image(url):
	response = requests.get(url, stream = True)
	with open("images/" + str(int(time.time())) + ".jpg", 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response
pull_newest_image(url)
def get_newest_image():
	x = os.listdir("images/")
	x.sort()
	return "images/" + x[-2]
print get_newest_image()
