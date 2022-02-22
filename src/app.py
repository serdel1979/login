from flask import Flask, redirect, render_template, request, url_for
from config import config

app=Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        print('post ',request.form['username'])
        print('post', request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    



if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()