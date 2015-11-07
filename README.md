# InWebSy

===============================================================================

## InWebSy is an Interactive Web System which uses Interactive Systems formalism

===============================================================================
### Interactive Web System

State Space : X = {in, out} && x ∈ X

Inputs : U = { ('login',{'name':'Dinesh','pass':'dinnu93'}), ('logout',{'name':'Dinesh'}) } && u ∈ U

Outputs : H = { <br>
                 {'nameBox': '<input name="name" placeholder="Name" class="form-control"/>', 'passBox': '<input type="password" placeholder="Password" name="pass" class="form-control"/>', 'loginBox': '<input type="submit" class="btn btn-primary btn-block" value="Log In">'}, <br>
                {'helloText': 'Hello', 'name': 'Dinesh', 'logoutBox': '<a href="/logout" class="btn btn-primary">Log Out</a>'}<br>
              }

State Changer Function : F : X -> X , X' = F(x,u)

Output Function : H : X -> Y , Y' = H(x,u)

G -> F/H : X * U -> X * Y 


```python

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

```