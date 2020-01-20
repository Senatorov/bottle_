from bottle import *
import sqlite3

@route('/greeting')
def greeting(username):
    return template('frame/greet', username=username)

@route('/')
def authorization():
    return template('frame/authorization')

@route('/', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if (username == '1') and (password == '1'):
        return greeting(username)
    else:
        return authorization()


run(host='localhost', port='1025', debug=True)