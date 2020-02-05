# -*- coding: utf-8 -*-

from selenium import webdriver

class MercadoLivre:
    def __init__(self, driver):
        self.driver = driver
        self.url =  'https://www.mercadolivre.com.br/'
        self.search_bar = 'as_word' # name
        self.btn_search = 'nav-search-btn' # class
        self.btn_ord = 'ui-dropdown__indicator' # class
        self.btn_menor_preco = 'Menor preço' # link text
        self.elements_result = 'results-item highlighted article grid item-info-height-127' # class for xpath

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
        self.driver.find_elements_by_class_name(
            self.btn_search)[0].click()

    def ordenar_busca(self):
        self.driver.find_elements_by_class_name(
            self.btn_ord)[0].click()
        self.driver.find_element_by_link_text(
            self.btn_menor_preco).click()

    def click_element(self):
        self.driver.find_elements_by_xpath(
            "//li[@class='"+self.elements_result+"']")[0].click()


ff = webdriver.Firefox()
g = MercadoLivre(ff)
g.navigate()
g.search('Sandalia feminina')
g.ordenar_busca()
g.click_element()
