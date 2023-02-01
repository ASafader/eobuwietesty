import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class DodawanieDoKoszyka(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.eobuwie.com.pl/")
        #zamknij alert o ciasteczkach
        zgoda = self.driver.find_element(By.CLASS_NAME, "e-button--type-primary.e-button--color-brand.e-consents-alert__button.e-button").click()

    def testDodanieDoKoszykaPoprawne(self):
        sleep(10)
        #uzytkownik klika w kategorie damskie
        self.driver.find_element(By.XPATH, "//ul[@id='mega-menu-list']/li[2]/a").click()
        #klikamy w pierwszy but
        self.driver.find_element(By.XPATH, "//ul[@class='products-list']/li[1]//a[@class='products-list__link']").click()
        #zapamiętaj nazwę buta
        nazwa_buta=self.driver.find_element(By.CLASS_NAME, 'e-product-name__model').text
        #klikamy wybierz rozmiar
        self.driver.find_element(By.CLASS_NAME, 'e-size-picker__select').click()
        #klikamy w pierwszy dostępny rozmiar
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@class='e-size-picker__option e-size-picker-option']").click()
        #dodaj do koszyka
        self.driver.find_element(By.XPATH, "//button[@data-testid='product-add-to-cart-button']").click()
        #kliknij w button przejdz do koszyka
        sleep(5)
        self.driver.find_element(By.XPATH, "//a[@data-testid='product-go-to-cart-link']").click()
        #sprawdzamy czy zalozenie jest poprawne (w koszyku znajduje sie jeden produkt) porownujemy wartosc otrzymana z oczekiwana
        #pobieramy element z wynikiem
        koszyk=self.driver.find_element(By.CLASS_NAME, 'cart__title')
        self.assertEqual(koszyk.text,'Koszyk (1)')
        #sprawdzamy czy nazwa buta w który kliknęliśmy jest taka sama jak nazwa buta w koszyku
        nazwa_buta_koszyk=self.driver.find_element(By.CLASS_NAME, 'cart-item__name-second').text
        self.assertEqual(nazwa_buta,nazwa_buta_koszyk)
        sleep(5)







if __name__ == '__main__':
    unittest.main()
