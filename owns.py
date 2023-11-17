import json
import requests
import subprocess
 
def send_get(url, param=None, headers=None):
    x = requests.get(url, json=param, headers=headers)
    #print(x.text)
    try:
        return json.loads(x.text)
    except:
        return x.text

rd = {
  "id": 11631253,
  "created_at": "2018-10-13T08:13:38.809469028Z",
  "phone": "+79000381454",
  "product": "vkontakte",
  "price": 21,
  "status": "RECEIVED",
  "expires": "2018-10-13T08:28:38.809469028Z",
  "sms": [
      {
        "id":3027531,
        "created_at":"2018-10-13T08:20:38.809469028Z",
        "date":"2018-10-13T08:19:38Z",
        "sender":"VKcom",
        "text":"VK: 09363 - use this code to reclaim your suspended profile.",
        "code":"09363"
      }
  ],
  "forwarding": 'false',
  "forwarding_number": "",
  "country":"russia"
}


def api(num, action, city=None, oper=None, apps=None, id=None):
    
    if num in [1, '1']:
        token = 'eyJhbGciOiJSUzUxMiIcCI6IkpXVCJ9.eyJleHAiOjE3MTU0MzM0OTQsImlhdCI6MTY4Mzg5NzQ5NCwicmF5IjoiNTdkNThiNzJjODYwZWIzMzEwNDhhZTkyYTUxZjY0NjAiLCJzdWIiOjQ1Nzc2NX0.lOxUc7dN4nU7Ul85XsdSStJCwwzvygCSxmJxslApPOqXSYmTtp704cd0wH-8a2YnlBkCRKbDTqMf68tgBVfRRI2cYhF7nf8Z3vGYyYGPdBFT4qR1GmM6T9s3pMqzMya-1sbJLerLCkgeqTkk0lBozHYVf_0jMoVVt9gMAFTCPsoPRJUeHHvg-NTYMqMziygUB_hrPQHy1Z9YIPfX2ko5dlCwKg74YfmBgn87JfgI0wv44Ns19MwljDi2c8wTCcQtIxecd6Tb0rbSn6HFwMqqfEospXhkWMV6fB-tbHZHLDCrgzszLxWZ5yGFUUa4IJOeA4hcHsILr1-PZt3hXGrlXA'
        headers = {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
        }
        if action == 'balance':
            return send_get('https://5sim.net/v1/user/profile', None, headers)
        if action == 'all':
            country = 'any'
            operator = 'any'
            return send_get('https://5sim.net/v1/guest/products/' + country + '/' + operator, None, headers)

        if action == 'buy':
            return send_get('https://5sim.net/v1/user/buy/activation/'+ city + '/' + oper + '/' + apps, None, headers)
        
        if action == 'code':
            return send_get('https://5sim.net/v1/user/check/' + str(id), None, headers)

    return False


def send_shell(*argv):
    subprocess.Popen(argv)
'''u = send_get('https://5sim.net/v1/user/check/367086045', None, headers)

sms = u['sms']
for i in sms:
    print(i['text'], i['code'])'''