import urllib.request
from bs4 import BeautifulSoup
import requests
url = "http://192.168.0.174"
def checking_connection():
    try:
        html_text = requests.get('http://192.168.0.174').text
        soup = BeautifulSoup(html_text, 'lxml')
        course = soup.find('h1')
        value = course.text
        return value
    except:
        pass


def sendrequest(url):
    urllib.request.urlopen(url)
def led_off():
    sendrequest(url+'/ledoff')
def led_on():
    sendrequest(url+'/ledon')
def fan_off():
    sendrequest(url+'/fanoff')
def fan_on():
    sendrequest(url + '/fanon')
