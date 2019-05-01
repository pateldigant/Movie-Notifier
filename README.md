# Movie Notifier

This script is used for getting notification via e-mail whenever online ticket booking starts on paytm.com
Script is pretty simple to use. Just edit the params.ini file and mention your desired city, movie, date, theatre, etc.

Requirements:
  - python 3.x
  - requests (pip install requests)
  - BeautifulSoup (pip install bs4)

To run the script continously make use of loop bash file and edit the sleep parameter. Currently set to 600(i.e script will run every 10 minutes).

Tip: The whole script can be run in an Android device via termux app so you don't need to find a server to host your app.