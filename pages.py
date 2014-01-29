_RESPONSE ="""
			<!doctype>
			<html>
				<head>
					<title>Your Details</title>
				</head>
				<body>
					<p>Thanks for giving me your info</p>
					<p>
					Your name: {}. <br />
					Your age: {}. <br />
					Your location: {}. <br />
					</p>
					<p> I stole your identity :) lol </p>
				</body>
			</html>
"""


_LOGIN_PAGE = """
<!doctype html>
<html>
	<head>
		<title>Please log in </title>
	</head>
	<body>
	<p> Please log in to use this system:</p>
		<form method = "POST" action ="/login">
			Username:<input type = "TEXT" name = "userid"/><br />
			Password:<input type = "PASSWORD" name = "passwd"/><br />
			
			   <select name='usertype'>
                <option value="crew">Booking Crew</option>
                <option value="team">Departures Team</option>
                <option value="pilot">Pilot</option>
            </select><br />
			<input type ="SUBMIT" value = "Sign in" /><br />
			If you have yey to make an account please visit <a href =  /register >our registration page</a>
	</body>
</html>
"""

_REG = """
<!doctype html>
<html>
	<head>
		<title>Please Register </title>
	</head>
	<body>
	<p> Please log in to use this system:</p>
		<form method = "POST" action ="/register">
			Username:<input type = "TEXT" name = "userid"/><br />
			Password:<input type = "PASSWORD" name = "passwd"/><br />
			
			   <select name='usertype'>
                <option value="crew">Booking Crew</option>
                <option value="team">Departures Team</option>
                <option value="pilot">Pilot</option>
            </select><br />
			<input type ="SUBMIT" value = "Register" />
	</body>
</html>
"""


_ADMIN = """
<!doctype html>
<html>
	<body>
	<form method = "POST" action ="/moveUsers">
	<input type ="SUBMIT" value = "Allow User Reg" />
	</form>
	</body>
</html>
"""

_TEAM ="""
<!doctype html>
<html>
	<head>
	<title>Logged In</title>
	</head>
	<body>
	You are logged in as a "Team"
	</body>
</html>
"""
_CREW ="""
<!doctype html>
<html>
	<head>
	<title>Logged In</title>
	</head>
	<body>
	You are logged in as a "Crew"
	</body>
</html>
"""