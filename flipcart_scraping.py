import requests
from bs4 import BeautifulSoup
import pandas as pd

products=[]
prices=[]
brands=[]
discounts = []

page= requests.get("https://www.flipkart.com/womens-ethnic-sets/pr?sid=clo,cfv,itg,tys&offer=nb:mp:10b7629130&marketplace=FLIPKART&restrictLocale=true&fm=personalisedRecommendation%2FC2&iid=R%3Ato%3Bpt%3Ahp%3Buid%3A1e2576c3-3cb9-11eb-a129-c5bd2430d0b6%3B.cid%3AS_F_N_clo_cfv_itg_tys__o_nb_mp_10b7629130__NONE_ALL%3Bnid%3Aclo_cfv_itg_tys_%3Bet%3AS%3Beid%3Aclo_cfv_itg_tys_%3Bmp%3AF%3Bct%3Ao%3B&ppt=hp&ppn=homepage&ssid=q2rox61oo00000001607805141969&otracker=hp_reco_Trending%2BOffers_6_13.dealCard.OMU_cid%3AS_F_N_clo_cfv_itg_tys__o_nb_mp_10b7629130__NONE_ALL%3Bnid%3Aclo_cfv_itg_tys_%3Bet%3AS%3Beid%3Aclo_cfv_itg_tys_%3Bmp%3AF%3Bct%3Ao%3B_8&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC2_Trending%2BOffers_DESKTOP_HORIZONTAL_dealCard_cc_6_NA_view-all_8&cid=cid%3AS_F_N_clo_cfv_itg_tys__o_nb_mp_10b7629130__NONE_ALL%3Bnid%3Aclo_cfv_itg_tys_%3Bet%3AS%3Beid%3Aclo_cfv_itg_tys_%3Bmp%3AF%3Bct%3Ao%3B")
    
soup = BeautifulSoup(page.content, "html.parser")
product=soup.find_all('div',attrs={'class':'_2pi5LC col-12-12'})

for a in product:
    product_names=a.find_all('a', attrs={'class':'IRpwTa'})
    for name in product_names:
        products.append(name.get_text(strip=True))
    product_prices=a.find_all('div', attrs={'class':'_30jeq3'})
    for price in product_prices:
        prices.append(price.get_text(strip=True))
    product_brand=a.find_all('div', attrs={'class':'_2WkVRV'})
    for brand in product_brand:
        brands.append(brand.get_text(strip=True))
    product_discount=a.find_all('div', attrs={'class':'_3Ay6Sb'})
    for discount in product_discount:
        discounts.append(discount.get_text(strip=True))
df=pd.DataFrame({'Product Name':products, 'Price':prices, 'Brand':brands , 'Discount': discounts})
df.to_csv('products.csv', index=False, encoding='utf-8')