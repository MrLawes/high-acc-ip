import requests
import json

ip_addr = raw_input('Your ip:')
url = 'http://api.map.baidu.com/highacciploc/v1?qcip=%s&qterm=pc&ak=omhNrOPQOYt5iVzNSlZ8MuE6tQC7KxL2&coord=bd09ll&extensions=3' % (ip_addr)
r = requests.get(url)
content = json.loads(r.content)
print content['content']['formatted_address']