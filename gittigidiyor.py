#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:34:07 2021

@author: Turayaraz
"""

from selenium import webdriver
import time
import unittest

path = "/Users/Turayaraz/desktop/chromedriver/chromedriver"
browser = webdriver.Chrome(executable_path=path)

class test_gittigidiyor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
     
        link ="http://www.gittigidiyor.com"
        browser.get(link)
        time.sleep(1)
        
    def test001_searchProduct(self):

        browser.find_element_by_css_selector("#__next > main > div:nth-child(2) > section.tyj39b-0.iqtPYy > section.tyj39b-4.jZoSqD > a > span").click()
        time.sleep(1)
        browser.find_element_by_tag_name("input").send_keys("bilgisayar")
        time.sleep(1)
        browser.find_element_by_xpath("//span[text()='BUL']").click()
        time.sleep(2)
        
    def test002_secondPage(self):
        scroll = browser.find_elements_by_xpath("//a[@title='2. sayfa']")
        for kaydir in scroll:
            browser.execute_script("arguments[0].scrollIntoView();", kaydir)
            browser.find_element_by_xpath("(//span[text()='2'])[2]").click()
            time.sleep(5)
        if  browser.current_url == "https://www.gittigidiyor.com/arama?k=bilgisayar&sf=2":
            time.sleep(1)
        else:
            browser.get("https://www.gittigidiyor.com/arama?k=bilgisayar&sf=2")
            time.sleep(1)
        
    def test003_ClickProduct(self):
        browser.find_element_by_xpath('//*[@id="__next"]/main/div[2]/div/div/div[2]/div/div[3]/div[3]/ul/li[2]/article/div[2]/a').click()
        time.sleep(1)
        fiyat = browser.find_element_by_xpath("//div[@id='sp-price-lowPrice']")
        dosya = open("fiyat.txt","w")
        dosya.write(fiyat.text)
        dosya.close()
        time.sleep(1)
        
    def test004_AddToBasket(self):
        browser.find_element_by_css_selector("#add-to-basket").click()
        time.sleep(1)
        browser.find_element_by_xpath("//div[contains(@class,'basket-container robot-header-iconContainer-cart')]").click()
        time.sleep(1)
        
    def test005_ComparePrice(self):
        sepet_fiyat = browser.find_element_by_xpath("//div[@class='total-price']//strong[1]").text
        with open("fiyat.txt","r") as dosya:
            oku = dosya.read()      
        if sepet_fiyat == oku:
            print("Seçilen ürün ile sepetteki ürün fiyatları aynı")
        else:
            print("Seçilen ürün ile sepetteki ürün fiyatları farklı")
            
    def test006_numberOfProduct(self):
        browser.find_element_by_xpath("//div[@class='gg-input gg-input-select ']//select[1]").send_keys("2")
        time.sleep(2)
        sepet_fiyat = browser.find_element_by_xpath("//div[@class='total-price']//strong[1]").text
        with open("fiyat.txt","r") as dosya:
            oku = dosya.read()
            sepet_fiyat = sepet_fiyat.replace('.', '')
            sepet_fiyat = sepet_fiyat.replace(',', '.')
            oku = oku.replace('.', '')
            oku = oku.replace(',', '.')
            sepet_fiyat = sepet_fiyat.replace(' TL', '')
            oku = oku.replace(' TL', '')
        if  float(sepet_fiyat) == float(oku)*2:
            print("2 Adet Ürün seçtiniz")
        else:
            print("2 adet ürün seçilemedi")
        time.sleep(3)            
            
    def test007_clearBasket(self):
        browser.find_element_by_xpath("//a[@class='btn-delete btn-update-item']//i").click()
        time.sleep(3)
        sil = browser.find_element_by_xpath("//div[@id='empty-cart-container']/div[1]/div[1]/div[1]/div[2]/h2[1]")
        if sil.text == "Sepetinizde ürün bulunmamaktadır.":
            print("Sepetinizdeki ürünler silindi")
        else:
            print("Sepetinizde ürünler var")

if __name__ == '__main__':
    unittest.main()
browser.quit()