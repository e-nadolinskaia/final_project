from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
	page = ProductPage(browser,link)
	browser.implicitly_wait(10)
	page.open()
	page.add_product()
	page.solve_quiz_and_get_code()

def test_comparing_book_names(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
	page = ProductPage(browser,link)
	browser.implicitly_wait(10)
	page.open()
	page.add_product()
	page.solve_quiz_and_get_code()
	page.name_added_product_is_equal_name_in_message()

def test_compairing_basket_cost_and_product_price(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
	page = ProductPage(browser,link)
	browser.implicitly_wait(10)
	page.open()
	page.add_product()
	page.solve_quiz_and_get_code()
	page.cost_of_basket_equal_product_price()
	
