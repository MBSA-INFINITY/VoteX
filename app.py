from flask import Flask, request, session, redirect,url_for, render_template, flash, abort
import os
from database.auth import auth 
from database.db import users_collection

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

exempted_endpoints = ['static','login','signup']


@app.route("/signup", methods = ['GET','POST'])
def signup():
    if request.method=='POST':
        name = request.form.get("name")
        username = request.form.get("email")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        user_details = {"name": name,"email": username}
        if password == repassword:
            if len(password)>=6:
                try:
                    _user_ = auth.create_user_with_email_and_password(username ,password)
                    auth.send_email_verification(_user_['idToken'])
                    user_details['merchant_id'] = _user_['localId']
                    user_details['verified_voter'] = False
                    user_details['verified_candidate'] = False
                    user_details['applied_for_kyc'] = False
                    users_collection.insert_one(user_details)
                    return render_template("success.html")
                except Exception as e:
                    return redirect(url_for('login'))
            else:
                flash('Password is less than 6 characters!')
                return redirect("/signup")
        else:
            flash('Both Passwords do not match!')
            return redirect("/signup")
    return render_template("signup.html")

@app.route("/login",methods = ['GET','POST'] )
def login():
    if request.method == 'POST':
        data = dict(request.form)
        email = data.get("email")
        password = data.get("password")
        user_details = users_collection.find_one({"email": email},{"_id": 0})
        if user_details:
            user = auth.sign_in_with_email_and_password(email ,password)
            access_token = user['idToken']
            acc_info = auth.get_account_info(access_token)
            print(acc_info)
            if not acc_info.get("users")[0].get("emailVerified"):
                abort(500,{"message": f"{email} is not verified!"})
            user_details = users_collection.find_one({"email": email, "merchant_id": user['localId']},{"_id": 0})
            if user_details:
                session['user'] = user['localId']
                return redirect("/")     
            else:
                abort(500,{"message": "Username or Password is Invalid!!"})

        else:
            flash("User doesn't exist!")
            return redirect("/login")
    if 'user' in session:
        return redirect("/")
    return render_template("login.html")


@app.route("/")
def dashboard():
    user_details = users_collection.find_one({"merchant_id": session['user']},{"_id":0})
    return render_template('dashboard.html',user_details=user_details)


@app.route("/logout", methods = ['GET','POST'])
def logout():
    session.pop('user')
    return redirect("/login")


@app.before_request
def before_request_func():
    if request.endpoint in exempted_endpoints:
        return 
    if 'user' not in session:
        return redirect(url_for('login'))
    

if __name__ == '__main__':
    app.run(debug=True)