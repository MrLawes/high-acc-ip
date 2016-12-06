# -*- coding:utf-8 -*-

import requests
import json

url = 'http://61.155.215.44:60617/api/get_wxpay_info/'
data = {
    'product_type': 'shishicai',
    'product_no': '20161012049',
    'product_name': json.dumps({'1': 1}),
    'uuid': '574e8d108f9a11e68e0400a0d1eb6408',
}
r = requests.post(url, data)
print r.content
print r.status_code