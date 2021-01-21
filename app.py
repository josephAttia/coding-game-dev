@app.route('/home')
def home():
    return 'You are logged on!'


@app.route('/login',  methods=['GET', 'POST'])
def login():
    unsucsessful = "Incorrect Username/Password"
    successful = 'Login Sucsessful'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if(email):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                print(auth.get_account_info(user['idToken']))
                userInfo = auth.get_account_info(user['idToken'])
                print(userInfo['users']['emailVerified'])
                return render_template('userProfile.html' , userEmail = email)
            except:        
                return 'Incorrect Username/Password'
    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    successfulSignUp = "SignUp sucsessful"
    unsuccessfulSignUp = "SignUp unsucsessful"
    if request.method == 'POST':
        emailSignUp = request.form['emailS']
        passwordSignUp = request.form['passwordS']
        if(emailSignUp):
            user = auth.create_user_with_email_and_password(emailSignUp, passwordSignUp)
            auth.send_email_verification(user['idToken'])
            return redirect(url_for('login'))
        else:
            return 'Incorrect Email'
    return render_template('signup.html',  signupBad = unsuccessfulSignUp)

@app.route('/logout')
def logout():
    auth.signOut()
    return redirect(url_for('home'))

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Joseph'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'}, 
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title = 'Home', user = user, posts=posts) 


@app.route('/about') 
def about():
    return "<h1>About Page</h1>" 

@app.route('/aceTest')
def aceTest():
    return render_template('aceEditor.html')


if __name__ == "__main__":
     app.run(debug=True)
