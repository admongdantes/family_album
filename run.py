# _*_ coding: utf-8 _*_

import datetime
import os
from MyVideo import MyVideo

from flask import Flask, render_template, url_for, redirect, g, current_app, request, session
app = Flask(__name__, static_folder = 'static')

app.secret_key = 'sjfsefhsehfsjefsefsefsefsefsefsefs'

def login():
	if session.get('userId'):
		return redirect(url_for('main'))
	
	if request.method == 'POST':
		userId = request.form['userId']
		passwd = request.form['passwd']

		if userId == 'dantes' and passwd == 'dantes1234':
			session['userId'] = userId;
			return redirect(url_for('main'))
		else:
			return render_template('login.html', the_date = datetime.date.today())
	else:
		return render_template('login.html', the_date = datetime.date.today())
	
mediaFileList = []
def main():
	session_check()
	global mediaFileList
	mediaList = []
	myVideoList = []
	#pageIndex = request.form['pageIndex']
	pageIndex = request.args.get('pageIndex')
	if pageIndex is None:
		pageIndex = '1'

	pageIndex = int(pageIndex)
	
	if not mediaFileList:
		mediaFileList = getFileList('/media/pi/UFD-T7 38AD', ['.mp4'])
		#mediaFileList.extend(getFileList('/media/pi/UFD-T7 38AD', ['.mp4']))
		
	for media in mediaFileList:
		mediaList.append(os.path.join('/static/media1', os.path.split(media)[1]))
		myVideoList.append(MyVideo(media))

	myVideoList = sorted(myVideoList, key=lambda x: x.mtime)
	pageUnit = 8
	start = (pageIndex-1) * pageUnit
	end = start + pageUnit
	myVideoList = myVideoList[start:end]
	for d in myVideoList:
		print(str(d.mtime))

	pageMap = {'pageIndex':pageIndex, 'pageUnit':pageUnit, 'pageSize':5, 'pageTotal':len(mediaFileList)}

	return render_template('main.html', result=mediaList, myVideoList=myVideoList, pageMap=pageMap)

def logout():
	session.clear()
	return redirect(url_for('login'))

def session_check():
	if not session.get('userId'):
		return redirect(url_for('login'))
	
@app.before_request
def before_request():
	g.my = "before_request"
	print('before request')

@app.teardown_request
def teardown_request(exception):
	print(app.app_context())
	print('end request')

@app.route('/hi')
def hi():
	return 'hi!! ' + g.my

def getFileList(dir, extfilter = None):
        fileList = []
        for dirName, subDirList, files in os.walk(dir):
                for filename in files:
                        if not extfilter is None:
                                if os.path.splitext(filename)[1] in extfilter:
                                        full_filename = os.path.join(dirName, filename)
                                        fileList.append(full_filename)
                        else:
                                full_filename = os.path.join(dirName, filename)
                                fileList.append(full_filename)  
        return fileList


#print(getFileList('/home/pi/webapps', ['.js', '.pack']))
#print(getFileList('/media/pi/UFD-T7 38AD', ['.mp4']))

app.add_url_rule('/login', 'login', login, methods = ['GET', 'POST'])
app.add_url_rule('/main', 'main', main, methods = ['GET'])
app.add_url_rule('/logout', 'logout', logout, methods = ['GET'])
	
if __name__ == "__main__":
	app.debug = True
	app.use_reloader = True
	app.run(host='0.0.0.0')


