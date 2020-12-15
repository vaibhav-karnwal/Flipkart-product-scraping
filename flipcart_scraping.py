import requests
from bs4 import BeautifulSoup
import pandas as pd

products=[]
prices=[]
stars=[]
ratings=[]

page= requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DHP")
    
soup = BeautifulSoup(page.content, "html.parser")
product=soup.find_all('div',attrs={'class':'_2pi5LC col-12-12'})

for a in product:
    product_names=a.find_all('div', attrs={'class':'_4rR01T'})
    for name in product_names:
        products.append(name.get_text(strip=True))
    product_prices=a.find_all('div', attrs={'class':'_30jeq3 _1_WHN1'})
    for price in product_prices:
        prices.append(price.get_text(strip=True))
    product_stars=a.find_all('div', attrs={'class':'_3LWZlK'})
    for star in product_stars:
        stars.append(star.get_text(strip=True))
    product_ratings=a.find_all('span', attrs={'class':'_2_R_DZ'})
    for rating in product_ratings:
        ratings.append(rating.get_text(strip=True))
        
df=pd.DataFrame({'Product Name':products,'Price':prices, 'Star':stars ,  'Rating & Reviews':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')