import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SearchTest(unittest.TestCase):
  def setUp(self) -> None:
    # Установка английского языка, для предотвращения изменения положения элементов
    self.options = webdriver.ChromeOptions()
    self.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    self.driver = webdriver.Chrome(options=self.options)
    self.driver.get('http://google.com/ncr')
  
  def test_search(self):
    # Проверка того, что первая ссылка ведет на https://selenide.org/
    input_field = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') 
    input_field.send_keys('selenide')
    input_field.send_keys(Keys.ENTER)
    time.sleep(1)
    first_entry = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
    url = first_entry.get_attribute('href')
    assert url == 'https://selenide.org/'

    # Проверка того, что первая картинка связана с selenide
    images_button = self.driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
    images_button.send_keys(Keys.ENTER)
    time.sleep(1)
    first_image = self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    image_alt = first_image.get_attribute('alt')
    assert 'selenide' in image_alt.lower()

    # Возвращение на страницу с результатом запроса, и проверка того что первая ссылка ведет на https://selenide.org/
    all_button = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
    all_button.send_keys(Keys.ENTER)
    time.sleep(1)
    first_entry = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
    url = first_entry.get_attribute('href')
    assert url == 'https://selenide.org/'

  def tearDown(self) -> None:
    self.driver.close()

if __name__ == '__main__':
  unittest.main()