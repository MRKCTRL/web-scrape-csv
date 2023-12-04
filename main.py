from bs4 import beautifulSoup
import requests
import pandas as csv


url = 'https://www.property24.com/for-sale/meredale/johannesburg/gauteng/5294?gclid=CjwKCAiAjrarBhAWEiwA2qWdCBijS6LLGTKHG4QNxZAOUm2fghUXMB2elukjEtTK66zNjq1R9yCAbBoCa7IQAvD_BwE'

response = requests.get(url)
soup = beautifulSoup(result.text, 'html.parser')
soup.find('span', class_='p24_price')

houses = soup.find_all('p24_price')[:]

price = soup.find_all('div class="p24_price"')

bedroom = soup.find_all('div class="p24_mBM"')

house_table = [title.text.strip() for home in bedroom]

df = pd.DataFrame(columns=house_table)

column_data = span.find_all('div')

for row in column_data[1:]:
    raw_data = row.find_all('div')
    indiviual_house = [data.text.strip() for data in raw_data]

    length = len(df)
    df.loc[length] = indiviual_house
    print(df)
    df.to_csv(r'<specify which folder.csv>', index=False)

# <span class="p24_price" itemprop="price" content="2000000">
#                 <meta itemprop="priceCurrency" content="ZAR">
#             R 2 000 000
#         </span>
# price = doc.find_all(text='R')
# parent = price[0].parent
# strong = parent.find('strong')
