from selenium import webdriver

class MercadoLivre:
    def __init__(self, driver):
        self.driver = driver
        self.url =  'https://www.mercadolivre.com.br/'
        self.search_bar = 'as_word' # name
        self.btn_search = 'nav-search-btn' # class

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
        self.driver.find_elements_by_class_name(
            self.btn_search)[0].click()



ff = webdriver.Firefox()
g = MercadoLivre(ff)
g.navigate()
g.search('Fone de ouvido')
