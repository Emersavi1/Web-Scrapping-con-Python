
# url -> https://www.futbolred.com/

import requests
from bs4 import BeautifulSoup

url_base = 'https://www.futbolred.com/'
for num in range(1, 10):
    url = f'{url_base}{num}'   
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        word = 'lesion'
        
        if word in soup.get_text().lower():
            print(f'Se encuentra la palabra {word} en la url {url}')
            
    else:
        print('Error, no se puede acceder a la página')