import requests

print("send get request")
response = requests.get("http://127.0.0.1:5000/products")
print(response)
print(response.content) # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
print(response.json()) # This method is convenient when the API returns JSON


print("send put request")
response = requests.put('http://127.0.0.1:5000/products/20', data = {'pid':20,'pname':'table111','qty':34,'price':45})
print(response.content)


print("send delete request")
response = requests.delete('http://127.0.0.1:5000/products/10', data = {'pid':100,'pname':'xxx','qty':34,'price':45})
print(response.content)



print("send post request")
response = requests.post('http://127.0.0.1:5000/products', data = {'pid':100,'pname':'xxx','qty':34,'price':45})
print(response)
print(response.content)

# Update an existing resource
#requests.put('http://127.0.0.1:5000/products', data = {'key':'value'})


#To implement GET request
print("send get request")
response = requests.get('http://127.0.0.1:5000/products', data = {'pid':100,'pname':'xxx','qty':34,'price':45})
print(response)
print(response.content)
