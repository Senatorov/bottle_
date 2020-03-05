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
        req_db = "SELECT * FROM UsersInfo WHERE Name='" + username + "' AND Password='" + password + "'"
        con = sqlite3.connect('DataBase_site.db')
        cursorObj = con.cursor()
        cursorObj.execute(req_db)
        data = cursorObj.fetchall()
        cursorObj.close()
        if len(data) == 1:
            return greeting(username)
        else:
            return authorization_fail()

    if registr:
        return regisration()



@route('/greeting')
def greeting(username):
    return template('frame/greet', username=username.title())

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

    req_nm = "SELECT * FROM UsersInfo WHERE Name ='" + username + "'"
    con = sqlite3.connect('DataBase_site.db')
    cursorObj = con.cursor()
    cursorObj.execute(req_nm)
    data_name = cursorObj.fetchall()
    cursorObj.close()


    if len(data_name) > 0:
        return f_registration_username()
    elif password != r_password:
        return f_registration_password()
    else:
        command = 'INSERT INTO UsersInfo VALUES("' + username + '","' + password + '")'
        # cursorObj.execute('INSERT INTO UsersInfo VALUES("Nikolay","qwerty123")')
        con = sqlite3.connect('DataBase_site.db')
        cursorObj = con.cursor()
        cursorObj.execute(command)
        con.commit()
        cursorObj.close()

        return authorization()







if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    run(host='0.0.0.0', port=port)

# run(host='localhost', port='8080', debug=True)
