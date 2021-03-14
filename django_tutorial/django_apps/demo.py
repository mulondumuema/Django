import requests
# we will segregate the base url and endpoints. base are fixed

BASE_URL='http://localhost:8000'
ENDPOINT='/api/employees/json1'
resp=requests.get(BASE_URL+ENDPOINT)
resp_data=resp.json()

print('Employee ID :', resp_data['eid'])
print('Employee Name :', resp_data['ename'])
print('Employee City :', resp_data['ecity'])
