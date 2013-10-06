from flask import Flask
import json
import test
import pull
app = Flask(__name__)
url = "http://18.111.27.86:8080/shot.jpg"
@app.route("/getFruit")
def getFruit():
	pull.pull_newest_image(url)
	pull.pull_newest_image(url)
	search = pull.get_newest_image()
	pot = test.scan_image(test.base, search)
	print "hi"
	return json.dumps(list(set(pot)))
@app.route("/setFruit")
def setFruit():
	pull.pull_newest_image(url)
	pull.pull_newest_image(url)	
	test.base = pull.get_newest_image()
	return ""
if __name__ == "__main__":
	app.run(debug = True)
