import requests
from bs4 import BeautifulSoup
import re
import smtplib, ssl
import configparser
import sys
import os
def sendmail(mailIds, sender_email, email_password, customMessage = None,date = 'Some Date'):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = sender_email  
	receiver_email = mailIds
	password = email_password
	message = """\
Subject: WE ARE IN THE ENDGAME NOW


Hi User,
Hurry up!!! Avengers Endgame IMAX 3D Tickets are now available on """ + date + """
		
Thanks & Regards,
Mr Crawler"""
	if customMessage:
		message = customMessage
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		for email in receiver_email:
			server.sendmail(sender_email, email, message)
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
		soup =  soup.find("div", {"id": "popular-movies"})

		movies_list = soup.find_all("li")

		res = None
		for movie in movies_list:
			if movie_name in str(movie).lower():
				res = str(movie)
				break
		if res is None:
			print('Movie not available')
			#os._exit(1)
		if res is not None:
			for date in dates:
				res1 = 'https://paytm.com' + re.search('href=\"(.*?)\?',res).group(1) + '?fromdate=' + date

				page2 = requests.get(res1)
				soup2 = BeautifulSoup(page2.text, 'html.parser')

				showtime_list = soup2.find_all('div',class_='SbzU')
				if theatre_name in str(showtime_list[0]).lower():
					if send_email == 'yes':
						sendmail(mailIds, sender_email, email_password, date=str(date))
					print('Success')
					#os._exit(0)
				else:
					print('Not available')
					#os._exit(1)

	except:
		print('Some exception occured')
		sendmail(['abc@gmail.com'],customMessage = 'Exception Occured')
		print(sys.exc_info()[0])
	else:
		break
