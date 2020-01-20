from bottle import *
import sqlite3

@route('/kek')
def img(username):
    return template('frame/kek', username=username)


@route('/test_page')
def test_page():
    return template('frame/test')

@route('/fucking_form')
def form():
    return template('frame/fucking_form')

@route('/fucking_form', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if (username == '1') and (password == '1'):
        return img(username)
    else:
        return form()


run(host='localhost', port='1025', debug=True)