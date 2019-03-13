from selenium_fixture import *
from application import *
import data


def test_create_user(app):
  app.go_to_page('https://dev.%%%%%.com')
  app.login(data.auth_data.get('email'), data.auth_data.get('password'))
  app.go_to_section('Administration')
  app.add_new_user(data.user1.get('First Name'), data.user1.get('Last Name'),
                   data.user1.get('Email'), data.user1.get('Password'),
                   data.user1.get('Country'), data.user1.get('Role'),
                   data.user1.get('Store cluster'), data.user1.get('Store'))
  app.check_adding_user(data.user1.get('First Name'), data.user1.get('Last Name'),
                        data.user1.get('Email'), data.user1.get('Country'),
                        data.user1.get('Role'), data.user1.get('Store cluster'),
                        data.user1.get('Store'))
  app.delete_user(data.user1.get('First Name'), data.user1.get('Last Name'),
                  data.user1.get('Role'))


