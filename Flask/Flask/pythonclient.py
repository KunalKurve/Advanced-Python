import requests

# we have requests for these as follows: 
# For reading - GET
# for Adding - POST
# for Updating - PUT
# for deleting - DELETE - we only need id

response = requests.post('http://127.0.0.1:5000/products', data = {'pid':100, 'pname': 'xxx', 'qty': 34, 'price':45})
print(response)