# Interactive Web System

# State Space : X = set([in, out]) x belongsTo X
# Inputs : U = set([('login',{'name':'Dinesh','pass':'dinnu93'}), ('logout',{'name':'Dinesh'})]) u belongsTo U
# Outputs : H = set([{'nameBox': '<input name="name"/>','passBox': '<input type="password" name="pass" />','loginBox':'<input type="submit" value="Log In">'},('HelloText',)])
# State Changer Function : F : X -> X , X' = F(x,u)
# Output Function : H : X -> Y , Y' = H(x,u)
# G -> F/H : X * U -> Y 
from flask import *

X = ['in','out']
U = [('login',{'name':'Dinesh','pass':'dinnu93'}), ('logout',{})]
H = [
        {'nameBox': '<input name="name" placeholder="Name" class="form-control"/>', 'passBox': '<input type="password" placeholder="Password" name="pass" class="form-control"/>', 'loginBox': '<input type="submit" class="btn btn-primary btn-block" value="Log In">'}, 
        {'helloText': 'Hello', 'name': 'Dinesh', 'logoutBox': '<a href="/logout" class="btn btn-primary">Log Out</a>'}
    ]
def F_H(x,u):
	if x == X[0] and u == U[1]:
		return (X[1], H[0])
	elif x == X[1] and u == U[0]:
		return (X[0], H[1])
	else:
		return 'Some Error Occured'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		name = request.form['name']
		password = request.form['pass']
		x = 'out'
		u = ('login',{'name': name,'pass': password})
		output = F_H(x,u)
		if output == 'Some Error Occured':
			return redirect(url_for('login'))
		else:
			output = output[1]
			return render_template('welcome.html')%(output['helloText'], output['name'], output['logoutBox'])
	else:
		output = H[0]
		return render_template('index.html')%(output['nameBox'], output['passBox'], output['loginBox'])

@app.route('/logout')
def logout():
	return redirect(url_for('login'))

if __name__ == "__main__":
    app.run()





