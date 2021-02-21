import requests
from bs4 import BeautifulSoup
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

AMAZON_PRODUCT_URL = "amzason single product url"
browser_header = {"User-Agent":"Yours", "Accept-Language": "Yours"}

response = requests.get(AMAZON_PRODUCT_URL, headers=browser_header)

soup = BeautifulSoup(response.text, "html.parser")

element_name = soup.find_all(name="span", class_="a-size-large product-title-word-break")
element_price = soup.find_all(name="span", class_="a-size-medium a-color-price")

product_price = int(float(element_price[0].getText().split('$')[1]))
print(element_name[0].getText().strip())
print(product_price)

if product_price < 505:
    message = Mail(
        from_email='from_email@example.com',
        to_emails='to@example.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)



URL = "https://www.billboard.com/charts/hot-100/2000-08-12"
# year = input("Which year will you like to travel to? ")
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, "html.parser")
#
# song_artist = soup.find_all(name="span", class_="chart-element__information__artist")
# song_name = soup.find_all(name="span", class_="chart-element__information__song")
#
# top_song_list = []
#
# for song in range(len(song_artist)):
#     artist = song_artist[song].getText()
#     name = song_name[song].getText()
#     top_song_list.append({"song_artist": artist, "song_name": name})
#
# print(len(top_song_list))