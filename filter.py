import requests
import time
	
headers = {
    'Content-Type': 'application/json',
}
	
with open('C:/Users/tung1/Desktop/dynamic_filter.json') as f:
    data = f.read().replace('\n', '').replace('\r', '').encode()
	
for i in range(1550):
    response = requests.post('https://10.55.104.28:8000/api/filters', headers=headers, data=data, verify=False, auth=('admin', 'admin'))
    if response.status_code == 200:
        print(f"Request {i+1}: Success")
        time.sleep(4)
    else:
        print(f"Request {i+1}: Failed") 
