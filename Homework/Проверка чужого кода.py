class OfferPage(BasePage):
    def create_offer_from_main_page_widget(self):
        try:
            if self.is_element_displayed(*OfferPageLocators.IS_OFFER_IN_WIDGET):
                create_offer_filled_widget = self.get_element(*OfferPageLocators.CREATE_OFFER_FROM_FILLED_WIDGET)
                create_offer_filled_widget.click()
                print('try')
        except:
            if self.is_element_displayed(*OfferPageLocators.EMTPY_OFFER_WIDGET):
                create_offer_empty_widget = self.get_element(*OfferPageLocators.CREATE_OFFER_FROM_EMPTY_WIDGET)
                create_offer_empty_widget.click()
                print('except')



try:
    element = driver.find_element(*OfferPageLocators.CREATE_OFFER_FROM_FILLED_WIDGET)

except:
    element = driver.find_element(*OfferPageLocators.CREATE_OFFER_FROM_FILLED_WIDGET)

try:
    element_empty.click()

except:
    element_full.click()