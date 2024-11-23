
import requests
#from random import choice

def filter_for_shopify(url:str) -> bool:
    
    #return choice([True, False])
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return False
    if not response.status_code == 200:
        return False
    if "Shopify.shop" in response.text:
        return True
    return False

# Test: 
#print(filter_for_shopify("https://sternsteiger.com"))
