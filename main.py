import requests
import time

time_stamp = int(time.time())
base_url = "https://sugang.konkuk.ac.kr/sugang/sugang?attribute=sugangMode&fake={}".format(time_stamp)
test_url = ""
# URL = 'http://api.mum.boundary.team/'
response = requests.get(test_url)
print(response)
print(response.text)
# response.status_code
# response.text
# print(response.cookies)