import requests 
from bs4 import BeautifulSoup 

class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'}
        self.response=requests.get(url=self.url,headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response,'lxml')

    def product_title(self):
        title=self.soup.find("span",{'class':'VU-ZEz'})
        if title:
            return title.text
        return 'tag not found'
        pass

    def product_price(self):
        price=self.soup.find("div",{'class':'Nx9bqj'})
        if price:
            return price.text
        return 'tag not found'
        pass

    

device_url='https://www.flipkart.com/apple-iphone-16-white-128-gb/p/itm7c0281cd247be'
device=PriceTracer(url=device_url)
print(device.product_title())
print(device.product_price())