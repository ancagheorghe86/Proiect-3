from .driver import Driver
from bdd.driver import Driver

class BasePage(Driver):
    def find(self, locator):
        '''locator va fi un tuplu cu parametrii pe care ii foloseam
        la functia find_element -> de exemplu (By.CSS_selector, "cjdved")
        "cjdved" este filtrul nostru

        metoda folosita pentru a cauta diferite imputuri in pagina
        sau :  self.driver.find_element(by=locator[0], value=locator[1])

        "*" related to Python Tuples
        "*" acest operator face legatura dintre ordinea elementelor in tuplu
        si implicit a valorii elementelor cu locatia in care aceste elemente
        sunt folosite'''

        return self.driver.find_element(*locator)
    def type(self, locator, text):
        # metoda folosita pentru a scrie text intr-un input
        # send_keys(text)

        element = self.find(locator)
        element.send_keys(text)




    def get_text(self, locator):
        element = self.find(locator)
        return element.text

    def button_click(self, locator):
        element = self.find(locator)
        element.click()


