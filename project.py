from flask import Flask, request,make_response,session, redirect,url_for,render_template

_PORT = 9001
_HOST = '0.0.0.0'
_DEBUG = True

import pages
flights = { '09:35': 'Freeport',
'17:00': 'Freeport',
'19:00': 'Freeport',
'09:55': 'West End',
'10:45': 'Treasure Cay',
'11:45': 'Rock Sound',
'17:55': 'Rock Sound',
'12:00': "Arthur's Town", }


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
		

		
		
@webapp.route('/register', methods=["GET","POST"])
def register():
	if request.method == "GET":
		return pages._REG
	else:
		u = request.form['userid']
		p = request.form['passwd']
		t = request.form['usertype']
					
		f = open('namesForReg.txt', 'a')
		print(u,p,t, sep=',', file=f)
		f.close()
		return  redirect(url_for("login"))
		
		
@webapp.route('/moveUsers', methods=["GET","POST"])
def moveUsers():
		
			f = open('registeredNames.txt', 'a')
			g = open('namesForReg.txt', 'r')
			# Now, let's find the bosses (admins) in the data.
			print()
			for line in g:
				u, p, t = line.strip().split(',')
				print(u,p,t, sep=',', file=f)
			f.close()
			g.close()
			
			g = open('namesForReg.txt', 'w')
			s = "null,null,null"
			print(s,file=g)
			g.close()
			return redirect(url_for("login"))

			
@webapp.route('/pilot', methods=["GET","POST"])
@checkLogin
def pilot():
	times =[]
	for dest in sorted(set(flights.values())):
		times=[time for time in flights if flights[time] == dest]
	return render_template('pilot.html',title = 'Pilot', list = times) 


@webapp.route('/crew', methods=["GET","POST"])
@checkLogin
def crew():
	times =[]
	for time in sorted(flights, key=lambda k: (flights[k], k)):
		times.append((flights[time], '\t', time))
	return render_template('crew.html',title = 'Crew', list = times)


@webapp.route('/team', methods=["GET","POST"])
@checkLogin
def team():
	times =[]
	for time, destination in sorted(flights.items()): 
		times.append((time, destination))
	return render_template('team.html',title = 'Team', list = times)


@webapp.route('/login', methods=["GET","POST"])
def login():
	
	if request.method == "GET":
		return pages._LOGIN_PAGE
	else:
		u_check = request.form['userid']
		p_check = request.form['passwd']
		t_check = request.form['usertype']
		
		if u_check == 'admin' and p_check == 'password':
			session['logged-in'] = True
			return pages._ADMIN
		
		validUser = False

		f = open('registeredNames.txt','r')
		for line in f:
			u, p, t = line.strip().split(',')
			if u == u_check and p == p_check and t_check == t:
				validUser = True
		f.close()
		if validUser:
			session['cu'] = u_check
			session['cp'] = p_check
			session['ct'] = t_check
			session['logged-in'] = True
			if(session['ct'] == "pilot"):
				return redirect(url_for('pilot'))
			elif(session['ct'] == "team"):
				return redirect(url_for('team'))
			elif(session['ct'] == "crew"):
				return redirect(url_for('crew'))
		else:
			return redirect(url_for('login'))
			
			
@webapp.route('/logout')
@checkLogin
def do_logout():
		session.pop('logged-in',None)
		session.pop('cu', None)
		session.pop('cp', None)
		session.pop('ct', None)
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
	

webapp.secret_key = b'\xe6N\xbd\xaf\xd0W\x85\xd7U\x14\xb5nL\x85\xf5\xfew}r\xf80\xa5S0\xf0\xe6\xa9\x1es\x83\x8a}fiO\xd7\xed$2O\x95r\xee\xdb\xca\xe6\x07\xe9'
webapp.run(host= _HOST,debug=_DEBUG,port=_PORT)

