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
        self.elements_result = 'searchResults' # id
        self.product_img = 'lazy-load' #class img xpath
        self.btn_grid_view = 'ico grid' # class

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
        self.driver.find_elements_by_class_name(
            self.btn_search)[0].click()

    def sort_search(self):
        self.driver.find_elements_by_class_name(
            self.btn_ord)[0].click()
        self.driver.find_element_by_link_text(
            self.btn_menor_preco).click()

    def set_grid_view(self):
        try:
            self.driver.find_element_by_xpath(
                "//a[@class='"+self.btn_grid_view+"']").click()
        except Exception:
            pass

        try:
            btn_grid_view = 'ico view-option-grid selected'
            self.driver.find_element_by_xpath(
                "//div[@class='"+self.btn_grid_view+"']").click()
        except Exception:
            pass


    def click_first_element(self):
        self.driver.find_elements_by_xpath(
            "//li[@class='"+self.elements_result+"']")[0].click()

    def _get_img_prod(self):
        return self.driver.find_element_by_xpath(
            "//img[@class='"+self.product_img+"']")

    def get_all_elements_result(self):
        ol_list= self.driver.find_element_by_id(self.elements_result)
        items = ol_list.find_elements_by_tag_name("li")
        for item in items:
            text = item.text
            print text

    def get_item_describe(self):
        #print("alo")
        src_prod = self._get_img_prod().get_attribute('src')
        return src_prod
        #print(src_prod)
        #print("tchau")

ff = webdriver.Firefox()
g = MercadoLivre(ff)
g.navigate()
g.search('Nintendo switch')
g.sort_search()
g.set_grid_view()
g.get_all_elements_result()

# save product_img
# ff.get(g.get_item_describe())
# ff.save_screenshot("./prod_img/prod1.png")
