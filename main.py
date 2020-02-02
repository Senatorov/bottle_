from bottle import *
import sqlite3

@route('/')
def authorization_fail():
    return template('frame/authorization_fail')


@route('/')
def authorization():
    return template('frame/authorization')

@route('/', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    sign = request.forms.get('Sign')
    registr = request.forms.get('Registr')

    if sign:
        if (username == '1') and (password == '1'):
            return greeting(username)
        else:
            return authorization_fail()

    if registr:
        return regisration()



@route('/greeting')
def greeting(username):
    return template('frame/greet', username=username)

@route('registration')
def regisration():
    return template('frame/registr')

@route('registration')
def f_registration_username():
    return template('frame/registr_fail_name')

@route('registration')
def f_registration_password():
    return template('frame/registr_fail_password')

@route('/registration', method='POST')
def register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    r_password = request.forms.get('r_password')

    if username == '!!!': ######################################################### SQLite3 name == username!!!!######################################################
        return f_registration_username()
    elif password != r_password:
        return f_registration_password()
    else:
        return authorization()







run(host='localhost', port='8080', debug=True)
