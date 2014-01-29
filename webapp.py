from flask import Flask, request,make_response,session, redirect,url_for,render_template

_PORT = 9001
_HOST = '0.0.0.0'
_DEBUG = True

import pages

from functools import wraps

webapp = Flask('__main__')

def checkLogin(func):

	@wraps(func)
	def wrapped_function(*args,**kwargs):
		if 'logged-in' in session:
			return(func(*args,**kwargs))
		else:
			return render_template('nologin.html',title = 'Authorisation Needed', nologin = url_for('login'))
	return wrapped_function
		
@webapp.route('/tell',methods=["GET","POST"])
@checkLogin
def tellform():
	if 'logged-in' in session:
		if request.method=="GET":
			return render_template('simple.html', title = "A Simple Form")
		else:
			res = pages._RESPONSE.format(request.form['tellname'],
										request.form['tellage'],
										request.form['telllocation'])
			#set the cookie for last visitor 
			cookiedResponse = make_response(res)
			cookiedResponse.set_cookie('lastVisitor', request.form['tellname'])
			return cookiedResponse
	else:
		return pages._NO_LOGIN.format(url_for("login"))
		
		
@webapp.route('/login', methods=["GET","POST"])
def login():
	if request.method == "GET":
		return pages._LOGIN_PAGE
	else:
		u = request.form['userid']
		p = request.form['passwd']
		if u == 'admin' and p == 'admin':
			session['logged-in'] = True
			return redirect(url_for("helloWorld"))
		else:
			session.pop('logged-in',None)
			return redirect(url_for("login"))

@webapp.route('/logout')
@checkLogin
def do_logout():
		session.pop('logged-in',None)
		return redirect(url_for('login'))
		
			
@webapp.route('/')
@checkLogin
def helloWorld():
	lastPerson = request.cookies.get('lastVisitor')
	if not lastPerson:
		lastPerson = 'nobody'
	return 'The last person to visit was called: {}.'.format(lastPerson)
	
@webapp.route('/bye')
def byebye():
	return "Bye bye from Webapp!"

@webapp.route('/config')
def showConfig():
		return "Here is the config. Host: {}, Port {},  Debug: {}.".format(_HOST,_PORT,_DEBUG)
	

@webapp.route('/hi/')
@webapp.route('/hi')
@webapp.route('/hi/<who>')
def sayHi(who= "user"):
	return "Hello {}.".format(who)	

	
@webapp.route('/remotehello')
@checkLogin
def rh():
	return 'Darren, your a nob, yes you Darren........you nob'
	
@webapp.route('/new')
@checkLogin
def sayNew():
	return "Hi I'm new!"

webapp.secret_key = b'\xe6N\xbd\xaf\xd0W\x85\xd7U\x14\xb5nL\x85\xf5\xfew}r\xf80\xa5S0\xf0\xe6\xa9\x1es\x83\x8a}fiO\xd7\xed$2O\x95r\xee\xdb\xca\xe6\x07\xe9'
webapp.run(host= _HOST,debug=_DEBUG,port=_PORT)

