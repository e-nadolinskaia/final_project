from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM_ELEMENT = (By.CSS_SELECTOR, '#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
	ADDING_LINK = (By.CSS_SELECTOR,'.btn-add-to-basket')
	MESSAGE_ADDED_BOOK_NAME = (By.CSS_SELECTOR, 'div[id="messages"] :nth-child(2) > strong')
	BOOK_NAME  = (By.CSS_SELECTOR, '.product_main h1')
	BASKET_COST = (By.CSS_SELECTOR,'div[id="messages"] :nth-child(3) p > strong')
	PRODUCT_PRICE = (By.CSS_SELECTOR,'.product_main :nth-child(2)')