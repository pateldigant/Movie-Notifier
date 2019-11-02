import os

exception_string = "Trying to Install required module: "
try:
    import requests
except ImportError:
    print(exception_string + "requests\n")
    os.system('python -m pip install requests')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print(exception_string + "BeautifulSoup\n")
    os.system('python -m pip install beautifulsoup4')

import requests
from bs4 import BeautifulSoup
import re
import smtplib
import ssl
import configparser
import sys


def sendmail(mail_ids, sender_email_parameter, email_password_parameter, custom_message=None, date_parameter='Date'):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email_parameter = sender_email_parameter
    receiver_email = mail_ids
    password = email_password_parameter
    message = """\
    Subject: WE ARE IN THE ENDGAME NOW
    
    
    Hi User,
    Hurry up!!! Avengers Endgame IMAX 3D Tickets are now available on """ + date_parameter + """
            
    Thanks & Regards,
    Mr Crawler"""

    if custom_message:
        message = custom_message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email_parameter, password)
        for email in receiver_email:
            server.sendmail(sender_email_parameter, email, message)


while True:
    try:
        config = configparser.ConfigParser()
        config.read('params.ini')
        website = 'https://paytm.com/movies/' + config['parameters']['city']
        dates = config['parameters']['dates'].split(',')
        movie_name = config['parameters']['movie'].lower()
        theatre_name = config['parameters']['theatre'].lower()
        send_email = config['parameters']['sendmail'].lower()
        sender_email = config['parameters']['senderEmail']
        email_password = config['parameters']['emailPassword']
        mailIds = config['parameters']['mailIds'].split(',')

        page = requests.get(website)
        soup = BeautifulSoup(page.text, 'html.parser')
        soup = soup.find("div", {"id": "popular-movies"})

        movies_list = soup.find_all("li")

        res = None
        for movie in movies_list:
            if movie_name in str(movie).lower():
                res = str(movie)
                break
        if res is None:
            print('Movie not available')
        # os._exit(1)
        if res is not None:
            for date in dates:
                res1 = 'https://paytm.com' + re.search('href=\"(.*?)\?', res).group(1) + '?fromdate=' + date

                page2 = requests.get(res1)
                soup2 = BeautifulSoup(page2.text, 'html.parser')

                showtime_list = soup2.find_all('div', class_='SbzU')
                if theatre_name in str(showtime_list[0]).lower():
                    if send_email == 'yes':
                        sendmail(mailIds, sender_email, email_password, date_parameter=str(date))
                    print('Success')
                # os._exit(0)
                else:
                    print('Not available')
            # os._exit(1)

    except:
        print('Some exception occured')
        sendmail(['abc@gmail.com'], custom_message='Exception Occurred')
        print(sys.exc_info()[0])
    else:
        break
