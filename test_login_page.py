from .pages.login_page import LoginPage
import time

def test_guest_can_see_login_form(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
	page = LoginPage(browser,link)
	page.open()
	page.should_be_login_form()

def test_guest_can_see_registration_form(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
	page = LoginPage(browser,link)
	page.open()
	page.should_be_register_form()


def test_login_in_url(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
	page = LoginPage(browser,link)
	page.open()
	page.should_be_login_url()