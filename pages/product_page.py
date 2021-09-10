from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product(self):
		adding_link = self.browser.find_element(*ProductPageLocators.ADDING_LINK)
		adding_link.click()

	def name_added_product_is_equal_name_in_message(self):
		name_added_book_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_BOOK_NAME)
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
		assert name_added_book_in_message.text == book_name.text, "Name ot the book in message is not equal name of added book!"


	def cost_of_basket_equal_product_price(self):
		cost_of_basket_in_message = self.browser.find_element(*ProductPageLocators.BASKET_COST)
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		assert cost_of_basket_in_message.text == product_price.text, "The cost of the basket is not equal product price!"