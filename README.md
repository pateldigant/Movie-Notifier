
# Paytm Movie Notifier  
  
> Get an instant email whenever movie bookings start.
  
This script is used for getting notification via e-mail whenever online ticket booking starts on **paytm.com**  
Script is pretty simple to use. Just edit the `params.ini` file and mention your desired *city*, *movie*, *date*, *theatre*, etc.

*Requirements:*  
 - [python 3.x](https://www.python.org/downloads/release/python-368/)  
 - [requests](https://2.python-requests.org/en/master/) (`pip install requests`)  
 - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (`pip install bs4`)  
  
To run the script continously make use of `loop.sh` bash file and edit the sleep parameter. Currently set to 600 seconds *(i.e script will run every 10 minutes)*.  

## Tips  

 - Multiple dates and multiple receiver email id's can be given in `params.ini`.
 - The whole script can be run on an **Android** OS via [termux](https://play.google.com/store/apps/details?id=com.termux&hl=en_IN) app so you don't need to find a server to host your app.
 - Instead of using your own gmail password you can create temporary application password which would only allow emailing for this script purpose. Check the tab **How to generate an App password** in google [help](https://support.google.com/accounts/answer/185833?hl=en)

 