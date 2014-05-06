import requests
import re
import random

theTao = requests.get('http://www.sacred-texts.com/tao/taote.htm').text.split('<h2>')
todaysTao = re.sub('<[^<]+?>|\\r', '', theTao[random.randint(1,81)])

for line in todaysTao.split('\\n'):
    print line
