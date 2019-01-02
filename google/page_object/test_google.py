from selenium_fixture import *

def test_login(app):
    app.go_to_gmail()
    app.switch_language()
    app.autorization('auto.python.ep@gmail.com', 'automationPython13')

def test_recovery_password(app):
    app.go_to_gmail()
    app.recovery_password('auto.python.ep@gmail.com')





