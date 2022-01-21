from flask import Flask, request, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


app = Flask(__name__)

app.config.from_pyfile('config.cfg')

mail = Mail(app)

s = URLSafeTimedSerializer('Thisisasercret!')



@app.route('/', methods=['GET','POST'])

def index():
	if request.method == 'GET':
		return '<form action="/" method="POST"><input name="email"><input type="submit"></form>'

	email = request.form['email']

	token = s.dumps(email, salt='email-confirm')

	msg = Message('HEALTH CHECK APP Confirm Email', sender='wutong9801@gmail.com', recipients=[email])

	link = url_for('confirm_email', token=token, _external=True)
#change here
	msg.body = 'HI! Dear User, \nThis is Health check app Team. \nHelp us secure your HC account by verifying your email {}. This let you access all of HC’s features.\nYour link is {}, click to verify and it is safe ,CUZ We are NO.1 in KOREA!ㅋㅋ'.format(email,link)

	mail.send(msg)

	return '<h1>The mail you entered is {}. The token is {}</h1>'.format(email, token)

@app.route('/confirm_email/<token>')

def confirm_email(token):
	try:
		email = s.loads(token, salt='email-confirm', max_age=3600)
	except SignatureExpired:
		return "<h1>The token is expired</h1>"
	print("the link has been clicked")
	return '<h1>The email is confirmed and you can use this email! The token is: {}</h1>'.format(token)
	return True






if __name__ == '__main__':

	app.run(debug=True)

















