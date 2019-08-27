from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PageProcessor:
  def __init__(self):
    self.browser = webdriver.Chrome()
  
  def test(self, url):
    self.browser.get(url)
    sleep(5)
    html = self.browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    self.browser.close()
    return html


if __name__=="__main__":
  processor = PageProcessor()
  print(processor.test('https://google.com'))
